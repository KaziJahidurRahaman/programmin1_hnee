import time
import math

#Uploads and traverses the measurements data and return the in the file as array
def ReadFile():
    lines = [] #keeping lines empty at the begining

    with open("measurements.csv", 'r') as measurements: #opening the file in READ mode
        for line in measurements:                       #each line of the file is traveresd
            words = []
            for word in line.strip().split(','):        #each word is the value of each column,
                                                            # using ',' as separator between coulns

                if word.strip() =='':                   #if there is a blank value that will be skipped
                   continue
                words.append(word.strip())
            lines.append(words)
    return lines


#Uploads and Processes file automatically and Publishes the calculated volumes both on screen and an unique file
def Fileupload():
    lines = ReadFile()

    outputfile = "SVOUTPUT" + str(time.time_ns()) + ".txt"      #defining unique file name based on current time
                                                                    # in nanosecond for each file upload task

    print("Serial",":","Volume")
    for idx,line in enumerate(lines):                           #Processing rows of the uploaded file, keeping track of line #
        if line[0].casefold() == 'germany':                     #matching the names case-insensitively
            if line[1].casefold() == "pinus sylvestris":
                equationParameters = line[2:]                   #Only collumn from 2 to rests are numeric parameters for eqtn
                equationParameters = [int(i) for i in equationParameters] # using list comprehension
                                                                            # to perform conversion from str to int
                volume = germany_pinus_sylvestris(equationParameters)

            elif line[1].casefold() == "fagus sylvatica":
                equationParameters = line[2:]
                equationParameters = [int(i) for i in
                                      equationParameters]  # using list comprehension to perform conversion
                volume = germany_fagus_sylvatica(equationParameters)

            else:
                volume = "Species not supported yet"

        elif line[0].casefold() == 'romania':
            if line[1].casefold() == "pinus sylvestris":
                equationParameters = line[2:]
                equationParameters = [int(i) for i in
                                      equationParameters]  # using list comprehension to perform conversion
                volume = romania_pinus_sylvestris(equationParameters)

            else:
                volume= "Species not supported yet"

        elif line[0].casefold() == 'netherlands':
            if line[1].casefold() == "pinus sylvestris":
                equationParameters = line[2:]
                equationParameters = [int(i) for i in equationParameters] # using list comprehension to perform conversion
                volume = netherlands_pinus_sylvestris(equationParameters)

            elif line[1].casefold() == "fagus sylvatica":
                equationParameters = line[2:]
                equationParameters = [int(i) for i in
                                      equationParameters]  # using list comprehension to perform conversion
                volume = netherlands_fagus_sylvatica(equationParameters)

            else:
                volume = "Species not supported yet"
        else:
            volume = "Country Not Supported Yet"

        print(str(idx+1)+": "+str(volume))

        with open(outputfile, "a") as file1:                   #openning our output file in append mode
            file1.writelines(str(idx+1)+": "+str(volume)+"\n") # Writing each volume data at the ending position of the file
    print("-"* 40)
    print("Results exported to the file "+outputfile+" under the same location")
    print("-"* 40)

def Manual():
    countries = {
        "1": "Germany",
        "2": "Romania",
        "3": "Netherlands",
    }

    tryagain = 'y'
    while tryagain.casefold() =='y':        #if country code is not valid it will give option to select agin without exiting
        print("Please Select Your Country From The List")
        for country in countries:
            print(country, ":", countries[country]) #showing the countries in our list

        choiceCountry = input("Your response: ")
        print("-"*40)
        if choiceCountry in countries.keys():   #Checking if country key is avaialbe in our list
            if countries [choiceCountry] =='Germany':
                VolumeGermany()
            elif countries [choiceCountry] =='Romania':
                VolumeRomania()
            elif countries [choiceCountry] =='Netherlands':
                VolumeNetherlands()
            else:
                print("Country Still Not Available")
            break                       #After completing volume calculation the loop shall be stopped for this calculation
                                                    # and get back to the caller
        else:
            print("Sorry, the  country code", choiceCountry, "is invalid.")
            tryagain = input("Do you want to try again? (Y/N)")






