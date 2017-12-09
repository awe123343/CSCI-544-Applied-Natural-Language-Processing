import numpy as np

def run_viterbi(em, tran, s, e):
    """Run the Viterbi algorithm.

    N - number of tokens (length of sentence)
    L - number of labels

    As an input, you are given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    You have to return a tuple (s,y), where:
    - s is the score of the best sequence
    - y is a size N array of integers representing the best sequence.
    """
#    print('1',em,'2',tran,'3',s,'4',e,'5')
    res=[[0 for i in range(len(em)+1)]for j in range(len(tran))] 
    back=[[0 for i in range(len(em)+1)]for j in range(len(tran))] 
    
    
    
    
    
    
    for i in range(len(em[0])):
            
        res[i][0]=s[i]+em[0][i]
    pp=[]
    f=[] 
    for i in range(1,len(em)):
        for j in range(len(tran)):
            
            for k in range(len(tran)):
                
                f.append(em[i][j]+tran[k][j]+res[k][i-1])
                
            
            res[j][i]=max(f)
            ind=f.index(max(f))
            pp.append(ind)
            back[j][i]=(ind)
    #        print(j,k,'111')
    #        for p in range(len(f)):
    #            
    #            res[p][i]=f[p]
    ##        print(res,'res')
            f=[]
            
    sd=[]
    for i in range(2,len(pp)-1,2):
        sd.append(min(pp[i],pp[i+1]))
        
    
    for i in range(len(em[0])):
            
        res[i][-1]=e[i]+res[i][-2]  
    path=-100000
    for i in range(len(res)):
        if res[i][-1]>path:
            nnn=i
            path=res[i][-1]
    final=[]
    final.append(nnn)        
    
    for i in range(len(em)-1,0,-1):
        final.append(back[nnn][i])
        nnn=back[nnn][i]
        
    final=final[::-1]    
        
                    
        
    
    L = s.shape[0]
    assert e.shape[0] == L
    assert tran.shape[0] == L
    assert tran.shape[1] == L
    assert em.shape[1] == L
    N = em.shape[0]
    y = []
    for i in xrange(N):
        
        
        
        # stupid sequence
        y.append(i % L)
#    # score set to 0
#    print(0.0,y)
    return (path, final)
