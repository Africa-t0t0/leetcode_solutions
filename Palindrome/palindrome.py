class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_ls = [item for item in str(x)]
        result = self.check_odd_or_even(x_ls)
        return result

    def check_odd_or_even(self, x_ls):
        large = len(x_ls)
        if large % 2 == 0:
            result = self.even_handler(x_ls)
        else:
            result = self.odd_handler(x_ls)
        return result

    def even_handler(self, x_ls):
        large = len(x_ls)
        aux = large // 2
        flag = False
        for i in range(large // 2 - 1, -1, -1):
            if x_ls[i] == x_ls[aux]:
                if i == 0:
                    flag = True
                    break
                aux += 1
            else:
                break
        return flag

    def odd_handler(self, x_ls):
        large = len(x_ls)
        aux = large // 2
        flag = False
        for i in range(large // 2, -1, -1):
            if x_ls[i] == x_ls[aux]:
                if i == 0:
                    flag = True
                    break
                aux += 1
            else:
                break
        return flag

x = [1,2,3,4,5,6]
x = [1,1,3,3,1,1]
x = [1,3,5,3,1]
large = len(x)

print(odd_handler(x))
