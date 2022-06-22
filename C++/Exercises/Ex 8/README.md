# Ex08 Developing the myString class

### Explanation

myString class is a simple class for storing and operating strings. It is provided by the following methods:

> - **MyString( const char** **\*)** - constructor with one parameter (there is a default value **nullptr**).
> - **MyString( std::string )** - a constructor with a single parameter.
> - **MyString( const MyString& )** - copy constructor.
> - **MyString( MyString&& )** - the transfer constructor.
> - **~myString ()** - destructor.
> - **length()** - the number of characters (the length of the string).
> - **get ()** - returns a pointer to the data (type ' char\*').

Characters are stored in a dynamic array.


### Overloading of operations in the myString class:

> - **operator +**  - addition (concatenation of two strings).
> - **operator -** - subtraction (all characters present in the second line are removed from the first line).
> - **operator** **\*** - multiplication by an integer (the string is repeated the specified number of times).
> - **operator =** - copying assignment.
> - **operator =** - moving assignment.
> - **operator ==** - equality comparison.
> - **operator !=** - comparison for inequality.
> - **operator >** - lexographic comparison .
> - **operator <** - lexographic comparison.
> - **operator >=** - lexographic comparison.
> - **operator <=** - lexographic comparison.
> - **operator !** - Latin letters change their case.
> - **operator []** - access to the symbol by index.
> - **operator ()** - substring search.
> - **operator >>** - write to the stream.


## Project structure

> - **myString.h** is the header file for the **myString**class.
> - **MyString.cpp** - a file with the implementation of methods of the **myString * * class.
> - **main.cpp** - pre-installation program for working with the **myString**class.