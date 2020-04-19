import numpy as np
import mathplotlib.pyplot as plt


pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2

ppoints, qpoints = 200, 200

max_iterations = 300

infinity_border = 10

image = np.zeros((ppoints, qpoints))
