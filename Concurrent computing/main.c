#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <pthread.h>

#define DT 0.5
#define N_THREADS 6

typedef struct {
    double x, y;
} vector;

typedef struct Args {
    int start;
    int end;
} Args;


int bodies, timeSteps;
double *masses, GravConstant;
vector *positions, *velocities, *accelerations;

vector addVectors(vector a, vector b) {
    vector c = {a.x + b.x, a.y + b.y};
    return c;
}

vector scaleVector(double b, vector a) {
    vector c = {b * a.x, b * a.y}; 
    return c;
}

vector subtractVectors(vector a, vector b){
    vector c = {a.x - b.x, a.y - b.y};
    return c;
}

double mod(vector a) {
    return sqrt(a.x * a.x + a.y * a.y);
}

void initiateSystem(char *fileName) {
    FILE *fp = fopen(fileName, "r");
    fscanf(fp, "%lf%d%d", &GravConstant, &bodies, &timeSteps);

    masses = (double *)malloc(bodies * sizeof(double));
    positions = (vector *)malloc(bodies * sizeof(vector));
    velocities = (vector *)malloc(bodies * sizeof(vector));
    accelerations = (vector *)malloc(bodies * sizeof(vector));

    for (int i = 0; i < bodies; i++) {
        fscanf(fp, "%lf", &masses[i]);
        fscanf(fp, "%lf%lf", &positions[i].x, &positions[i].y);
        fscanf(fp, "%lf%lf", &velocities[i].x, &velocities[i].y);
    }

    fclose(fp);
}

void resolveCollisions() {
    int i, j;
    for (i = 0; i < bodies - 1; i++)
        for (j = i + 1; j < bodies; j++) {
            if (positions[i].x == positions[j].x && positions[i].y == positions[j].y) {
                vector temp = velocities[i];
                velocities[i] = velocities[j];
                velocities[j] = temp;
            }
        }
}

void computeAccelerations(int start, int end) {
    for (int i = start; i < end; i++) {
        accelerations[i].x = 0;
        accelerations[i].y = 0;
        for (int j = 0; j < bodies; j++) {
            if (i != j) {
                double d = mod(subtractVectors(positions[i], positions[j]));
                accelerations[i] = addVectors(accelerations[i], scaleVector(GravConstant * masses[j] / (d * d * d), subtractVectors(positions[j], positions[i])));
            }
        }
    }
}

void computeVelocities(int start, int end) {
    for (int i = start; i < end; i++)
        velocities[i] = addVectors(velocities[i], scaleVector(DT, accelerations[i]));
}

void computePositions(int start, int end) {
    for (int i = start; i < end; i++)
        positions[i] = addVectors(positions[i], scaleVector(DT,velocities[i]));
}

void* simulate(void* arg) {
    Args* a =  (Args*)arg;
    computeAccelerations(a->start, a->end);
    computePositions(a->start, a->end);
    computeVelocities(a->start, a->end);
    return NULL;
}

int main(int argC, char *argV[]) {
    initiateSystem(argV[1]);

    pthread_t threads[N_THREADS];
    Args args[N_THREADS];

    int chunksNum = bodies / N_THREADS;
    for (int i = 0; i < N_THREADS; i++) {
        args[i].start = chunksNum * i;
        args[i].end = chunksNum * (i + 1);
    }
    args[N_THREADS - 1].end = bodies;

    FILE *fpt;
    fpt = fopen("output.csv", "w+");

    fprintf(fpt, "t, ");
    for (int i = 0; i < bodies; i++) 
        fprintf(fpt, "x%d, y%d, ", i+1, i+1);
    fprintf(fpt, "\n");

    if (argC != 2) {
        fprintf(fpt, "Usage : %s <file name containing system configuration data>", argV[0]);
    } else {
        for (int i = 0; i < timeSteps; i++) {
            for (int j = 0; j < N_THREADS; ++j)
                pthread_create(&threads[j], NULL, simulate, &args[j]);

            for (int j = 0; j < N_THREADS; ++j)
                pthread_join(threads[j], NULL);

            resolveCollisions();

            fprintf(fpt, "%d, ", i);
            for (int j = 0; j < bodies; j++) 
                fprintf(fpt, "%lf, %lf, ", positions[j].x, positions[j].y);
            fprintf(fpt, "\n");
        }
    }
    fclose(fpt);
    return 0;
}