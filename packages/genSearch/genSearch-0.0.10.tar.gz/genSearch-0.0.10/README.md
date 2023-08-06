# Primitive Genetic Search Algorithm

## Overview

Given a function, `decoder`, that establishes a bijection between solution-type objects and bitstrings of a given length, and a `cost` function, which maps solution-type objects to real numbers, this algorithm optimizes the `cost` function.

### Connection to Evolution
This algorithm solves problems by modeling evolutionary competition. Elements in a problem's domain are mapped to bitstrings, analogous to DNA sequences, via `decoder`. A random population is generated and winners are chosen via tournaments using each individual's `cost` as its "fitness" (lower fitness wins). Winners then reproduce: offspring are generated selecting from two winners' bits (genes), and occassionally switching them, analogous to mutation. The algorithm iterates this process a set number of times. When done, it returns the best individual of the final generation.

<br>

## Installation

Activate your virtual environment and run:
> `pip install genSearch`

<br>

## Usage

The algorithm is contained in the function:
>`genetic_simulation(decoder, cost)`
<p>
which returns as a tuple an object that minimizes `cost` and `cost` evaluated at this input.
<p>
Here is an example of the algorithm in action to find the square root of 2 on the interval [0, 10]:

```
import genSearch

# bitstring to value in [0, 10]
def decoder(x):
    # Convert to base 10 equivalent
    xbase10 = int(x, 2)
    # Find the number divisions of the interval
    resolution = 2**len(x)
    # Return value scaled to interval
    return 10 * xbase2 / resolution

# function to be minimized
def cost(num):
    return (num**2 - 2)**2

solution = genSearch.genetic_simulation(decoder, cost)

print(f"Solution: {solution[0]}")
print(f"Cost: {solution[1]}")

```


To use this algorithm, first import the package into the working python project using

>`import genSearch`
<br>

Then, define a `decoder` which converts binary strings to objects in the domain of `cost`, and a `cost` which assigns a real number to objects in its domain. The object type of the domain is to be defined by clients according to the problem at hand.
<p>

<br>

Once these parameters are defined, you can run the function and store its result:

```
import genSearch

def decoder(x):
    ...
    return object

def cost(object):
    ...
    return cost 


result = genSearch.genetic_simulation(decoder, cost)
```
<p>

Note that `result[0]` contains the approximate solution to your problem and `solution[1]` contains the cost associated with this solution.

<br>

## Hyperparameters

The simulation is controlled by the following variables.
```
## Population size
N_POP = 100  
## Bitstring length      
N_LEN = 64         
## Crossover rate     
R_CROSS = 0.5    
## Bit mutation rate       
R_MUT = 1.0 / N_LEN
## Number of generations      
N_GEN = 100       
```
<br>

Clients may access and modify these via the following:

```
# N_POP
genSearch.getPop()
genSearch.setPop(new_x)

# N_LEN
genSearch.getLen()
genSearch.setLen(new_x)

# R_Cross
genSearch.getCross()
genSearch.setCross(new_x)

# R_Mut
genSearch.getMut()
genSearch.setMut(new_x)

# N_Gen
genSearch.getGen()
genSearch.setGen(new_x)
```

The setter functions return `True` upon execution. 

<br>


## Credit

This package is inspired by [Jason Brownlee's algorithm](https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/). This package reorganizes and simplifies his algorithm to facilitate versatile use.
