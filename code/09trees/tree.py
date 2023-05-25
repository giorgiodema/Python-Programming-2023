import string

class Node:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

def read_tree(path):
    f = open(path,"r")
    root = None

    it = iter(f)
    try:
        parents = list(next(it))
        parents = [(i,x) for i,x in enumerate(parents)]
        parents = list(filter(lambda x: x[1].isalnum(),parents))
        parents = [(Node(x[1],None,None),x[0]-1,x[0]+1) for x in parents]
        # root
        root = parents[0][0]
        
        while True:
            links = list(next(it))
            while len(list(filter(lambda x:x.isalnum(),links)))==0:
                parents = [(e[0],e[1]-1 if e[1] else None,e[2]+1 if e[2] else None) for e in parents]
                for i in range(len(parents)):
                    if parents[i][1]!=None:
                        if len(links)<=parents[i][1]+1 or links[parents[i][1]+1]!="/":
                            parents[i] = (parents[i][0],None,parents[i][2])
                    if parents[i][2]!=None:
                        if len(links)<=parents[i][2]-1 or links[parents[i][2]-1]!="\\":
                            parents[i] = (parents[i][0],parents[i][1],None)
                    
                links = list(next(it))

            childrens = links
            childrens = [(i,x) for i,x in enumerate(childrens)]
            childrens = list(filter(lambda x: x[1].isalnum(),childrens))
            childrens = [(Node(x[1],None,None),x[0]-1,x[0]+1) for x in childrens]
            for p in parents:
                left  = list(filter(lambda c:p[1]==c[1]+1,childrens)) if p[1]!=None else None
                right = list(filter(lambda c:p[2]==c[2]-1,childrens)) if p[2]!=None else None
                left = left[0][0] if left else None
                right = right[0][0] if right else None
                p[0].left = left
                p[0].right = right
            parents = childrens

    except StopIteration:
        return root


if __name__=="__main__":
    r = read_tree("./ex02.txt")
    print()