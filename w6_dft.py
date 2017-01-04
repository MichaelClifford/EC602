from numpy import zeros,exp,array,pi

def DFT(x):
	try:

		if type(x) != str: 
	  
			N = len(x)
			ans = 1 + zeros((N,),dtype ="complex128")
			n = array((range(N)))
		    
			for k in range(N):
				ans[k] = round(sum(x*exp(-2j*pi*n*k/N)),10)
		    
			return ans

		else:
			raise ValueError("input must be be a sequence of numbers")

	except (TypeError):
		raise ValueError("input must be be a sequence of numbers")
