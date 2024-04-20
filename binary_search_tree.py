class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        if self.root.data is None:
            self.root.data = data
        else:
            def insert_to_vertex(data, vertex):
                if data < vertex.data:
                    if vertex.left is None:
                        vertex.left = Node(data)
                    else:
                        insert_to_vertex(data, vertex.left)
                elif data > vertex.data:
                    if vertex.right is None:
                        vertex.right = Node(data)
                    else:
                        insert_to_vertex(data, vertex.right)
            insert_to_vertex(data, self.root)

    def remove(self, data):
        def remove_from_vertex(data, vertex):
            if vertex is None:
                return vertex
            if data < vertex.data:
                vertex.left = remove_from_vertex(data, vertex.left)
            elif data > vertex.data:
                vertex.right = remove_from_vertex(data, vertex.right)
            else:
                if vertex.left is None:
                    temp = vertex.right
                    return temp
                elif vertex.right is None:
                    temp = vertex.left
                    return temp
                temp = find_min(vertex.right)
                vertex.data = temp.data
                vertex.right = remove_from_vertex(vertex.data, vertex.right)
            return vertex

        def find_min(vertex):
            while vertex.left:
                vertex = vertex.left
            return vertex

        self.root = remove_from_vertex(data, self.root)


    def display(self):
        result = ""

        def vlr(result, vertex):
            if vertex:
                if vertex.data:
                    result += str(vertex.data) + " "
                    result = vlr(result, vertex.left)
                    result = vlr(result, vertex.right)
            return result

        def lvr(result, vertex):
            if vertex:
                if vertex.data:
                    result = lvr(result, vertex.left)
                    result += str(vertex.data) + " "
                    result = lvr(result, vertex.right)
            return result

        def lrv(result, vertex):
            if vertex:
                if vertex.data:
                    result = lvr(result, vertex.left)
                    result = lvr(result, vertex.right)
                    result += str(vertex.data) + " "
            return result

        print(vlr(result, self.root))
        print(lvr(result, self.root))
        print(lrv(result, self.root))


bst = BST()
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(8)
bst.insert(7)
bst.insert(99)
bst.display()

print("\n")

bst.remove(8.5)
bst.display()
