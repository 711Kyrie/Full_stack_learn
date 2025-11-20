# 【一】需求介绍
# 设定好用户年龄，用户通过输入猜测的年龄进行匹配
# 最大尝试次数：用户最多尝试猜测3次
# 最大尝试次数后：如3次后，问用户是否还想继续玩
# 如果回答Y或y，就再给3次机会，提示【还剩最后三次机会】
# 3次都猜错的话游戏结束
# 如果回答N或n，游戏结束！
# 如果格式输入错误，提示【输入格式错误，请重新输入：】
# 如果猜对了，游戏结束！
real_age = 18
guess_count = 1
extra_round_used = False

while True:
    if guess_count == 4:
        if not extra_round_used:
            is_again = input('您已经尝试了三次 是否继续(y/n)>>>:')
            if is_again.lower() == 'y':
                print('还剩最后三次机会')
                guess_count = 1
                extra_round_used = True
            else:
                print('下次记得来玩哟!!!')
                break
        else:
            print('游戏结束')
            break

    guess_age = input('请输入猜测的年龄>>>:')
    try:
        guess_age = int(guess_age)
    except ValueError:
        print('输入格式错误，请重新输入：')
        continue

    if guess_age > real_age:
        print('哎呀 讨厌 猜大了')
        guess_count += 1
    elif guess_age < real_age:
        print('不好意思 没那么小')
        guess_count += 1
    else:
        print('哈哈哈 你真棒!!!')
        break
