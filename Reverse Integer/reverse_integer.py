class Solution:
    def reverse(self, x: int) -> int:
        values_ls = [char for char in str(x)]
        try:
            aux = int(values_ls[0])
        except:
            aux = values_ls[0]
            del values_ls[0]
            values_ls.append(aux)
        values_ls.reverse()
        final_value = int(''.join(values_ls))
        result = self.check_valid_range(final_value)
        return result

    @staticmethod
    def check_valid_range(value):
        if value <= pow(-2, 31) or value >= pow(2, 31) - 1:
            value = 0
            return value
        return value
