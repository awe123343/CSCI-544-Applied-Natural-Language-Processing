from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    f1 = FST('soundex-generate')
    #dic={1:['b','f','p','v'],2:['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],3:['d','t'],4:['l'],5:['m','n'],6:['r']}
    dic1=['b','f','p','v','B','F','P','V']
    dic2=['c', 'g', 'j', 'k', 'q', 's', 'x', 'z','C','G','J','K','Q','S','X','Z']
    dic3=['d','t','D','T']
    dic4=['l','L']
    dic5=['m','n','M','N']
    dic6=['r','R']
    
    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('next')
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.add_state('8')
    f1.add_state('7')
    f1.add_state('10')
    f1.add_state('finish')
    f1.initial_state = 'start'
    # Set all the final states
    f1.set_final('2')
    f1.set_final('1')

    f1.set_final('3')
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')
    f1.set_final('7')
    f1.set_final('8')
    f1.set_final('10')
    f1.set_final('start')

    
    vowels = ['a', 'e','h', 'i', 'o', 'u', 'w', 'y','A','E','H','I','O','U','W']
    
    for letter in string.digits:
        f1.add_arc('start', '10', (letter), (letter))
        f1.add_arc('10', '10', (letter), (letter))
        f1.add_arc('1', '10', (letter), (letter))
        f1.add_arc('2', '10', (letter), (letter))
        f1.add_arc('3', '10', (letter), (letter))
        f1.add_arc('4', '10', (letter), (letter))
        f1.add_arc('5', '10', (letter), (letter))
        f1.add_arc('6', '10', (letter), (letter))
        f1.add_arc('8', '10', (letter), (letter))

        
    
        
            
            
    for letter in string.ascii_letters:

        
    
        if letter in dic1:
            f1.add_arc('start', '1', (letter), (letter))
            f1.add_arc('1', '1', (letter), ())
            f1.add_arc('3', '1', (letter), '1')
            f1.add_arc('4', '1', (letter), '1')
            f1.add_arc('5', '1', (letter), '1')
            f1.add_arc('6', '1', (letter), '1')
            f1.add_arc('7', '1', (letter), '1')
            f1.add_arc('8', '1', (letter), '1')
            f1.add_arc('10', '1', (letter), '1')
            
            
        
            
            
        if letter in dic2:
            f1.add_arc('start', '2', (letter), (letter))
            f1.add_arc('1', '2', (letter), '2')
            f1.add_arc('2', '2', (letter), ())
            f1.add_arc('3', '2', (letter), '2')
            f1.add_arc('4', '2', (letter), '2')
            f1.add_arc('5', '2', (letter), '2')
            f1.add_arc('6', '2', (letter), '2')
            f1.add_arc('7', '2', (letter), '2')
            f1.add_arc('8', '2', (letter), '2')
            f1.add_arc('10', '2', (letter), '2')
        
        if letter in dic3:
            f1.add_arc('start', '3', (letter), (letter))
            f1.add_arc('1', '3', (letter), '3')
            f1.add_arc('2', '3', (letter), '3')
            f1.add_arc('3', '3', (letter), ())
            f1.add_arc('4', '3', (letter), '3')
            f1.add_arc('5', '3', (letter), '3')
            f1.add_arc('6', '3', (letter), '3')
            f1.add_arc('7', '3', (letter), '3')
            f1.add_arc('8', '3', (letter), '3')
            f1.add_arc('10', '3', (letter), '3')
            
            
        
        if letter in dic4:
            f1.add_arc('start', '4', (letter), (letter))
            f1.add_arc('1', '4', (letter), '4')
            f1.add_arc('2', '4', (letter), '4')
            f1.add_arc('4', '4', (letter), ())
            f1.add_arc('6', '4', (letter), '4')
            f1.add_arc('7', '4', (letter), '4')
            f1.add_arc('3', '4', (letter), '4')
            f1.add_arc('8', '4', (letter), '4')
            f1.add_arc('5', '4', (letter), '4')
            f1.add_arc('10', '4', (letter), '4')
            
            
        if letter in dic5:
            f1.add_arc('start', '5', (letter), (letter))
            f1.add_arc('1', '5', (letter), '5')
            f1.add_arc('2', '5', (letter), '5')
            f1.add_arc('6', '5', (letter), '5')
            f1.add_arc('4', '5', (letter), '5')
            f1.add_arc('5', '5', (letter), ())
            f1.add_arc('3', '5', (letter), '5')
            f1.add_arc('7', '5', (letter), '5')
            f1.add_arc('8', '5', (letter), '5')
            f1.add_arc('10', '5', (letter), '5')
            
        
        if letter in dic6:
            f1.add_arc('start', '6', (letter), (letter))
            f1.add_arc('1', '6', (letter), '6')
            f1.add_arc('2', '6', (letter), '6')
            f1.add_arc('3', '6', (letter), '6')
            f1.add_arc('6', '6', (letter), ())
            f1.add_arc('4', '6', (letter), '6')
            f1.add_arc('5', '6', (letter), '6')
            f1.add_arc('3', '6', (letter), '6')
            f1.add_arc('8', '6', (letter), '6')
            f1.add_arc('10', '6', (letter), '6')
            
        if letter in vowels:
            f1.add_arc('start', '8', (letter), (letter))
            f1.add_arc('1', '8', (letter), ())
            f1.add_arc('2', '8', (letter), ())
            f1.add_arc('3', '8', (letter), ())
            f1.add_arc('4', '8', (letter), ())
            f1.add_arc('5', '8', (letter), ())
            f1.add_arc('6', '8', (letter), ())
            f1.add_arc('7', '8', (letter), ())
            f1.add_arc('8', '8', (letter), ())
            f1.add_arc('10', '8', (letter), ())
     

            

            
            
            
        
         
            
            

 
    
        

                
                
    return f1
    
    
        
     

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    f2.add_state('start')
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.add_state('5')
    f2.add_state('6')
    f2.add_state('8')
    f2.add_state('7')
    f2.add_state('9')
    f2.add_state('0')

    
    f2.initial_state = 'start'
    # Set all the final states
    f2.set_final('2')
    f2.set_final('1')

    f2.set_final('3')
    f2.set_final('4')
    f2.set_final('5')
    f2.set_final('6')
    f2.set_final('7')
    f2.set_final('8')
    f2.set_final('9')
    f2.set_final('0')



    # Add the arcs
    for letter in string.letters:
        f2.add_arc('start', '0', (letter), (letter))
    for letter in string.digits:
        f2.add_arc('start', '5', (letter), (letter))

    for letter in string.digits:
        f2.add_arc('5', '6', (letter), (letter))
        f2.add_arc('6', '7', (letter), (letter))
        f2.add_arc('7', '7', (letter), ())
        f2.add_arc('0', '1', (letter), (letter))
        f2.add_arc('1', '2', (letter), (letter))
        f2.add_arc('2', '3', (letter), (letter))
        f2.add_arc('3', '3', (letter), ())
        

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('start')
    f3.add_state('1')
    f3.add_state('2')
    f3.add_state('3')
    f3.add_state('4')
    f3.add_state('5')
    f3.add_state('6')
    f3.add_state('8')
    f3.add_state('7')
    f3.add_state('9')
    
    f3.add_state('0')
    f3.add_state('15')
    f3.add_state('16')
    f3.add_state('17')
    
    f3.initial_state = 'start'
    # Set all the final states
  
    f3.set_final('3')
    f3.set_final('6')
    f3.set_final('17')
    


    num=['1','2','3','4','5','6','7','8','9']

    # Add the arcs
    
   
        
    for letter in string.letters:
        f3.add_arc('start', '0', (letter), (letter))
        
    for letter in string.digits:
        f3.add_arc('start', '15', (letter), (letter))
    f3.add_arc('15', '16', (), ('0'))
    f3.add_arc('16', '17', (), ('0'))
    
        
    for letter in string.digits:
        f3.add_arc('0', '1', (letter), (letter))
        f3.add_arc('1', '2', (letter), (letter))
        f3.add_arc('2', '3', (letter), (letter))
    
    f3.add_arc('0', '4', (), ('0'))
    f3.add_arc('4', '5', (), ('0'))
    f3.add_arc('5', '6', (), ('0'))
    
    f3.add_arc('1', '5', (), ('0'))
    f3.add_arc('5', '6', (), ('0'))
    
    f3.add_arc('2', '6', (), ('0'))
       
        
 
     
        
            
    
    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
