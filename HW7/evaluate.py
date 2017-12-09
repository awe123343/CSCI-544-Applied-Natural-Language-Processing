#!/usr/bin/env python
import argparse # optparse is deprecated
from nltk.corpus import wordnet
import re
import spacy
nlp = spacy.load('en')
import sys
import nltk
import sys
import math
import re
import numpy as np
from nltk import ngrams

from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot
from sklearn import svm, grid_search
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit


import nltk

import spacy
from itertools import islice # slicing for iterators
import nltk
nlp = spacy.load('en')
arr=np.full((113305,29),0)
res=np.full((113305),0)

def aa(h1,h2,ref):
#    h1="Republican leaders justify its policy need to combat electoral fraud."
#    h2="Republican leaders justify its policy of need in the combat against electoral fraud."
#    ref="Republican leaders justify their policy by the need to combat electoral fraud."
    a=[]
    h1ngram=[]
    h2ngram=[]
    refngram=[]
    h1_match=sum(1 for w in h1 if w in ref) 
    h2_match=sum(1 for w in h2 if w in ref) 
    g1,g2=0,0

    
    p1=float(h1_match)/float(len(h1))
    r1=float(h1_match)/float(len(ref))
    p2=float(h2_match)/float(len(h2))
    r2=float(h2_match)/float(len(ref))
   
    if ((0.85)*p1+(0.15)*r1)==0:
        g1=1
        
        l1=0
    if ((0.85)*p2+(0.15)*r2)==0:
        g2=1
        l2=0
        
    if g1==0:
        l1=p1*r1/((0.85)*p1+(0.15)*r1)
    if g2==0:
        
        l2=p2*r2/((0.85)*p2+(0.15)*r2)
    

    
    for i in range(len(ref)):
        ref[i]=re.sub("[.;:!?#/,]","",ref[i])
    for i in range(len(h1)):
        h1[i]=re.sub("[.;:!?#/,]","",h1[i])
    for i in range(len(h2)):
        h2[i]=re.sub("[.;:!?#/,]","",h2[i])
        
    for i in range(len(h1)):
        h1[i]=h1[i].lower()
    for i in range(len(h2)):
        h2[i]=h2[i].lower()
    for i in range(len(ref)):
        ref[i]=ref[i].lower()
        
    h1=' '.join(h1)
    h2=' '.join(h2)
    ref=' '.join(ref)
        
            
            
    for i in range(1,5):
        nngram = ngrams(h1.split(), i)
        for grams in nngram:
            a.append(grams)
        h1ngram.append(a)
        a=[]
        
    for i in range(1,5):
        nngram = ngrams(h2.split(), i)
        for grams in nngram:
            a.append(grams)
        h2ngram.append(a)
        a=[]
        
    for i in range(1,5):
        nngram = ngrams(ref.split(), i)
        for grams in nngram:
            a.append(grams)
        refngram.append(a)
        a=[]
        
        
    c=0  
    h11gram=0
    h12gram=0
    h13gram=0
    h14gram=0
    h21gram=0
    h22gram=0
    h23gram=0
    h24gram=0
    cc=[]
    for i in h1ngram:
        for j in i:
            for p in refngram:
                for k in p:
                    if j==k:
                        c+=1
                        break
        cc.append(c)
        c=0
    h11gram,h12gram,h13gram,h14gram=cc[0],cc[1],cc[2],cc[3]
    cc=[]
    c=0
    for i in h2ngram:
        for j in i:
            for p in refngram:
                for k in p:
                    if j==k:
                        c+=1
                        break
        cc.append(c)
        c=0
    h21gram,h22gram,h23gram,h24gram=cc[0],cc[1],cc[2],cc[3]
    
    ph1=[]
    if len(h1ngram[0]) !=0:
        
        ph1.append(float(h11gram)/float(len(h1ngram[0])))
    else:
        ph1.append(0)
        
    if len(h1ngram[1]) !=0:
        ph1.append(float(h12gram)/float(len(h1ngram[1])))
    else:
        ph1.append(0)
        
    if len(h1ngram[2]) !=0:    
        ph1.append(float(h13gram)/float(len(h1ngram[2])))
        
    else:
        ph1.append(0)
        
    if len(h1ngram[3]) !=0:   
        ph1.append(float(h14gram)/float(len(h1ngram[3])))
    else:
        ph1.append(0)
    
    ph2=[]
    
    if len(h2ngram[0]) !=0: 
        ph2.append(float(h21gram)/float(len(h2ngram[0])))
    else:
        ph2.append(0)
        
    if len(h2ngram[1]) !=0: 
        ph2.append(float(h22gram)/float(len(h2ngram[1])))
    else:
        ph2.append(0)
    
    if len(h2ngram[2]) !=0:
        ph2.append(float(h23gram)/float(len(h2ngram[2])))
    else:
        ph2.append(0)
    
    if len(h2ngram[3]) !=0:
        ph2.append(float(h24gram)/float(len(h2ngram[3])))
    else:
        ph2.append(0)
    
    logh1=[]
    logh2=[]    
    for i in ph1:
        try:
            logh1.append(math.log(i))
        except:
            logh1.append(0)
    for i in ph2:
        try:
            logh2.append(math.log(i))
        except:
            logh2.append(0)
        
    
    
    ratioh1=float(len(h1.split()))/float(len(ref.split()))
    ratioh2=float(len(h2.split()))/float(len(ref.split()))
    lenh1=len(h1.split())
    lenh2=len(h2.split())
    lenref=len(ref.split())
    
    doch1 = nlp(unicode(h1))
    doch2 = nlp(unicode(h2))
    docref = nlp(unicode(ref))
    sim1= doch1.similarity(docref)
    sim2= doch2.similarity(docref)

    h1 = ' '.join(h1)
    h2 = ' '.join(h2)
    ref = ' '.join(ref)
    
    posh1={}
    posh2={}
    posref={}
    texth1 = nltk.word_tokenize(h1)
    texth2 = nltk.word_tokenize(h2)
    textref = nltk.word_tokenize(ref)
    for k,l in nltk.pos_tag(texth1):
        posh1[l]= posh1.get(l,0)+1
             
    for k,l in nltk.pos_tag(texth2):
        posh2[l]= posh2.get(l,0)+1
             
    for k,l in nltk.pos_tag(textref):
        posref[l]= posref.get(l,0)+1
    
    
    precisionposh1=[]   
    precisionposh2=[]         
    
        
    a=[]   
    posh1=[]
    posh2=[]
    posref=[]
    nngram = ngrams(nltk.pos_tag(texth1), 4)
    for grams in nngram:
        for i,j in grams:
            a.append(j)
        posh1.append(a)
        a=[]
            
    nngram = ngrams(nltk.pos_tag(texth2), 4)
    for grams in nngram:
        for i,j in grams:
            a.append(j)
        posh2.append(a)
        a=[]
    
    nngram = ngrams(nltk.pos_tag(textref), 4)
    for grams in nngram:
        for i,j in grams:
            a.append(j)
        posref.append(a)
        a=[]
    
    
    
    for i in posh1:
            if i in posref:
    
                
                precisionposh1.append(1)
                    
    for i in posh2:
            if i in posref:
                
                precisionposh2.append(1)
                
                
    score1 = S_METEOR(h1,ref)
    score2 = S_METEOR(h2,ref)
                
                


    return l1,l2,sim1,sim2,score1,score2,sum(precisionposh1),sum(precisionposh2)










