# This function computes all permutations
def permute (a, lo):
  hi = len(a)
  if (lo == hi):
    print ('a',a)
  else:
    for i in range (lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permute (a, lo + 1)
      a[lo], a[i] = a[i], a[lo]
      

# This function computes all subsets of a list      
def subsets (a, b, lo):
  hi = len(a)
  if (lo == hi):
    print (b)
    return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1)
    subsets (a, b, lo + 1)


# This function computes all combinations of a given size
def combine (a, b, lo, size):
  hi = len(a)
  if (lo == hi):
    if (len(b) == size):
      print (b)
    return
  
  if (len(b) == size):
    print (b)
  else:
    c = b[:]
    b.append(a[lo])
    combine (a, c, lo + 1, size)
    combine (a, b, lo + 1, size)

    
def main ():
  a = ['A', 'B', 'C']  
  b= [1,2,3]
  c = []
  #permute (a, 0)
  subsets (b, c, 0)
  #combine(a,c,0,3)
main()
