class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # Solution 3 

        trusts = {}
        unique = set()
      
        for x in trust:         
            trusts[x[0]] = trusts.get(x[0], set())
            trusts[x[0]].add(x[1])
           
        print(trusts)
       
        for key, val in trusts.items():
            print(key, val)
            unique ^= val    
        print(unique)
        
        try:
            unique = unique.pop()
        except:
            return -1

        try:
            if not trusts[unique]:
                pass
        except:
            return unique
        
        return -1

        # A different way 

        trusts = {}  # Dictionary to store the trust relationships
        
        # Initialize a set containing all people in the town
        all_people = set(range(1, n + 1))
        
        for trustee, trusted in trust:
            trusts[trustee] = trusts.get(trustee, set())  # Initialize with empty set if not present
            trusts[trustee].add(trusted)  # Add the trusted person to the set of people trusted by the trustee
        
        # Calculate the set difference to find people who trust no one
        trust_no_one = all_people - set(trusts.keys())
        
        # If there is more than one person who trusts no one, or there are no people who trust no one, return -1
        if len(trust_no_one) != 1:
            return -1
        
        judge = trust_no_one.pop()  # Get the only person who trusts no one
        
        # Check if the judge is trusted by everyone else
        for person, trusted_people in trusts.items():
            if judge not in trusted_people:
                return -1
        
        return judge  # Return the judge if found


        # Fastest online solution

        in_degree = [0] * (N + 1)
        out_degree = [0] * (N + 1)
        for a in trust:
            out_degree[a[0]] += 1
            in_degree[a[1]] += 1
        for i in range(1, N + 1):
            if in_degree[i] == N - 1 and out_degree[i] == 0:
                return i
        return -1

        # Solution 2

        trusts = {}  # Dictionary to store the trust relationships
        trust_count = [0] * (n + 1)  # List to count the number of people trusting each person

        # Populate the trust relationships and count the trust counts
        for a, b in trust:
            trust_count[b] += 1  # Person b is trusted by someone
            trusts[a] = trusts.get(a, set())  # Initialize with empty set if not present
            trusts[a].add(b)  # Add person b to the set of people trusted by person a

        # Find the judge: someone who is trusted by everyone else and trusts no one
        for person in range(1, n + 1):
            if trust_count[person] == n - 1 and person not in trusts:
                return person

        return -1  # No judge found

        # Solution 1 (incomplete)
               
        trusts = {}
        vals = set()

        for x in trust:         
            trusts[x[0]] = trusts.get(x[0], x[1])
            vals.add(x[1])

        print(trusts)
       
        for key, val in trusts.items():
            print(key, val)
            try:
                if trusts[val]:
                   pass
            except: 
                 return val if len(vals) == 1 else -1

        return -1