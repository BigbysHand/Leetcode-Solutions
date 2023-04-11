class Solution(object):
    def isIsomorphic(self, s, t):
        linked = list(zip(s, t))

        if (len(set(linked)) != len(set(s)) or (len(set(linked)) != len(set(t)))):
            return False
        
        print(len(set(linked)))

        return True
            
sol = Solution()

# print(sol.isIsomorphic("badc", "baba"))

#4
#2
s = "badc"
t = "baba"

map1 = []
map2 = []
for idx in s:
    print(idx)
    map1.append(s.index(idx))
for idx in t:
    map2.append(t.index(idx))
if map1 == map2:
    print(True)
print(False)

print(map1, map2)


# a = [1, 5, 2, 6]
# print(a[:0])

        # mark_s, mark_t = 0, 0
        # #since len(s) == len(t)
        # for i in range(1, len(s)):
        #     #if current s and t val been passed before add a mark
        #     if s[i] in s[:i]:
        #         mark_s += 1
        #     if t[i] in t[:i]:
        #         mark_t += 1
        # #if marks are same ret True
        # if mark_t == mark_s:
        #     return True
        # #else marks not same ret False
        # else:
        #     return False