def LCS(s1, s2):
    m=[]
    l, xl = 0, 0
    for k in range(1+len(s1)):
        
        m.append([0] * (1 + len(s2)))

    
    for i in range(1, 1 + len(s1)):
        for j in range(1, 1 + len(s2)):
            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1] + 1
                if m[i][j] > l:
                    l = m[i][j]
                    xl = i
            else:
                m[i][j] = 0
    s = xl - l
    e = xl
    return (s1[s : e], s, e)





def chunk_(h, r):
    
    
  (seq, start, end) = LCS(h, r)
  chunknum = 0
  ngram = 0


  
  while len(seq) != 0:
    chunknum += 1
    ngram += len(seq)
    h = h[:start] + h[end:]
    (seq, start, end) = LCS(h, r)
  return (chunknum, ngram)


def S_METEOR(h, r):
    
  

  a = 0.9
  b = 3.0
  g = 0.26
  
  th = 5
  fmatchweight = 0.8
  smatchweight = 0.9
  htrun=[]
  rtrun=[]
  
  
  
  for i in h:
      htrun.append(i[:th])
  for i in r:
      rtrun.append(i[:th])
          
  rset = set(r)
  rset_trun = set(rtrun)
  
  summ=[]
  for i in h:
      if i in rset:
          summ.append(fmatchweight)
  m = sum(summ)
  summ=[]        
  
  for i in htrun:
      if i in rset_trun:
          summ.append(smatchweight)
          
          
  mt = sum(summ)
  # Precision
  Pre = float(m + mt) / float(len(h) * fmatchweight + len(htrun) * smatchweight)
  # Recall
  Rec = float(m + mt) / float(len(r) * fmatchweight + len(rtrun) * smatchweight)

  F_1 = (a * Pre + (1-a) * Rec)
  if (F_1 != 0.0):
    F_mean = (Pre * Rec) / F_1
  else:
    F_mean = 0.0

  (chunknum, ngramnum) = chunk_(h, r)
  (chunkt, gramst) = chunk_(htrun, rtrun)
  
  ngra = ngramnum * fmatchweight + (gramst * smatchweight)
  nchu = chunknum * fmatchweight + (chunkt * smatchweight)


  if (ngra - 1) == 0:
    penalty = 1.0
  else:
    penalty = float(nchu - 1) / float(ngra - 1)

  Diff = g * (penalty**b)
  score = (1 - Diff)*F_mean  
          

  return score
    


 
