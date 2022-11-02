from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ### 我的解法 ###
        # # 迴圈跑完list, 從第一個開始，count=1, 第二個和第一個比，如果相同，刪除他, 且removecount++
        # count = 0
        # remove_count = 0
        # i = 0
        # while i < len(nums):
        #     # print(i)
        #     if i + 1 < len(nums):
        #         if nums[i] == nums[i + 1]:
        #             remove_count += 1
        #             nums.remove(nums[i + 1])
        #             # print(nums)
        #             i -= 1
        #         else:
        #             count += 1  # 新增i這個項目
        #     else:
        #         count += 1
        #     i += 1
        # for i in range(remove_count):
        #     nums.append("_")
        #
        # print(nums)
        # return count

        #### 方法1: python指令 ###
        # # nums =  doesn't replace elements in the original list. creating a new list object
        # # nums[:] = replaces element in place
        # print(set(nums))
        # nums[:] = sorted(set(nums))
        # # print(nums)
        # return len(nums)

        #### 方法2: two pointer ###
        # # 有一個slow和fast指標，fast會遍歷所有index. slow只有在和fast不同時會往前一步(count+1的感覺)
        # # slow往前一步的同時，也把fast的內容存進來。除了排序，也方便做下一輪的比較。
        if not nums: return 0
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1

        #### 方法3: pop() ###
        # 跟我的解法滿類似，寫法清楚簡單許多。
        # i = 1
        # while i < len(nums):
        #     if nums[i] == nums[i - 1]:
        #         nums.pop(i)  # 這個i還要再跑一次，所以不用+1
        #     else:
        #         i += 1
        # print(nums)
        # return len(nums)


if __name__ == '__main__':
    myans = Solution()
    # print(myans.removeDuplicates([1,1,2]))
    print(myans.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
