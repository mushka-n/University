#include <iostream>
#include <mpi.h>
#include <math.h>

#define N 400

using namespace std;

int main(int argc, char **argv) {
    int rank, size, i, j, k;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    size_t N_rank = N / size;
    size_t a[N * N], a_rank[N_rank * N], b[N * N], c[N * N], c_rank[N_rank * N];

    if (rank == 0) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                a[i * N + j] = rand() % 10;
                b[i * N + j] = rand() % 10;
            }
        }
    }

    MPI::COMM_WORLD.Scatter(a, N_rank * N, MPI_DOUBLE, a_rank, N_rank * N, MPI_DOUBLE, 0);
    MPI::COMM_WORLD.Bcast(b, N * N, MPI_DOUBLE, 0);

    double start = MPI::Wtime();

    for (int i = 0; i < N_rank; ++i) {
        for (int j = 0; j < N; ++j) {
            for (int k = 0; k < N; ++k) {
                c_rank[i * N + j] += a_rank[i * N + k] * b[k * N + j];
            }
        }
    }

    MPI::COMM_WORLD.Gather(c_rank, N_rank * N, MPI_DOUBLE, c, N_rank * N, MPI_DOUBLE, 0);

    double end = MPI::Wtime() - start;
    if (rank == 0) { std::cout << "Time: " << roundf((end - start) * 1000) / 1000 << "s" << std::endl; }
  
    MPI_Finalize();
    return 0;
}