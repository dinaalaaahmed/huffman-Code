f =open("input.txt", "r")

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
def addcode(Node,c,char):
    Node.code+=c;
    Node.code+=char;
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




def traverse(node,c):
        if (righ(node)== 0 and lef(node)==0 ):
            return
        if(lef(node)!=0):
          addcode(lef(node),c,"0")
          print(code(lef(node)))
          traverse(lef(node), code(lef(node)))
        if (righ(node)!= 0):
            addcode(righ(node),c,"1")
            print(code(righ(node)))
            traverse(righ(node), code(righ(node)))
encoding = {}
decoding = {}
def traverseandmap(node):
    if (righ(node) == 0 and lef(node) == 0):
        encoding[value(node)]=code(node)
        decoding[code(node)]=value(node)
        return
    if (lef(node) != 0):
        traverseandmap(lef(node))
    if (righ(node) != 0):
        traverseandmap(righ(node))


traverse(left,"")
traverseandmap(left)
for x in encoding:
    print(encoding[x]+x)

encode=""
for x in contents:
    encode+=encoding[x]


f=open("encoding.txt", "+w")
f.write(encode)

f=open("encoding.txt", "+r")
decode=f.read()

f=open("decoding.txt", "+w")

decodingstring=""
y="";
for x in decode:
    y+=x;
    if(y in decoding):
        decodingstring+=decoding[y];
        y=""


f.write(decodingstring)