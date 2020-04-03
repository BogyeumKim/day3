from random import randrange

result=[]

def game():


        user_num = int(input('가위0 바위1 보2'))

        com=randrange(0,3)

        if com<user_num:
            com = com+3

            win=''

        if com-user_num==2:
            win='User'
        elif com-user_num==1:
            win='Com'
        else:
            win='Draw'

        return result.append(win)

for x in range(10):
    game()


print(result)