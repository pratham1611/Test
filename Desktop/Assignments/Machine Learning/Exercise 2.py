import numpy
import pandas
import matplotlib.pyplot
lstCol1=list(range(0,6)) #stores range 0 to 5 in a list
print("List 1 :",lstCol1)
lstCol2=[0,1,4,9,16,25] #creates list2
print("List 2 :",lstCol1)
arr=numpy.array([lstCol1,lstCol2]) #creates 6 X 2 array with lstCol1 and lstCol2 
print(arr) #prints that array
dframe=pandas.DataFrame({'x':lstCol1,'y':lstCol2}) #put that array in a dataframe with column labels 'x' and 'y'
print(dframe) #prints dframe
matplotlib.pyplot.plot(lstCol1,lstCol2) #plot x v/s y using matplotlib
dframe.loc[:,"y"].mean() #using the mean function of dframe to locate column label 'y' and calculate average