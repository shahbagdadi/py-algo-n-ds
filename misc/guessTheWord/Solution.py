class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        def pair_matches(a, b):        
                    return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [collections.defaultdict(int) for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][c] += 1
            return max(candidates, key=lambda x:sum(counts[i][c] for i, c in enumerate(x)))

        candidates = wordlist[:]        
        while candidates:
            s = most_overlap_word() 
            print(s)    
            matches = master.guess(s)
            if matches == 6:
                return
            candidates = [w for w in candidates if pair_matches(s, w) == matches]   # filter words with same matches