from numpy import *
import operator
"""[k-Nearest Neighbors algorithm]

[With a simple dataset, test k-Nearest Neighbors algorithm]
"""


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # Distance calculation
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


def file2matrix(filename):
    # open the file
    fr = open(filename)
    # read the lines in file
    number_of_lines = len(fr.readlines())
    # Create numpy matrix
    return_mat = zeros(number_of_lines, 3)

    class_label_vector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        list_from_list = line.split('\t')
        return_mat[index, :] = listFromLine[0:3]
        class_label_vector.append(int(list_from_list))

    return return_mat, class_label_vector


def autoNorm(dataSet):
    """
    Automatically normalize the data to values between 0 and 1.

    Arguments:
        dataSet {[type]} -- [description]
    """
    min_vals = dataSet.min(0)
    max_vals = dataSet.max(0)
    ranges = max_vals - min_vals
    norm_data_set = zeros(shape(dataSet))
    m = dataSet.shap[0]
    norm_data_set = dataset - tile(min_vals, (m, 1))
    norm_data_set = norm_data_set / tile(ranges, (m, 1))

    return norm_data_set, ranges, min_vals


def dating_class_tesst():
    """
    Calculate the test error on classifier
    """
    ho_ratio = 0.10
    dating_data_mat, dating_labels = file2matrix('file.txt')
    norm_mat, ranges, min_vals = autoNorm(dating_data_mat)
    m = norm_mat.shape[0]
    num_test_veces = int(m * ho_ratio)
    error_count = 0.0
    for i in range(num_test_veces):
        classifier_res = classify0(norm_mat[i, :], norm_mat[num_test_veces:m, :],
                                   datingLabels[num_test_veces:m], 3)
        print("The classifier came back with: %d, the real answer is: %d"
              % (classifier_res, dating_labels[i]))
        if (classifier_res != dating_labels[i]):
            error_count += 1.0
    print("The total error rate is: %f" %
          (error_count / float(num_test_veces)))

def classify_person():
    """    
    Dating site predictor function
    """
    res_list = ['not at all', 'in small doses', 'in large doses']
    
    group, labels = createDataSet()
    a = classify0([0, 0], group, labels, 3)
    print(a)