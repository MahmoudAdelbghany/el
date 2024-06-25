def generate_hpp_code(author_name, class_name):
    from datetime import datetime

    now = datetime.now()
    date_str = now.strftime("%a %b %d %H:%M:%S %p %Z %Y")

    hpp_code = f"""
#pragma once
/*********************************************/
// 
//           CopyRight {author_name}
//
/*********************************************/
/*
author : {author_name}
date   : {date_str}
brief  :
*/

namespace svm {{
class {class_name}{{
public:
    {class_name}();
    ~{class_name}();
private:

}};
}}
"""
    return hpp_code


def generate_cpp_code(author_name, class_name):
    from datetime import datetime

    now = datetime.now()
    date_str = now.strftime("%a %b %d %H:%M:%S %p %Z %Y")

    cpp_code = f"""
/*********************************************/
// 
//           CopyRight {author_name}
//
/*********************************************/
/*
author : {author_name}
date   : {date_str}
brief  :
*/
#include "{class_name.lower()}.hpp"

namespace svm {{
    {class_name}::{class_name}(){{}}
    {class_name}::~{class_name}(){{}}
}}
"""
    return cpp_code


author_name = input("Enter your name: ")
class_name = input("Enter the class name: ")

hpp_code = generate_hpp_code(author_name, class_name)
cpp_code = generate_cpp_code(author_name, class_name)


# print("Header File (.hpp):")
# print(hpp_code)
# print("\nImplementation File (.cpp):")
# print(cpp_code)
hpp = open(f"{class_name.lower()}.hpp", "w")
hpp.write(hpp_code)
hpp.close()
cpp = open(f"{class_name.lower()}.cpp", "w")
cpp.write(cpp_code)
cpp.close()
