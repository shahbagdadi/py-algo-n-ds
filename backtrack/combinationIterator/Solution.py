
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.n = combinationLength
        self.i = 0
        self.ans = []
        self.permute(0,'')
        # print(self.ans)


    def permute(self,start, s):
        if len(s) == self.n:
            self.ans.append(s)
        for i in range(start, len(self.c)):
            self.permute(i + 1, s + self.c[i]),


    def next(self) -> str:
        ans = self.ans[self.i]
        self.i += 1
        return ans


    def hasNext(self) -> bool:
        return self.i < len(self.ans)

ci = CombinationIterator('abcd',2)
while ci.hasNext():
    print(ci.next())