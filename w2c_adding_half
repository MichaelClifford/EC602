from math import inf

def number_from_half(s : str):
    """return the number represented by s, a binary16 stored as a 4-character hex number"""
    
    numb = int(s,16)
    sign = (numb & 0x8000) >> 15
    exp = ( numb & 0x7c00) >> 10
    frac = (numb & 0x3ff);
    
    if exp == 0b00000:
        ans = (-1)**(sign)*2**(-14)*((2**(-10))*frac)
    elif exp == 0b11111:
        ans == 'inf'
    else:
        ans = (-1)**(sign)*2**(exp-15)*(1+(2**-10)*frac)
    
    return ans

def main():
    """add all binary16 numbers from standard input until a non-number is entered, then print the total.
    Numbers are represented in 4-character hex string format, one per line"""
    ans = 0
    x = 1
    
    try:
        while x == 1:
            ans += number_from_half(input())
    except:
        ValueError

    print(ans)
    return ans 


if __name__ == '__main__':
    main()
