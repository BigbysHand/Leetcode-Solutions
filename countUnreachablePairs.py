class Solution(object):
    def countPairs(self, n, edges):
        self.n = n
        length = len(edges)
        connected = False
        object = []
        unCon = 0

        #defines the distinct objects from edges
        for pairs in edges:
            temp = []
            for i in range(edges.index(pairs) + 1, len(edges) - 1):
                if(any(x in pairs for x in edges[i])):
                    connected = True
                    temp.append(edges[i][0])
                    temp.append(edges[i][1])
                    edges.remove(edges[i])

                 
            temp.append(pairs[0])
            temp.append(pairs[1])
            edges.remove(pairs)

            if connected:
                temp = list(dict.fromkeys(temp))
                temp.sort()
                object.append(temp)
            

        
        #appends the sungular objects to the obj array
        for i in range(n - length):
            object.append([0])
        print(object)
        #enumerates for the unconnected nodes
        for i, obj in enumerate(object[:-1]):
            for j, nextObj in enumerate(object[i + 1:]):
                unCon += len(obj) * len(nextObj)
            object.remove(obj)
        print()
        return unCon

sol = Solution()

sol.countPairs(6, [[0,1],[2,3],[4,5]])


# x = ([[0,1], [0, 2], [1, 2]])

# print(len(x))