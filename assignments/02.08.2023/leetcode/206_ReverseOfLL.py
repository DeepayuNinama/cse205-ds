from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev    