class Tree(object):

    def __init__(self, value, name='root', children=None):
        self.name = name
        self.value = value
        self.parent = None
        self.children = []
        if children is not None:
            for child in children:
                self.add_node(child)

    def depth(self):
        stree = self
        depth = 0
        while len(stree.children) > 0:
            stree = stree.first_child()
            depth += 1
        return depth

    def first_child(self):
        assert len(self.children) > 0
        return self.children[0]

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        return False

    def is_root(self):
        if self.name == 'root':
            return True
        return False

    def add_node(self, node):
        assert isinstance(node, Tree)
        node.parent = self
        self.children.append(node)

    def get_item(self,item):
        for child in self.children:
            if child.name == item:
                return child
        return None

    def add_to_node(self,item,count):
        for child in self.children:
            if child.name == item:
                child.value += count
                return child
        child = Tree(count,item)
        child.parent = self
        self.children.append(child)
        return child

    def has_sibling(self):
        if self.parent is not None:
            siblings = self.parent.children
            return siblings
        return None

    def remove_node(self,node):
        if node in self.children:
            self.children.remove(node)
