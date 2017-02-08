import os
import re
import stemmer

unusedWords = ['as', 'at', 'in', 'inside', 'within', 'between', 'among', 'on', 'with', 'of', 'for', 'toward', 'to', 'onto', 'into', 'from', 'out of', 'away', 'before', 'front', 'ahead', 'after', 'behind', 'back', 'and', 'or', 'nor', 'but', 'so', 'yet', 'except', 'a', 'the', 'this', 'that', 'my', 'your' ,'his', 'her', 'its', 'our', 'their', 'no', 'yes']

def terminating(cond):
    if cond:
        return True
    raise StopIteration

def common_start(sa, sb):
    return ''.join(a for a, b in zip(sa, sb) if terminating(a == b))

def similarity(prevWord, nextWord):
    if (prevWord in nextWord) & (float(len(prevWord))/len(nextWord) >= 0.5):
        return True
    else:
        return False

def removeSimilarWords(wordList):
    pivot = 0
    while pivot < len(wordList) - 1:
        prevWord = wordList[pivot]
        nextWord = wordList[pivot + 1]
        if similarity(prevWord, nextWord):
            wordList.pop(pivot+1)
        else:
            pivot += 1
    pivot = 0
    '''
    while pivot < len(wordList) - 1:
        prevWord = wordList[pivot]
        nextWord = wordList[pivot + 1]
        commonStr = common_start(prevWord, nextWord)
        p = float(len(commonStr))/len(prevWord)
        q = float(len(commonStr))/len(nextWord)        
        if ( p*q >= 0.25 ):
            wordList.pop(pivot+1)
        else:
            pivot += 1
    '''
    return wordList

def getHamWords(): #11k
    wordList = []
    for root, dirs, files in os.walk('./'):
        if 'ham' in root or 'Ham' in root or 'HAM' in root:
            for file in files:
                f = open(root+'/'+file, 'r')
                tmp = [ x.lower() for x in re.split('[^a-zA-Z]+',f.read()) ] #Only select English words in the list
                tmp = filter(lambda a: (len(a) >= 2) & (a not in unusedWords), tmp) #Remove non-useful words to detect spam or not
                wordList += tmp
                f.close()
    wordList = list(set(wordList)) #Remove overlapping words
    wordList.sort()
    return removeSimilarWords(wordList)

def getSpamWords(): #28k
    wordList = []
    for root, dirs, files in os.walk('./'):
        if 'spam' in root or 'Spam' in root or 'SPAM' in root:
            for file in files:
                f = open(root+'/'+file, 'r')
                tmp = [ x.lower() for x in re.split('[^a-zA-Z]+',f.read()) ] #
                tmp = filter(lambda a: (len(a) >= 2) & (a not in unusedWords), tmp)
                wordList += tmp
                f.close()
    wordList = list(set(wordList)) #Remove overlapping words
    wordList.sort()
    return removeSimilarWords(wordList)
                
def selectFeatures():
    for root, dirs, files in os.walk('./'):
        print (root, dirs, files)
        for file in files:
            print file





#Main Routine
if __name__ == "__main__":
    print "done"