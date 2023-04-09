class Solution(object):
    def countPairs(self, n, edges):
        self.n = n

        unReach = 0
        length = len(edges)
        singular = False

        objects = []
        scanned = []

        #object check
        for i, edge in enumerate(edges):
            temp = []
            temp.append(edge)
            #print(temp)
            #print(edge[0], edge[1])
            for nextEdge in edges[i+1:]:
                if(any(x in nextEdge for x in temp)):
                    print(nextEdge)
                    node = list(value for value in nextEdge if value not in temp)
                    print(node[0])
                    if node != []:
                        temp.append(node[0])
                else:
                    continue
            objects.append(temp)
            scanned.append(edge)
            scanned.append(nextEdge)

        #print(objects)

                    #temp.append(x not in nextEdge for x in temp)
        
        #print(temp)

                    

            #print(temp)
        return unReach

sol = Solution()

sol.countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]])

