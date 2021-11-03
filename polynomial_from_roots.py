import numpy as np
def Poly(l,a):
    n=a
    for i in range(a):
        l[i]=-l[i]
    matrix=np.zeros(shape=(a,2))
    for i in range(0,a):
        matrix[i][0]=1
        matrix[i][1]=l[i]

    poly=np.zeros(shape=(1,3))
    while(a>1):
        #print("size for a",a,"-->",np.size(poly))
        for i in range(0,np.size(matrix[0])):
            for j in range(0,2):
                poly[0][i+j]+=(matrix[0][i]*matrix[1][j])
                '''
                if(a==2):
                    print(matrix[0][i],"*",matrix[1][j],"index of poly-->",i+j)
                '''
        matrix=np.append(matrix,np.zeros(shape=(a,1)),axis=1)
        matrix[0]=poly
        for i in range(1,a-1):
            matrix[i]=matrix[i+1]
        matrix=np.delete(matrix,a-1,0)
        #print("lue of a:",a,matrix,"---->",poly)
        poly=np.zeros(shape=(1,np.size(matrix[0])+1))
        a-=1
    print("\nPolynomial matrix",matrix,"\n")
    return matrix[0]
def printPoly(poly, n):

    print("polynomial equation:")
    for i in range(n):
        print(poly[i], end = "");
        if (i != 0):
            print("x^", i, end = "");
        if (i != n - 1):
            print(" + ", end = "");
print("Enter the number in a single line separated by space:")
val = list(map(float,input().split(",")))
a=len(val)
poly=Poly(val,a)
n=np.size(poly)
printPoly(poly,n)

