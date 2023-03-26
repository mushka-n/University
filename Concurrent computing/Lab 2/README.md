# Matrix Multiplication

## Usage

### Row-wise

```console
 mpicxx main-row-wise.cpp -o main-row-wise && mpiexec -n <num of threads> main-row-wise
```

### Column-wise

```console
 mpicxx main-col-wise.cpp -o main-col-wise && mpiexec -n <num of threads> main-col-wise
```

## Test results

### System specs

- Intel(R) Core(TM) i5-9400 CPU @ 2.90GHz 2.90 GHz (6 cores, 6 threads)
- mpicxx compiler 11.3.0

### Comparison table (row-wise)

| Threads\ Size | 100x100 | 200x200 | 400x400 |
| ------------- | ------- | ------- | ------- |
| 1             | 0.002s  | 0.023s  | 0.193s  |
| 2             | 0.001s  | 0.011s  | 0.121s  |
| 4             | 0.001s  | 0.006s  | 0.055s  |
| 6             | <0.001s | 0.005s  | 0.05s   |

![visualization/row-wise-data.png](visualization/row-wise-data.png)

### Comparison table (column-wise)

| Threads\ Size | 100x100 | 200x200 | 400x400 |
| ------------- | ------- | ------- | ------- |
| 1             | 0.003s  | 0.021s  | 0.175s  |
| 2             | 0.001s  | 0.012s  | 0.097s  |
| 4             | 0.001s  | 0.005s  | 0.056s  |
| 6             | <0.001s | 0.004s  | 0.037s  |

![visualization/col-wise-data.png](visualization/col-wise-data.png)
