package com.company;

public class Complex {
    private double a, b, r = 0, fi = 0;

    /////////////////// CONSTRUCTORS //////////////////

    public Complex() {
        a = 0;
        b = 0;
    }

    public Complex(double na, double nb) {
        a = na;
        b = nb;
        CountTrig();
    }

    public Complex(double na) {
        a = na;
        b = 0;
        if (a!=0) CountTrig();
    }

    public void CountTrig() {
        r = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
        if (a > 0) {
            fi = Math.atan(b/a);
        } else {
            if (b > 0) {
                fi = Math.PI +  Math.atan(b/a);
            } else {
                fi = - Math.PI +  Math.atan(b/a);
            }
        }
    }

    /////////////////// OPERATIONS ////////////////////

    public Complex Add(Complex toAdd) {
        Complex res = new Complex(a, b);
        res.a += toAdd.a;
        res.b += toAdd.b;
        return res;
    }

    public Complex Subtract(Complex toSubtract) {
        Complex res = new Complex(a, b);
        res.a -= toSubtract.a;
        res.b -= toSubtract.b;
        return res;
    }

    public Complex Multiply(Complex byMultiply) {
        Complex res = new Complex();
        res.a = a * byMultiply.a + b * byMultiply.b * -1;
        res.b = a * byMultiply.b + b * byMultiply.a;
        return res;
    }

    public Complex Divide(Complex byDivide) {
        if (byDivide.a == 0 && byDivide.b ==0){
            System.out.println("Error: Cannot divide by 0");
            return new Complex(a,b);
        }
        Complex res = new Complex();
        double denominator = Math.pow(byDivide.a, 2) - (Math.pow(byDivide.b, 2) * -1);
        res.a = (a * byDivide.a - b * byDivide.b * -1) / denominator;
        res.b = (b * byDivide.a - a * byDivide.b) / denominator;
        return res;
    }

    /////////////////////// PRINT /////////////////////

    public String Print() {
        String aPrint = String.valueOf(a);
        String bPrint = String.valueOf(b) + 'i';
        if (b > 0) bPrint = " + " + bPrint;
        else if (b == 0){
            bPrint = "";
        }
        else {
            bPrint = " - " + bPrint.replace("-", "");
        }
        return (aPrint + bPrint);
    }

    public String PrintTrig() {
        if (a == 0 && b == 0){
            return "Error: Given complex number has no trigonometric form";
        }
        String printFi = String.valueOf(fi);
        return (r + " * ( cos(" + printFi + ") + i sin(" + printFi + ") )");
    }
}
