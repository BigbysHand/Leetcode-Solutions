class Solution(object):
    def countPairs(self, n, edges):
        self.n = n
        length = len(edges)
        connected = False
        object = []
        unCon = 0
        i = 0

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

        if len(object) == 1:
            unCon = (n - length) * len(object)
            #print(len(edgesOG[0]))

        else:
            while i < len(object):
                unCon += len(object[i]) * ((len(object[i + 1]) + (n - length)))
                i += 1
                print(unCon)

        #print(unCon)
        print(object)
        
        return unCon

sol = Solution()

sol.countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]])


# x = ([[0,1], [0, 2], [1, 2]])

# print(len(x))