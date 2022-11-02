# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #### 我的迴圈(iterative)寫法  ####
        # 第一直覺的寫法是，兩個list依序比，最小的就放到新的list
        # cur = ListNode()
        # dummy = cur
        # # 只要L1或L2不是空的就繼續，若是空的，就直接接到linked list最尾端
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         cur.next = list1
        #         list1 = list1.next
        #     else:
        #         cur.next = list2
        #         list2 = list2.next
        #     cur = cur.next
        # if list1: # 如果list1中還有值，就接到最後面
        #     cur.next = list1
        # elif list2:
        #     cur.next = list2
        # dummy = dummy.next  #不然一開始會是0
        # return dummy

        #### 別人的遞迴(recursive)寫法  ####
        # 假設list1=[1,4],  list2=[2]
        # 我只要返回目前最小的值就好，剩下的交給下一回合去處理
        # 結束條件要先寫，不然不會停止。
        if list1 == None:  # 當list1為空，就把list2剩下的接到最尾巴。
            return list2
        if list2 == None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)  # 這裡會得到最後尾巴返回的值。我把它串接起來
            return list1  # 然後返回我自己，因為我是這個回合中最小的
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2