def word_matches(h, ref):
    
#    doc1 = nlp(unicode(h))
#    doc2 = nlp(unicode(ref))

#    r=[]
#    p=[]
#    ref=list(ref)
#    for i in range(len(ref)):
#        ref[i]=re.sub("[.;:!?#/,]","",ref[i])
#    for i in range(len(h)):
#        h[i]=re.sub("[.;:!?#/,]","",h[i])
#    rr=ref
#    
#    for i in range(len(rr)):
#        try:
#            s= wordnet.synsets(rr[i])
#            for j in s:
#                r.append(j)
#            
#            p=set(p)
#            p=list(p)
#            r.append(p)
#            p=[]
#        except:
#            pass
#    c=0
#    f=0
#    for w in range(len(h)):
#        try:
#            d=wordnet.synsets(h[w])
#            for pp in d:
#                for j in r:
#                    try:
#                        if (pp.wup_similarity(j))>0.85:
#                            h[w]=j.name().split('.')[0]
#                            f=1
#                            c+=1
#                            break
#                    except:
#                        pass
#                if f==1:
#                    f=0
#                    break
#        except:
#            pass
#        
#        
#    
#    return c
#                    
        
            
    
    
    
    return sum(1 for w in h if w in ref)
# 
def main():
    parser = argparse.ArgumentParser(description='Evaluate translation hypotheses.')
    parser.add_argument('-i', '--input', default='data/hyp1-hyp2-ref',
            help='input file (default data/hyp1-hyp2-ref)')
    parser.add_argument('-n', '--num_sentences', default=None, type=int,
            help='Number of hypothesis pairs to evaluate')
    # note that if x == [1, 2, 3], then x[:None] == x[:] == x (copy); no need for sys.maxint
    opts = parser.parse_args()
 
    # we create a generator and avoid loading all sentences into a list
    g=0
    def sentences():
        with open(opts.input) as f:
            for pair in f:
                yield [sentence.strip().split() for sentence in pair.split(' ||| ')]
 
    # note: the -n option does not work in the original code
    for h1, h2, ref in islice(sentences(), opts.num_sentences):
        rset = ref
        g1,g2=0,0
        
        g+=1
        arr[g][0],arr[g][1],arr[g][2],arr[g][3],arr[g][4],arr[g][5],arr[g][6],arr[g][7]=aa(h1,h2,ref)
        p1=float(h1_match)/float(len(h1))
        r1=float(h1_match)/float(len(ref))
        p2=float(h2_match)/float(len(h2))
        r2=float(h2_match)/float(len(ref))
       
        if ((0.85)*p1+(0.15)*r1)==0:
            g1=1
            
            l1=0
        if ((0.85)*p2+(0.15)*r2)==0:
            g2=1
            l2=0
            
        if g1==0:
            l1=p1*r1/((0.85)*p1+(0.15)*r1)
        if g2==0:
            
            l2=p2*r2/((0.85)*p2+(0.15)*r2)
#        print(h1_match,h2_match)
#        print(1 if h1_match-h2_match>0.0005 else 0 if abs(h1_match-h2_match)<=0.0005
#              else -1)
        print(1 if l1 > l2 else # \begin{cases}
                (0 if l1 == l2
                    else -1)) # \end{cases}
        
# 
# convention to allow import of this file as a module
if __name__ == '__main__':
    main()
