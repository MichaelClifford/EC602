
class Polynomial():
    #Class that converts a sequence of values into a Polynomial representation (Ax^n+..+Zx^0) leveraging the Dictionary Data type
    
    #init method takes in a list of coefficintes and converts to a dictionary type 
    #object of the form {key:value} = {exponent:coeficeint}
    
    def __init__(self, coefficient):
        self.coefficient = coefficient
        self.poly = {}
        
        for i in range(len(coefficient)):
            if coefficient[i] == 0:
                pass
            else:
                self.poly[len(coefficient)-i-1] = coefficient[i]
        

    #method to get items out of Polynomial using keys values 
   
    def __getitem__(self,key):
        try:
            return self.poly[key]
        except:
            IndexError
            return 0
            
            
    #method to set coefficinets as long as they are non-zero.  
    
    def __setitem__(self,key, value):
        try:
            if value == 0:
                   del self.poly[key]
            else:
                  self.poly[key] = value
        except:
            KeyError
            pass
                
    #method to access the keys in in the Polynomial 
    
    def keys(self):
        return self.poly.keys()
    
    #method to access the ietmes in the Polynomial
    
    def items(self):
        return self.poly.items()
      
    # method for printing polynomial representation as dictionary   
    def __str__(self):
        return str(self.poly)
    
    # method to evalute the polynomial for a given value of x
    def eval(self,x):
        y = 0
        for i in self.poly.keys():
            y += self.poly[i]*x**i
        return y
    
    
    # method to perform a derivative 
    def deriv(self):
        dx = Polynomial([])
        for i in list(self.poly.keys()):
            if i == 0:
                pass
            else:
                dx[i-1] = self.poly[i]*i
        return dx

        
    # method to add two Polynomials using +
    
    def __add__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            if i in list(B.keys()):
                c[i] = B[i]+self[i]
            else:
                c[i] = self[i]
        for j in list(B.keys()):
            if j in list(self.keys()):
                c[j] = self[j] + B[j]
            else:
                c[j] = B[j]
        return c
            
    
    # Method for subtracting two Polynomials using -
    
    def __sub__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            if i in list(B.keys()):
                c[i] = B[i]-self[i]
            else:
                c[i] = self[i]
        for j in list(B.keys()):
            if j in list(self.keys()):
                c[j] = self[j] - B[j]
            else:
                c[j] = -B[j]
        return c
            
            
    #Method for Multiplying two Polynomials using *
    
    def __mul__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            for j in list(B.keys()):
                    if c[i+j] != None:
                        c[i+j] += self[i]*B[j]
                    else:
                        c[i+j] = self[i]*B[j]
        return c
    
    #Method for testing the equality of two Polynomials
    
    def __eq__(self,other):
        if self.poly == other.poly:
            return True
        else:
            return False
    
