#include<iostream>
#include <csignal> 

void handler(int signal_num) 
{ 
    std::cout << "The interrupt signal is (" << signal_num << ")."<<std::endl; 
   
    exit(signal_num); 
}


int main() {

    signal(SIGINT, handler);

    while (true)
    {
        std::cout<<"Hello, C++!"<<std::endl;
    }
    


    return EXIT_SUCCESS;
}