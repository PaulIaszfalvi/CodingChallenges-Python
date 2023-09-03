#One Away
def oneAway(s1, s2):    
    if abs(len(s1) - len(s2)) > 1:
        print("Bigger than 1 difference")
        return False

    if s2 in s1:
        print("Found needle")
        return True

    counter_s2 = 0
    counter_difference = 0
    
    for i in range(len(s1)):
        if  s1[i + counter_difference] != s2[i]:
            counter_difference += 1

        if counter_difference > 1:
            return False
    
    print("One Away!")
    return True


print(oneAway("abcde", "abcde"))