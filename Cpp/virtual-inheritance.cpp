#include <iostream>
#include <string>
using namespace std;

/*

          A (voice())
        |            |    
    B(voice())       C
               |
               D

*/

class A{
public:
virtual void voice(){
    cout << "This came from A" << endl;
    }    
};

class B: public virtual A{
public:
virtual void voice() override{
    cout << "This came from B" << endl;    
}
    };
    
class C: public virtual A{};
class D: public B, public C{};

int main(){
D d;
d.A::voice();
d.B::voice();
d.C::voice();
return 0;  
}
