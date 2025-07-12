class Solution:

    def maxArea(self, height: List[int]) -> int:
        return self.better_solution(height)

    @staticmethod
    def greedy_solution(height_ls: list) -> int:

        result_ls = list()

        for i in range(0, len(height_ls)):
            for j in range(0, len(height_ls)):
                max_value = min(height_ls[i], height_ls[j])
                index = abs(i - j)
                value = max_value * index
                result_ls.append(value)

        return max(result_ls)

    @staticmethod
    def greedy_solution2(height_ls: list) -> int:
        result = 0

        for i in range(0, len(height_ls)):
            for j in range(0, len(height_ls)):
                if i == j:
                    continue
                index = abs(i - j)
                max_value = min(height_ls[i], height_ls[j])

                value = max_value * index

                if value > result:
                    result = value
        return result

    @staticmethod
    def better_solution(height_ls: list) -> int:
        right_index = len(height_ls) - 1
        current_index = 0
        max_value = 0

        while True:
            if current_index == len(height_ls) - 1 or right_index == 0:
                return max_value

            current_height = min(height_ls[right_index], height_ls[current_index])
            current_distance = abs(current_index - right_index)
            current_value = current_height * current_distance

            if current_value > max_value:
                max_value = current_value

            if height_ls[right_index] < height_ls[current_index]:
                right_index -= 1
            else:
                current_index += 1
