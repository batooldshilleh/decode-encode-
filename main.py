alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def case (plan_text,shift_num,direc):
    new_text = " "
    for char_1 in plan_text:
        if char_1 in alphabet:
            posetion = alphabet.index(char_1)
            if direc == "e":
                new_posetion = shift_num + posetion
            elif direc == "d":
                new_posetion = shift_num - posetion
            new_char = alphabet[new_posetion]
            new_text += new_char
        else :
            new_text += char_1
    print(new_text)
flag = True
while flag:
        direction = input( "Hi user if you wont to decode the world rite 'd', if you wont to encode the world rite 'e' ^_^ \n")
        text = input("Hi  enter your text  ^_^ \n ").lower()
        shift = int(input("Hi  enter the number of shift <3 \n "))
        shift = shift % 25
        case(plan_text=text, shift_num=shift, direc=direction)
        retray = input("Hi taype 'yes' to contenyo or taype 'no' to stope ")
        if retray == "no":
            flag = False
            print("Good bay 🥺")





