def scorer():
    Cquestion = int (input("On a scale of 1-10, How does the risk affect the confidentiality of the object? > "))
    Iquestion = int (input("On a scale of 1-10, How does the risk affect the integrity of the object? > "))
    Aquestion = int (input("On a scale of 1-10, How does the risk affect the availabilty of the object? > "))
    
    Total = Cquestion + Iquestion + Aquestion
    
    
    print(f"With a total score of {Total}/30,")
    
    if Total <= 10:
        print("This is a mild risk!")
    elif Total <= 20 and Total > 10:
        print("This is a moderate risk!")
    elif Total > 20 and Total <=30:
        print("This is a high level risk!")
        
        
   
    
    
    
reassess = False

while reassess == False:
    scorer()
    restart = input("Would you like to assess another risk?y/n:") 
    if restart == "n":
        reassess = True
        
    