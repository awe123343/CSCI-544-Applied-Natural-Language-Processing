#!/bin/python
import re
import nltk
armu,auma,aumo,awaw,bafe,bigdict,bone,brch, bubr,buco,bucon,busp,cap10,cap100,cap500,cap1000,cvco,cvcv,cvcvp,dico,edun,enst,fi5k,fi10,fi100,fi500,fi1000,la10,la100,la500,la1000,loc,locou,low100,low500,low1000,peofam,peope,peopela,pro,spsp,spspte,tiho,tire,trro, tvtvne,tvtvpr,veca, ven,gogo=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
def preprocess_corpus(train_sents):
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/architecture.museum', 'r') as f:
        r = f.readlines()
        global armu
        for i in r:
            armu.append(i.split("\n")[0])
        
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/automotive.make', 'r') as f:
        r = f.readlines()
        global auma
        for i in r:
            auma.append(i.split("\n")[0])
            
        
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/automotive.model', 'r') as f:
        r = f.readlines()
        global aumo
        for i in r:
            aumo.append(i.split("\n")[0])
            
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/award.award', 'r') as f:
        r = f.readlines()
        global awaw
        for i in r:
            awaw.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/base.events.festival_series', 'r') as f:
        r = f.readlines()
        global bafe
        for i in r:
            bafe.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/bigdict', 'r') as f:
        r = f.readlines()
        global bigdict
        for i in r:
            bigdict.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/book.newspaper', 'r') as f:
        r = f.readlines()
        global bone
        for i in r:
            bone.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/broadcast.tv_channel', 'r') as f:
        r = f.readlines()
        global brch
        for i in r:
            brch.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/business.brand', 'r') as f:
        r = f.readlines()
        global bubr
        for i in r:
            bubr.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/business.consumer_company', 'r') as f:
        r = f.readlines()
        global buco
        for i in r:
            buco.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/business.consumer_product', 'r') as f:
        r = f.readlines()
        global bucon
        for i in r:
            bucon.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/business.sponsor', 'r') as f:
        r = f.readlines()
        global busp
        for i in r:
            busp.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/cap.10', 'r') as f:
        r = f.readlines()
        global cap10
        for i in r:
            cap10.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/cap.100', 'r') as f:
        r = f.readlines()
        global cap100
        for i in r:
            cap100.append(i.split("\n")[0])
        
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/cap.500', 'r') as f:
        r = f.readlines()
        global cap500
        for i in r:
            cap500.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/cap.1000', 'r') as f:
        r = f.readlines()
        global cap1000
        for i in r:
            cap1000.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/cvg.computer_videogame', 'r') as f:
        r = f.readlines()
        global cvco
        for i in r:
            cvco.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/cvg.cvg_developer', 'r') as f:
        r = f.readlines()
        global cvcv
        for i in r:
            cvcv.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/cvg.cvg_platform', 'r') as f:
        r = f.readlines()
        global cvcvp
        for i in r:
            cvcvp.append(i.split("\n")[0])
    f.close()
    
    
    
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/dictionaries.conf', 'r') as f:
        r = f.readlines()
        global dico
        for i in r:
            dico.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/education.university', 'r') as f:
        r = f.readlines()
        global edun
        for i in r:
            edun.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/english.stop', 'r') as f:
        r = f.readlines()
        global enst
        for i in r:
            enst.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/firstname.5k', 'r') as f:
        r = f.readlines()
        global fi5k
        for i in r:
            fi5k.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/firstname.10', 'r') as f:
        r = f.readlines()
        global fi10
        for i in r:
            fi10.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/firstname.100', 'r') as f:
        r = f.readlines()
        global fi100
        for i in r:
            fi100.append(i.split("\n")[0])
    f.close()
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/firstname.500', 'r') as f:
        r = f.readlines()
        global fi500
        for i in r:
            fi500.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/firstname.1000', 'r') as f:
        r = f.readlines()
        global fi1000
        for i in r:
            fi1000.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/lastname.10', 'r') as f:
        r = f.readlines()
        global la10
        for i in r:
            la10.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/lastname.100', 'r') as f:
        r = f.readlines()
        global la100
        for i in r:
            la100.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/lastname.500', 'r') as f:
        r = f.readlines()
        global la500
        for i in r:
            la500.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/lastname.1000', 'r') as f:
        r = f.readlines()
        global la1000
        for i in r:
            la1000.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/location', 'r') as f:
        r = f.readlines()
        global loc
        for i in r:
            loc.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/location.country', 'r') as f:
        r = f.readlines()
        global locou
        for i in r:
            locou.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/lower.100', 'r') as f:
        r = f.readlines()
        global low100
        for i in r:
            low100.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/lower.500', 'r') as f:
        r = f.readlines()
        global low500
        for i in r:
            low500.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/lower.1000', 'r') as f:
        r = f.readlines()
        global low1000
        for i in r:
            low1000.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/people.family_name', 'r') as f:
        r = f.readlines()
        global peofam
        for i in r:
            peofam.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/people.person', 'r') as f:
        r = f.readlines()
        global peope
        for i in r:
            peope.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/people.person.lastnames', 'r') as f:
        r = f.readlines()
        global peopela
        for i in r:
            peopela.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/product', 'r') as f:
        r = f.readlines()
        global pro
        for i in r:
            pro.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/sports.sports_league', 'r') as f:
        r = f.readlines()
        global spsp
        for i in r:
            spsp.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/sports.sports_team', 'r') as f:
        r = f.readlines()
        global spspte
        for i in r:
            spspte.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/time.holiday', 'r') as f:
        r = f.readlines()
        global tiho
        for i in r:
            tiho.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/time.recurring_event', 'r') as f:
        r = f.readlines()
        global tire
        for i in r:
            tire.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/transportation.road', 'r') as f:
        r = f.readlines()
        global trro
        for i in r:
            trro.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/tv.tv_network', 'r') as f:
        r = f.readlines()
        global tvtvne
        for i in r:
            tvtvne.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/tv.tv_program', 'r') as f:
        r = f.readlines()
        global tvtvpr
        for i in r:
            tvtvpr.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/venture_capital.venture_funded_company', 'r') as f:
        r = f.readlines()
        global veca
        for i in r:
            veca.append(i.split("\n")[0])
    f.close()
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/venues', 'r') as f:
        r = f.readlines()
        global ven
        for i in r:
            ven.append(i.split("\n")[0])
    f.close()
    
    
    with open('C:/C/Fall2017/NLP/HW6/Homework-6/data/lexicon/government.government_agency', 'r') as f:
        r = f.readlines()
        global gogo
        for i in r:
            gogo.append(i.split("\n")[0])
    f.close()
    
    return armu,auma,aumo,awaw,bafe,bigdict,bone,brch, bubr,buco,bucon,busp,cap10,cap100,cap500,cap1000,cvco,cvcv,cvcvp,dico,edun,enst,fi5k,fi10,fi100,fi500,fi1000,la10,la100,la500,la1000,loc,locou,low100,low500,low1000,peofam,peope,peopela,pro,spsp,spspte,tiho,tire,trro, tvtvne,tvtvpr,veca, ven,gogo
    
    """Use the sentences to do whatever preprocessing you think is suitable,
    such as counts, keeping track of rare features/words to remove, matches to lexicons,
    loading files, and so on. Avoid doing any of this in token2features, since
    that will be called on every token of every sentence.

    Of course, this is an optional function.

    Note that you can also call token2features here to aggregate feature counts, etc.
    """
    pass

