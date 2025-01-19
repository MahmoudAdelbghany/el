#include <vector>
#include <string>
#include <iostream>
#define ENTER_FUNCTION backtrace bt(__PRETTY_FUNCTION__);
//#define EXIT_FUNCTION 
#define PRINT_BACKTRACE backtrace::print_backtrace();

class backtrace
{

    static std::vector<std::string> backtrace_stack;
    std::string function_name;

public:
    backtrace(const std::string& func_name) : function_name(func_name)
    {
        std::cout << "enter to function : " << func_name << std::endl;
        backtrace_stack.push_back(func_name);
    }
    ~backtrace()
    {
        std::cout << "exit from function : " << function_name<< std::endl;
        backtrace_stack.pop_back();
        
    }
    static void print_backtrace()
    {
        for (size_t i = 0; i < backtrace_stack.size(); i++)
        {
            std::cout << i << "- "<<backtrace_stack[i]<< std::endl;
        }
    }
};

std::vector<std::string> backtrace::backtrace_stack;
