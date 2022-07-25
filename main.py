from svlib import *

print("\nWelcome to Tree Stem Volume Estimator")
print("\nPlease choose operation type")

print("1. Calculate volume manually")
print("2. Calculate volume by uploading file")
tasktype = input("Your response :")
print("-"*40)


if tasktype == '1':
    tryflag = 'y'
    while tryflag.casefold() == 'y':
        Manual()
        tryflag = input("Do you want to calculate again? (Y/N): ")
        # if temptryflag.casefold() not in ['y','yes','n','no']:
        #     print("Sorry! Invalid response. Try Again")
        # else:
elif tasktype =='2':
    Fileupload()

print("Thank You for using our app!")
print("-"*40)
