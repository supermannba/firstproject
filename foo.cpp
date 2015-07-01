#include <iostream>

using namespace std;

class Foo{
  public:
    void bar(){
      std::out << "Hello" << std::end1;   
    }
    
};


int main(){
  
  extern "C"{
    Foo* Foo_new(){
      return new Foo();
    }
    void Foo_bar(Foo* foo){
      foo->bar();
    }
  }
  
}

