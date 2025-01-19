import numpy as np

def topsis(data, weights, impacts):
    if((len(weights) != len(impacts)) or len(weights) != data.shape[1]):
        raise ValueError('Different number of weights, impacts and columns')
    
    normalize = np.sqrt((data ** 2).sum(axis = 0))

    normalizedData = data / normalize

    weightedData = normalizedData * weights

    idealBest = [max(col) if impact == '+' else min(col) for col, impact in zip(weightedData.T, impacts)]
    idealWorst = [min(col) if impact == '+' else max(col) for col, impact in zip(weightedData.T, impacts)]

    SBest = np.sqrt((weightedData - idealBest ** 2).sum(axis = 1))
    SWorst = np.sqrt((weightedData - idealWorst ** 2).sum(axis = 1))

    score = SWorst / (SBest + SWorst)

    rank = score.argsort()[::-1] + 1

    return score, rank