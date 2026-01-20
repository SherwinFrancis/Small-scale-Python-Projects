def isValid(s):
        stack = []
        BDict = {")":"(","]":"[","}":"{"}

        if (s[0] == ")" or s[0] == "]" or s[0] == "}"):
            return False

        for i in s:
            if len(stack) != 0 and (i == ")" or i == "]" or i == "}") and BDict[i] != stack[-1]:
                return False
            elif len(stack) != 0 and (i == ")" or i == "]" or i == "}") and BDict[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if stack == []:
            return True
        else:
            return False
