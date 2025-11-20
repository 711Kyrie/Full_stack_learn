# 【一】需求介绍
# 用户可以注册，并将注册信息临时保存起来，登陆时可根据指定用户名或密码进行登陆

# 设定好用户名和密码，用户通过输入指定的用户名和密码进行登陆

# 最大尝试次数：用户最多尝试猜测3次

# 最大尝试次数后：如3次后，问用户是否继续登陆

# 如果回答Y或y，就再给3次机会，提示【还剩最后三次机会】
# 3次都猜错的话登录结束
# 如果回答N或n，登陆结束！
# 如果格式输入错误，提示【输入格式错误，请重新输入：】
# 如果猜对了，登陆结束！

real_username_password = []
login_count = 1
max_count = 3
extra_round_used = False



while True:
    if login_count == 4:
        if not extra_round_used:
            is_agin = input('您已经尝试了三次 是否继续(y/n)>>>:')
            if is_agin.lower() == 'y': 
                print('还剩最后三次机会')
                login_count = 1
                extra_round_used = True
            else:
                print('登录失败')
                break
        else:
            print('登录失败')
            break          
    input_username = input('请输入用户名>>>:')
    input_password = input('请输入密码>>>:')     
    if real_username_password == []:
        real_username_password.append(input_username)
        real_username_password.append(input_password)
        print('注册成功')
        continue
    if input_username == real_username_password[0] and input_password == real_username_password[1]:
        print('登陆成功')
        break
    else:
        login_count += 1
        print(f'用户名或密码错误，还有{max_count + 1 - login_count}次机会')
        