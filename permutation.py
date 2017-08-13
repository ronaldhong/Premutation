
#def permutation_2

def permutation(A, nun):
    lis=[]
    for i in A:
        for j in A:
          lis.append(i+j)
    print (lis)


permutation(['a','b','c','d','e'],2)
