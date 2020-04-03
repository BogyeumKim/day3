import random

nums=[]

def check(num_list, target):

    result = False

    for x in num_list: ## x= nums
        if x == target:  ## num == 1~45의 랜덤숫자인데 x ==num
            result = True
            break

    return result

#루프를 nums가 6번 나오게 돌림
while len(nums)<6:
    # 1~45까지 숫자를 뽑는다
    num=random.randrange(1,46)

    abc=num

    nums.append(abc)
    # 중복된숫자가있으면 다시 뽑는다

    print(nums)