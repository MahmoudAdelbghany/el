#include <iostream>
#include <array>
#include <numeric>  

int main() {
    

   std::array<int, 10> arr = {1,2,3,4,5,6,7,8,9,10};
   std::cout<<std::accumulate(arr.begin(), arr.end(), 0)<<std::endl;



    return EXIT_SUCCESS;
}