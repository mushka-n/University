# Ex05 Development of the simplest template functions



## Explanation

### **less** function


Template function that compares two elements of type **T** and returns the logical result `true` if the first element is smaller than the second. For strings, a lexicographic comparison is performed (to make a specialization).

> The result of solving the problem is the header file **task1.h** and the main program file **main1.cpp** with a demonstration of the work of the template function.


### **averageArr** function

Template function, that returns the arithmetic mean for all elements. A pointer to the first element and the size of the array are passed to the function.

> The result of solving the problem is the header file **task2.h** and the main program file **main2.cpp** with a demonstration of the work of the template function.


### **minArr** function

Template function, which takes an array of elements of type T by reference and determines the minimum value. We do not pass the size of the array to the function.

> The result of solving the problem is the header file **task3.h** and the main program file **main3.cpp** with a demonstration of the work of the template function.


## Project structure

The files **task1.h**, **task2.h**, **task3.h** are placed in the `include` directory
Files `**main1.cpp**, **main2.cpp**, **main3.cpp**` are placed in the `src` directory