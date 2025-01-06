## Intro
I am going to use LibClang as it is independent of CLang versions, you can also use LibTooling

## Need Modules
- [anaconda](https://anaconda.org/conda-forge/clang)
- [pip](https://pypi.org/project/libclang/)

## Links
- [docs](https://clang.llvm.org/doxygen/modules.html)
- [Problems with C/C++ languages](https://clang.llvm.org/docs/Modules.html?utm_source=chatgpt.com#problems-with-the-current-model)
### LibClang
- [libclang docs](https://clang.llvm.org/doxygen/group__CINDEX.html)
- [libclang tutorial](https://clang.llvm.org/docs/LibClang.html)
- [tutorial2](https://shaharmike.com/cpp/libclang/)
### LibTooling
- [LibTooling tutorial](https://clang.llvm.org/docs/LibTooling.html)

## example.cpp

```cpp
#include <iostream>
#include <string>

typedef int my_type_t;

// Example class with some member variables and functions
class ExampleClass {
	int userKurwa;
public:
    int publicVar;
private:
    float privateVar;
protected:
    std::string protectedVar;

public:
    ExampleClass() : publicVar(0), privateVar(0.0f), protectedVar("protected") {}
    ~ExampleClass() {}

    void publicFunction(int arg1, float arg2) {}
private:
    float privateFunction() { return 0.0f; }
protected:
    void protectedFunction() {}
};

// Example struct with some member variables and functions
struct ExampleStruct {
    int publicVar;
private:
    float privateVar;
protected:
    std::string protectedVar;

public:
    ExampleStruct() : publicVar(0), privateVar(0.0f), protectedVar("protected") {}
    ~ExampleStruct() {}

    void publicFunction(int arg1, float arg2) {}
private:
    float privateFunction() { return 0.0f; }
	ExampleStruct aaa;
	my_type_t bbbbb;
protected:
    void protectedFunction() {}
};

int ccccccc = 0;

int main() {
    ExampleClass obj1;
    ExampleStruct obj2;

    return 0;
}
```

## Output
```
............................................
All classes and structures contained in
#include <iostream>
#include <string>
...........................................

---
Class: ExampleClass
  Attributes: ['userKurwa', 'publicVar', 'privateVar', 'protectedVar']
  Methods: ['publicFunction', 'privateFunction', 'protectedFunction']
  Bases: []
  Is Abstract: (False,)
---
Struct: ExampleStruct
  Attributes: ['publicVar', 'privateVar', 'protectedVar', 'aaa', 'bbbbb']
  Methods: ['publicFunction', 'privateFunction', 'protectedFunction']
  Bases: []
  Is Abstract: (False,)
---
```
