from csv import writer
import pandas as pd
#Check if user wants to add to list or see list
print("Would you like to add something to your list or see the list? [y/n]")
answer = input()
#Add work (input) to csv file if the input is "y"
if answer =="y":
    print("What do you have for work?")
    lst = input()
    with open('worklist.csv', 'a') as f_object:


        writer_object = writer(f_object)


        writer_object.writerow(lst)    

        f_object.close()
#Print list if the input is "n"
elif answer =="n":
    #Allow unlimited fields
    work = pd.read_csv("worklist.csv", sep='\t')
    #Remove commas from output
    work = work.apply(lambda x: x.str.replace(',', ''))
    #Print the list
    print(work)
    
    
