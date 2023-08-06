## Python C++ std iostream
Using C++ std lib iostream in py

### Installtion
    pip install py_cppstd

### Import
    from py_cppstd import std  
__then__:  
`std.load()`  
__or__  
`std = std()`

### How to use *iostream*
**recommend** to use ***;*** when end line.  

    std.include('iostream') # include 'iostream'  
    # prints 114514 and '\n' and flush the stream  
    std.cout << 114514 << std.endl  
    num: int  
    std.cin >> num # input a number to num