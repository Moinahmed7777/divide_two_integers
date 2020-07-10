# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:10:07 2020

@author: Necro
"""

def div(X,Y):
    if Y == -1 and X == -2147483648:
        return 2147483647
    
    X3=X
    Y3=Y
    X=abs(X)
    Y=abs(Y)
    countcum=0 
    count=1

    while (Y<=X):

        Y=Y<<1
        count=count<<1

        if Y>=X:
            Y=Y>>1
            count=count>>1
            X,Y=X-Y,abs(Y3)
            countcum+=count
            count=1
    if X3 <0 or Y3<0:
        if X3 <0 and Y3<0:
            return(countcum)
        else:
            return(-countcum)
    else:
        return(countcum)



def main():
    dividend = 10 
    divisor = 3
    Ans=(div(dividend,divisor))
    if Ans==3:
        print("Testcase for"," dividend ",dividend," divisor ", divisor,"passed")
    else:
        print("Testcase for"," dividend ",dividend," divisor ", divisor,"failed")
        
    dividend = 7 
    divisor = -3
    Ans=(div(dividend,divisor))
    if Ans==-2:
        print("Testcase for"," dividend ",dividend," divisor ", divisor,"passed")
    else:
        print("Testcase for"," dividend ",dividend," divisor ", divisor,"failed")
        
    
if __name__ == '__main__':

    main()