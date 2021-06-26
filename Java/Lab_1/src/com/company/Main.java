package com.company;

public class Main {
    public static void main(String[] args) {
        Complex z0 = new Complex(0, -9);
        Complex z1 = new Complex(1, 8);
        Complex z2 = new Complex(2, 7);
        Complex z3 = new Complex(3, -6);
        Complex z4 = new Complex(4, -5);
        Complex z5 = new Complex(5, 4);
        Complex z6 = new Complex(6, 3);
        Complex z7 = new Complex(7, -2);
        Complex z8 = new Complex(8, -1);
        Complex z9 = new Complex(9, 0);


        System.out.println(z1.Print() + " + " + z2.Print() + " = " + z1.Add(z2).Print());
        System.out.println(z1.Print() + " - " + z2.Print() + " = " + z1.Subtract(z2).Print());
        System.out.println(z1.Print() + " * " + z2.Print() + " = " + z1.Multiply(z2).Print());
        System.out.println(z1.Print() + " / " + z2.Print() + " = " + z1.Divide(z2).Print());
        System.out.println(z1.Print() + " = " + z1.PrintTrig());

        System.out.println("\n-----------------------------------\n");

        Complex[][] list1 = {{z1,z0},{z4,z9}};
        Complex[][] list2 = {{z3,z2},{z7,z5}};
        Matrix m1 = new Matrix(list1);
        Matrix m2 = new Matrix(list2);

        System.out.println("M1");
        m1.PrintMatrix();
        System.out.println("\nM2");
        m2.PrintMatrix();


        Matrix m3 = m1.Add(m2);
        System.out.println("\nAdd");
        m3.PrintMatrix();

        Matrix m4 = m1.Subtract(m2);
        System.out.println("\nSubtract");
        m4.PrintMatrix();

        Matrix m5 = m1.Multiply(m2);
        System.out.println("\nMultiply");
        m5.PrintMatrix();


        System.out.print("\n\nM3");
        Complex[][] list3 = {{z1,z3,z4,z6},{z8,z2,z0,z5},{z3,z2,z0,z9},{z3,z3,z6,z5}};
        Matrix m6 = new Matrix(list3);
        System.out.println();
        m6.PrintMatrix();
        System.out.println("\nDet = " + m6.Determinant().Print() );
    }
}
