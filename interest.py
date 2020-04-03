
money = 1000
rate = 0.0075

count = 1


for i in range(1,11):
# while count < 11:

    money= money + ( money*rate)

    print(count,money)

    count += 1