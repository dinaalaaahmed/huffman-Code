# read from input file
f = open("input.txt", "r")

if f.mode == 'r':
    contents = f.read()

print(contents)

# declaring some variables
char = {}
encoding = {}
decoding = {}
decodingString = ""
node = []

# declaring frequency dictionary
for x in contents:
    if x in char:
        char[x] += 1

    else:
        char[x] = 1

for x in char:
    print(char[x])


# declaring class Node
class Node:
    def __init__(self, value, left, code, right, prop):
        self.value = value
        self.left = left
        self.right = right
        self.code = code
        self.prop=prop

# declaring some functions
def value(self):
    return self.value


def add_code(self, c, char):
    self.code += c
    self.code += char


def code(self):
    return self.code


def prop(self):
    return self.prop


def left_node(self):
    return self.left


def right_node(Node):
    return Node.right

# making array of chars
for x in char:
    node1 = Node(x, 0, "", 0, char[x])
    node.append(node1)

# sort the array of chars with probability
sorted_with_prop = sorted(node, key=prop, reverse=True)

for x in sorted_with_prop:
    print(value(x))

node = sorted_with_prop

# make the huffmanCode tree

while True:
    left = node.pop()
    print(value(left)+"left")
    if len(node) == 0:
        print(value(left)+"done")
        break
    right = node.pop()
    print(value(right)+"right")
    node2 = Node(value(left)+value(right), left, "", right, prop(left)+prop(right))
    print(value(node2))
    node.append(node2)
    sorted_with_prop = sorted(node, key=prop, reverse=True)
    node = sorted_with_prop

# declare codes to each char in the tree

def traverse(node,c):
    if right_node(node) == 0 and left_node(node) == 0:
        return
    if left_node(node) != 0:
        add_code(left_node(node), c, "0")
        print(code(left_node(node)))
        traverse(left_node(node), code(left_node(node)))
    if right_node(node) != 0:
        add_code(right_node(node), c, "1")
        print(code(right_node(node)))
        traverse(right_node(node), code(right_node(node)))

# get codes of each char in tree and put it encoding and decoding dictionary
def traverse_and_map(node):
    if right_node(node) == 0 and left_node(node) == 0:
        encoding[value(node)] = code(node)
        decoding[code(node)] = value(node)
        return
    if left_node(node) != 0:
        traverse_and_map(left_node(node))
    if right_node(node) != 0:
        traverse_and_map(right_node(node))


traverse(left, "")
traverse_and_map(left)

for x in encoding:
    print(encoding[x]+x)

encode = ""

# encode the input file

for x in contents:
    encode += encoding[x]


f = open("encoding.txt", "+w")
f.write(encode)

f = open("encoding.txt", "+r")
decode = f.read()

f = open("decoding.txt", "+w")


y = ""

# decode the encoded file

for x in decode:
    y += x
    if y in decoding:
        decodingString += decoding[y]
        y = ""


f.write(decodingString)
