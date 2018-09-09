Scores={'Team1':'4','Team2':'3','Team3':'5','Team4':'2'} #creates Scores dictionary
print (Scores) #prints Scores dictionary
Scores['Team5']='5' #add new key:val pair to Scores dictionary
print(Scores) #prints updated Scores dictionary
print(Scores.keys()) #print all keys of dictionary
lenVal=[len(v) for v in Scores.values()]  #gets length of individual values of each key
print(lenVal) #prints a list with length of individual values
intval=[int(v) for v in Scores.values()] #converts string values to int values and adding them to a list
avglistval=sum(intval)/len(intval) #calculates average of list values
print(avglistval) #prints average of list