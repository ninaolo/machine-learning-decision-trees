# Assignment 1

**Question:**

The file dtree.py defines a function entropy which calculates the entropy of a dataset. Import this file along with the monks datasets and use it to calculate the entropy of the training datasets.

**Output:**
```
Entropy of monk1test: 1.0
Entropy of monk2test: 0.9135964672699597
Entropy of monk3test: 0.9977724720899821
```

# Assignment 2

**Question:**

Use the function averageGain (defined in dtree.py) to calculate the expected information gain corresponding to each of the six attributes. Note that the attributes are represented as instances of the class Attribute (defined in monkdata.py) which you can access via m.attributes[0], ..., m.attributes[5].

**Output:**
```
Information gain of monk1test:
A1: 0.0
A2: 0.0
A3: 0.0
A4: 0.0
A5: 0.3112781244591327
A6: 0.0
Best attribute is: A5

Information gain of monk2test:
A1: 0.004305211728930836
A2: 0.004305211728930836
A3: 0.0006307506257382522
A4: 0.004305211728930836
A5: 0.005406547281522678
A6: 0.0006307506257382522
Best attribute is: A5

Information gain of monk3test:
A1: -1.1102230246251565e-16
A2: 0.3189814390160157
A3: 0.0
A4: 0.00448288653959783
A5: 0.34757342843558225
A6: 0.0
Best attribute is: A5
```

**Question:**

Based on the results, which attribute should be used for splitting the examples at the root node?

**Answer:**
The attribute with the highest information gain.
```
a5 for monk1test
a5 for monk2test
a5 for monk3test
```
