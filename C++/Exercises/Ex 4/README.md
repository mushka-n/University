
# **Ex04** Generalized programming using pointers


## Explanation

```
Set of comparators for qsort operation from the cstdlib standard library.
```


### Comparators

Comparators for comparing the following array elements:

> - **comp1**: integer (comparison by value) - type int
> - **comp2**: real number (comparison by value) - type double 
> - **comp3**: string (comparison by value) - type const char*
> - **comp4**: string (length comparison) - type const char*
> - **comp5**: string (comparison by the number of spaces) - type const char*
> - **comp6**: structure **Person** (comparison by age)


### Program composition

> - **task1.h** - header file containing the **comp** headers, the **Person structure**
> - **task1.cpp** - a file containing the implementation of the **comp function**
> - **main1.cpp** - a file containing **main**