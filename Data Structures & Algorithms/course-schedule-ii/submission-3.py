class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        visit, cycle = set(), set()

        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
        res = []
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True

        for course in range(numCourses):
            if not dfs(course): return []
        return res 
            
