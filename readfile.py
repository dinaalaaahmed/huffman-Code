from queue import PriorityQueue
Tree = PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list.
f=open("guru99.txt", "w")
f.write("HIIIIbla")
f =open("guru99.txt", "r")
if f.mode == 'r':
    contents = f.read()

print(contents)
char = {}

for x in contents:
        if x in char:
            char[x]+=1

        else:
            char[x]=1

for x in char:
    print(char[x])

class Node:
    def __init__(self, value, left ,code,right,prop):
        self.value = value
        self.left = left
        self.right = right
        self.code = code
        self.prop=prop;
def value(Node):
    return Node.value
def addcode(Node,c):
    Node.code+=c;
def code(Node):
    return Node.code
def prop(Node):
    return Node.prop
def lef(Node):
    return Node.left
def righ(Node):
    return Node.right
node=[]
for x in char:
    node1=Node(x,0,"",0,char[x]);
    node.append(node1)
sorted_with_prop=sorted(node, key= prop,reverse=True)

for x in sorted_with_prop:
    print(value(x))
node=sorted_with_prop;

while True:
    left = node.pop()
    print(value(left)+"left")
    if(len(node)==0):
        print(value(left)+"done")
        break
    right = node.pop()
    print(value(right)+"right")

    node2=Node(value(left)+value(right),left,"",right,prop(left)+prop(right))
    print(value(node2))
    node.append(node2)
    sorted_with_prop = sorted(node, key=prop, reverse=True)
    node=sorted_with_prop



def traverse(node):
    if(lef(node)!=0and righ(node)!=0):
        if(lef(node)!=0):
          addcode(lef(node),"0")
          print(code(lef(node)))
        if (righ(node)!= 0):
            print(code(righ(node)))
            addcode(righ(node),"1")
        traverse(lef(node))
        traverse(righ(node))
    else:
        return

traverse(left)








