package com.company;

public class Matrix {
    private final int m;
    private int n;
    private final Complex[][] matrix;

    /////////////////// CONSTRUCTORS //////////////////

    public Matrix(int mNew, int nNew) {
        m = mNew;
        n = nNew;
        matrix = new Complex[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = new Complex();
            }
        }
    }

    public Matrix(Complex[][] matrixNew) {
        m = matrixNew.length;
        n = 0;
        for (int i = 0; i < m; i++) {
            int maxlength = matrixNew[i].length;
            if (maxlength > n) {
                n = maxlength;
            }
        }
        matrix = new Complex[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j < matrixNew[i].length) {
                    matrix[i][j] = matrixNew[i][j];
                } else {
                    matrix[i][j] = new Complex();
                }
            }
        }
    }


    /////////////////// OPERATIONS ////////////////////

    public Matrix Add(Matrix toAdd) {
        Matrix res = new Matrix(m,n);
        if (m == toAdd.m && n == toAdd.n) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    res.matrix[i][j] = matrix[i][j].Add(toAdd.matrix[i][j]);
                }
            }
        } else System.out.println("Matrices need to be the same size");
        return res;
    }

    public Matrix Subtract(Matrix toSubtract) {
        Matrix res = new Matrix(m,n);
        if (m == toSubtract.m && n == toSubtract.n) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    res.matrix[i][j] = matrix[i][j].Subtract(toSubtract.matrix[i][j]);
                }
            }
        } else System.out.println("Matrices need to be the same size");
        return res;
    }

    public Matrix Multiply(Matrix toMultiply) {
        Matrix res = new Matrix(m, toMultiply.n);
        System.out.println(String.valueOf(m) + ' ' + (toMultiply.n));
        if (n == toMultiply.m) {
            for (int i = 0; i < res.m; i++) {
                for (int j = 0; j < res.n; j++) {
                    for (int k = 0; k < n; k++) {
                        // c += A[i,k] * B[k,j]
                        res.matrix[i][j] = res.matrix[i][j].Add(matrix[i][k].Multiply(toMultiply.matrix[k][j]));
                    }
                }
            }
        } else System.out.println("Matrices dont have the proper sizes");
        return res;
    }

    /////////////////// DETERMINANT ///////////////////

    // Counts det for a given matrix
    private Complex CountDet(Complex[][] mat) {
        int size = mat.length;
        if (size == 2) {
            // [0,0] * [1,1] - [1,0] * [0,1]
            return mat[0][0].Multiply(mat[1][1]).Subtract(mat[1][0].Multiply(mat[0][1]));
        }

        Complex determinant = new Complex();
        for (int i = 0; i < size; i++) {
            Complex a = mat[0][i].Multiply(new Complex(Math.pow(-1, i)));
            Complex A = SetMinor(mat, i).Multiply(a);
            determinant = determinant.Add(A);
        }
        return determinant;
    }

    // Specifies and counts a minor
    private Complex SetMinor(Complex[][] mat, int a) {
        int size = mat.length - 1;
        Complex[][] minor = new Complex[size][size];

        int im = -1, jm;
        for (int i = 1; i < size + 1; i++) {
            im++;
            jm = 0;
            for (int j = 0; j < size + 1; j++) {
                if (j != a) {
                    minor[im][jm] = mat[i][j];
                    jm++;
                }
            }
        }
        return CountDet(minor);
    }

    public Complex Determinant() {
        if (m != n) {
            System.out.println("Not a square matrix");
            return new Complex();
        }
        return CountDet(matrix);
    }

    /////////////////////// PRINT /////////////////////

    public void PrintMatrix() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j].Print() + "  ");
            }
            System.out.println(' ');
        }
    }
}
