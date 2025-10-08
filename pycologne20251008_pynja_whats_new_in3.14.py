from __future__ import annotations

import itertools


# look at separates repository

# Josh Comeau
# friendly-introduction-to-svg


# this was not possible before python 3.14
class A:
    def f(self)->A:
        return A()

# never nester
t=[[0,5],[1,2,3],[]]
for a in itertools.product(*t):
    pass

# black as code formatter

# typst as new latex alternative