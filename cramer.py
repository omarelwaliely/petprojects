import numpy as np
import copy

def isFloat(var):
    try:
        float(var)
    except ValueError:
        return False
    return True

def determinant(A, currentdet=0):
    if len(A) == 1 and len(A[0]) == 1:
        val = A[0][0]
        return val
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for currentcol in range(len(A)): 
        Acop = copy.deepcopy(A[1:])
        for i in range(len(Acop)): 
            Acop[i] = Acop[i][0:currentcol] + Acop[i][currentcol+1:] 
        sign = (-1) ** (currentcol % 2) 
        sub = determinant(Acop)
        currentdet += sign * A[0][currentcol] * sub
    return currentdet

def main():
    number = input("Enter how many equations do you have: ")
    while not (number.isnumeric()):
        number = input(f"Please re-enter, that was not a possible number: ")
    number = int(number)
    A = np.empty(shape=[number, number+1])
    B = []
    B.append(np.empty(shape = [number,number]))
    for i in range(number):
        B.append(np.empty(shape = [number,number]))
        for j in range((number)+1):
            if(j == number):
                x = input(f"Please enter b{i+1}{i+1}: ")
            else:
                x = input(f"Please enter A{i+1}{j+1}: ")
            while not isFloat(x):
                x = input(f"Please re-enter, that was not a valid number: ")
            A[i,j] = x
    for i in range(number+1):
        k=0
        for j in range(number):
            if(i!= j):
                B[i][:,k] = A[:,j]
                k = k+1
            else:
                B[i][:,k] = A[:,number]
                k = k+1
    adet =  determinant(B[number].tolist())
    if(adet == 0):
        print("The Matrix you inputted is not invertible!")
        return
    k=0
    print("\nHere is the Solution:")
    for i in range (number):
        ans = determinant(B[i].tolist()) / adet
        print(f"a{k}= {ans}")
        k = k+1
    return
main()