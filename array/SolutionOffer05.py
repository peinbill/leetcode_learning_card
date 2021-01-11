class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")

class Solution2:
    def replaceSpace(self, s: str) -> str:
        result = ""
        for i in s:
            if i==' ':
                result = result+"%20"
            else:
                result = result+i
        return result

if __name__=="__main__":
    solution=Solution2()
    print(solution.replaceSpace("We are happy."))