import sys
from fst import FST
from fsmutils import composewords
from fsmutils import trace

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return  list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    
    f.add_state('1')
    f.add_state('0')
    f.add_state('1a')
    f.add_state('2a')
    f.add_state('2')
    f.add_state('20')
    f.add_state('30')
    f.add_state('40')
    f.add_state('50')
    f.add_state('60')
    f.add_state('70')
    f.add_state('80')
    f.add_state('90')
    f.add_state('100')
    f.add_state('200')
    f.add_state('300')
    f.add_state('400')
    f.add_state('500')
    f.add_state('600')
    f.add_state('700')
    f.add_state('800')
    f.add_state('900')
    f.add_state('3')
    f.add_state('3a')
    
    
    f.initial_state = 'start'
    f.set_final('start')
    f.set_final('3')
    f.set_final('3a')
    f.set_final('2')
    f.set_final('1')
    f.set_final('0')
    
    

    f.add_arc('start', '1', ('0'), ())
    f.add_arc('1', '1a', ('0'), ())
    f.add_arc('1', '0', ('0'), ())
    f.add_arc('0', '0', ('0'), ["zero"])
    for ii in range(1,10):
        f.add_arc('1a', '3', [str(ii)], [kFRENCH_TRANS[ii]])
 
    
    
    
    f.add_arc('1', '2', ('1'), ())
    f.add_arc('1', '2a', ('1'), ())
    
    f.add_arc('2', '3', ('0'), ['dix'])
    f.add_arc('2', '3', ('1'), ["onze"])
    f.add_arc('2', '3', ('2'), ["douze"])
    f.add_arc('2', '3', ('3'), ["treize"])
    f.add_arc('2', '3', ('4'), ["quatorze"])
    f.add_arc('2', '3', ('5'), ["quinze"])
    f.add_arc('2', '3', ('6'), ["seize"])
    
    f.add_arc('2a', '3', ('7'), ["dix sept"])
    f.add_arc('2a', '3', ('8'), ["dix huit"])
    f.add_arc('2a', '3', ('9'), ["dix neuf"])
    
    
    f.add_arc('1', '20', ('2'), ['vingt'])
    for ii in range(2,10):
        f.add_arc('20', '3', [str(ii)], [kFRENCH_TRANS[ii]])
    f.add_arc('20', '3', ('0'), ())
    f.add_arc('20', '3', ('1'), ['et un'])
    f.add_arc('20', '3', ('1'), ['et un'])
    
    
    f.add_arc('1', '30', ('3'), ['trente'])
    for ii in range(2,10):
        f.add_arc('30', '3', [str(ii)], [kFRENCH_TRANS[ii]])
    f.add_arc('30', '3', ('0'), ())
    f.add_arc('30', '3', ('1'), ['et un'])
    
    
    f.add_arc('1', '40', ('4'), ['quarante'])
    for ii in range(2,10):
        f.add_arc('40', '3', [str(ii)], [kFRENCH_TRANS[ii]])
    f.add_arc('40', '3', ('0'), ())
    f.add_arc('40', '3', ('1'), ['et un'])
    
    
    f.add_arc('1', '50', ('5'), ['cinquante'])
    for ii in range(2,10):
        f.add_arc('50', '3', [str(ii)], [kFRENCH_TRANS[ii]])
    f.add_arc('50', '3', ('0'), ())
    f.add_arc('50', '3', ('1'), ['et un'])
    
    
    
    f.add_arc('1', '60', ('6'), ['soixante'])
    for ii in range(2,10):
        f.add_arc('60', '3', [str(ii)], [kFRENCH_TRANS[ii]])
    f.add_arc('60', '3', ('0'), ())
    f.add_arc('60', '3', ('1'), ['et un'])
    
    
    
    f.add_arc('1', '2', ('7'), ['soixante'])
    f.add_arc('1', '70', ('7'), ['soixante'])
    f.add_arc('1', '2a', ('7'), ['soixante'])
    f.add_arc('70', '3', ('1'), ['et onze'])
    
    
    
    f.add_arc('1', '1a', ('8'), ['quatre vingt'])
    f.add_arc('1a', '3a', ('0'), ())
    
    
    f.add_arc('1', '2', ('9'), ['quatre vingt'])
    f.add_arc('1', '2a', ('9'), ['quatre vingt'])

    
    
    f.add_arc('start', '100', ('1'), ['cent'])
    f.add_arc('100', '1a', ('0'), ())
    f.add_arc('100', '2', ('1'), ())
    f.add_arc('100', '2a', ('1'), ())
    
    f.add_arc('100', '20', ('2'), ['vingt'])
    f.add_arc('100', '30', ('3'), ['trente'])
    f.add_arc('100', '40', ('4'), ['quarante'])
    f.add_arc('100', '50', ('5'), ['cinquante'])
    f.add_arc('100', '60', ('6'), ['soixante'])
    
    
    f.add_arc('100', '2', ('7'), ['soixante'])
    f.add_arc('100', '70', ('7'), ['soixante'])
    f.add_arc('100', '2a', ('7'), ['soixante'])
    
    f.add_arc('100', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('100', '2', ('9'), ['quatre vingt'])
    f.add_arc('100', '2a', ('9'), ['quatre vingt'])
    
    
    
    f.add_arc('start', '200', ('2'), ['deux cent'])
    f.add_arc('200', '1a', ('0'), ())
    f.add_arc('200', '2', ('1'), ())
    f.add_arc('200', '2a', ('1'), ())
    
    f.add_arc('200', '20', ('2'), ['vingt'])
    f.add_arc('200', '30', ('3'), ['trente'])
    f.add_arc('200', '40', ('4'), ['quarante'])
    f.add_arc('200', '50', ('5'), ['cinquante'])
    f.add_arc('200', '60', ('6'), ['soixante'])
    
    
    f.add_arc('200', '2', ('7'), ['soixante'])
    f.add_arc('200', '70', ('7'), ['soixante'])
    f.add_arc('200', '2a', ('7'), ['soixante'])
    
    f.add_arc('200', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('200', '2', ('9'), ['quatre vingt'])
    f.add_arc('200', '2a', ('9'), ['quatre vingt'])
    
    
    f.add_arc('start', '300', ('3'), ['trois cent'])
    f.add_arc('300', '1a', ('0'), ())
    f.add_arc('300', '2', ('1'), ())
    f.add_arc('300', '2a', ('1'), ())
    
    f.add_arc('300', '20', ('2'), ['vingt'])
    f.add_arc('300', '30', ('3'), ['trente'])
    f.add_arc('300', '40', ('4'), ['quarante'])
    f.add_arc('300', '50', ('5'), ['cinquante'])
    f.add_arc('300', '60', ('6'), ['soixante'])
    
    
    f.add_arc('300', '2', ('7'), ['soixante'])
    f.add_arc('300', '70', ('7'), ['soixante'])
    f.add_arc('300', '2a', ('7'), ['soixante'])
    
    f.add_arc('300', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('300', '2', ('9'), ['quatre vingt'])
    f.add_arc('300', '2a', ('9'), ['quatre vingt'])
    
    
    f.add_arc('start', '400', ('4'), ['quatre cent'])
    f.add_arc('400', '1a', ('0'), ())
    f.add_arc('400', '2', ('1'), ())
    f.add_arc('400', '2a', ('1'), ())
    
    f.add_arc('400', '20', ('2'), ['vingt'])
    f.add_arc('400', '30', ('3'), ['trente'])
    f.add_arc('400', '40', ('4'), ['quarante'])
    f.add_arc('400', '50', ('5'), ['cinquante'])
    f.add_arc('400', '60', ('6'), ['soixante'])
    
    
    f.add_arc('400', '2', ('7'), ['soixante'])
    f.add_arc('400', '70', ('7'), ['soixante'])
    f.add_arc('400', '2a', ('7'), ['soixante'])
    
    f.add_arc('400', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('400', '2', ('9'), ['quatre vingt'])
    f.add_arc('400', '2a', ('9'), ['quatre vingt'])
    
    
    
    f.add_arc('start', '500', ('5'), ['cinq cent'])
    f.add_arc('500', '1a', ('0'), ())
    f.add_arc('500', '2', ('1'), ())
    f.add_arc('500', '2a', ('1'), ())
    
    f.add_arc('500', '20', ('2'), ['vingt'])
    f.add_arc('500', '30', ('3'), ['trente'])
    f.add_arc('500', '40', ('4'), ['quarante'])
    f.add_arc('500', '50', ('5'), ['cinquante'])
    f.add_arc('500', '60', ('6'), ['soixante'])
    
    
    f.add_arc('500', '2', ('7'), ['soixante'])
    f.add_arc('500', '70', ('7'), ['soixante'])
    f.add_arc('500', '2a', ('7'), ['soixante'])
    
    f.add_arc('500', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('500', '2', ('9'), ['quatre vingt'])
    f.add_arc('500', '2a', ('9'), ['quatre vingt'])
    
    
    
    f.add_arc('start', '600', ('6'), ['six cent'])
    f.add_arc('600', '1a', ('0'), ())
    f.add_arc('600', '2', ('1'), ())
    f.add_arc('600', '2a', ('1'), ())
    
    f.add_arc('600', '20', ('2'), ['vingt'])
    f.add_arc('600', '30', ('3'), ['trente'])
    f.add_arc('600', '40', ('4'), ['quarante'])
    f.add_arc('600', '50', ('5'), ['cinquante'])
    f.add_arc('600', '60', ('6'), ['soixante'])
    
    
    f.add_arc('600', '2', ('7'), ['soixante'])
    f.add_arc('600', '70', ('7'), ['soixante'])
    f.add_arc('600', '2a', ('7'), ['soixante'])
    
    f.add_arc('600', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('600', '2', ('9'), ['quatre vingt'])
    f.add_arc('600', '2a', ('9'), ['quatre vingt'])
    
    
    
    f.add_arc('start', '700', ('7'), ['sept cent'])
    f.add_arc('700', '1a', ('0'), ())
    f.add_arc('700', '2', ('1'), ())
    f.add_arc('700', '2a', ('1'), ())
    
    f.add_arc('700', '20', ('2'), ['vingt'])
    f.add_arc('700', '30', ('3'), ['trente'])
    f.add_arc('700', '40', ('4'), ['quarante'])
    f.add_arc('700', '50', ('5'), ['cinquante'])
    f.add_arc('700', '60', ('6'), ['soixante'])
    
    
    f.add_arc('700', '2', ('7'), ['soixante'])
    f.add_arc('700', '70', ('7'), ['soixante'])
    f.add_arc('700', '2a', ('7'), ['soixante'])
    
    f.add_arc('700', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('700', '2', ('9'), ['quatre vingt'])
    f.add_arc('700', '2a', ('9'), ['quatre vingt'])
    
    
    
    f.add_arc('start', '800', ('8'), ['huit cent'])
    f.add_arc('800', '1a', ('0'), ())
    f.add_arc('800', '2', ('1'), ())
    f.add_arc('800', '2a', ('1'), ())
    
    f.add_arc('800', '20', ('2'), ['vingt'])
    f.add_arc('800', '30', ('3'), ['trente'])
    f.add_arc('800', '40', ('4'), ['quarante'])
    f.add_arc('800', '50', ('5'), ['cinquante'])
    f.add_arc('800', '60', ('6'), ['soixante'])
    
    
    f.add_arc('800', '2', ('7'), ['soixante'])
    f.add_arc('800', '70', ('7'), ['soixante'])
    f.add_arc('800', '2a', ('7'), ['soixante'])
    
    f.add_arc('800', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('800', '2', ('9'), ['quatre vingt'])
    f.add_arc('800', '2a', ('9'), ['quatre vingt'])
    
    
    
    f.add_arc('start', '900', ('9'), ['neuf cent'])
    f.add_arc('900', '1a', ('0'), ())
    f.add_arc('900', '2', ('1'), ())
    f.add_arc('900', '2a', ('1'), ())
    
    f.add_arc('900', '20', ('2'), ['vingt'])
    f.add_arc('900', '30', ('3'), ['trente'])
    f.add_arc('900', '40', ('4'), ['quarante'])
    f.add_arc('900', '50', ('5'), ['cinquante'])
    f.add_arc('900', '60', ('6'), ['soixante'])
    
    
    f.add_arc('900', '2', ('7'), ['soixante'])
    f.add_arc('900', '70', ('7'), ['soixante'])
    f.add_arc('900', '2a', ('7'), ['soixante'])
    
    f.add_arc('900', '1a', ('8'), ['quatre vingt'])
    
    f.add_arc('900', '2', ('9'), ['quatre vingt'])
    f.add_arc('900', '2a', ('9'), ['quatre vingt'])
    
    
    
    
    
    
    
    
    
    
    


    
    

    
    
    
        
   
   
     
    
    

    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
        print " ".join(f.transduce(prepare_input(000)))
        print " ".join(f.transduce(prepare_input(16)))
        print " ".join(f.transduce(prepare_input(103)))
        print " ".join(f.transduce(prepare_input(104)))
        print " ".join(f.transduce(prepare_input(94)))
        print " ".join(f.transduce(prepare_input(95)))
        print " ".join(f.transduce(prepare_input(96)))
        print " ".join(f.transduce(prepare_input(97)))
        print " ".join(f.transduce(prepare_input(98)))
        print " ".join(f.transduce(prepare_input(99)))
        print (trace(f,str(user_input)))