def token2features(sent, i, add_neighs = True):

    """Compute the features of a token.

    All the features are boolean, i.e. they appear or they do not. For the token,
    you have to return a set of strings that represent the features that *fire*
    for the token. See the code below.

    The token is at position i, and the rest of the sentence is provided as well.
    Try to make this efficient, since it is called on every token.

    One thing to note is that it is only called once per token, i.e. we do not call
    this function in the inner loops of training. So if your training is slow, it's
    not because of how long it's taking to run this code. That said, if your number
    of features is quite large, that will cause slowdowns for sure.

    add_neighs is a parameter that allows us to use this function itself in order to
    recursively add the same features, as computed for the neighbors. Of course, we do
    not want to recurse on the neighbors again, and then it is set to False (see code).
    """
    
    ftrs = []
    # bias
    ftrs.append("BIAS")
    # position features
    if i == 0:
        ftrs.append("SENT_BEGIN")
    if i == len(sent)-1:
        ftrs.append("SENT_END")

    # the word itself
    word = unicode(sent[i])
#    print(word,'5555555555555555555')
    ftrs.append("WORD=" + word)
    ftrs.append("LCASE=" + word.lower())
    # some features of the word
    if word.isalnum():
        ftrs.append("IS_ALNUM")
    if word.isnumeric():
        ftrs.append("IS_NUMERIC")
    if word.isdigit():
        ftrs.append("IS_DIGIT")
    if word.isupper():
        ftrs.append("IS_UPPER")
    if word.islower():
        ftrs.append("IS_LOWER")
        
    if word[0].isupper() and word[1:].islower():
        ftrs.append("CAPTI")
    if ((",") or ("'") or ("!") or (".") or ("$") or (":") or (";")) == word:
        ftrs.append("PUNC")
        
    if ("www.") in word or ("http") in word:
        ftrs.append("URL")
    f=nltk.pos_tag([word])
    
    if 'PRP' == f[0][1]:
        ftrs.append("PRP")
    if 'NP' == f[0][1]:
        ftrs.append("NP")
    if 'RB' == f[0][1]:
        ftrs.append("RB")
    if 'AT' == f[0][1]:
        ftrs.append("AT")
    if 'NN' == f[0][1]:
        ftrs.append("NN")
    if 'VBP' == f[0][1]:
        ftrs.append("VBP")

    if 'VBD' == f[0][1]:
        ftrs.append("VBD")
    if 'JJ'== f[0][1]:
        ftrs.append("JJ")
        
    if 'NNS' == f[0][1]:
        ftrs.append("NNS")
    if 'VB' == f[0][1]:
        ftrs.append("VB")
    if 'CC' == f[0][1]:
        ftrs.append("CC")
    if 'DT' == f[0][1]:
        ftrs.append("DT")
    if 'IN' == f[0][1]:
        ftrs.append("IN")
    if 'NNPS' == f[0][1]:
        ftrs.append("NNPS")
    if 'JJR' == f[0][1]:
        ftrs.append("JJR")
    if 'JJS' == f[0][1]:
        ftrs.append("JJS")
    if 'VBG' == f[0][1]:
        ftrs.append("VBG")
    if 'RBS' == f[0][1]:
        ftrs.append("RBS")
    if 'RBR' == f[0][1]:
        ftrs.append("RBR")
        
    if 'NNP' == f[0][1]:
        ftrs.append("NNP")
    if '#' in word:
        ftrs.append("HASH")
    if '@' in word:
        ftrs.append("PERSON")