def VolumeGermany():
    Specieses = {
        "1": {
            "SName":"Pinus sylvestris",
            "Variables": ["a","b","c","D","H"]          #Required variables in equations, # of v's varies for spcs to spcs
        },  # V = a.D^b 〖.H〗^c                 a,b,c,D,H
        "2": {
            "SName": "Fagus sylvatica",
            "Variables": ["a","b","c","D","H"]
        }  # V = a + b.D.H^2 + c.D^3           a,b,c,D,H
    }

    print("Select Tree Species From The List")
    for species in Specieses:
        print(species, ":", Specieses[species]["SName"])

    tryagain = 'y'
    while tryagain.casefold() =='y':
        choiceSpecies = input("Your response: ")
        print("-" * 40)
        if choiceSpecies in Specieses.keys():
            print("Please provide the measurements")
            values = []
            volume =0
            for variable in Specieses[choiceSpecies]["Variables"]:
                values.append(float(input(variable+':')))           #Type conversion to float, inputs in python are string
            # print(values)
            if Specieses[choiceSpecies]["SName"] == 'Pinus sylvestris':
                volume = germany_pinus_sylvestris(values)
            elif Specieses[choiceSpecies]["SName"] == 'Fagus sylvatica':
                volume = germany_fagus_sylvatica(values)
            else:
                print("Sorry. Species not found")
            print('-'*40)
            print("Volume =",volume)
            break

        else:
            print("Sorry, the  species code", choiceSpecies, "is invalid.")
            tryagain = input("Do you want to try again? (Y/N)")
def VolumeRomania():
    Specieses = {
        "1": {
            "SName":"Pinus sylvestris",
            "Variables": ["a","b","c","d","e","D","H"]
        }
    }
    print("Select Tree Species From The List")
    for species in Specieses:
        print(species, ":", Specieses[species]["SName"])

    tryagain = 'y'
    while tryagain.casefold() == 'y':
        choiceSpecies = input("Your response: ")
        print("-" * 40)

        if choiceSpecies in Specieses.keys():
            print("Please provide the measurements")
            values = []
            volume = 0
            for variable in Specieses[choiceSpecies]["Variables"]:
                values.append(float(input(variable + ':')))         #Type conversion to float, inputs in python are string
            if Specieses[choiceSpecies]["SName"] == 'Pinus sylvestris':
                volume = romania_pinus_sylvestris(values)
            else:
                print("Sorry. Species not found")
            print('-' * 40)
            print("Volume =", volume)
            break

        else:
            print("Sorry, the  species code", choiceSpecies, "is invalid.")
            tryagain = input("Do you want to try again? (Y/N)")

def VolumeNetherlands():
    Specieses = {
        "1": {
            "SName": "Pinus sylvestris",
            "Variables": ["a", "b", "c", "D", "H"]
        },  # V = a.D^b 〖.H〗^c                 a,b,c,D,H
        "2": {
            "SName": "Fagus sylvatica",
            "Variables": ["a", "b", "c", "D", "H"]
        }  # V = a + b.D.H^2 + c.D^3           a,b,c,D,H
    }

    print("Select Tree Species From The List")
    for species in Specieses:
        print(species, ":", Specieses[species]["SName"])

    tryagain = 'y'
    while tryagain.casefold() == 'y':
        choiceSpecies = input("Your response: ")
        print("-" * 40)

        if choiceSpecies in Specieses.keys():
            print("Please provide the measurements")
            values = []
            Volume = 0
            for variable in Specieses[choiceSpecies]["Variables"]:
                values.append(float(input(variable + ':')))         #Type conversion to float, inputs in python are string
            if Specieses[choiceSpecies]["SName"] == 'Pinus sylvestris':
                Volume = netherlands_pinus_sylvestris(values)
            elif Specieses[choiceSpecies]["SName"] == 'Fagus sylvatica':
                Volume = netherlands_fagus_sylvatica(values)
            else:
                print("Sorry. Species not found")
            print('-' * 40)
            print("Volume =", Volume)
            break
        else:
            print("Sorry, the  species code", choiceSpecies, "is invalid.")
            tryagain = input("Do you want to try again? (Y/N)")

def germany_pinus_sylvestris(values):
    a = values[0]
    b = values[1]
    c = values[2]
    D= values[3]
    H= values[4]

    V = a*(pow(D,b))*pow(H,c)
    return V

def germany_fagus_sylvatica(values):
    a = values[0]
    b = values[1]
    c = values[2]
    D = values[3]
    H = values[4]

    V = a + b*D*pow(H,2)+c*pow(D,3)
    return V

def romania_pinus_sylvestris(values):
    a = values[0]
    b = values[1]
    c = values[2]
    d = values[3]
    e = values[4]
    D = values[5]
    H = values[6]

    V = a * pow(10,( b * math.log(D) + c*(math.log(pow(D,2)) + d*math.log(H) + e * math.log(pow(H,2)))))
    return V

def netherlands_pinus_sylvestris(values):
    a = values[0]
    b = values[1]
    c = values[2]
    D = values[3]
    H = values[4]

    V= pow(D,a) * pow(H,b) * math.exp(c)
    return V

def netherlands_fagus_sylvatica(values):
    a = values[0]
    b = values[1]
    c = values[2]
    D = values[3]
    H = values[4]

    V = pow(D,a) * pow(H,b) * math.exp(c)
    return V
