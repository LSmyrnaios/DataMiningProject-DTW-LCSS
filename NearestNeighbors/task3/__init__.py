import operator
from NearestNeighbors.task2A1 import findKnearestNeighbors
from SupportMethods import readDatasets
from SupportMethods.writePredictionsToCsv import write_predictions_to_csv


def runClassification(K):

    print 'Start KNN Classification..'

    dataSets = readDatasets.read_dataset(True, False, True)
    trainSet = dataSets[0]
    testSet = dataSets[1]

    makeListsOfNeighborsForAllTests = True
    plotPatterns = False    # We just want the KNN, not the html-maps.

    maxWarpingWindowPercentage = 0.33  # For testSet_a2, we need a bigger window to get the right patternIDs.

    neighborsTestsLists = findKnearestNeighbors(K, maxWarpingWindowPercentage, plotPatterns, makeListsOfNeighborsForAllTests, trainSet,
                                                testSet)

    # patterns = ['15466', '15466', '15466', '58984', '58984', '96548', '58984', '58984']

    testNum = 0
    testData = []
    for test in neighborsTestsLists:

        testNum += 1

        classVotes = {}
        for x in range(len(test)):
            response = test[x]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1

        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
        print sortedVotes

        testData.append((testNum, sortedVotes[0][0]))


    write_predictions_to_csv(testData)


    # 1/10 train
    # gia ka8e train
    # Split train_dataset into 0.7% train and 0.3% test.
    # train_x, test_x, train_y, test_y = train_test_split(train_data[headers[2:4]], train_data[headers[-1]], train_size=0.7, test_size=0.3)


if __name__ == '__main__':
    K = 5
    runClassification(K)