#    armu,auma,aumo,awaw,bafe,bigdict,bone,brch,bubr,buco,bucon,busp,cvco,cvcv,cvcvp,edun,loc,locou,peope,peofam,pro,spsp,spspte,tire,tiho,trro,tvtvne,tvtvpr,veca,ven,gogo=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    
    if word.lower() in ["museum", "park","gallery"] :
        ftrs.append("LOC")
    
                
            
    for ss in auma:
        if unicode(word.lower()) == ss.lower():
        
            ftrs.append("PRODUCT")
            break
            
    for ss in aumo:
        if word.lower() == ss.lower():
        
            ftrs.append("PRODUCT")
            break
        
    
    if word.lower() in ["prize", "award","awards"] :
        ftrs.append("EVENT")
        
    if word.lower() == "festival":
        
        ftrs.append("EVENT")
        
        
        
#    for ss in bigdict:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("bigdict")
#            
#            
            
            
        
#    for ss in bone:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("bone")

    if word.lower() == "festival":
        
        ftrs.append("EVENT")
        
    if word.lower() in ["tv","channel"]:
        
        ftrs.append("TVSHOW")
    
#    for ss in brch:
#        if word.lower() == ss.lower().split():
#        
#            ftrs.append("brch")
#            break
            
#    for ss in bubr:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("bubr")
#            break
        
    for ss in buco:
        if word.lower() == ss.lower() and word.lower() not in low500 :
        
            ftrs.append("PRODCUT")
            break
        
    for ss in pro:
        if word.lower() == ss.lower() and word.lower() not in low500 and  word.lower() not in ["nikon","sony","samsung","kodak","htc","motorola","nokia","apple","canon"] :
        
            ftrs.append("PRODCUT")
            break
        
    for ss in cvcv:
        if word.lower() == ss.lower() and word.lower() not in low500 :
        
            ftrs.append("PRODCUT")
            break
        
    for ss in veca:
        if word.lower() == ss.lower() and word.lower() not in low500 :
        
            ftrs.append("COMPANY")
            break
#    for ss in bucon:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("bucon")
#            break
#        
#    for ss in busp:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("busp")

    if word.lower() in ["nikon","sony","samsung","kodak","htc","motorola","nokia","apple"]  :
        ftrs.append("COMPANY")
