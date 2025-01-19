#include <iostream>
#include <vector>

class String
{
    std::vector<char> string;
    size_t length;

public:
    String() : length(0) {}

    void setString(const char *str)
    {
        length = 0;
        while (str[length] != '\0')
        {
            length++;
        }
        string.resize(length);
        for (size_t i = 0; i < length; i++)
        {
            string[i] = str[i];
        }
    }
    char *getString()
    {

        return string.data();
    }
    size_t getLength()
    {
        return length;
    }
};

int main()
{
    String str;
    str.setString("Hello, World!");
    std::cout << str.getString() << " (Length: " << str.getLength() << ")" << std::endl;
    return EXIT_SUCCESS;
}