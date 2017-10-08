#!/usr/bin/env python
from collections import defaultdict
from csv import DictReader, DictWriter
from nltk.corpus import stopwords 
import nltk
import codecs
import random
from nltk.stem import PorterStemmer
import re
import sys
from nltk.corpus import wordnet as wn
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
kTOKENIZER = TreebankWordTokenizer()

def morphy_stem(word):
    """
    Simple stemmer
    """
    ps= PorterStemmer()
    stem = ps.stem(word)
    if stem:
        return stem.lower()
    else:
        return word.lower()

class FeatureExtractor:
    def __init__(self):
        from nltk.corpus import cmudict 
        self.d = cmudict.dict() 
        h=[]
#        with open('myfile.txt') as f:
#            self.mylist = f.read().splitlines() 
        
        
            
        
        

            
       
                 
        
        return None
    def NN(self,text):
        cv=[]
        ps=PorterStemmer()
        for i in text:
            q=self.mine(i['text'])
            for j in q.split():
                cv.append(ps.stem(j))
            
        return cv
        
   
    def punc(self,text):
        text=text.lower()
        text =  re.sub ('[!@$%?<>^&_*"+-;,.]', ' ', text)
        text = text.strip()
        return text
        
                
    def stopwords(self,text):
        f=[]
        stop_words = set(stopwords.words('english'))
        words = text.split()
        for r in words:
            if r not in stop_words:
                f.append(r)
        return ' '.join(f)
    def num_syllables(self, word):
        
      
      
  
      if word not in self.d:
          return 1
      else:
          a=[]
          for i in self.d[word]:
              aa=[]
              for j in i:
                  if j[-1].isdigit():
                      aa.append(j)
              a.append(len(aa))
      return max(a)
  
        
        
        

    def features(self, text):
        text=text.lower()
        lo=len(text)
        text =  re.sub ('[!@#$%?^&:*"+-;,.]', ' ', text)
        text = text.strip()
        tt=[]
        for word in text.split():
            tt.append(self.num_syllables(word))
        cccc=sum(tt)
        gf=0
        
            
            
#        if 0<len(text)<15:
#            qq=text.split()
#            
#            qq.append('dark')
#            text=' '.join(qq)
#        elif 14<len(text)<35:
#      
#            qq=text.split()
#            
#            qq.append('dark')
#            qq.append('last')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            qq.append('sky')
#            
#            
#            text=' '.join(qq)
#        elif 34<len(text)<37:
#       
#            qq=text.split()
#            
#            qq.append('sky')
#            text=' '.join(qq)
#        elif 36<len(text)<45:
#       
#            qq=text.split()
#            
#            qq.append('fair')
#            text=' '.join(qq)
#            
#        elif 44<len(text):
#         
#            qq=text.split()
#            
#            qq.append('thi')
#            text=' '.join(qq)
#        
#            
    
            
        
        
        
        
        f=[]
        stop_words = set(stopwords.words('english'))
        words = text.split()
        for r in words:
            if r not in stop_words and r not in ['1','2','3','4','5','6','7','8','9']:
                f.append(r)
        text=' '.join(f)
        
        d = defaultdict(int)
        for ii in kTOKENIZER.tokenize(text):
            d[morphy_stem(ii)] += 1
        if 9<cccc:
            d['c']
        d['c']=cccc
        d['w']=lo
        return d
reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')


def prepfile(fh, code):
  if type(fh) is str:
    fh = open(fh, code)
  ret = gzip.open(fh.name, code if code.endswith("t") else code+"t") if fh.name.endswith(".gz") else fh
  if sys.version_info[0] == 2:
    if code.startswith('r'):
      ret = reader(fh)
    elif code.startswith('w'):
      ret = writer(fh)
    else:
      sys.stderr.write("I didn't understand code "+code+"\n")
      sys.exit(1)
  return ret

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--trainfile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input train file")
    parser.add_argument("--testfile", "-t", nargs='?', type=argparse.FileType('r'), default=None, help="input test file")
    parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")
    parser.add_argument('--subsample', type=float, default=1.0,
                        help='subsample this fraction of total')
    args = parser.parse_args()
    trainfile = prepfile(args.trainfile, 'r')
    if args.testfile is not None:
        testfile = prepfile(args.testfile, 'r')
    else:
        testfile = None
    outfile = prepfile(args.outfile, 'w')
    # Create feature extractor (you may want to modify this)
    trainn = DictReader(trainfile, delimiter='\t')

    fe=FeatureExtractor()
    # Read in training data
    train = DictReader(trainfile, delimiter='\t')
    
    
   
    pss=PorterStemmer()

    # Split off dev section
    dev_train = []
    dev_test = []
    full_train = []
    p=0
    cc=0
    s1,s2,s3,s4,s5=0,0,0,0,0
    b1,b2,b4,b3,b5=0,0,0,0,0
    mm=0
    for ii in train:
        cc+=1
        if args.subsample < 1.0 and int(ii['id']) % 100 > 100 * args.subsample:
            continue
        
        
        p+=len(ii['text'].split())
        mm+=len(list(ii['text']))
        
        if 0<len(ii['text'])<15:
            s1+=1
            b1+=1
            
        elif 14<len(ii['text'])<35:
            s2+=1
            b2+=1
      
            
            

        elif 34<len(ii['text'])<37:
       
            s3+=1
            b3+=1
        elif 36<len(ii['text'])<45:
         
            s4+=1
            b4+=1
            
        elif 44<len(ii['text']):
         
            s5+=1
            b5+=1
        
      
        feat = fe.features(ii['text'])

    
        if int(ii['id']) %5== 0:
            dev_test.append((feat, ii['cat']))
        else:
            dev_train.append((feat, ii['cat']))
        full_train.append((feat, ii['cat']))
        
        
        
            
       
            
    # Train a classifier
    sys.stderr.write("Training classifier ...\n")
    classifier = nltk.classify.NaiveBayesClassifier.train(dev_train)
    
    right = 0
    left=0
    total = len(dev_test)
    for ii in dev_test:
        
        prediction = classifier.classify(ii[0])
        if prediction == ii[1]:
            
            
            right += 1
            
        
      
       
    sys.stderr.write("Accuracy on dev: %f\n" % (float(right) / float(total)))
    if testfile is None:
        sys.stderr.write("No test file passed; stopping.\n")
    else:
        # Retrain on all data
        classifier = nltk.classify.NaiveBayesClassifier.train(dev_train + dev_test)

        # Read in test section
        test = {}
        cor=3666
        for ii in DictReader(testfile, delimiter='\t'):
            
            test[ii['id']] = classifier.classify(fe.features(ii['text']))

        # Write predictions
        o = DictWriter(outfile, ['id', 'pred'])
        o.writeheader()
        for ii in sorted(test):
            
            o.writerow({'id': ii, 'pred': test[ii]})
