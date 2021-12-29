from itertools import permutations

#checks if s
def isPermutation(s):
    a = permutations(s[::], len(s))
    for item in a:
        print(item)
#Permutation 
def myIsPermutation(s):
    if len(s) == 1:     #Base Case
        return [s]
    
    perms = myIsPermutation(s[1:])
    char = s[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])   #iterate through items and place char in every spot between them
    
    return result
