Python

#Motivation

We start from the assumptions of the paper by Diamond and Dybvig to develop a few extensions to their theoretical model that seem to fit the observed mechanisms of bank runs. Specifically, we considered that some insights from behavioral economics that use a hyperbolic discounting factor might help to improve the quality of the standard model on bank runs. An improved model of bank runs will make it possible for banks and/or policy makers to act in times of financial distress. Moreover, we decided to use Python as the main platform to develop our work because it is a great tool to formalize our mathematical formulations and visually explore our results. 
We will begin with a description of the standard model by making ad hoc use of variables and constraints to solve the optimization problem of allocation and consumption in different time periods. We will show that banks provide improved distribution efficiency than autarky, but bank runs equilibria are also possible, which are potential catastrophes and much worse than autarky.

#Extending the existing model using some insights from behavioural economics
So far we explained and simulated the standard Diamond and Dybvig model without making any assumption about the discounting technique used.Indeed, the authors do not specify the functional form of their discount factor, and we could assume that they use exponential discounting, the standard model which implies consistent preferences over time. Although this is the most commonly used model in economics because of its simplicity, other models have shown to describe the empirical reality better (Frederik et al., 2002). 
Exponential discounting assumes that the marginal rate of substitution between consumption in different time periods is only dependent on the time interval between the two time periods. In other words, the discount rate should be constant over time: 1 / (1+K)t. However, empirical studies such as Thaler (1981) show that often people show time inconsistent tendencies. Most people prefer $50 today to $55 tomorrow while preferring $55 in 366 days to $50 in 365 days. Behavioral economists developed the hyperbolic discounting model to incorporate this human tendency for time inconsistent behavior. In this model, the discounting factor depends on both the length of the delay and on the timing of the delay. As a result, hyperbolic discounting discounts future rewards more than exponential discounting for short delays but less for long delays. This makes it more useful to predict actual human behavior.
As Diamond and Dybvig (1983) pointed out, bank runs can occur due to self-fulfilling expectations of the behavior of other individuals. Hyperbolic discounting and time inconsistent models try to capture the variations in degree of patience across time. 
To get a better empirical description of bank runs it might be beneficial to incorporate the hyperbolic discounting assumption. It might be possible that individuals after learning their type at T=1 still behave contrary to their type.
Our model should be therefore integrated as follows:

Max U(c1;c2) = [tu(c1) + (1 -t)*p*u(c2)]

With
 p=1/1+kD
 
Where k is a parameter that indicates the degree of discounting and D is the number of weeks of delay. This is the hyperbolic discounting factor.
On the other hand, the exponential discounting factor used in time consistent models is p'=e^(-kD)
We use Python to evaluate these two functional specifications and compare the resulting discounting factors. We assume k=1 for simplicity.
The discounting factor of next week (n=1) with respect to today(n=0) for the exponential discounting is 
e^(-1)/e(^-0)=1/e
The discounting factor of 12 weeks from now (n=12) with respect to 11 weeks from now (n=11)is 
e^(-12)/e^(-11)=1/e
So this is what we mean by "consistent preferences"= constant delta of discount factor for the same time span (one week)
However, with hyperbolic discounting we can see that the discounting factor of next week with respect to today is 1/(1+1)/(1/(1)=0,5, while the discounting factor of 12 weeks from now with respect to 11 weeks is (1/13)/(1/12)=12/13=0,92
We can see that for low Ds, that is for a short time delay, the discounting factor is similar, but as we increase D, the hyperbolic discounting factor tends to 1, so the present value of a reward in the far future is almost zero according to hyperbolic discounting.




| weeks | d_exp | d_hyper |
|-------|-------|---------|
| 1     | 0,367 | 0,5     |
| 2     | 0,367 | 0,66    |
| 12    | 0,367 | 0,923   |
| 40    | 0,367 | 0,975   |
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def U(c1,c2,sign=1.0):\n",
    "    return sign*(t*u(c1)+(1-t)*p*u(c2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-40-c87ebcad174e>, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-40-c87ebcad174e>\"\u001b[0;36m, line \u001b[0;32m7\u001b[0m\n\u001b[0;31m    'jac' : lambda x: np.array([-t, 1.0]))\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def func_deriv(c1,c2,sign=1.0):\n",
    "    dfdc1 = sign*(t*u)\n",
    "    dfdc2 = sign*((1-t)*p*u)\n",
    "    return np.array([dfdc1,dfdc2])\n",
    "cons=({'type': 'ineq',\n",
    "     'fun' : lambda x: np.array([x-tc1])\n",
    "     'jac' : lambda x: np.array([-t, 1.0])]\n"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [conda root]",
   "language": "python",
   "name": "conda-root-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
