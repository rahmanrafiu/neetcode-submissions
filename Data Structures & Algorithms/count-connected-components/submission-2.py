class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        connect = {i:[] for i in range(n)}
        res = 0
        for a, b in edges:
            connect[a].append(b)
            connect[b].append(a)
        
        visit = set()

        def dfs(edge):
            visit.add(edge)
            for con in connect[edge]:
                if con not in visit:
                    dfs(con)

        for i in range(n):
            if i not in visit:
                dfs(i)   
                res += 1

        return res         

        