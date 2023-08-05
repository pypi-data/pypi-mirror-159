from typing import Union
from scipy import sparse
import numpy as np
from scipy.sparse.linalg import norm
from time import time
from progressbar import progressbar
from psi_score.utils import l_plus_m, dict_to_sparse_matrix, X

def propagation_matrix(adjacency, ls, ms, lpms):
    N = len(adjacency)
    A = dict()
    B = {i: {} for i in range(N)}
    Deg = N*[0]
    c = []
    d = []
    for j in adjacency:
        A[j] = dict()
        for k in adjacency[j]:
            A[j][k] = ms[k] / lpms[j]
            B[j][k] = ls[k] / lpms[j]
            Deg[j] += 1
        if ls[j]+ms[j] == 0:
            c.append(0)
            d.append(0)
        else:
            c.append(ms[j]/(ls[j]+ms[j]))
            d.append(ls[j]/(ls[j]+ms[j]))

    A = dict_to_sparse_matrix(A, shape=(N, N))
    B = dict_to_sparse_matrix(B, shape=(N, N))
    c = np.array(c)
    d = np.array(d)
    Deg = np.array(Deg)
    return A, B, c, d, Deg

def power_newsfeed(A, b_i, Deg, n_iter=1000, tol=1e-6):
    p_i = b_i.copy()
    n_mult = 0
    n_msg = 0
    for _ in range(n_iter):
        p_i_old = p_i.copy()
        nnz_idx = np.where(p_i != 0)[0]
        n_msg += Deg[nnz_idx].sum()     
        p_i = A.dot(p_i) + b_i
        n_mult += 1
        gap = np.sum(abs(p_i - p_i_old))
        # gap = norm(p_i - p_i_old, ord=1)
        if gap < tol:
            return p_i, n_msg, n_mult
    raise RuntimeError(f'Power-NF error: failed to converge in {n_iter} iterations.')

def wall_steady_state(i, c, p_i, d):
    N = len(d)
    d_i = d[i]*X(i, N)
    q_i = c * p_i + d_i
    return q_i

def get_psi_score(
        adjacency: dict[list], ls: Union[list, np.ndarray], 
        ms: Union[list, np.ndarray], n_iter: int =1000, 
        tol: float =1e-6, solver: str ='power_psi'
    ) -> tuple:
    """ Solves the Psi-score problem with a chosen algorithm.

    Parameters
    ----------
    adjacency: dict[list]
        Adjacency list of the graph where edges go from followers to leaders.
    ls: Union[list, np.ndarray]
        Posting activity of each node.
    ms: Union[list, np.ndarray]
        Re-posting activity of each node.
    solver: str
        * ``'power_psi'``, power iterations for the Psi_score vector.
        * ``'power_nf'``, for each ``i`` it uses power iterations for the vector ``p_i``, the expected probabilities to find a post of origin ``i`` on other users' NewsFeeds.
        * ``'scipy'``, use the linear system solver from the scipy.sparse library.

    n_iter: int, optional
        Maximum number of iterations for Power-Psi and Power-NF, default=1000

    tol: float, optional
        Tolerance for the convergence of Power-Psi and Power-NF, default=1e-6

    Returns
    -------
    Psi: np.ndarray
        Psi-score vector
    t: float
        Computation time in seconds.
    n_msg: int or None
        Number of messages (or update in the Psi-score vector), ``None`` for the scipy solver.
    n_mult: int or None
        Number of matrix-vector multiplications to reach convergence, ``None`` for the scipy solver.
    
    References
    ----------
    * Giovanidis, A., Baynat, B., Magnien, C., & Vendeville, A. (2021). 
      Ranking Online Social Users by Their Influence. IEEE/ACM Transactions on Networking, 29(5), 2198–2214. 
      https://doi.org/10.1109/tnet.2021.3085201
    * Arhachoui, N., Bautista, E., Danisch, M., & Giovanidis, A. (2022). 
      A Fast Algorithm for Ranking Users by their Influence in Online Social Platforms. 
      arXiv preprint. https://doi.org/10.48550/ARXIV.2206.09960
    """

    N = len(adjacency)
    lpms = l_plus_m(adjacency, ls, ms)
    A, B, c, d, Deg = propagation_matrix(adjacency, ls, ms, lpms)
    t = time()
    n_mult = 0
    n_msg = 0

    if solver == 'scipy':
        P = sparse.linalg.spsolve((sparse.identity(N)-A).tocsc(), B.tocsc())
        Psi = 1/N * (P.T.dot(c) + d)
        t = time() - t
        return Psi, t

    elif solver == 'power_nf':
        t = time()
        Psi = []
        for i in progressbar(range(N)):
            b_i = B.dot(X(i, N))
            p_i, n_msg_i, n_mult_i = power_newsfeed(A, b_i, Deg, n_iter=n_iter, tol=tol)
            n_mult += n_mult_i
            n_msg += n_msg_i
            q_i = wall_steady_state(i, c, p_i, d)
            Psi.append(1/N * np.sum(q_i))

    elif solver == 'power_psi':
        At = A.T 
        s = c
        B_norm = norm(B, ord=1)
        for i in progressbar(range(n_iter)):
            s_old = s.copy()
            nnz_idx = np.where(s != 0)[0]
            n_msg += Deg[nnz_idx].sum()
            s = At.dot(s) + c
            n_mult += 1
            gap = sum(abs(s - s_old))
            gap = gap * B_norm
            if gap < tol:
                Psi = 1/N * (B.T.dot(s) + d)
                n_mult += 1
        if gap >= tol:
            raise RuntimeError(f'Power-Psi error: failed to converge in {n_iter} iterations.')
    
    else:
        raise ValueError('Unknown solver.')

    t = time() - t
    return Psi, t, n_msg, n_mult
