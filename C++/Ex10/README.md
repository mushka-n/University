# Ex10 Translation of an arithmetic expression from an infix to a postfix record

## Brief information from the theory

### The concept of an arithmetic expression

An arithmetic expression is an expression in which the operands are objects on which arithmetic operations are performed. For example,

```
(1 + 2) / (3 + 4 * 6.7) - 5.3 * 4.4
```

In this form of notation (called * * infix**, where the operation signs are between the operands), the order of actions is determined by the placement of parentheses and the priority of operations. ** The postfix** (or reverse Polish) form of the entry does not contain brackets, and the operation signs follow the corresponding operands. Then for the given example, the postfix form will have the form:

```
1 2 + 3 4 6.7 * + / 5.3 4.4 * -
```

### Translation to the postfix form

This algorithm is based on the use of a stack. A string of characters is received at the input of the algorithm, and a string with a postfix form should be received at the output. Each operation and parentheses are assigned a priority:

```
( - 0
) - 1
+- - 2
*/ - 3
```

It is assumed that the input string contains a syntactically correct expression.

The input string is viewed character-by-character from left to right until the end of the string is reached. We will consider as operands any sequence of characters of the input string that does not coincide with the characters of the operations defined in the table. Operands are rewritten to the output string as they appear. When an operation appears in the input line, the priority of this operation is calculated. The sign of this operation is placed on the stack if:

- The priority of the operation is 0 (this is '(' ),
- The priority of the operation is strictly greater than the priority of the operation lying at the top of the stack,
- The stack is empty.

Otherwise, all signs of operations with a priority greater or equal to the priority of the current operation are extracted from the stack. They are rewritten to the output string, after which the sign of the current operation is placed on the stack. There is a special feature in the processing of the closing bracket. The appearance of a closing parenthesis in the input string leads to the ejection and writing to the output string of all operation characters before the appearance of the opening parenthesis. The opening parenthesis is pushed out of the stack, but it is not written to the output string. Thus, neither the opening nor closing brackets fall into the output string. After viewing the entire input string, all the stack elements are sequentially extracted, while simultaneously writing the signs of operations extracted from the stack to the output string.



### Explanation
```
Function **infix2prefix** converts a record of an arithmetic expression in infix form 
to a record of the same expression, but in postfix form
```

> *Note*
> It is assumed that only digits, operation signs, parentheses and a decimal point are used in writing an arithmetic expression. The numbers are written only positive, they can be both integer and real. The brackets are placed correctly. The depth of the parenthesis embedding is no more than 100. The number of operations in the expression is no more than 200.


## Project structure

> - **include/MyStack.h** - header file for the **MyStack**class template.
> - **include/postfix.h** - header file for the function being created.
> - **src/postfix.cpp** - a file with the implementation of the function.
> - **main.cpp** - pre-installation program for working with the function.