/*
When you write f() = 10;, you are assigning the value 10 to the static variable x through the reference returned by f().
Similarly, f() = 0; sets x to 0.
*/
#include <iostream>

int &f() {
    static int x = 0;
    return x;
}

int main() {
    f() = 10;
    std::cout << f() << std::endl;
    f() = 0;
    std::cout << f() << std::endl;
    return EXIT_SUCCESS;
}