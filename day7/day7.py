lines = []
with open('./input.txt') as file:
    lines = [line.rstrip() for line in file]

# We want a tree-like structure
# tree structure

class Node:
    def __init__(self, data):
        self.children = []
        self.parent = data["parent"]
        self.name = data["name"]
        self.mem = 0
    def add_mem(self, mem):
        self.mem = self.mem + mem
    def add_child(self, child):
        self.children.append(child)
    def print(self):
        print(self.name + " has " + str(self.mem))

        
# If we see cd, switch current directory to whatever follows it
root = Node({"name": "root", 
            "parent": "none"
            })

curr_node = root

# Variables
curr_size = 0

# If statements for the different type of lines that can be encountered
for line in lines:
    if line[0:4] == "$ ls":
        curr_size = 0
    elif line[0:4] == "$ cd":
        if line[5:7] == "..":
            curr_node = curr_node.parent
            curr_node.add_mem(curr_size)
            curr_size = curr_node.mem
        elif line[5:6] == "/":
            print("start")
        else:
            new_node = Node({"name": line[5:], "parent": curr_node})
            curr_node.add_child(new_node)
            curr_node = new_node
    else:
        file = line.split()
        if file[0].isdigit():
            curr_size = curr_size + int(file[0])
            curr_node.add_mem(int(file[0]))

while not curr_node.parent == "none":
    curr_node = curr_node.parent
    curr_node.add_mem(curr_size)
    curr_size = curr_node.mem


# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
def tree_traversal_100K(node):
    size = 0
    child_list = node.children
    while not len(child_list) == 0:
        new_children = []
        for c in child_list:
            if int(c.mem) < 100000:
                size = size + c.mem
            new_children.extend(c.children)
        child_list = new_children                
    return size


print("100K: " + str(tree_traversal_100K(root)))

available_space = 70000000 - root.mem
needed_space = 30000000 - available_space

def tree_traversal_deletion(node, t):
    min = int(root.mem)
    child_list = node.children
    while not len(child_list) == 0:
        new_children = []
        for c in child_list:
            if int(c.mem) > needed_space and int(c.mem) < min:
                min = int(c.mem)
            new_children.extend(c.children)
        child_list = new_children                
    return min

print(needed_space)
print("Deletion size: " + str(tree_traversal_deletion(root, needed_space)))





