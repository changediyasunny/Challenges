"""
Given a source and a target node for a n-ary tree find the distance between them.
Having a parent will allow you to get to a solution without traversing entire tree.
Bonus: How would the solution be if the TreeNode was defined as below:

getDistance(A, G) ==> 2
getDistance(M, H) ==> 5
getDistance(C, L) ==> 3
getDistance(B, M) ==> 2


                   A
              /  /  \  \
            B   F   D   E
           / \      |   / | \
           K  J      G  C  H  I
          / \                 \
         N   M                 L
"""

class TreeNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.children = []
        self.parent = parent

    def __repr__(self):
        return self.val

def dfs(root, val):
    stack = [(root, [])]
    while stack:
        curr, path = stack.pop()
        if curr.val == val:
            return path + [val]
        for nei in curr.children:
            stack.append((curr, path + [nei.val]))
    return []

def bfs(root, key):
    queue = [(root, [])]
    visited = {root}
    while queue:
        curr, path = queue.pop(0)
        if curr == key:
            return path + [key]

        for nei in curr.children:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, path + [curr]))
    return []

def lca(root, n1, n2):
    path_to_n1 = bfs(root, n1)
    path_to_n2 = bfs(root, n2)

    lca_node = None
    for p1, p2 in zip(path_to_n1, path_to_n2):
        if p1 != p2:
            break

        lca_node = p1

    return lca_node

# Method 1
def distance_DSF(root, n1, n2):
    # Get the path to n1 and n2 using children nodes
    path_to_n1 = set(bfs(root, n1))
    path_to_n2 = set(bfs(root, n2))
    print(path_to_n1)
    print(path_to_n2)
    # Distance will be unique nodes are path of the Union
    return len(path_to_n1.union(path_to_n2) - path_to_n1.intersection(path_to_n2))

def distsance_DFS_parent(root, n1, n2):
    # Get distance between n1 and n2 using BFS
    def helper(n1, n2):
        queue = [(n1, [])]
        visited = {n1}

        while queue:
            curr, path = queue.pop(0)
            if curr == n2:
                return path + [n2]

            neighbors = curr.children + [curr.parent]
            for nei in neighbors:
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, path + [curr]))
        return []

    path = helper(n1, n2)
    # Return distance -1 because we need to the number of edges in the path
    return len(path) - 1 if path else 0

def distance_LCA(root, n1, n2):
    # dist(n1, n2) = dist(root, n1) + dist(root, n2) - 2 * dist(root, lca(n1, n2))
    path_to_n1 = bfs(root, n1)
    path_to_n2 = bfs(root, n2)
    lca_node = lca(root, n1, n2)
    path_to_lca = bfs(root, lca_node)

    return (len(path_to_n1) - 1 if len(path_to_n1) else 0) + \
           (len(path_to_n2) - 1 if len(path_to_n2) else 0) - \
           2 * (len(path_to_lca) - 1 if len(path_to_lca) else 0)

def create_tree():
    root = TreeNode('A')
    # Level 1 nodes
    B = TreeNode('B', root)
    F = TreeNode('F', root)
    D = TreeNode('D', root)
    E = TreeNode('E', root)

    root.children = [B, F, D, E]
    # Level 2 nodes
    K = TreeNode('K', B)
    J = TreeNode('J', B)
    G = TreeNode('G', D)
    C = TreeNode('C', E)
    H = TreeNode('H', E)
    I = TreeNode('I', E)

    B.children = [K, J]
    D.children = [G]
    E.children = [C, H, I]
    # Level 3 nodes
    N = TreeNode('N', K)
    M = TreeNode('M', K)
    L = TreeNode('L', I)

    K.children = [N, M]
    I.children = [L]

    # Method 1
    print(distance_DSF(root, M, H))


create_tree()
