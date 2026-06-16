class Solution(object):
    def processStr(self, s):
        result=[]
        for i in list(s):
            if i.islower():
                result.append(i)
            elif i=='*':
                if not result:
                    continue
                else:
                    result.pop()
            elif i=='#':
                result.extend(result)
            elif i=='%':
                result=result[::-1]
        return "".join(result)