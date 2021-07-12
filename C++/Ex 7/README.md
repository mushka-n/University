# Ex07 Development of the Fraction class, code design according to the standard

### Explanation

The Fraction class represents ordinary fractions. It is provided by the following methods:

> - **Fraction(..)** - constructor with two parameters, with default values (0,1).
> - * * Fraction(..)** - copy constructor.
> - **normalize()** - closed method of normalization (reduction of the fraction 2/4 -> 1/2).
> - **getValue()**. - a method that returns a string type **std::string** that contain an image of fractions, such as "1/2" or "-5/6". A fraction with a single denominator is output as an integer.
> - **getNumerator ()** - return the numerator.
> - **getDenominator ()** - return the denominator.

As fields for storing the numerator and denominator, I used

```cpp
int numerator, denominator;
```

Operation overloading is implemented in the Fraction class:

> - **operator +** - addition
> - **operator -** - subtraction
> - **operator** **\*** - multiplication
> - **operator /** - division
> - **operator =** - assignment

If a zero appears in the denominator, an exception is thrown using the **throw** operator.

### Codestyle

> The code is designed in accordance with the standard described in https://google.github.io/styleguide/cppguide.html


## Project structure

- **Fraction.h** is the header file for the **Fraction**class.
- **Fraction.cpp** - a file with the implementation of methods of the **Fraction**class.
- **main.cpp** - pre-installation program for working with the **Fraction**class.