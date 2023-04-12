class Solution(object):
    def simplifyPath(self, path):
        #gen array split by "/"
        path_arr = path.split("/")
        #remove blanks
        iter_path = list(filter(lambda x: x != "", path_arr))
        #gen blank arr
        conPath = []
        #pass through iter_path
        for ele in iter_path:
            #if ele is "." continue
            if ele == ".":
                continue
            #if ".." try pop last thing in conPath
            elif ele == "..":
                try:
                    conPath.pop()
                except:
                    continue
            #else append
            else:
                conPath.append(ele)
        #ret "/" joined conPath with "/" at [0]
        return "/"+"/".join(conPath)
