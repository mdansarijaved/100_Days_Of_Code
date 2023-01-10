import random 

card_holders = input("Enter the card holders name: ")

card_holders = card_holders.split(", ")

x = int(len(card_holders))


ran_num = random.randint(0,x)

print(f"Today's lucky winner is {card_holders[ran_num-1]}")