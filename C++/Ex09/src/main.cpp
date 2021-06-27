#include "MyStack.h"
#include <iostream>

int main()
{

    MyStack<int> st(3);

    std::cout << st.get()<< "\n";
    std::cout << std::boolalpha << st.isEmpty()<< "\n";

    st.push(1);
    st.push(2);
    st.push(3);

    std::cout << std::boolalpha << st.isFull()<< "\n";

    std::cout <<st.get() << "\n";

    while(!st.isEmpty())
        std::cout << st.pop() <<" ";
    std::cout <<"\n"<< st.pop() ;
    return 0;
}