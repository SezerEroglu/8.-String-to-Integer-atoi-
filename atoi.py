class Solution:
    def myAtoi(self, s: str) -> int:
        whiteSpaceEnd = 0
        digitStart = None
        digitEnd = None
        multiplier = None
        returnNumber = 0

        for i in range(len(s)):
            if s[i] == " " and digitStart is None:
                if multiplier is not None:
                    break
                whiteSpaceEnd += 1
            elif s[i].isdigit():
                if digitStart is None:
                    digitStart = i
                    if i > 1 and s[i - 1] == "-":
                        multiplier = -1
            elif digitStart is not None:
                digitEnd = i
                break
            elif (s[i] == "-" or s[i] == "+"):
                if multiplier is None:
                    if s[i] == "-":
                        multiplier = -1

                    elif s[i] == "+":
                        multiplier = 1
                else:
                    break

            elif digitStart is None:
                break

        if digitStart is not None:
            if digitEnd is None:
                digitEnd = len(s)
            if multiplier is None:
                multiplier = 1
            returnNumber = int(s[digitStart:digitEnd]) * multiplier
        else:
            return 0

        if returnNumber > 2**31 - 1:
            returnNumber = 2**31 - 1
        elif returnNumber < -(2**31):
            returnNumber = -(2**31)
        return returnNumber