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
Average information gain of monk1test:
a1: 0.0
a2: 0.0
a3: 0.0
a4: 0.0
a5: 0.3112781244591327
a6: 0.0

Average information gain of monk2test:
a1: 0.004305211728930836
a2: 0.004305211728930836
a3: 0.0006307506257382522
a4: 0.004305211728930836
a5: 0.005406547281522678
a6: 0.0006307506257382522

Average information gain of monk3test:
a1: -1.1102230246251565e-16
a2: 0.3189814390160157
a3: 0.0
a4: 0.00448288653959783
a5: 0.34757342843558225
a6: 0.0
```
