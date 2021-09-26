class Solution:
    def decodedString(self, s):
        n = len(s)

        stackNum = []
        stackStr = []

        cur_str = ''
        cur_num = 0

        for c in s:

            if c == '[':
                stackStr.append(cur_str)
                stackNum.append(cur_num)

                cur_str = ''
                cur_num = 0

            elif c == ']':
                cur_str = stackStr.pop() + cur_str * stackNum.pop()

            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)

            else:
                cur_str += c
                cur_num = 0

        return cur_str
