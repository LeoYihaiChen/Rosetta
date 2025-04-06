py_file = open("/Users/yihaichen/Desktop/mycomputer/code/code/c_cpp/generated.cpp", "w")

py_file.writelines("#include <stdio.h>\n"
                "int main()\n"
                "{\n"
                '\tprintf("hello world");'
                "\treturn 0;\n"
                "}\n"
                )

py_file.close()
