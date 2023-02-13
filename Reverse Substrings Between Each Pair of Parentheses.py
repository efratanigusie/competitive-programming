class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        tmp = ''
        for char in s:
            if char == '(':
                stack.append(tmp)
                tmp = ''
            elif char == ')':
                tmp = stack.pop() + tmp[::-1]
            else:
                tmp += char
        return tmp
