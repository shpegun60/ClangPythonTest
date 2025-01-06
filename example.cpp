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
