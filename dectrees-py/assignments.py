import monkdata
import dtree

def calculateEntropyOfTrainingSets():
    print("Entropy of monk1test: " + str(dtree.entropy(monkdata.monk1test)))
    print("Entropy of monk2test: " + str(dtree.entropy(monkdata.monk2test)))
    print("Entropy of monk3test: " + str(dtree.entropy(monkdata.monk3test)))

def calculateAverageInformationGainOfTrainingSets():
    print("Average information gain of monk1test:")
    for i in range(6):
        print("a" + str(i+1) + ": " + str(dtree.averageGain(monkdata.monk1test, monkdata.attributes[i])))
    print("")

    print("Average information gain of monk2test:")
    for i in range(6):
        print("a" + str(i+1) + ": " + str(dtree.averageGain(monkdata.monk2test, monkdata.attributes[i])))
    print("")

    print("Average information gain of monk3test:")
    for i in range(6):
        print("a" + str(i+1) + ": " + str(dtree.averageGain(monkdata.monk3test, monkdata.attributes[i])))

calculateAverageInformationGainOfTrainingSets()
