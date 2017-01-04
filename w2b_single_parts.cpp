// single_parts
#include <iostream>
#include <iomanip>

using namespace std;


typedef unsigned int raw32; // raw32 is a pseudonym for unsigined int

// a structure which mimics exactly the internal representaion of single
//single_parts uses 32-bits of storage


struct Single_Parts{

raw32 fraction : 23; // use 23 bits for this
raw32 exponent : 8; // use 8 bits for this 
raw32 sign : 1; //use 1 bit for this

};

// these represent the the posistions of the SIGN, EXPONENT and FRACTION of single. 

const raw32 MASK_SIGN = 1U << 31;
const raw32 MASK_BEXP = 0xffU << 23;
const raw32 MASK_FRAC = 0x7fffffU; 



// print out the parts of the structure Single_Parts
void print_sp(Single_Parts sp) 
{ 
  if (sp.sign==1)
         cout << "negative"  << endl;
  else 
        cout << "positive" << endl;

 cout << hex  
      << setfill('0') 
      << "expo: " << sp.exponent << endl
      << "frac: " << sp.fraction << endl
      << dec;
}

// define Single_Parts, build(), and take_apart() for float

Single_Parts take_apart(float s){

Single_Parts sp;

raw32 x= *reinterpret_cast<raw32*>(&s);

sp.sign = (x bitand MASK_SIGN) >> 31;
sp.exponent = (x bitand MASK_BEXP) >> 23;
sp.fraction = (x bitand MASK_FRAC);

return sp;

}


float build(Single_Parts sp){

  return *reinterpret_cast<float*>(&sp);
}



int main()
{

    float num_from_build;

    float numbers[5]={1.0/3,2,1.3e10,3e11,6};
    
    // show the structure of the numbers 
    for (int i=0;i<5;i++)
    {   
        // take apart the numbers, then re-build to test that it works.
        
        Single_Parts s = take_apart(numbers[i]);
        num_from_build = build(s);

        cout << endl;
        print_sp(s);
        cout << numbers[i] << " " << num_from_build  << endl;
    }

    // example of a weird number, negative zero.
    float neg_zero{-0.0};

    cout << endl; 
    cout << neg_zero << endl;

    print_sp(take_apart(neg_zero));

    return 0;
}
