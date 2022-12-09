def nonEnglish (string):
    
    counter = 0 
    nonEnglishCounter = 0
    
    for i in string:    
        
        if ord(i) <= 127:
            counter = counter + 1
            
        elif ord(i)>= 127:
            nonEnglishCounter = nonEnglishCounter + 1
                    
    if counter == len (string):
        print ('The name of this App is in English.')
            
    elif nonEnglishCounter <= 2:
        print ('The name of this App is in English, but may contain non-English characters or emojis.')
            
    else:
        print ('This App is not in English or may have unknown characters.')