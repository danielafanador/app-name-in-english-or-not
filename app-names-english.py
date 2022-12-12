apps_in_english = []
apps_w_special_characters = []
apps_not_in_english = []
    
for app in list_of_csv[1:]:    
    
    name = app [0]
    counter = 0 
    nonEnglishCounter = 0    
    
    for i in name:    
        
        if ord(i) <= 127:
            counter += 1

        elif ord(i)>= 127:
            nonEnglishCounter += 1
                    
    if counter == len (name):
        apps_in_english.append(name)
        
        
    elif nonEnglishCounter <= 2:
        apps_w_special_characters.append(name)
    
    else:

        apps_not_in_english.append(name)
        
#print (apps_in_english)
#print (apps_w_special_characters)
#print (apps_not_in_english)