def nonEnglish (string):
    
    counter = 0 
    
    for i in string:    
        
        if ord(i) <= 127:
            counter = counter + 1
            
            if counter == len (string):
                print ('This App is in English.')
            
        elif ord(i)>= 127:
            print ('This App is not in English or may have unknown characters.')
            break