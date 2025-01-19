#include <iostream>
#include <array>
#include <numeric>  

int main() {
    const int start = 10;
    const int end = 1000;
    const int size = end - start + 1;

   std::array<int, size> arr = {};

    std::iota(arr.begin(), arr.end(), start);

    // for (int i : arr) {
    //     std::cout<<i<<std::endl;
    // }
   

    return EXIT_SUCCESS;
}