import os
import re
import stemmer

unusedWords = ['as', 'at', 'in', 'inside', 'within', 'between', 'among', 'on', 'with', 'of', 'for', 'toward', 'to', 'onto', 'into', 'from', 'out of', 'away', 'before', 'front', 'ahead', 'after', 'behind', 'back', 'and', 'or', 'nor', 'but', 'so', 'yet', 'except', 'a', 'the', 'this', 'that', 'my', 'your' ,'his', 'her', 'its', 'our', 'their', 'no', 'yes']

pSpam = 1500.0/(1500.0+3672.0)
pHam = 1 - pSpam

def getWordsFrom(string): # get the list of words from './string' directory
    string = string.lower()
    wordList = []
    for root, dirs, files in os.walk('./'):
        if string in root.lower():
            for file in files:
                f = open(root+'/'+file, 'r')
                tmp = [ x.lower() for x in re.split('[^a-zA-Z]+',f.read())] 
                #Only select English words in the list
                tmp = filter(lambda a: (len(a) >= 2) & (a not in unusedWords), tmp) 
                #Remove non-useful words to detect spam or not
                wordList += tmp
                f.close()

    p = stemmer.PorterStemmer()
    for i in xrange(len(wordList)):
        wordList[i] = p.stem(wordList[i], 0,len(wordList[i])-1)
        
    wordList = list(set(wordList)) 
    #Remove overlapping words
    wordList.sort()
    return wordList    

def vocabulary():
    return list(set(getWordsFrom('./trainingHam') + getWordsFrom('./trainingSpam')))



def bayesian(feature):
    pSpamX = pSpam
    for i in xrange(len(feature)):
        
    
    pHamX = 

#Main Routine
if __name__ == "__main__":
    print "done"
