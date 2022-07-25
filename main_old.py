from svlib import EstimateVolume


print("\nWelcome to Tree Stem Volume Estimator")

countries = {
    "1" : {
        "Name" : "Germany",
        "Specieses" :{
            "1" : "Pinus sylvestris",   #V = a.D^b 〖.H〗^c                 a,b,c,D,H
            "2" : "Fagus sylvatica"     #V = a + b.D.H^2 + c.D^3           a,b,c,D,H
        }
    },
    "2" : {
        "Name" : "Romania",
        "Specieses" :{
            "1" : "Pinus sylvestris"    # V = a. 10^( b.log(D) + c.(logD^2) + d.log(H) + e. log(H^2) )         #a,b,c,d,e,D,H
        }
    },
     "3" : {
        "Name" : "Netherlands",
        "Specieses" :{
            "1" : "Pinus sylvestris",   # V= D^a H^b 〖exp〗^c                                  a,b,c,D,H
            "2" : "Fagus Sylvatica"     # V = D^a . H^b . exp(c),   # V= a.D^b.H^c       a,b,c,D,H
        }
    },
}

print("\nSelect Your Country From The List")
for country in countries:
    print(country, ":", countries[country]["Name"])
choiceCountry = input("Press the country code and press enter: ")

if choiceCountry in countries.keys():
    choice = input("Do you want to start volume calculation? \nPress y for Yes and n for No:")

    while choice.upper() == 'Y':
        print("\nSelect Tree Species From The List")
        for species in countries[choiceCountry]["Specieses"]:
            print(species, ":", countries[choiceCountry]["Specieses"][species])
        choiceSpecies = input("Press the species code and press enter: ")

        if choiceSpecies in countries[choiceCountry]["Specieses"].keys():
            print("\nYou have chosen", countries[choiceCountry]["Specieses"][choiceSpecies])
                # "\nPlease provide the following parameters:\n")

            # if countries[choiceCountry]["Name"] == "Germany":
            #     a = input("Value of 'a': ")
            #     b = input("Value of 'b': ")
            #     c = input("Value of 'c': ")
            #     D = input("Value of 'D': ")
            #     H = input("Value of 'H': ")

            estimatedVolume = EstimateVolume(countries[choiceCountry]["Name"],
                                             countries[choiceCountry]["Specieses"][choiceSpecies])

            # elif countries[choiceCountry]["Name"] == "Netherlands":
            #     print("Netherlands")
            # elif countries[choiceCountry]["Name"] == "Romania":1
            #     print("Romania")
            # else:
            #     print("Sorry, the volume estimation service for the country you selected is not avaailable now\n")

        else:
            print("Die")
            #choice = input("Do you want to start volume calculation? Press y for Yes and n for No:")

        choice = input("Do you want to calculate again?")           #Whie controller
else:
    print("Sorry, the  country code",choiceCountry,"is invalid.")


print("Thank You for using our application")