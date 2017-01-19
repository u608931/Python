
# coding: utf-8

# In[7]:

import numpy as np
from scipy.optimize import minimize

def U(c1,c2,sign=1.0):
    return sign*(t*u(c1)+(1-t)*p*u(c2))


# In[10]:

def func_deriv(c1,c2,sign=1.0):
    dfdc1 = sign*(t*u)
    dfdc2 = sign*((1-t)*p*u)
    return np.array([dfdc1,dfdc2])
cons=({'type': 'ineq',
     'fun' : lambda c1: np.array([x-tc1])},
     {'type': 'ineq',
        'fun' : lambda c2: np.array([(1-t)*c2-(1-x)*R])})


# In[11]:

res = minimize(U, [-1.0,1.0], args=(-1.0,),
                method='SLSQP', options={'disp': True})

