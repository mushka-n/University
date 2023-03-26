#include <iostream>
#include <mpi.h>

#define N 400

using namespace std;

int main(int argc, char **argv) {
    int rank, size, i, j, k;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    size_t N_rank = N / size;
    size_t a[N * N], b[N * N], b_rank[N_rank * N], c[N * N], c_rank[N * N];

    if (rank == 0) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                a[i * N + j] = rand() % 10;
                b[i * N + j] = rand() % 10;
            }
        }
    }

    MPI::COMM_WORLD.Scatter(b, N_rank * N, MPI::DOUBLE, b_rank, N_rank * N, MPI::DOUBLE, 0);
    MPI::COMM_WORLD.Bcast(a, N * N, MPI::DOUBLE, 0);

    double start = MPI_Wtime();

    for (int j = 0; j < N_rank; ++j) {
        for (int i = 0; i < N; ++i) {
            for (int k = 0; k < N; ++k) {
                c_rank[i * N + k] += a[i * N + (j + rank * N_rank)] * b_rank[j * N + k];
            }
        }
    }

    MPI::COMM_WORLD.Reduce(c_rank, c, N * N, MPI::DOUBLE, MPI::SUM, 0);

    double end = MPI_Wtime();
    if (rank == 0) { std::cout << "Time: " << end - start << "seconds" << std::endl;}

    MPI_Finalize();
    return 0;
}