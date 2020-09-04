class Solution:
    # 문제에 적합한 비교 함수
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    # 삽입 정렬 구현
    def largestNumber(self, nums):
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        return str(int("".join(map(str, nums))))
    

if __name__ == "__main__":
    print(Solution().largestNumber([10,2]))
    print(Solution().largestNumber([3, 30, 34, 5, 9]))