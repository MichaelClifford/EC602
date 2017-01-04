# include <vector>


using namespace std;

typedef vector<double> Poly;// defining a type "Poly that is a vector of doubles"

// each element of the vector is sum number, N is the length of the vector
// the start at index[N-1]X^N-1+...+index[1]X^1 + Index[0] 

# include <vector>
# include <string>

using namespace std;

typedef vector<double> Poly;
typedef string BigInt;

//1 Convert big ints into polys:


Poly BI_to_Po(const BigInt &a){
	

	Poly b;
	b.resize(a.length());
	int p = 0;
	for(int e = a.length()-1; e >= 0; e--) {
		b[p++] = a[e] - 48;
	}
	return b;
}

BigInt Po_to_BI(const Poly &a){

	BigInt b;
	b.resize(a.size());
	int p = 0;

	for (int e = a.size()-1; e>=0; e--){

		b[p++] = a[e]+48;
	}

		return b;
}


Poly multiply_poly(const Poly &a,const Poly &b){

	Poly A = a; 
	Poly B = b;
	Poly C(A.size()+B.size()-1,0); 

	for(int i = 0; i < A.size(); i++){       //for i in A
		for(int j = 0; j < B.size(); j++){     // for j in B
			C[j+i] += A[i]*B[j];
			

		//itertae through A and multiply each element of B and

		}
	
}
return C;
}

BigInt multiply_int(const BigInt &a, const BigInt &b){

Poly av = BI_to_Po(a);
Poly bv = BI_to_Po(b);
Poly cv = multiply_poly(av,bv);

int carry = 0;
for(int i = 0; i< cv.size();i++){

	cv[i] += carry;
	carry = (int) cv[i]/10;
	cv[i] = (int)cv[i]%10; 

}

while(carry >0){
	cv.push_back(carry%10);
	carry -= 10;
}

return Po_to_BI(cv);

}
