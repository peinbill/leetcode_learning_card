from typing import List
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.marked = [[False for i in range(self.n)] for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board,word,i,j):
                    return True
        return False



    def dfs(self,board:List[List[str]],word:str,i:int ,j:int)->bool:
        if i>self.m or j>self.n or j<0 or i <0:
            return False
        if self.marked[i][j]== True:
            return False

        if len(word)==0:
            return True

        if board[i][j]==word[0]:
            self.marked[i][j]=True
            if len(word)>1:
                word=word[1:]
            else:
                return True
            result = self.dfs(board,word,i+1,j) or self.dfs(board,word,i-1,j) or self.dfs(board,word,i,j+1) or self.dfs(board,word,i,j-1)
            self.marked[i][j]=False
            return result

        return False