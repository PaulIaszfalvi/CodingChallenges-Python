class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

      # Second attempt
        ans = set()
        temp = s
        
        # If s itself is out of range
        if int(s) > finish:
            return 0
        
        # Add s if in range [start, finish]
        if int(s) >= start:
            ans.add(s)
        
        # Generate numbers while temp is less than finish
        while not ans or int(temp) < finish:
            temp = max(ans) if ans else s
            for i in range(1, limit + 1):
                new_num = str(i) + temp
                num_val = int(new_num)
                if num_val > finish:  # Stop if we exceed finish
                    break
                if num_val >= start:  # Only add if >= start
                    ans.add(new_num)
            # Break if no progress (no larger number added)
            if not any(int(x) > int(temp) for x in ans):
                break
        
        print(ans)
        return len(ans)

# First attempt

 l = len(s)
        ans = set()
        temp = s
        
        if int(s) > finish:
            return 0
        
        if int(s) > start:
            ans.add(s)

        while not ans or int(temp) < finish:
       
            temp = max(ans) if ans else s
            for i in range(1, limit + 1):
                new_num = str(i) + temp  
                if int(new_num) <= finish:  
                    ans.add(new_num)
                else:
                    break  
        
            if not any(int(x) > int(temp) for x in ans):
                break

        print(ans)
    
        return len(ans)
