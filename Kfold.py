# split k fold
def crossValidationSplit(dataSet, nFold):
    dataSetSplit = list()
    dataSetCopy = list(dataSet).copy()
    foldSize = int(len(dataSet) / nFold)
    for _ in range(nFold):
        fold = list()
        while len(fold) < foldSize:
            index = randrange(len(dataSetCopy))
            fold.append(dataSetCopy.pop(index))
        dataSetSplit.append(fold)
    return dataSetSplit




# Evaluate alg using crossValidationSplit
def evaluateAlg(dataSet, alg, nFold, *args):
    folds = crossValidationSplit(dataSet, nFold)
    scores = list()
    for idx, fold in enumerate(folds):
        trainSet = list()
        for n_idx, n_fold in enumerate(folds):
            if n_idx != idx:
                trainSet.extend(n_fold)
        # print(len(trainSet))
        # exit()
        # testSet = fold[-1]
        testSet = list()
        for row in fold:
            rowCopy = list(row)
            testSet.append(rowCopy)
            rowCopy[-1] = None
        predicted = alg(trainSet, testSet, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracyMetric(actual, predicted)
        scores.append(accuracy)
    return scores