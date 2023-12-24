import sys
import random
n1=1
n2=2
n3=3
n4=4
n5=5
n6=6
n7=7
n8=8
n9=9



player1_symbol = 'x'
player2_symbol = 'o'

continue_game = 'y'
while continue_game == 'y':
    
    print(" ",n1," | ",n2," | ",n3)
    print("-----------------")
    print(" ",n4," | ",n5," | ",n6)
    print("-----------------")
    print(" ",n7," | ",n8," | ",n9)
    
    player_1 = input("Enter your name: ")
    player_2 = input("Enter your name: ")
    

    toss = random.randint(1,2)
   
    if toss == 1:
        value1 = eval(input(player_1 + " Please enter the box number: "))
        if value1 == n1:
            n1 = player1_symbol
            
        elif value1 == n2:
            n2 = player1_symbol
            
        elif value1 == n3:
            n3 = player1_symbol
            
        elif value1 == n4:
            n4 = player1_symbol
            
        elif value1 == n5:
            n5 = player1_symbol
            
        elif value1 == n6:
            n6 = player1_symbol
            
        elif value1 == n7:
            n7 = player1_symbol
            
        elif value1 == n8:
            n8 = player1_symbol
            
        elif value1 == n9:
            n9 == player1_symbol
            
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        value2 = eval(input(player_2 + " Please enter the box number: "))
        if value2 == value1:
            value2 = eval(input("Box occupied, Try another! "))
            if value2 == n1:
                n1 = player2_symbol

            elif value2 == n2:
                n2 = player2_symbol
            
            elif value2 == n3:
                n3 = player2_symbol
            
            elif value2 == n4:
                n4 = player2_symbol

            elif value2 == n5:
                n5 = player2_symbol
            
            elif value2 == n6:
                n6 = player2_symbol
            
            elif value2 == n7:
                n7 = player2_symbol
            
            elif value2 == n8:
                n8 = player2_symbol
            
            else:
                n9 = player2_symbol
        elif value2 == n1:
            n1 = player2_symbol

        elif value2 == n2:
            n2 = player2_symbol
            
        elif value2 == n3:
            n3 = player2_symbol
            
        elif value2 == n4:
            n4 = player2_symbol

        elif value2 == n5:
            n5 = player2_symbol
            
        elif value2 == n6:
            n6 = player2_symbol
            
        elif value2 == n7:
            n7 = player2_symbol
            
        elif value2 == n8:
            n8 = player2_symbol
            
        else:
            n9 = player2_symbol

        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        value3 = eval(input(player_1 + " Please enter the box number: "))

        if value3 == value2 or value3 == value1:
            value3 = eval(input("Box already occupied. Try another: "))
            if value3 == n1:
                n1 = player1_symbol
                
            elif value3 == n2:
                n2 = player1_symbol
                    
            elif value3 == n3:
                n3 = player1_symbol

            elif value3 == n4:
                n4 = player1_symbol
                
            elif value3 == n5:
                n5 = player1_symbol
                
            elif value3 == n6:
                n6 = player1_symbol
                
            elif value3 == n7:
                n7 = player1_symbol
                
            elif value3 == n8:
                n8 = player1_symbol
                
            else:
                n9 = player1_symbol
                
        elif value3 == n1:
            n1 = player1_symbol
                
        elif value3 == n2:
            n2 = player1_symbol
                    
        elif value3 == n3:
            n3 = player1_symbol

        elif value3 == n4:
            n4 = player1_symbol
                
        elif value3 == n5:
            n5 = player1_symbol
                
        elif value3 == n6:
            n6 = player1_symbol
                
        elif value3 == n7:
            n7 = player1_symbol
                
        elif value3 == n8:
            n8 = player1_symbol
                
        else:
            n9 = player1_symbol

                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        value4 = eval(input(player_2 + " Please ente you box: "))
        if value4 == value1 or value4 == value2 or value4 == value3:
            value4 = eval(input("Box is already occupied, please select an empty box ! "))
            if value4 == n1:
                n1 = player2_symbol

            elif value4 == n2:
                n2 = player2_symbol
            
            elif value4 == n3:
                n3 = player2_symbol
            
            elif value4 == n4:
                n4 = player2_symbol
            
            elif value4 == n5:
                n5 = player2_symbol
            
            elif value4 == n6:
                n6 = player2_symbol
            
            elif value4 == n7:
                n7 = player2_symbol
            
            elif value4 == n8:
                n8 = player2_symbol
            
            else:
                n9 = player2_symbol

        elif value4 == n1:
            n1 = player2_symbol

        elif value4 == n2:
            n2 = player2_symbol
            
        elif value4 == n3:
            n3 = player2_symbol
            
        elif value4 == n4:
            n4 = player2_symbol
            
        elif value4 == n5:
            n5 = player2_symbol
            
        elif value4 == n6:
            n6 = player2_symbol
            
        elif value4 == n7:
            n7 = player2_symbol
            
        elif value4 == n8:
            n8 = player2_symbol
            
        else:
            n9 = player2_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)


        value5 = eval(input(player_1 + " Please enter your box number: "))

        if value5 == value1 or value5 == value2 or value5 == value3 or value5 == value4:
            value5 = eval(input("Box is already occupied, please select an empty box "))
            if value5 == n1:
                n1 = player1_symbol
                
            elif value5 == n2:
                n2 = player1_symbol
                    
            elif value5 == n3:
                n3 = player1_symbol

            elif value5 == n4:
                n4 = player1_symbol
                
            elif value5 == n5:
                n5 = player1_symbol
                
            elif value5 == n6:
                n6 = player1_symbol
                
            elif value5 == n7:
                n7 = player1_symbol
                
            elif value5 == n8:
                n8 = player1_symbol
                
            else:
                n9 = player1_symbol


        elif value5 == n1:
            n1 = player1_symbol

        elif value5 == n2:
            n2 = player1_symbol
                    
        elif value5 == n3:
            n3 = player1_symbol

        elif value5 == n4:
            n4 = player1_symbol
                
        elif value5 == n5:
            n5 = player1_symbol
                
        elif value5 == n6:
            n6 = player1_symbol
                
        elif value5 == n7:
            n7 = player1_symbol
                
        elif value5 == n8:
            n8 = player1_symbol
                
        else:
            n9 = player1_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins!")
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")

        value6 = eval(input(player_2 + " Please enter your box number: "))
        if value6 == value1 or value6 == value2 or value6 == value3 or value6 == value4 or value6 == value4:
            value6 = eval(input("Box is already occupied, please select an empty box ! "))
            if value == n1:
                n1 = player2_symbol

            elif value6 == n2:
                n2 = player2_symbol
            
            elif value6 == n3:
                n3 = player2_symbol
            
            elif value6 == n4:
                n4 = player2_symbol
            
            elif value6 == n5:
                n5 = player2_symbol
            
            elif value6 == n6:
                n6 = player2_symbol
            
            elif value6 == n7:
                n7 = player2_symbol
            
            elif value6 == n8:
                n8 = player2_symbol
            
            else:
                n9 = player2_symbol

        elif value6== n1:
            n1 = player2_symbol

        elif value6 == n2:
                n2 = player2_symbol
            
        elif value6 == n3:
            n3 = player2_symbol
            
        elif value6 == n4:
            n4 = player2_symbol
            
        elif value6 == n5:
            n5 = player2_symbol
            
        elif value6 == n6:
            n6 = player2_symbol
            
        elif value6 == n7:
            n7 = player2_symbol
            
        elif value6 == n8:
            n8 = player2_symbol
            
        else:
            n9 = player2_symbol        
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins")
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")
            

        value7 = eval(input(player_1 + " Please enter your box number: "))

        if value7 == value1 or value7 == value2 or value7 == value3 or value7 == value4 or value7 == value5 or value7 == value6:
            value7 = eval(input("Box is already occupied, please select an empty box "))
            if value7 == n1:
                n1 = player1_symbol
                
            elif value7 == n2:
                n2 = player1_symbol
                    
            elif value7 == n3:
                n3 = player1_symbol

            elif value7 == n4:
                n4 = player1_symbol
                
            elif value7 == n5:
                n5 = player1_symbol
                
            elif value7 == n6:
                n6 = player1_symbol
                
            elif value7 == n7:
                n7 = player1_symbol
                
            elif value7 == n8:
                n8 = player1_symbol
                
            else:
                n9 = player1_symbol

        elif value7 == n1:
            n1 = player1_symbol
                
        elif value7 == n2:
            n2 = player1_symbol
                    
        elif value7 == n3:
            n3 = player1_symbol

        elif value7 == n4:
            n4 = player1_symbol
            
        elif value7 == n5:
            n5 = player1_symbol
                
        elif value7 == n6:
            n6 = player1_symbol
                
        elif value7 == n7:
            n7 = player1_symbol
                
        elif value7 == n8:
            n8 = player1_symbol
                
        else:
            n9 = player1_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins")
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")

        value8 = eval(input(player_2 + " Please enter your box number: "))

        if value8 == value1 or value8 == value2 or value8 == value3 or value8 == value4 or value8 == value5 or value8 == value6 or value8 == value7:
            value8 = eval(input("Box is already occupied, please select an empty box "))
            if value8 == n1:
                n1 = player2_symbol
                
            elif value8 == n2:
                n2 = player2_symbol
                    
            elif value8 == n3:
                n3 = player2_symbol

            elif value8 == n4:
                n4 = player2_symbol
                
            elif value8 == n5:
                n5 = player2_symbol
                
            elif value8 == n6:
                n6 = player2_symbol
                
            elif value8 == n7:
                n7 = player2_symbol
                
            elif value8 == n8:
                n8 = player2_symbol
                
            else:
                n9 = player2_symbol

        elif value8 == n1:
            n1 = player2_symbol
                
        elif value8 == n2:
            n2 = player2_symbol
                    
        elif value8 == n3:
            n3 = player2_symbol
            
        elif value8 == n4:
            n4 = player2_symbol
            
        elif value8 == n5:
            n5 = player2_symbol
                
        elif value8 == n6:
            n6 = player2_symbol
                
        elif value8 == n7:
            n7 = player2_symbol
                
        elif value8 == n8:
            n8 = player2_symbol
                
        else:
            n9 = player2_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins")
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")


        value9 = eval(input(player_2 + " Please enter your box number: "))

        if value9 == value1 or value9 == value2 or value9 == value3 or value9 == value4 or value9 == value5 or value9 == value6 or value9 == value7:
            value9 = eval(input("Box is already occupied, please select an empty box "))
            if value9 == n1:
                n1 = player1_symbol
                
            elif value9 == n2:
                n2 = player1_symbol
                    
            elif value9 == n3:
                n3 = player1_symbol

            elif value9 == n4:
                n4 = player1_symbol
                
            elif value9 == n5:
                n5 = player1_symbol
                
            elif value9 == n6:
                n6 = player1_symbol
                
            elif value9 == n7:
                n7 = player1_symbol
                
            elif value9 == n8:
                n8 = player1_symbol
                
            else:
                n9 = player1_symbol

        elif value9 == n1:
            n1 = player1_symbol
                
        elif value9 == n2:
            n2 = player1_symbol
                    
        elif value9 == n3:
            n3 = player1_symbol

        elif value9 == n4:
            n4 = player1_symbol
            
        elif value9 == n5:
            n5 = player1_symbol
                
        elif value9 == n6:
            n6 = player1_symbol
                
        elif value9 == n7:
            n7 = player1_symbol
                
        elif value9 == n8:
            n8 = player1_symbol
                
        elif value9 == n9:
            n9 = player1_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins")
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")
        
        else:
            
            print("Game draw!")
            break

    
    else:
        value1 = eval(input(player_2 + " Please enter the box number: "))
        if value1 == n1:
            n1 = player1_symbol
            
        elif value1 == n2:
            n2 = player1_symbol
            
        elif value1 == n3:
            n3 = player1_symbol
            
        elif value1 == n4:
            n4 = player1_symbol
            
        elif value1 == n5:
            n5 = player1_symbol
            
        elif value1 == n6:
            n6 = player1_symbol
            
        elif value1 == n7:
            n7 = player1_symbol
            
        elif value1 == n8:
            n8 = player1_symbol
            
        elif value1 == n9:
            n9 == player1_symbol
            
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        value2 = eval(input(player_1 + " Please enter the box number: "))
        if value2 == value1:
            value2 = eval(input("Box occupied, Try another! "))
            if value2 == n1:
                n1 = player2_symbol

            elif value2 == n2:
                n2 = player2_symbol
            
            elif value2 == n3:
                n3 = player2_symbol
            
            elif value2 == n4:
                n4 = player2_symbol

            elif value2 == n5:
                n5 = player2_symbol
            
            elif value2 == n6:
                n6 = player2_symbol
            
            elif value2 == n7:
                n7 = player2_symbol
            
            elif value2 == n8:
                n8 = player2_symbol
            
            else:
                n9 = player2_symbol
        elif value2 == n1:
            n1 = player2_symbol

        elif value2 == n2:
            n2 = player2_symbol
            
        elif value2 == n3:
            n3 = player2_symbol
            
        elif value2 == n4:
            n4 = player2_symbol

        elif value2 == n5:
            n5 = player2_symbol
            
        elif value2 == n6:
            n6 = player2_symbol
            
        elif value2 == n7:
            n7 = player2_symbol
            
        elif value2 == n8:
            n8 = player2_symbol
            
        else:
            n9 = player2_symbol

        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        value3 = eval(input(player_2 + " Please enter the box number: "))

        if value3 == value2 or value3 == value1:
            value3 = eval(input("Box already occupied. Try another: "))
            if value3 == n1:
                n1 = player1_symbol
                
            elif value3 == n2:
                n2 = player1_symbol
                    
            elif value3 == n3:
                n3 = player1_symbol

            elif value3 == n4:
                n4 = player1_symbol
                
            elif value3 == n5:
                n5 = player1_symbol
                
            elif value3 == n6:
                n6 = player1_symbol
                
            elif value3 == n7:
                n7 = player1_symbol
                
            elif value3 == n8:
                n8 = player1_symbol
                
            else:
                n9 = player1_symbol
                
        elif value3 == n1:
            n1 = player1_symbol
                
        elif value3 == n2:
            n2 = player1_symbol
                    
        elif value3 == n3:
            n3 = player1_symbol

        elif value3 == n4:
            n4 = player1_symbol
                
        elif value3 == n5:
            n5 = player1_symbol
                
        elif value3 == n6:
            n6 = player1_symbol
                
        elif value3 == n7:
            n7 = player1_symbol
                
        elif value3 == n8:
            n8 = player1_symbol
                
        else:
            n9 = player1_symbol

                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        value4 = eval(input(player_1 + " Please ente you box: "))
        if value4 == value1 or value4 == value2 or value4 == value3:
            value4 = eval(input("Box is already occupied, please select an empty box ! "))
            if value4 == n1:
                n1 = player2_symbol

            elif value4 == n2:
                n2 = player2_symbol
            
            elif value4 == n3:
                n3 = player2_symbol
            
            elif value4 == n4:
                n4 = player2_symbol
            
            elif value4 == n5:
                n5 = player2_symbol
            
            elif value4 == n6:
                n6 = player2_symbol
            
            elif value4 == n7:
                n7 = player2_symbol
            
            elif value4 == n8:
                n8 = player2_symbol
            
            else:
                n9 = player2_symbol

        elif value4 == n1:
            n1 = player2_symbol

        elif value4 == n2:
            n2 = player2_symbol
            
        elif value4 == n3:
            n3 = player2_symbol
            
        elif value4 == n4:
            n4 = player2_symbol
            
        elif value4 == n5:
            n5 = player2_symbol
            
        elif value4 == n6:
            n6 = player2_symbol
            
        elif value4 == n7:
            n7 = player2_symbol
            
        elif value4 == n8:
            n8 = player2_symbol
            
        else:
            n9 = player2_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)


        value5 = eval(input(player_2 + " Please enter your box number: "))

        if value5 == value1 or value5 == value2 or value5 == value3 or value5 == value4:
            value5 = eval(input("Box is already occupied, please select an empty box "))
            if value5 == n1:
                n1 = player1_symbol
                
            elif value5 == n2:
                n2 = player1_symbol
                    
            elif value5 == n3:
                n3 = player1_symbol

            elif value5 == n4:
                n4 = player1_symbol
                
            elif value5 == n5:
                n5 = player1_symbol
                
            elif value5 == n6:
                n6 = player1_symbol
                
            elif value5 == n7:
                n7 = player1_symbol
                
            elif value5 == n8:
                n8 = player1_symbol
                
            else:
                n9 = player1_symbol


        elif value5 == n1:
            n1 = player1_symbol

        elif value5 == n2:
            n2 = player1_symbol
                    
        elif value5 == n3:
            n3 = player1_symbol

        elif value5 == n4:
            n4 = player1_symbol
                
        elif value5 == n5:
            n5 = player1_symbol
                
        elif value5 == n6:
            n6 = player1_symbol
                
        elif value5 == n7:
            n7 = player1_symbol
                
        elif value5 == n8:
            n8 = player1_symbol
                
        else:
            n9 = player1_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins!")
            
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")
            

        value6 = eval(input(player_1 + " Please enter your box number: "))
        if value6 == value1 or value6 == value2 or value6 == value3 or value6 == value4 or value6 == value4:
            value6 = eval(input("Box is already occupied, please select an empty box ! "))
            if value == n1:
                n1 = player2_symbol

            elif value6 == n2:
                n2 = player2_symbol
            
            elif value6 == n3:
                n3 = player2_symbol
            
            elif value6 == n4:
                n4 = player2_symbol
            
            elif value6 == n5:
                n5 = player2_symbol
            
            elif value6 == n6:
                n6 = player2_symbol
            
            elif value6 == n7:
                n7 = player2_symbol
            
            elif value6 == n8:
                n8 = player2_symbol
            
            else:
                n9 = player2_symbol

        elif value6== n1:
            n1 = player2_symbol

        elif value6 == n2:
                n2 = player2_symbol
            
        elif value6 == n3:
            n3 = player2_symbol
            
        elif value6 == n4:
            n4 = player2_symbol
            
        elif value6 == n5:
            n5 = player2_symbol
            
        elif value6 == n6:
            n6 = player2_symbol
            
        elif value6 == n7:
            n7 = player2_symbol
            
        elif value6 == n8:
            n8 = player2_symbol
            
        else:
            n9 = player2_symbol        
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins")
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")
            
            

        value7 = eval(input(player_2 + " Please enter your box number: "))

        if value7 == value1 or value7 == value2 or value7 == value3 or value7 == value4 or value7 == value5 or value7 == value6:
            value7 = eval(input("Box is already occupied, please select an empty box "))
            if value7 == n1:
                n1 = player1_symbol
                
            elif value7 == n2:
                n2 = player1_symbol
                    
            elif value7 == n3:
                n3 = player1_symbol

            elif value7 == n4:
                n4 = player1_symbol
                
            elif value7 == n5:
                n5 = player1_symbol
                
            elif value7 == n6:
                n6 = player1_symbol
                
            elif value7 == n7:
                n7 = player1_symbol
                
            elif value7 == n8:
                n8 = player1_symbol
                
            else:
                n9 = player1_symbol

        elif value7 == n1:
            n1 = player1_symbol
                
        elif value7 == n2:
            n2 = player1_symbol
                    
        elif value7 == n3:
            n3 = player1_symbol

        elif value7 == n4:
            n4 = player1_symbol
            
        elif value7 == n5:
            n5 = player1_symbol
                
        elif value7 == n6:
            n6 = player1_symbol
                
        elif value7 == n7:
            n7 = player1_symbol
                
        elif value7 == n8:
            n8 = player1_symbol
                
        else:
            n9 = player1_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins")
            break
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")
            break

        value8 = eval(input(player_1 + " Please enter your box number: "))

        if value8 == value1 or value8 == value2 or value8 == value3 or value8 == value4 or value8 == value5 or value8 == value6 or value8 == value7:
            value8 = eval(input("Box is already occupied, please select an empty box "))
            if value8 == n1:
                n1 = player2_symbol
                
            elif value8 == n2:
                n2 = player2_symbol
                    
            elif value8 == n3:
                n3 = player2_symbol

            elif value8 == n4:
                n4 = player2_symbol
                
            elif value8 == n5:
                n5 = player2_symbol
                
            elif value8 == n6:
                n6 = player2_symbol
                
            elif value8 == n7:
                n7 = player2_symbol
                
            elif value8 == n8:
                n8 = player2_symbol
                
            else:
                n9 = player2_symbol

        elif value8 == n1:
            n1 = player2_symbol
                
        elif value8 == n2:
            n2 = player2_symbol
                    
        elif value8 == n3:
            n3 = player2_symbol

        elif value8 == n4:
            n4 = player2_symbol
            
        elif value8 == n5:
            n5 = player2_symbol
                
        elif value8 == n6:
            n6 = player2_symbol
                
        elif value8 == n7:
            n7 = player2_symbol
                
        elif value8 == n8:
            n8 = player2_symbol
                
        else:
            n9 = player2_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins")
        
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")
            
        
        value9 = eval(input(player_1 + " Please enter your box number: "))

        if value9 == value1 or value9 == value2 or value9 == value3 or value9 == value4 or value9 == value5 or value9 == value6 or value9 == value7:
            value9 = eval(input("Box is already occupied, please select an empty box "))
            if value9 == n1:
                n1 = player1_symbol
                
            elif value9 == n2:
                n2 = player1_symbol
                    
            elif value9 == n3:
                n3 = player1_symbol

            elif value9 == n4:
                n4 = player1_symbol
                
            elif value9 == n5:
                n5 = player1_symbol
                
            elif value9 == n6:
                n6 = player1_symbol
                
            elif value9 == n7:
                n7 = player1_symbol
                
            elif value9 == n8:
                n8 = player1_symbol
                
            else:
                n9 = player1_symbol

        elif value9 == n1:
            n1 = player1_symbol
                
        elif value9 == n2:
            n2 = player1_symbol
                    
        elif value9 == n3:
            n3 = player1_symbol

        elif value9 == n4:
            n4 = player1_symbol
            
        elif value9 == n5:
            n5 = player1_symbol
                
        elif value9 == n6:
            n6 = player1_symbol
                
        elif value9 == n7:
            n7 = player1_symbol
                
        elif value9 == n8:
            n8 = player1_symbol
                
        elif value9 == n9:
            n9 = player1_symbol
                
        print(" ",n1," | ",n2," | ",n3)
        print("-----------------")
        print(" ",n4," | ",n5," | ",n6)
        print("-----------------")
        print(" ",n7," | ",n8," | ",n9)

        if (n1==player1_symbol and n2==player1_symbol and n3==player1_symbol)or(n1==player1_symbol and n4==player1_symbol and n7==player1_symbol)or(n1==player1_symbol and n5==player1_symbol and n9==player1_symbol)or(n2==player1_symbol and n5==player1_symbol and n8==player1_symbol)or(n3==player1_symbol and n6==player1_symbol and n9==player1_symbol)or(n4==player1_symbol and n5==player1_symbol and n6==player1_symbol)or(n7==player1_symbol and n8==player1_symbol and n9==player1_symbol)or(n3==player1_symbol and n5==player1_symbol and n7==player1_symbol):
            print(player1_symbol," wins")
            
        elif (n1==player2_symbol and n2==player2_symbol and n3==player2_symbol)or(n1==player2_symbol and n4==player2_symbol and n7==player2_symbol)or(n1==player2_symbol and n5==player2_symbol and n9==player2_symbol)or(n2==player2_symbol and n5==player2_symbol and n8==player2_symbol)or(n3==player2_symbol and n6==player2_symbol and n9==player2_symbol)or(n4==player2_symbol and n5==player2_symbol and n6==player2_symbol)or(n7==player2_symbol and n8==player2_symbol and n9==player2_symbol)or(n3==player2_symbol and n5==player2_symbol and n7==player2_symbol):
            print(player2_symbol," wins")
            
        else:
            print("Game draw!")
            

    continue_game = input("Do you want to play another game?(y/n): ")
    

