import random
import monkdata as m
import dtree as d
import matplotlib.pyplot as pyplot

class DataSet:
    def __init__(self, dataset, name):
        self.dataset = dataset
        self.name = name


testSets = [DataSet(m.monk1test, "monk1test"),
            DataSet(m.monk2test, "monk2test"),
            DataSet(m.monk3test, "monk3test")]

trainingSets = [DataSet(m.monk1, "monk1"),
                DataSet(m.monk2, "monk2"),
                DataSet(m.monk3, "monk3")]


def partition(data, fraction):
    """ Partition data according to a given fraction and return a test and validation set. """
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def calculateEntropyOfTrainingSets():
    """ Assignment 1: Calculate the entropy of the different training sets. """
    for set in trainingSets:
        print("Entropy of " + set.name + ": " + str(d.entropy(set.dataset)))
    print("")


def calculateAverageInformationGainOfTrainingSets():
    """ Assignment 2: Calculate the information gains of the different training sets. """
    for set in trainingSets:
        printInformationGainOfDataset(set.dataset, set.name)


def splitOnA5AndComputeInformationGainsOfSubsets():
    """ Assignment 3: Split on attribute 5 (A5) and compute the gains of the subsets. """
    a5 = m.attributes[4]

    for set in trainingSets:
        for attributeValue in a5.values:
            subset = d.select(set.dataset, a5, attributeValue)
            printInformationGainOfDataset(subset, set.name + " splitted on A5 = " + str(attributeValue))


def printInformationGainOfDataset(dataset, name):
    print("\nInformation gain of " + name + ":")
    for i in range(len(m.attributes)):
        print(m.attributes[i].name + ": " + str(d.averageGain(dataset, m.attributes[i])))
    print("Best attribute is: " + str(d.bestAttribute(dataset, m.attributes)))


def buildTreesAndComputePerformance():
    """ Assignment 3: """
    for i in range(len(trainingSets)):
        tree = d.buildTree(trainingSets[i].dataset, m.attributes)
        performanceOnTest = d.check(tree, testSets[i].dataset)
        performanceOnTrain = d.check(tree, trainingSets[i].dataset)
        print("Error of " + trainingSets[i].name + " on " + testSets[i].name + ": " + str(1 - performanceOnTest))
        print("Error of " + trainingSets[i].name + " on " + trainingSets[i].name + ": " + str(1 - performanceOnTrain))
        print("")


def findBestPrunedTree(originalTrainSet, fraction):
    """ Find the best pruned tree, given a training set and a fraction for partitioning. """
    trainSet, validationSet = partition(originalTrainSet.dataset, fraction)
    tree = d.buildTree(trainSet, m.attributes)

    bestTreeSoFar = tree
    bestPerformanceSoFar = d.check(tree, validationSet)
    print("Pruning " + originalTrainSet.name + " with fraction = " + str(fraction) +
          " and performance on new validation set = " + str(bestPerformanceSoFar))

    while (True):
        possibleWaysToPruneTree = d.allPruned(bestTreeSoFar)

        if (len(possibleWaysToPruneTree) == 0):
            print("No more ways to prune tree. Returning.")
            return bestTreeSoFar, bestPerformanceSoFar

        bestPrunedTree, performance = getBestPerformingTree(possibleWaysToPruneTree, validationSet)

        if (performance >= bestPerformanceSoFar):
            print("Found pruned tree which performed better: " + str(performance))
            bestTreeSoFar = bestPrunedTree
            bestPerformanceSoFar = performance
        else:
            print("All pruned trees perform worse. Stopping here.")
            return bestTreeSoFar, bestPerformanceSoFar


def getBestPerformingTree(possibleWaysToPruneTree, validationSet):
    """ Find the best performing tree from the given trees on the given validation set. """
    performances = []

    for prunedTree in possibleWaysToPruneTree:
        prunedPerformance = d.check(prunedTree, validationSet)
        performances.append(prunedPerformance)

    bestPerformance = max(performances)
    index = performances.index(bestPerformance)
    return possibleWaysToPruneTree[index], bestPerformance


def findFractionPerformances(originalTrainSet, originalTestSet, fractions):
    """ Find the classification performances of the given fractions. """
    performances = []
    originalTree = d.buildTree(originalTrainSet.dataset, m.attributes)
    originalPerformance = d.check(originalTree, originalTestSet.dataset)
    print("\n------------------------------------------------------")
    print("Performance of " + originalTrainSet.name + " tree on " + originalTestSet.name + ": " + str(
        originalPerformance) + "\n")

    for fraction in fractions:
        tree, performance = findBestPrunedTree(originalTrainSet, fraction)
        performanceOnTestSet = d.check(tree, originalTestSet.dataset)
        print("Performance of best pruned tree on test set: " + str(performanceOnTestSet) + "\n")
        performances.append(performanceOnTestSet)

    for i in range(len(fractions)):
        print(str(fractions[i]) + ": " + str(performances[i]))

    return performances

def plotFractionErrorRelationship():
    """ Assignment 4: Plot classification performances for different pruning fractions. """
    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    plotLines = []
    pyplot.xlabel("Fraction")
    pyplot.ylabel("Error")

    for i in range(len(trainingSets)):
        performances = findFractionPerformances(trainingSets[i], testSets[i], fractions)
        errors = [1 - x for x in performances]
        plotLines += pyplot.plot(fractions, errors , label=trainingSets[i].name)

    pyplot.legend(handles=plotLines)
    pyplot.show()