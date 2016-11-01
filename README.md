# ML Decision Trees
This is a lab assignment in a machine learning course at KTH. Assignment questions and corresponding answers are listed below.

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

**Task:**

Split the monk1 data into subsets according to the selected attribute using the function select (again, defined in dtree.py) and compute the information gains for the nodes on the next level of the tree.

**Output:**

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

**Question:**

Which attributes should be tested for these nodes?

**Answer:**

```
No attribute for A5 = 1 (the tree stops here and there are no information gains)
A4 for A5 = 2
A6 for A5 = 3
A1 for A5 = 4
```

**Task:**

Build the full decision trees for all three Monk datasets using buildTree. Then, use the function check to measure the performance of the decision tree on both the training and test datasets.

**Output:**

```
Error of monk1 on monk1test: 0.17129629629629628
Error of monk1 on monk1: 0.0

Error of monk2 on monk2test: 0.30787037037037035
Error of monk2 on monk2: 0.0

Error of monk3 on monk3test: 0.05555555555555558
Error of monk3 on monk3: 0.0
```

# Assignment 4

**Task:**

Write code which performs the complete pruning by repeatedly calling allPruned and picking the tree which gives the best classifiction performance on the validation dataset. You should stop pruning when all the pruned trees perform worse than the current candidate.

**Output:**

```

------------------------------------------------------
Performance of monk1 tree on monk1test: 0.8287037037037037

Pruning monk1 with fraction = 0.3 and performance on new validation set = 0.7586206896551724
Found pruned tree which performed better: 0.8045977011494253
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.75

Pruning monk1 with fraction = 0.4 and performance on new validation set = 0.8
Found pruned tree which performed better: 0.8
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.7777777777777778

Pruning monk1 with fraction = 0.5 and performance on new validation set = 0.7741935483870968
Found pruned tree which performed better: 0.8225806451612904
Found pruned tree which performed better: 0.8709677419354839
Found pruned tree which performed better: 0.8709677419354839
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.8055555555555556

Pruning monk1 with fraction = 0.6 and performance on new validation set = 0.78
Found pruned tree which performed better: 0.8
Found pruned tree which performed better: 0.8
Found pruned tree which performed better: 0.8
Found pruned tree which performed better: 0.8
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.75

Pruning monk1 with fraction = 0.7 and performance on new validation set = 0.8421052631578947
Found pruned tree which performed better: 0.9210526315789473
Found pruned tree which performed better: 0.9210526315789473
Found pruned tree which performed better: 0.9210526315789473
Found pruned tree which performed better: 0.9210526315789473
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.7777777777777778

Pruning monk1 with fraction = 0.8 and performance on new validation set = 0.76
Found pruned tree which performed better: 0.84
Found pruned tree which performed better: 0.84
Found pruned tree which performed better: 0.84
Found pruned tree which performed better: 0.84
Found pruned tree which performed better: 0.84
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.8148148148148148

0.3: 0.75
0.4: 0.7777777777777778
0.5: 0.8055555555555556
0.6: 0.75
0.7: 0.7777777777777778
0.8: 0.8148148148148148

------------------------------------------------------
Performance of monk2 tree on monk2test: 0.6921296296296297

Pruning monk2 with fraction = 0.3 and performance on new validation set = 0.5546218487394958
Found pruned tree which performed better: 0.5966386554621849
No more ways to prune tree. Returning.
Performance of best pruned tree on test set: 0.6712962962962963

Pruning monk2 with fraction = 0.4 and performance on new validation set = 0.5392156862745098
Found pruned tree which performed better: 0.6470588235294118
No more ways to prune tree. Returning.
Performance of best pruned tree on test set: 0.6712962962962963

Pruning monk2 with fraction = 0.5 and performance on new validation set = 0.6
Found pruned tree which performed better: 0.6235294117647059
No more ways to prune tree. Returning.
Performance of best pruned tree on test set: 0.6712962962962963

Pruning monk2 with fraction = 0.6 and performance on new validation set = 0.5735294117647058
Found pruned tree which performed better: 0.6176470588235294
Found pruned tree which performed better: 0.6617647058823529
Found pruned tree which performed better: 0.6911764705882353
Found pruned tree which performed better: 0.7058823529411765
Found pruned tree which performed better: 0.7058823529411765
Found pruned tree which performed better: 0.7058823529411765
Found pruned tree which performed better: 0.7058823529411765
Found pruned tree which performed better: 0.7058823529411765
Found pruned tree which performed better: 0.7058823529411765
Found pruned tree which performed better: 0.7058823529411765
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.6412037037037037

Pruning monk2 with fraction = 0.7 and performance on new validation set = 0.45098039215686275
Found pruned tree which performed better: 0.5490196078431373
No more ways to prune tree. Returning.
Performance of best pruned tree on test set: 0.6712962962962963

Pruning monk2 with fraction = 0.8 and performance on new validation set = 0.5588235294117647
Found pruned tree which performed better: 0.6470588235294118
No more ways to prune tree. Returning.
Performance of best pruned tree on test set: 0.6712962962962963

0.3: 0.6712962962962963
0.4: 0.6712962962962963
0.5: 0.6712962962962963
0.6: 0.6412037037037037
0.7: 0.6712962962962963
0.8: 0.6712962962962963

------------------------------------------------------
Performance of monk3 tree on monk3test: 0.9444444444444444

Pruning monk3 with fraction = 0.3 and performance on new validation set = 0.8255813953488372
Found pruned tree which performed better: 0.8255813953488372
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.8287037037037037

Pruning monk3 with fraction = 0.4 and performance on new validation set = 0.8918918918918919
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.9722222222222222

Pruning monk3 with fraction = 0.5 and performance on new validation set = 0.819672131147541
Found pruned tree which performed better: 0.8360655737704918
Found pruned tree which performed better: 0.8524590163934426
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.8888888888888888

Pruning monk3 with fraction = 0.6 and performance on new validation set = 0.8775510204081632
Found pruned tree which performed better: 0.9183673469387755
Found pruned tree which performed better: 0.9387755102040817
Found pruned tree which performed better: 0.9591836734693877
Found pruned tree which performed better: 0.9795918367346939
Found pruned tree which performed better: 0.9795918367346939
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.9722222222222222

Pruning monk3 with fraction = 0.7 and performance on new validation set = 0.918918918918919
Found pruned tree which performed better: 0.918918918918919
Found pruned tree which performed better: 0.918918918918919
Found pruned tree which performed better: 0.918918918918919
Found pruned tree which performed better: 0.918918918918919
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.9722222222222222

Pruning monk3 with fraction = 0.8 and performance on new validation set = 0.92
Found pruned tree which performed better: 1.0
Found pruned tree which performed better: 1.0
Found pruned tree which performed better: 1.0
Found pruned tree which performed better: 1.0
All pruned trees perform worse. Stopping here.
Performance of best pruned tree on test set: 0.9722222222222222

0.3: 0.8287037037037037
0.4: 0.9722222222222222
0.5: 0.8888888888888888
0.6: 0.9722222222222222
0.7: 0.9722222222222222
0.8: 0.9722222222222222
```

**Task:**

Evaluate the effect pruning has on the test error for the monk1 and monk3 datasets, in particular determine the optimal partition into training and pruning by optimizing the parameter fraction. Plot the classification error on the test sets as a function of the parameter fraction ∈ {0.3, 0.4, 0.5, 0.6, 0.7, 0.8}.

**Output:**

Run the function `plotFractionErrorRelationship()`.
