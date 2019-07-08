# coding: utf-8
from numpy import *
'''
@ content 基于概率论的分类方法：朴素贝叶斯
@ author https://github.com/commitsession
'''

# 词表向向量转换函数
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word : %s is not in my Vocabulary!" % word)
    return returnVec


# 朴素贝叶斯词袋模型
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


# 朴素贝叶斯分类训练函数
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbuse = sum(trainCategory) / float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbuse


# 朴素贝叶斯分类函数
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


# test
def testingNB():
    postingList, classVec = loadDataSet()
    print(postingList)
    print(classVec)
    mylist = createVocabList(postingList)
    print(mylist)
    # inputList=postingList[0]
    # inputList = ['hello', 'world']
    # returnVec = setOfWords2Vec(mylist, inputList)
    # print(returnVec)
    trainMat = []
    for postinDoc in postingList:
        trainMat.append(bagOfWords2VecMN(mylist, postinDoc))
    print(trainMat)
    p0Vect, p1Vect, pAbuse = trainNB0(trainMat, classVec)
    print(p0Vect)
    print(p1Vect)
    print(pAbuse)

    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(bagOfWords2VecMN(mylist, testEntry))
    print(thisDoc)
    testClassify = classifyNB(thisDoc, p0Vect, p1Vect, pAbuse)
    print(testClassify)

    testEntry = ['stupid', 'garbage']
    thisDoc = array(bagOfWords2VecMN(mylist, testEntry))
    print(thisDoc)
    testClassify = classifyNB(thisDoc, p0Vect, p1Vect, pAbuse)
    print(testClassify)


testingNB()
