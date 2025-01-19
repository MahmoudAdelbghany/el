#include <iostream>
#include <cctype>
#include <algorithm>
#include <array>

#define arr_size 10

bool all_even(const std::array<int, arr_size>& arr)
{
    return std::all_of(arr.begin(), arr.end(), [](int x)
                       { return x % 2 == 0; });
}

bool any_even(const std::array<int, arr_size>& arr)
{
    return std::any_of(arr.begin(), arr.end(), [](int x)
                       { return x % 2 == 0; });
}

int main()
{
    char c1 = 'a';
    char c2 = '8';

    if (std::isdigit(c1))
    {
        std::cout << c1 << " is a digit\n";
    }
    else
    {
        std::cout << c1 << " is not a digit\n";
    }

    if (std::isdigit(c2))
    {
        std::cout << c2 << " is a digit\n";
    }
    else
    {
        std::cout << c2 << " is not a digit\n";
    }

    std::array<int, arr_size> arr1 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    std::array<int, arr_size> arr2 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    std::array<int, arr_size> arr3 = {1, 2, 4, 6, 8, 10, 12, 14, 16, 18};

    if (all_even(arr1))
    {
        std::cout << "All elements of arr1 are even\n";
    }
    else
    {
        std::cout << "Not all elements of arr1 are even\n";
    }

    if (all_even(arr2))
    {
        std::cout << "All elements of arr2 are even\n";
    }
    else
    {
        std::cout << "Not all elements of arr2 are even\n";
    }

    if (any_even(arr2))
    {
        std::cout << "At least one element of arr2 is even\n";
    }
    else
    {
        std::cout << "No element of arr2 is even\n";
    }

    if (all_even(arr3))
    {
        std::cout << "All elements of arr3 are even\n";
    }
    else
    {
        std::cout << "Not all elements of arr3 are even\n";
    }

    if (any_even(arr3))
    {
        std::cout << "At least one element of arr3 is even\n";
    }
    else
    {
        std::cout << "No element of arr3 is even\n";
    }

    return EXIT_SUCCESS;
}