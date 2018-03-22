from tree import Tree
from memory_profiler import profile

# @profile
def starCubing(tree,cur_node,min_sup):
    tree_c = None
    if cur_node.value >= min_sup:
        if not cur_node.is_root():
            # print(cur_node.value)
            pass
        if cur_node.is_leaf():
            # print(cur_node.value)
            pass
        else:
            tree_c = Tree(cur_node.value, cur_node.name+'_tree')
            tree.add_node(tree_c)

    if not cur_node.is_leaf():
        starCubing(tree, cur_node.first_child(), min_sup)
    if tree_c is not None:
        starCubing(tree_c, tree_c, min_sup)
        tree.remove_node(tree_c)
    siblings = cur_node.has_sibling()
    if siblings is not None:
        if cur_node in siblings:
            siblings.remove(cur_node)
        for sibling in siblings:
            starCubing(tree, sibling, min_sup)

    return tree
