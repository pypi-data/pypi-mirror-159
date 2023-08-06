"""Various useful functions"""
from itertools import permutations

def tree_list(m):
    """
    Return the list of all possible lineage trees given m mutations,
    that is, a number of (m+1)**(m-1) trees in tuple form.
    """
    if m == 0: return [((),)]
    def trees(nodes):
        if len(nodes) == 1: return [[[nodes[0]]] + [[]]*m]
        if len(nodes) >= 2:
            treelist, current, child = [], nodes[:-1], nodes[-1]
            for oldtree in trees(current):
                for parent in [0] + current:
                    newtree = [oldtree[i].copy() for i in range(m+1)]
                    newtree[parent].append(child)
                    treelist.append(newtree)
            return treelist
    treeset = set()
    for nodes in permutations(range(1,m+1)):
        for tree in trees(list(nodes)):
            for i in range(m+1):
                tree[i].sort()
                tree[i] = tuple(tree[i])
            treeset.add(tuple(tree))
    tree0 = (tuple(range(1,m+1)),) + ((),)*m
    treelist = [tree0] + list(treeset - {tree0})
    return treelist


# Tests
if __name__ == '__main__':
    print(tree_list(2))
