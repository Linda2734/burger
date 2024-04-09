print("Hello. Welcome to Codetown Burger Co")
burger_num = int(input("How many burgers would you like?"))
burger_num = int(str(burger_num).replace(" ", ""))

cost = 5.0 * burger_num



for i in range(burger_num):
    print(f"order for burger for burger {i+1}")    
    bun_type = int(input(f"Would you like burger {i+1} to have milk burger bun[0], or gluten free bun[1] "))
    bun_type = int(str(bun_type).replace(" ", ""))
    while bun_type not in [0, 1]:
        bun_type = int(input("Please enter a valid choice, milk burger bun[0], or gluten free bun[1] "))

    if bun_type == 0:
        print(f"Ok, milk burger bun for burger {i+1} ")
    else:
        print(f"Ok, gluten free burger bun for burger {i+1} ")
        cost+=1
            
    
    sauce = int(input(f"Would you like, tomato sauce[0], barbeque sauce[1], or no sauce[2] for burger {i+1} "))
    sauce = int(str(sauce).replace(" ", ""))

    while sauce not in [0,1,2]:
        sauce = int(input("Please enter a valid choice, tomato sauce[0], barbeque sauce[1], or no sauce[2] "))

    if sauce == 0:
        print(f"Ok, tomato sauce for burger {i+1} ")

    elif sauce == 1:
        print(f"Ok, barbeque sauce for burger {i+1} ")

    else:
        print(f"Ok, no sauce for burger {i+1} ")

    
    patty_num = int(input(f"Would you like, 0, 1, 2, or 3 patties for burger {i+1} "))
    patty_num = int(str(patty_num).replace(" ", ""))

    while patty_num not in [0,1,2,3]:
        patty_num = int(input("Please enter a valid choice, 0, 1, 2, or 3 patties "))

    if patty_num == 0:
        print(f"Ok, no patties for burger {i+1} ")

    elif patty_num == 1:
        print(f"Ok, 1 patty for burger {i+1} ")

    elif patty_num == 2:
        print(f"Ok, 2 patties for burger {i+1} ")
        cost+=3

    else:
        print(f"Ok, 3 patties for burger {i+1} ")
        cost+=6

    


    cheese_num = int(input(f"Would you like, 0, 1, 2, or 3 slices of cheese for burger {i+1} "))
    cheese_num = int(str(cheese_num).replace(" ", ""))

    while cheese_num not in [0,1,2,3]:
        cheese_num = int(input("Please enter a valid choice, 0, 1, 2, or 3 slices of cheese "))

    if cheese_num == 0:
        print(f"Ok, no slices for burger {i+1} ")

    elif cheese_num == 1:
        print(f"Ok, 1 slice for burger {i+1} ")

    elif cheese_num == 2:
        print(f"Ok, 2 slices for burger {i+1} ")
        cost+=1

    else:
        print(f"Ok, 3 slices for burger {i+1} ")
        cost+=2

    
    salad_counter = 0

    tomato = int(input(f"Would you like no tomato[0], or tomato[1] for burger {i+1} "))
    tomato = int(str(tomato).replace(" ", ""))

    while tomato not in [0,1]:
        tomato = int(input("Please enter a valid choice tomato[0], or no tomato[1] "))

    if tomato == 0:
        print(f"Ok, no tomato it is for burger {i+1} ")
        salad_counter+=1

    else:
        print(f"Ok, tomato it is for burger {i+1} ") 

    

    
    lettuce = int(input(f"Would you like no lettuce[0], or lettuce[1] for burger {i+1} "))
    lettuce = int(str(lettuce).replace(" ", ""))

    while lettuce not in [0,1]:
        lettuce = int(input("Please enter a valid choice lettuce[0], or no lettuce[1] "))
  

    if lettuce == 0:
        print(f"Ok, no lettuce it is for burger {i+1} ")
        salad_counter+=1

    else:
        print(f"Ok, lettuce it is for burger {i+1} ") 

    


    onion = int(input(f"Would you like no onion[0], or onion[1] for burger {i+1} "))
    onion = int(str(onion).replace(" ", ""))

    while onion not in [0,1]:
        onion = int(input("Please enter a valid choice onion[0], or no onion[1] "))

    if onion == 0:
        print(f"Ok, no onion it is for burger {i+1} ")
        salad_counter+=1

    else:
        print(f"Ok, onion it is for burger {i+1} ") 

    if salad_counter == 2:
        cost+=1

    elif salad_counter == 3:
        cost+=2

    if burger_num > 1:
        print(f"your current base cost for {burger_num} burgers  $", cost)
    elif burger_num == 1:
        print(f"your current base cost for {burger_num} burger  $", cost)
    

print("Your total cost is $",cost)
tip = input("Would you like to add a tip, [y], or [n]")
tip = tip.lower()

while tip not in ["y", "n"]:
    tip = input("Please select from the given options, [y], or [n]")

if tip == "y":
    tip = int(input("5%(select[0]), 10%(select[1]), or 20%(select[2])"))

    while tip not in [0, 1, 1]:
        tip = int(input("Please select from the given options, 5%(select[0]), 10%(select[1]), or 20%(select[2])"))
    
    if tip == 0:
        tip = cost*0.05
        print(f"Thank you for tipping ${tip}")
    elif tip == 1:
        tip = cost*0.1
        print(f"Thank you for tipping ${tip}")

    elif tip == 2:
        tip = cost*0.2
        print(f"Thank you for tipping ${tip}")


elif tip == "n":
    print("Ok, have a nice day")
    


    