# Assignment 1

**Task:**

The file dtree.py defines a function entropy which calculates the entropy of a dataset. Import this file along with the monks datasets and use it to calculate the entropy of the training datasets.

**Output:**
```
Entropy of monk1: 1.0
Entropy of monk2: 0.957117428264771
Entropy of monk3: 0.9998061328047111
```

# Assignment 2

**Task:**

Use the function averageGain (defined in dtree.py) to calculate the expected information gain corresponding to each of the six attributes. Note that the attributes are represented as instances of the class Attribute (defined in monkdata.py) which you can access via m.attributes[0], ..., m.attributes[5].

**Output:**
```
Information gain of monk1:
A1: 0.07527255560831925
A2: 0.005838429962909286
A3: 0.00470756661729721
A4: 0.02631169650768228
A5: 0.28703074971578435
A6: 0.0007578557158638421
Best attribute is: A5

Information gain of monk2:
A1: 0.0037561773775118823
A2: 0.0024584986660830532
A3: 0.0010561477158920196
A4: 0.015664247292643818
A5: 0.01727717693791797
A6: 0.006247622236881467
Best attribute is: A5

Information gain of monk3:
A1: 0.007120868396071844
A2: 0.29373617350838865
A3: 0.0008311140445336207
A4: 0.002891817288654397
A5: 0.25591172461972755
A6: 0.007077026074097326
Best attribute is: A2
```

**Question:**

Based on the results, which attribute should be used for splitting the examples at the root node?

**Answer:**
The attribute with the highest information gain.
```
A5 for monk1
A5 for monk2
A2 for monk3
```

# Assignment 3

**Task**

Split the monk1 data into subsets according to the selected attribute using the function select (again, defined in dtree.py) and compute the information gains for the nodes on the next level of the tree.

**Output**

```
Information gain of monk1 splitted on A5 = 1:
A1: 0.0
A2: 0.0
A3: 0.0
A4: 0.0
A5: 0.0
A6: 0.0
Best attribute is: A1

Information gain of monk1 splitted on A5 = 2:
A1: 0.040216841609413634
A2: 0.015063475072186083
A3: 0.03727262736015946
A4: 0.04889220262952931
A5: 0.0
A6: 0.025807284723902146
Best attribute is: A4

Information gain of monk1 splitted on A5 = 3:
A1: 0.03305510013455182
A2: 0.002197183539100922
A3: 0.017982293842278896
A4: 0.01912275517747053
A5: 0.0
A6: 0.04510853782483648
Best attribute is: A6

Information gain of monk1 splitted on A5 = 4:
A1: 0.20629074641530198
A2: 0.033898395077640586
A3: 0.02590614543498493
A4: 0.07593290844153944
A5: 0.0
A6: 0.0033239629631565126
Best attribute is: A1
```

**Question**
Which attributes should be tested for these nodes?

**Answer**
```
No attribute for A5 = 1 (the tree stops here and there are no information gains)
A4 for A5 = 2
A6 for A5 = 3
A1 for A5 = 4
```

**Task**
Build the full decision trees for all three Monk datasets using buildTree. Then, use the function check to measure the performance of the decision tree on both the training and test datasets.

**Output**
```
Error of monk1 on monk1test: 0.17129629629629628
Error of monk1 on monk1: 0.0

Error of monk2 on monk2test: 0.30787037037037035
Error of monk2 on monk2: 0.0

Error of monk3 on monk3test: 0.05555555555555558
Error of monk3 on monk3: 0.0
```
