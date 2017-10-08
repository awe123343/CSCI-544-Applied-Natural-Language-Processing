#!/usr/bin/env python
import argparse
import collections
import sys
import codecs
if sys.version_info[0] == 2:
  from itertools import izip
else:
  izip = zip
from collections import defaultdict as dd
import re
import os.path
import gzip
import tempfile
import shutil
import atexit
import pronouncing
# Use word_tokenize to split raw text into words
from string import punctuation

import nltk
from nltk.tokenize import word_tokenize

scriptdir = os.path.dirname(os.path.abspath(__file__))

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

def addonoffarg(parser, arg, dest=None, default=True, help="TODO"):
  ''' add the switches --arg and --no-arg that set parser.arg to true/false, respectively'''
  group = parser.add_mutually_exclusive_group()
  dest = arg if dest is None else dest
  group.add_argument('--%s' % arg, dest=dest, action='store_true', default=default, help=help)
  group.add_argument('--no-%s' % arg, dest=dest, action='store_false', default=default, help="See --%s" % arg)



class LimerickDetector:

    def __init__(self):
        """
        Initializes the object to have a pronunciation dictionary available
        """
        from nltk.corpus import cmudict 
        self.d = cmudict.dict() 
        dictlist=[]
        self._pronunciations = nltk.corpus.cmudict.dict()
        for key, value in self._pronunciations.iteritems():

       
            temp = [key,value]
            dictlist.append(temp)
        ggg=[]
        
        
        for i in range(len(dictlist)):
            if  len(dictlist[i][1])>1:
                for j in range(len(dictlist[i][1])):
                    
                    ppp=' '.join(dictlist[i][1][j])
                    ppp=[dictlist[i][0],ppp]
                    ggg.append(ppp)
        
            else:
                ccc=' '.join(dictlist[i][1][0])
                ccc=[dictlist[i][0],ccc]
                ggg.append(ccc)
        
            
        for i in range(len(ggg)):
            ggg[i]=tuple(ggg[i])
        
        
        self.rhyme_dict = collections.defaultdict(list)
        for word, phones in ggg:
            rp = self.finding(phones)
            if rp is not None:
                self.rhyme_dict[rp].append(word)
 
            
      

    def num_syllables(self, word):
        
      
      
    
      word = word.lower()
      word=word.strip(".#:$^;@&?,&!*")
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

     


    def guess_syllables(self, word):
        
      
        
        v = 'aouyei'
        word = word.lower()
        word=word.strip(".#:$^;@&?,&!*")
        c = 0
        if word[0] in v:
            c +=1
        for i in range(1,len(word)):
            if word[i] in v and word[i-1] not in v:
                c +=1
                
        if word.endswith('le'):
            c+=1
        if word.endswith('e'):
            c -= 1
       
        if c == 0:
            c +=1
        return c
    def finding(self,a):
        numm=['1','2']
        a = a.split()
        
        for j in range(len(a)-1,0,-1):
            
            if a[j][-1] in numm:
                return ' '.join(a[j:])
        return ' '.join(a)
    def rhymes(self, a, b):
 
                     
 
        
        a = a.lower()
        b =b.lower()
        
        try:
            cmu_my_word = self._pronunciations.get(a)
            aaa=[]
            all_poss=[]
            if len(cmu_my_word) > 0:
                for i in cmu_my_word:
                    i = [' '.join(i)]
                    qwerty=self.rhyme_dict.get(self.finding(i[0]), [])
                    for w in qwerty:
                        if w!=a:
                            aaa.append(w)
                if b not in aaa:
                    return False
                
                else:
                    return True
            else:
                return []
        except:
            return False

        # TODO: provide an implementation!


    def is_limerick(self, text):
        """
        Takes text where lines are separated by newline characters.  Returns
        True if the text is a limerick, False otherwise.

        A limerick is defined as a poem with the form AABBA, where the A lines
        rhyme with each other, the B lines rhyme with each other, and the A lines do not
        rhyme with the B lines.


        Additionally, the following syllable constraints should be observed:
          * No two A lines should differ in their number of syllables by more than two.
          * The B lines should differ in their number of syllables by no more than two.
          * Each of the B lines should have fewer syllables than each of the A lines.
          * No line should have fewer than 4 syllables

        (English professors may disagree with this definition, but that's what
        we're using here.)


        """
        cc=[]
        text=text.strip()
        text =  re.sub ('[!@#$%?^&:*"+-,.]', '', text)
        
        text = text.split("\n")
        r = []
        for i in range(len(text)):
            text[i] = text[i].strip()
            
        for i in range(len(text)):
            r.append(list(text[i].split(" ")))
        for line in text:
            if line !=['']:
                cc.append(line)
        text=cc
        
        text = r


        
        if len(text)<>5:
            return False
        
        A_lines = [text[0],text[1],text[4]]
        B_lines=[text[2],text[3]]
        s=0
        p=0
        Asyll=[]
        Bsyll=[]
        for i in range(len(A_lines)):
            for j in A_lines[i]:
                s+=self.num_syllables(j)
            Asyll.append(s)
            s=0
        for i in range(len(B_lines)):
            for j in B_lines[i]:
                p+=self.num_syllables(j)
            Bsyll.append(p)
            p=0
        for i in Asyll:
            if i<4:
                return False
        for i in Bsyll:
            if i<4:
                return False
        if self.rhymes(A_lines[0][-1],B_lines[0][-1]):
            return False
        
        
        
        if abs(Asyll[0]-Asyll[1])>2 | abs(Asyll[0]-Asyll[2])>2 | abs(Asyll[2]-Asyll[1])>2:
            return False
        if abs(Bsyll[0]-Bsyll[1])>2:
            return False
        for i in Bsyll:
            for j in Asyll:
                if i>=j:
                    return False
                
        if self.rhymes(A_lines[0][-1],A_lines[1][-1]) & self.rhymes(A_lines[0][-1],A_lines[2][-1]) & self.rhymes(A_lines[2][-1],A_lines[1][-1]) & self.rhymes(B_lines[0][-1],B_lines[1][-1]):
            return True
        else:
            return False
        
            
                
        
        # TODO: provide an implementation!


# The code below should not need to be modified
def main():
  parser = argparse.ArgumentParser(description="limerick detector. Given a file containing a poem, indicate whether that poem is a limerick or not",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  addonoffarg(parser, 'debug', help="debug mode", default=False)
  parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input file")
  parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")




  try:
    args = parser.parse_args()
  except IOError as msg:
    parser.error(str(msg))

  infile = prepfile(args.infile, 'r')
  outfile = prepfile(args.outfile, 'w')

  ld = LimerickDetector()
  lines = ''.join(infile.readlines())
  outfile.write("{}\n-----------\n{}\n".format(lines.strip(), ld.is_limerick(lines)))

if __name__ == '__main__':
  main()
