class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        # Solution 3 

        product, temp = 0, 0
        for i in bank:
            count = i.count('1')
            if count == 0:
                continue
            product += temp * count
            temp = count
        return product

        # Solution 2

        # product = temp = 0

        # for i in bank:
        #     count = 0
        #     for j in i:
        #         if j == '1':
        #             count += 1
        #     if temp == 0:
        #         temp = count
        #         continue
        #     elif count != 0:               
        #         product += temp * count
        #         temp = count
        
        # return product

        # Solution 1

        # devices = []
        # product = 0

        # for i in bank:
        #     count = 0
        #     for j in i:
        #         if j == '1':
        #             count += 1
        #     if count != 0:
        #         devices.append(count)

        # print(devices)
        
        # for i in range(1, len(devices)):
        #     product += devices[i] * devices[i-1]
       
        # return product