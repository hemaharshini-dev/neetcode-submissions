class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for word in words for c in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break


        visit = set()
        path = set()
        res = []

        def dfs(c):
            
            if c in path:
                return False

            if c in visit:
                return True

            path.add(c)

            for nei in adj[c]:
                if not dfs(nei):
                    return False

            path.remove(c)
            visit.add(c)
            res.append(c)

            return True

        for c in adj:
            if not dfs(c):
                return ""

        res.reverse()
        return "".join(res)