#    for ss in bucon:
#        if unicode(word.lower()) == ss.lower().split()[0]:
#            print(ss.lower().split(),word,ss.lower().split()[0])
#        
#            ftrs.append("PRODUCT")
#            break
   
        
#    if word in cap10:
#        ftrs.append("cap10")
#        
#    if word in cap100:
#        ftrs.append("cap100")
#        
#    if word in cap500:
#        ftrs.append("LOC")
        
#    if word in cap1000:
#        ftrs.append("LOC")
        
#    for ss in cvco:
#        if word.lower() in ss.lower().split():
#        
#            ftrs.append("cvco")
#            break
        
    if word.lower() in ["studio","studios","games","game"]  :
        
        ftrs.append("PRODUCT")
        

#    for ss in cvcvp:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("cvcvp")    

        
#    if word in dico:
#        ftrs.append("dico")
        
    
    if word.lower() in ["unversity","collge","school"]:
        
            ftrs.append("LOC")
        
 
        
#    if word in enst:
#        ftrs.append("enst")
#        
    if word in fi5k:
        ftrs.append("PERSON")
        
#    if word in fi10:
#        ftrs.append("fi10")
#        
#    if word in fi100:
#        ftrs.append("fi100")
#        
#    if word in fi500:
#        ftrs.append("fi500")
#        
#    if word in fi1000:
#        ftrs.append("fi1000")
        
#    if word in la10:
#        ftrs.append("la10")
#        
#    if word in la100:
#        ftrs.append("la100")
#        
#    if word in la500:
#        ftrs.append("la500")
#        
        
    if word in la1000:
        ftrs.append("PERSON")
        
        
#    for ss in loc:
#        if unicode(word.lower()) in ss.lower().split() and unicode(word.lower()) not in low500:
#        
#            ftrs.append("LOC")
#            break
#        
    for ss in locou:
        if unicode(word.lower()) in ss.lower().split() and unicode(word.lower()) not in enst:
            ftrs.append("LOC")
            break



        
#    if word in low100:
#        ftrs.append("low100")
#        
#    if word in low500:
#        ftrs.append("low500")
        
#    if word in low1000:
#        ftrs.append("low1000")
#        

    for ss in peofam:
        if unicode(word.lower()) == ss.lower():
        
            ftrs.append("PERSON")
            break
    
#    for ss in peope:
#        if unicode(word.lower()) == ss.lower():
#        
#            ftrs.append("PERSON")
#            break
    
#    for ss in peopela:
#        if unicode(word.lower()) == ss.lower():
#        
#            ftrs.append("PERSON")
#            break
#    

    
    
        
#    for ss in pro:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("pro")    
#        

    if word.lower() == "league":
    
        ftrs.append("SPORT")  
            
    
    if word.lower() in ["f.c.","fc","club"] :
    
        ftrs.append("SPORT")  
        
    if word.lower() in ["day"] :
    
        ftrs.append("EVENT")  
            

#    for ss in tire:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("tire")    
            
    if word.lower() in ["road","drive","highway","street","route"]:
    
        ftrs.append("OTHER")    
   
   
    for ss in tvtvne:
        if word.lower() == ss.lower() and word.lower() not in low1000:
        
            ftrs.append("TVSHOW")    
            break
            
#    for ss in tvtvpr:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("tvtvpr")    
        

#    for ss in veca:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("veca")    
#
#    for ss in ven:
#        if word.lower() == ss.lower():
#        
#            ftrs.append("ven")    
    if word.lower() in ['federal','office','department','ministry','agency']:
        
        ftrs.append("LOC")    


        

    

    # previous/next word feats
    if add_neighs:
        if i > 0:
            for pf in token2features(sent, i-1, add_neighs = False):
                ftrs.append("PREV_" + pf)
        if i < len(sent)-1:
            for pf in token2features(sent, i+1, add_neighs = False):
                ftrs.append("NEXT_" + pf)
                
#        if i > 1:
#            for pf in token2features(sent, i-2, add_neighs = False):
#                ftrs.append("PREVofPREV_" + pf)
#        if i < len(sent)-2:
#            for pf in token2features(sent, i+2, add_neighs = False):
#                ftrs.append("NEXTofNEXT_" + pf)

    # return it!
    return ftrs

if __name__ == "__main__":
    sents = [
    [ "I", "love", "food," ,"and","white","http:/house",",","@bush"]
    ]
    cap10=preprocess_corpus(sents)
    
    for sent in sents:
        for i in xrange(len(sent)):
            print sent[i], ":", token2features(sent, i)
