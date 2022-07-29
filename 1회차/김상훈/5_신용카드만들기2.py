import sys

sys.stdin = open("_신용카드만들기2.txt")


T = int(input())
for _ in range(1,T+1):

    card_numbers = input()
    list_card =[]
    for i in card_numbers:
        list_card.append(i)
        
        if card_numbers[0] == '3' or card_numbers[0] == '4' or card_numbers[0] == '5' or card_numbers[0] == '6' or card_numbers[0] == '9' and list_card =='-':
            m = 1
        else :
            m = 0
    
    print(f'#{_} {m}')    

