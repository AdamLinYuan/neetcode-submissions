class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        arr1, arr2 = self.toArr(num1), self.toArr(num2)
        res = self.mul(arr1, arr2)
        return str(res)
        
    def toArr(self, num: str):
        arr = []
        for n in num:
            arr.append(int(n))
        
        return arr[::-1]

    def mul(self, arr1, arr2):
        res = 0

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                res += (arr1[i] * 10**i) * (arr2[j] * 10**j)

        return res
        