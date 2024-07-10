# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10
"""
if folder, then add to stack, if ../ then pop from stack, if ./ then do nothing

"""
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        go_back = "../"
        do_nothing = "./"
        stack = []
        for log in logs:
            if log == go_back:
                if not stack:
                    continue
                stack.pop()
            elif log == do_nothing:
                pass
            else:
                stack.append(log)
        return len(stack)
