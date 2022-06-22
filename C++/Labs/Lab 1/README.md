# Lab 1

** Task 1**

```
Write a program that determines which is the smallest positive integer
the number is divided by all numbers from the range [1...20] without a trace.
```

**The composition of the project**

```
- unsigned long findValue(unsigned int min,unsigned max) - number search function.
Divisors: [min..max]
- int main()
```

**Files:** task1.h, task1.cpp, main1.cpp

** Task 2**

```
Write a prototype of a library for working with prime numbers.
```

**The composition of the project**

```
- bool checkPrime(unsigned int value) - checking the number for simplicity.
- unsigned long long nPrime(unsigned n) - finding the nth prime number (in a row).
- unsigned long long nextPrime(unsigned long long value) - finding the nearest next prime number to value.
- int main() - a simple demonstration (script).
```
**Files:** task2.h, task2.cpp, main2.cpp

** Task 3**
```
Find the sum of all prime numbers less than two million.
```

**The composition of the project**

```
- unsigned long long sumPrime(unsigned int hbound) - the sum of all numbers up to hbound (not including it)
- main()
```

**Files:** task2.h, task2.cpp, task3.h, task3.cpp, main3.cpp

** Task 4**

```
Implement the function of adding two super-long numbers specified as strings.
```

**Explanation**

As a result of the *sum* function, an array should appear in dynamic memory with the result of addition.

**The composition of the project**

```
- char * sum(char *x, char *y) - sum of the numbers x and y
-main ()
```

**Files:** task4.h, task4.cpp, main4.cpp

** Task 5**

```
Implement the function of splitting a string into substrings using a separator character.
```

**Explanation**

As a result of the *split* function, a NEW array of strings should appear in dynamic memory.

**The composition of the project**

```
- void split(char ***result, int *N, char *buf, char ch) - splitting the buf string into substrings and writing
the result in result, with the assignment to the address N of the number of received substrings.
- main()
```

**Files:** task5.h, task5.cpp, main5.cpp