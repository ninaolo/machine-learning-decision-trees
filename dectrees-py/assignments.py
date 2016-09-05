import monkdata as m
import dtree as d
import drawtree as draw

class TrainingSet:
    def __init__(self, dataset, name):
        self.dataset = dataset
        self.name = name


trainingSets = [TrainingSet(m.monk1test, "monk1test"),
                TrainingSet(m.monk2test, "monk2test"),
                TrainingSet(m.monk3test, "monk3test")]

""" Assignment 1 """
def calculateEntropyOfTrainingSets():
    for set in trainingSets:
        print("Entropy of " + set.name + ": " + str(d.entropy(set.dataset)))
    print("")


""" Assignment 2 """
def calculateAverageInformationGainOfTrainingSets():
    for set in trainingSets:
        printInformationGainOfDataset(set.dataset, set.name)


def splitOnA5AndComputeInformationGainsOfSubsets():
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

def drawMonk1():
    tree = d.buildTree(m.monk1test, m.attributes)
    draw.drawTree(tree)

def drawMonk2():
    tree = d.buildTree(m.monk2test, m.attributes)
    draw.drawTree(tree)

""" Assignment 3 """
def buildTreesAndComputePerformance():
    pass