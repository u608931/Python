{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The Simulation of Bank Run"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this part we run a simple simulation.\n",
    "The original model was written by C. Yenko."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import random\n",
    "import matplotlib.pyplot as plt\n",
    "import plotly.plotly as py\n",
    "from plotly.graph_objs import *\n",
    "import math\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "interestRate = 0.2\n",
    "# Some initial interest rate must be set, otherwise the trial would not work. \n",
    "maxWithdrawals = 70\n",
    "# The maximum number of people (out of 100) who may withdraw their money without the bank has to close.\n",
    "numTrials = 100\n",
    "# The total number of simulations made; during each of them the bank either close or not."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then we write the general simulation code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def runTrial(interestRate,maxWithdrawals,initialInvestment):\n",
    "        numWithdrawals = 0\n",
    "        # The initial number of withdrawals is 0. \n",
    "        # It increases by 1 with each person who decides during any round to withdraw.\n",
    "        withdrawParameter = 0\n",
    "        # This parameter increases with every withdrawal. \n",
    "        # Higher the parameter is, higher is the current risk aversion of every person.\n",
    "        peopleList = []\n",
    "        for i in range(0,100):\n",
    "            peopleList.append([random.normalvariate(.5,.5/3),0,i])\n",
    "        # The People List contains personal data of every person out of 100.\n",
    "        # [0] The first number is a random risk parameter with mean=0.5 and SD=(0.5/3).\n",
    "        # [1] The second one determines whether the person has already decided to withdraw (1) or not (0).\n",
    "        # [2] At the third position is \"i\" - a number in range 0-99 which serves as a personal ID.\n",
    "        for roundNum in range (0,3):\n",
    "        # There are 3 rounds of each simulation, in the Diamond&Dybvig paper described as periods T=0,1,2.\n",
    "            if numWithdrawals < maxWithdrawals:\n",
    "            # A condition necessary for each round; if not satisfied the bank has already closed.\n",
    "                for person in peopleList:\n",
    "                    if numWithdrawals < maxWithdrawals:\n",
    "                        if not person[1] == 1:\n",
    "                        # Check if this person has still her investment in bank.\n",
    "                        # I.e. this person has not withdrawn in previous rounds.\n",
    "                            num = random.random()\n",
    "                            # Return a random number in range [0.0, 1.0).\n",
    "                            currentRiskAversionParam = person[0]+withdrawParameter-interestRate\n",
    "                            # It is different for each person because of the random risk parameter.\n",
    "                            # It also varies between rounds as the withdraw parameter may change.\n",
    "                            if num < currentRiskAversionParam:\n",
    "                            # Then this person withdraws.\n",
    "                                numWithdrawals = numWithdrawals + 1\n",
    "                                person[1]=1\n",
    "                                # Ensure this person may not participate in following rounds.\n",
    "                                withdrawParameter = numWithdrawals/100\n",
    "                                # So that the parameter is higher for every following person and round.\n",
    "        if numWithdrawals < maxWithdrawals:\n",
    "            return 0\n",
    "        else:\n",
    "            return 1\n",
    "        # This loop runs after the whole trial (3 rounds with 100 persons).\n",
    "        # The trial counts for 1 in case that the bank had to close during it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "x = []\n",
    "y = []\n",
    "for inc in range(0,100,1):\n",
    "        interestRate = float(inc)/100\n",
    "        # The interest rate gradually increases from 0.00 to 0.99.\n",
    "        closeSum = 0\n",
    "        for i in range(0,numTrials):\n",
    "            closeSum = closeSum + runTrial(interestRate,maxWithdrawals,initialInvestment)\n",
    "            # This variable sums the total number of trials when the bank had to close.\n",
    "        fractionClose = float(closeSum)/numTrials\n",
    "        x.append(interestRate)\n",
    "        y.append(fractionClose)\n",
    "        # Both the interest rate and the fraction of closed banks are added to lists representing x and y axis."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nTkSuQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0xe200208>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(x,y)\n",
    "plt.xlabel(\"interest Rate\")\n",
    "plt.ylabel(\"Bank closure % (out of 100 trials)\")\n",
    "plt.title(\"interest Rate vs. Bank Closure\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "x = []\n",
    "y = []\n",
    "for inc in range(0,100,1):\n",
    "        interestRate = 0.2\n",
    "        # The interest rate is now fixed again.\n",
    "        maxWithdrawals = inc\n",
    "        # The maximum number of withdrawals gradually icreases from 0 to 99.\n",
    "        closeSum = 0\n",
    "        for i in range(0,numTrials):\n",
    "            closeSum = closeSum + runTrial(interestRate,maxWithdrawals,initialInvestment)\n",
    "        fractionClose = float(closeSum)/numTrials\n",
    "        x.append(maxWithdrawals)\n",
    "        y.append(fractionClose)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "plt.plot(x,y)\n",
    "plt.xlabel(\"Maximum of withdrawals until closure\")\n",
    "plt.ylabel(\"Bank closure % (out of 100 trials)\")\n",
    "plt.title(\"Max Withdrawals vs. Bank Closure\")\n",
    "plt.show()"
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
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}

# Analyzing and extending the Diamond and Dybvig model with some insights from Behavioural Economics"
   
#Final assignment for the Course Applied Economic Analysis, 31/01/2017"
  
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

 
