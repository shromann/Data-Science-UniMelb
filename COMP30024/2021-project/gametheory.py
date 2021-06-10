"""
Solver for single-stage, zero-sum matrix-form games using scipy default
linear programming routines.

Original by Matthew Farrugia-Roberts, 2021

Students
* please note this implementation is not guaranteed to be free of errors,
  for example it has not been extensively tested.
* please report bugs to <matt.farrugia@unimelb.edu.au>.
* please feel free adapt for your own use-case.
"""

import numpy as np
import scipy.optimize as opt

def solve_game(V, maximiser=True, rowplayer=True):
    """
    Given a utility matrix V for a zero-sum game, compute a mixed-strategy
    security strategy/Nash equilibrium solution along with the bound on the
    expected value of the game to the player.
    By default, assume the player is the MAXIMISER and chooses the ROW of V,
    and the opponent is the MINIMISER choosing the COLUMN. Use the flags to
    change this behaviour.

    Parameters
    ----------
    * V: (n, m)-array or array-like; utility/payoff matrix;
    * maximiser: bool (default True); compute strategy for the maximiser.
        Set False to play as the minimiser.
    * rowplayer: bool (default True); compute strategy for the row-chooser.
        Set False to play as the column-chooser.

    Returns
    -------
    * s: (n,)-array; probability vector; an equilibrium mixed strategy over
        the rows (or columns) ensuring expected value v.
    * v: float; mixed security level / guaranteed minimum (or maximum)
        expected value of the equilibrium mixed strategy.

    Exceptions
    ----------
    * OptimisationError: If the optimisation reports failure. The message
        from the optimiser will accompany this exception.
    """
    V = np.asarray(V)
    # lprog will solve for the column-maximiser
    if rowplayer:
        V = V.T
    if not maximiser:
        V = -V
    m, n = V.shape
    # ensure positive
    c = -V.min() + 1
    Vpos = V + c
    # solve linear program
    res = opt.linprog(
        np.ones(n),
        A_ub=-Vpos,
        b_ub=-np.ones(m),
    )
    if res.status:
        raise OptimisationError(res.message) # TODO: propagate whole result
    # compute strategy and value
    v = 1 / res.x.sum()
    s = res.x * v
    v = v - c # re-scale
    if not maximiser:
        v = -v
    return s, v


class OptimisationError(Exception):
    """For if the optimiser reports failure."""


if __name__ == "__main__":
    # Rock paper scissors example (row player, maximiser)
    print("test: rock paper scissors")
    RPS = np.array([
        [  0, -1, +1 ],
        [ +1,  0, -1 ],
        [ -1, +1,  0 ],
    ])
    print("game:", *RPS, sep="\n ")
    print("soln:", *solve_game(RPS))
    print("true:", np.array([1/3, 1/3, 1/3]), 0.0)
    print()

    print("test: textbook example")
    # Hespanha textbook example (column player, minimiser)
    A = np.array([
        [  3,  0 ],
        [ -1,  1 ],
    ])
    print("game:", A, sep="\n")
    print("soln:", *solve_game(A, maximiser=False, rowplayer=False))
    print("true:", np.array([1/5, 4/5]), 3/5)
    print()

    print("test: student example")
    V = np.array([[3, -1], [-1, -1]])
    print("game:", V, sep="\n")
    print("soln:", *solve_game(V, maximiser=True))
    print("true:", "(any strategy)         ", -1.0)
    print()
