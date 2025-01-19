#include <iostream>
#include "backtrace.hpp"

void foo();
void boo();
void fun();

void foo()
{
    ENTER_FUNCTION;
    // std::cout << "foo" << std::endl;
    boo();
}

void boo()
{
    ENTER_FUNCTION;
    // std::cout << "boo" << std::endl;
    fun();
}

void fun()
{
    ENTER_FUNCTION;
    // std::cout << "fun" << std::endl;
    PRINT_BACKTRACE;
}

int main()
{
    ENTER_FUNCTION;
    foo();

    return 0;
}
