"""FluffyClone simulation module"""
import numpy as np

class Simulation:
    """
    Run a simulation and store the results.
    """
    def __init__(self, t, a, b, e, ld, xi, sg, gm, tree=None):
        # Get a sample from the model
        sample = get_sample(t, a, b, e, ld, xi, sg, gm, tree=tree)
        x, y, z, r, clone, allel, wrate = sample
        # Store the main random variables
        self.x, self.y, self.z, self.r = x, y, z, r
        # Store useful biological quantities
        self.clone, self.allel, self.wrate = clone, allel, wrate

def random_step(state, weight):
    """
    Make one step of random walk on the weighted graph defined by weight.
    This is an intermediate function in Wilson's method for simulating
    random spanning trees from the weighted uniform distribution.

    NB: here we construct an in-tree so all directions are reversed
    """
    p = weight[:,state]/np.sum(weight[:,state])
    return np.nonzero(np.random.multinomial(1, p))[0][0]

def loop_erasure(path):
    """
    Compute the loop erasure of a given path.
    This is an intermediate function in Wilson's method for simulating
    random spanning trees from the weighted uniform distribution.
    """
    if path[0] == path[-1]: return [path[0]]
    else: i = np.max(np.arange(len(path))*(np.array(path)==path[0]))
    if path[i+1] == path[-1]: return [path[0], path[i+1]]
    else: return [path[0]] + loop_erasure(path[i+1:])

def random_tree(w, root=0):
    """
    Generate a random spanning tree from the weighted uniform distribution
    using Wilson's method, given a weighted digraph adjacency matrix w.

    Random forests associated with the FluffyClone model correspond to
    such random spanning trees with root 0. More precisely, a forest with
    m vertices corresponds to a weight matrix w with shape (m+1,m+1)
    and particular entries w0[:,0] = 0 and w0[0,1:] = 1.

    NB: w must be a zero-diagonal square matrix with nonnegative entries
    """
    m = w.shape[0]
    tree = [[] for i in range(m)]
    v = {root} # Vertices of the tree
    r = list(set(range(m)) - v) # Remaining vertices
    np.random.shuffle(r) # Random order
    r = list(r)
    # Main loop of Wilson's method
    while len(r) > 0:
        state = r[0]
        path = [state]
        # compute a random path that reaches the current tree
        while path[-1] not in v:
            state = random_step(path[-1], w)
            path.append(state)
        path = loop_erasure(path)
        # Append the loop-erased path to the current tree
        for i in range(len(path)-1):
            v.add(path[i])
            r.remove(path[i])
            tree[path[i+1]].append(path[i])
    for i in range(m): tree[i].sort()
    return tuple([tuple(tree[i]) for i in range(m)])

def random_forest(w):
    """
    Generate a random forest from the weighted uniform distribution
    using Wilson's method, given a weighted digraph adjacency matrix w.
    The result is a tuple u representing a spanning tree rooted at 0,
    or equivalently a forest u[1:] where u[0] is the list of roots.

    Notes:
    - w[0,:], w[:,0] and w diagonal entries are ignored
    - all other entries must be nonnegative
    """
    w0 = w - np.diag(np.diag(w))
    w0[0] = 1
    w0[:,0] = 0
    return random_tree(w0)

def adjacency_matrix(tree):
    """
    Return the adjacency matrix of a tree given in tuple or dictionary form.
    """
    if type(tree) is dict:
        m = max([max(children) for children in tree.values()]) + 1
        z = np.zeros((m,m), dtype=int)
        for i, children in tree.items():
            for j in children:
                z[i,j] = 1
    if type(tree) is tuple:
        m = len(tree)
        z = np.zeros((m,m), dtype=int)
        for i in range(m):
            for j in tree[i]:
                z[i,j] = 1
    return z

def dict_from_adjacency(z):
    """
    Return the adjacency list of a tree given its adjacency matrix.
    The output is a dictionary x where x[i] is the children set of node i.
    """
    m = z[0].size
    tree = {}
    for i in range(m):
        children = []
        for j in range(m):
            if z[i,j] == 1: children.append(j)
        if len(children) > 0:
            tree[i] = set(children)
    return tree

def tuple_from_adjacency(z):
    """
    Return the adjacency list of a tree given its adjacency matrix.
    The output is a tuple x where x[i] is the children list of node i,
    itself in the form of a tuple arranged in ascending order.
    """
    m = z[0].size
    tree = []
    for i in range(m):
        children = []
        for j in range(m):
            if z[i,j] == 1: children.append(j)
        tree.append(tuple(children))
    return tuple(tree)

def cov_brownian(t):
    """
    Covariance matrix of the standard brownian motion (Wiener process).
    """
    n = len(t)
    cov = np.zeros((n,n))
    for k in range(n):
        cov[k:,k] = t[k]
        cov[k,k:] = t[k]
    return cov

def get_sample(t, a, b, e, ld, xi, sg, gm, tree=None):
    """
    Sample (x,y,z) from the model and return useful intermediate quantities.
    If a tree is provided then the prior parameter e is ignored.
    """
    m, n = ld.shape[0], t.shape[0]
    # Sample Z and get the reachability matrix
    if tree is None:
        tree = random_forest(np.exp(e))
    z = adjacency_matrix(tree)
    r = np.linalg.inv(np.eye(m) - z).astype(int)
    # Sample Y
    y = np.zeros((m,n))
    mean, cov = np.zeros(n-1), cov_brownian(t[1:])
    for i in range(m):
        y[i,1:] = sg[i] * np.random.multivariate_normal(mean, cov)
    # Sample X
    clone = np.zeros((m,n)) # Clone sizes
    allel = np.zeros((m,m,2)) # Allelic quantities
    wrate = np.zeros((m,m,n,2)) # Contribution rates
    for i in range(m):
        clone[i] = xi[i] * np.exp((ld[i] - (sg[i]**2)/2)*t + y[i])
        for j in range(1,m):
            allel[i,j] = gm[j] * (a[j]*(1-r[j,i]) + b[j]*r[j,i])
            for k in range(n):
                wrate[i,j,k] = allel[i,j] * clone[i,k]
    x = np.random.poisson(np.sum(wrate, axis=0))
    # Return main random variables and useful biological quantities
    return x, y, z, r, clone, allel, wrate


# Tests
if __name__ == '__main__':
    # Tuple form
    tree = ((3,), (), (), (1, 2))
    z = adjacency_matrix(tree)
    print(tuple_from_adjacency(z))
    # Dictionary form
    tree = {0: {3}, 3: {1, 2}}
    z = adjacency_matrix(tree)
    print(dict_from_adjacency(z))
    # Covariance
    t = np.linspace(0, 4, 5)
    print(cov_brownian(t))
    # Trees
    w = np.ones((5,5))
    print(random_forest(w))
    # Sampling
    t = np.linspace(0, 1, 10)
    a = np.array([[0,0],[2,0],[2,0],[2,0]])
    b = np.array([[0,0],[1,1],[1,1],[1,1]])
    e = 100*(2*z - 1)
    ld = np.array([0,-5,7,-7])
    xi = np.array([50,30,1,100])
    sg = np.array([1,1,1,1])
    gm = np.array([0,1,1,1])
    sim = Simulation(t, a, b, e, ld, xi, sg, gm)
    print(sim.z)
    print(dict_from_adjacency(adjacency_matrix(random_tree(w))))
