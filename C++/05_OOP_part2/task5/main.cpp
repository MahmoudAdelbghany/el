#include<iostream>

int main() {

    int a = 5;
    int b = 10;
    if (a < b and b > 0) {
        std::cout << "a is less than b and b is positive" << std::endl;
    } else {
        std::cout << "a is not less than b or b is not positive" << std::endl;
    }
    if (a > 0 or b > 0) {
        std::cout << "either a or b is positive" << std::endl;
    } else {
        std::cout << "a and b are not positive" << std::endl;
    }
    if (not a > 0) {
        std::cout << "a is not positive" << std::endl;
    } else {
        std::cout << "a is positive" << std::endl;
    }

    return EXIT_SUCCESS;
}