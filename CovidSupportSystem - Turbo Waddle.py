from ast import Global 

Stats = 1
Prevent = 2
Symptoms = 3
Treatment = 4
Reportcase = 5
Exit = 6

global SA, USA, China
SA = 1868 
USA = 39730
China = 790

def repeat():
    Main = input("Would you like to return to the main menu? y/n")
    if Main == 'n':
        print("Thank you for using our COVID Support System")
    elif Main == 'y':
        Choice()


def Options():
    print("Welcom to the Covid 19 support service.Please select an option below:")
    print("1.Statistics")
    print("2.Preventation")
    print("3.Symptoms")
    print("4.Treatment")
    print("5.Report case")
    print("6.Exit")

    
 
 
def Choice():
    Options()
    Enter = int(input("Enter choice(1/2/3/4/5/6):"))

    if Enter == 1:
         Stat()
    elif Enter == 2:
        Preventations()
    elif Enter == 3:
        Symp()
    elif Enter == 4:
       Treat()
    elif Enter == 5:
       Report()
    elif Enter == 6:
       print("Thank you for using our COVID-19 Support System")
       Exit()
    
      


def Stat():
    print("Cuurently in SA there are 1 868 Confirmed cases")
    print("Currently in USA there are 39 730 Confirmed casses")
    print("Currently in China there are 790 Confirmed casses")
    
    print(" ")
    Country = input("Would you like to see the Confirmed casses for a random country? y/n:")
    if Country == 'y':
            Type = int(input("To select a random country, type a number from 0 to 9:"))
            if Type == 0: 
                        print("South Korea has 282 976 confirmed casses")
            elif Type == 1: 
                        print("France has 69 046 confirmed casses") 
            elif Type == 2: 
                        print("Australia has 31 689 confirmed casses")
            elif Type == 3: 
                        print("Germany has 225 557 confrimed casses")            
            elif Type == 4: 
                        print("Japan has 61 063 confirmed casses")   
            elif Type == 5: 
                        print("United Kingdom has 84 401 confirmed casses")
            elif Type == 6:
                        print("India has 4 194 confirmed casses")
            elif Type == 7:
                        print("Greece has 21 863 confirmed casses")
            elif Type == 8:
                        print("Ukraine has 0 confirmed casses")
            elif Type == 9: 
                        print("Turkey has 29 492 confirmed casses")  
            repeat()

def Preventations():
    print("To prevent the spread of Covid-19:")
    print("Clean your hands often. Use soap and water, or an alcohol-based hand rub")
    print("Maintain a safe distance from anyone who is coughing or sneezing.")
    print("Don't touch your eyes, nose or mouth.")
    print("Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze")
    print("Stay home if you feel unwell.")
    print("If you have a fever, cough and difficulity breathing, seek medical attention. Call in advance.")
    print("Follw the directions of your local health authority.")
    repeat()

def Symp():
    print(" ")
    print("Most common symtoms:")
    print("Fever")
    print("dry cough")
    print("tiredness")
    print(" ")
    print("Less common symptoms:")
    print("aches and pains")
    print("sore throat")
    print("diarrhoea")
    print("conjunctivitis")
    print("headache")
    print("loss of taste or smell")
    print("a rash on skin, or discolouration of fingers or toes")
    print(" ")
    print("Serious Symptoms:")
    print("difficulity breathing or shortness of breath")
    print("chest pain or pressure")
    print("loss of speech or movement")
    repeat()

def Treat():
     print("If you feel sick you should rest, drink plenty of fluid, and eat nutritious food. Stay in a seperate room from other family members, and use a dedicated bathroom if possible. Clean and disinfect frequently touched surfaces.")
     repeat()

def Report():
    global SA, USA, China
    Covid = input("Do you have any of the symptoms? y/n:")
    if Covid == 'n':
                print("You do not have COVID 19")
                repeat()
    elif Covid == 'y':
                Temp = input("Is your temperature above 38.5 C? y/n:")
                if Temp == 'n':
                    print("You do not have COVID 19")
                    repeat()
                elif Temp == 'y':
                    print("In which country are you select an option below") 
                    print("1.SA")
                    print("2.USA")
                    print("3.China")
                    State = int(input("Enter option(1/2/3):"))
                    if State == 1:
                        SA = SA + 1
                        print("There are currently" + " " + str(SA) + " " + "casses in South Africa")
                    elif State == 2:
                        USA = USA + 1
                        print("There are currently" + " " + str(USA) + " " + "casses in USA")
                    elif State == 3:
                        China = China + 1
                        print("There are currently" + " " + str(China) + " " + "casses in China")

                print("You have COVID 19 please see Treatment") 
                repeat()

def Exit():
    Exit

Choice()