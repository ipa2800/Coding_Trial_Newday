#this is my first python program
#from 2017-06-25
#keep 100 days plan
#
# a = 5
# print(a)
#
# my_name = 'chenganggang '
# my_add = 'SMTH '
# my_room ='8F602 '
# profile = my_name + my_add + my_room
# print(profile)
#
# print(type(a))
# b = str(a)
# print(type(b))
#
# word = 'friends'
# find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
# print(find_the_evil_in_your_friends)
# print(word[-2:-1])
#
# phone_number='13906916781'
# hiding_number=phone_number.replace(phone_number[:6],'*'*6).replace(phone_number[-3:],'*'*3)
# print(hiding_number)
#
# search= '168'
# number_a= '6516829'
# number_b= '6521689'
# print(search)
# print(search + ' is at ' + str(number_a.find(search)) + ' of ' + number_a)
# print(search + ' is at ' + str(number_b.find(search)) + ' of ' + number_b)
# print(type(number_a.find(search)))
# print(len(search))
#
# print('{} a word she can get what she {} for'.format('hello','test'))
#
#
# # city = input('pls input your city name:')
# # url = 'your city is in {} of china'
# # print (url.format(city))
#
# # def sheshidu_conver(C):
# #     sheshidu = C* 9/5+32
# #     return str(sheshidu)+'F'
# #
# # C2F = sheshidu_conver(35)
# # print(C2F)
# #
# # def g2kg_conver(A):
# #     g2kg = A / 1000
# #     return str(g2kg)
# #
# # KG = g2kg_conver(int(input('please input kilo:')))
# # print(KG)
#
# def triangle_calc(a,b):
#     c = (a**2+b**2)**0.5
#     return str(c)
#
# a = 3
# b = 4
# c = triangle_calc(a,b)
# print('The right triangle third sides\'s length is ' +c)
#
# def flashligh(battery1,battery2):
#     return 'Light'
#
# nanfu1=600
# nanfu2=1200
#
# C=flashligh(battery2=nanfu1,battery1=nanfu2)
# print(C)
#
#
# file=open('D://personal/coding/open.txt','a')
# file.write('i am king of the world!\n')
#
#
# def write_to_desktop(name,content):
#     path = 'C://Users/Administrator/Desktop/'
#     file = open(path+'name'+'.txt','w')
#     content=input('please input your word:')
#     content.replace(a,b)
#     file.write(content)
#     file.close()
#     print ('Successful Done')
#     return
#
# write_to_desktop(content,name)

# def text_filter(text,changeword='a',changedword='b'):
#     return text.replace(changeword,changedword)
#
# a=text_filter('helloa','ll','oo')
# print(a)



# def sina_colltection(name,collection):

#
# def creat_file(name,msg):
#     path= 'C://Users/Administrator/Desktop/'
#     full_path = path + name +'.txt'
#     file = open(full_path,'w')
#     file.write(msg)
#     file.close()
#     print('write successful')
#     return
#
# def text_filter(word,oldword = "lame",newword = 'Awesome'):
#     return word.replace(oldword,newword)
#
# def filter_creat(name,msg):
#     text = text_filter(msg)
#     creat_file(name,text)
#     return
# filter_creat('filter','lame is a big man!')


# def login():
#     password = input('Pls enter your passowrd:')
#     if password == '12345':
#         print('login successful')
#     else:
#         print('Password Error!!!!!')
#         login()
# login()

# def login():
#     password = input('Pls input your passowrd:')
#     password_correct = password == '12345'
#     if password_correct:
#         print('login successful!')
#     else:
#         print('Error Password!')
#         login()
#
# # login()
#
# passwordlist=['12345','123456']
# def login():
#     password = input('pls input your passowrd:')
#     password_correct = password == passwordlist[-1]
#     password_reset = password == passwordlist[0]
#     if password_correct:
#         print('login successful')
#     elif password_reset:
#         password_1st=None
#         password_2st=None
#         while password_1st != password_2st:
#             password_1st = input('pls input your new password:')
#             password_2st = input('pls input your new passowrd again:')
#
#         passwordlist.append(input('pls input your new password:'))
#         login()
#
#     else:
#         print('Error password!')
#         login()
# login()

# for every_letter in 'Go to shoping!':
#     print(every_letter)
#
# for num in range(1,11):
#     print(str(num)+'+1=',num+1)

# songlist = ['离歌','天使与海豚','海阔天空']
# for song in songlist:
#     if song == '海阔天空':
#         print(song + ' -- beyond')
#     elif song == '离歌':
#         print(song + ' -- 信乐团')
#     else:
#         print(song + ' -- 梁咏琪')
#
#
# for i in range(1,10):
#     for j in range(1,10):
#         print('{}*{}={}'.format(i,j,i*j))
#
# while 1<5:
#     print('hello')
#
#
# for i in range(1,10):
#     path = 'C:/Users/Administrator/Desktop/'
#     name = str(i)
#     file = open(path+name+'.txt','w')


# def invest(amount,rate,time):
#     for year in range(1,time):
#         invest_total = amount*(1+rate)
#         amount = invest_total
#         print('year {}: ${}'.format(year,int(invest_total)))
#
# invest(100,0.05,10)
#
# for i in range(1,101):
#     if i%2 == 0:
#         print(i)


# import random
# sz_list=[]
# st_list=['Big','Small','Exit']
# result = 'None'
#
# def sz():
#     sz1 = random.randrange(1-6)
#     sz2 = random.randrange(1-6)
#     sz3 = random.randrange(1-6)
#     sz_list.append(sz1, sz2, sz3)
#     if sum(sz_list) <= 10:
#         result = 'Small'
#     else:
#         result = 'Big'
#     return
#
#
# for status in st_list:
#     print('<<<<<Game Start!>>>>>')
#     select = input('Big or Small or Exit:')
#     print('<<<<<Role the Dice!>>>>>')
#     sz()
#         if select == result:
#             jieguo='Win!'
#         else:
#             jieguo='Lose!'
#     print('The point are [{},{},{}],Your {}'.format(sz_list(1),sz_list(1),sz_list(1),jieguo))

#
# import random
# def roll_dice(number=3,points=None):
#     print('<Roll the Dice!>')
#     if points == None:
#         points=[]
#         while number > 0:
#             point = random.randrange(1,7)
#             points.append(point)
#             number = number -1
#         return points
#
# def roll_result(total):
#     isBig = 11 <= total <=18
#     isSmall = 3 <= total <= 10
#     if isBig:
#         return 'Big'
#     if isSmall:
#         return 'Small'
#
# def start_game():
#     print('<Game Start>')
#     choice = ['Big','Small']
#     your_choice = input('Big or Small:')
#     if your_choice in choice:
#         saizi = roll_dice()
#         print(saizi)
#         total = sum(saizi)
#         youWin = your_choice == roll_result(total)
#
#         if youWin:
#             print('You Win!!!')
#         else:
#             print('You Lose!!!')
#     else:
#         print('Invialid Word!')
#         start_game()
# start_game()



#
# import random
# def roll_dice(numbers=3,point=None):
#     if point == None:
#         while numbers != 0:
#             point = random.randrange(1,7)
#             points = []
#             points = points.append(point)
#             numbers = numbers -1
#             return points
#
# def bigorsmall(total):
#     isBig = 11 <= total <= 18
#     isSmall= 3 <= total <=10
#     if isBig:
#         return 'Big'
#     elif isSmall:
#         return 'Small'
#
# def Start_Game():
#     print('<Game start!>')
#     choice = ['Big','Small']
#     your_choice = input('Pls input your choice:')
#     if your_choice in choice:
#         saizi=roll_dice()
#         total = sum(saizi)
#         yourwin = your_choice == bigorsmall(total)
#
#         if yourwin:
#             print('the result is {},you {}'.format(saizi),'win')
#         else:
#             print('the result is {},you {}'.format(saizi), 'Lose')
#     else:
#         print('Invild input')
#         Start_Game()
# Start_Game()

# class coke_cola():
#     it_taste = 'so good'
# coke_for_zq= coke_cola()
# coke_for_cgg = coke_cola()
# print(coke_for_cgg.it_taste)
# print(coke_for_zq.it_taste)

#
# class i_like_moto():
#     moto = '360'
#
# huawei = i_like_moto
# print(i_like_moto.moto)
# print(huawei.moto)
#
# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('c://a/sina.html', 'wb') as f:
#     f.write(html)


# import this

# name_list = ['ganggang','qiaoqiao','yutong','sijing']
# for x in range(0,4):
#     print(name_list[x].title()+':'+'Nice to meet you')
#
#
# #
#
# motorcyles = ['Honda','Dayang','Chongqing']
# popped_motorcyles = motorcyles.pop()
# print(popped_motorcyles)
# print(motorcyles)
#
# def invite():
#
#     invite_namelist = ['Chenchao', 'Susan', 'Shanda', 'Xiaoge']
#     for x in invite_namelist:
#         print(x.title() + ' is my guest.')
#     invite_namelist.remove('Shanda')
#     invite_namelist.append('Qiaoling')
#     print('#####NameList Changed#####')
#     for x in invite_namelist:
#         print(x.title() + ' is my guest.')
#     print('####We have a new Tab#####')
#     invite_namelist.insert(2, 'Zhangqiao'),invite_namelist.insert(3, 'Chenyutong'),invite_namelist.append('ChenSijing')
#     for x in invite_namelist:
#         print(x.title() + ' is my guest.')
#     print('###We can only invite 2 guests####')
#
#     while len(invite_namelist) > 2:
#         popped_guest = invite_namelist.pop()
#         print(popped_guest + ' will remove from namelist')
#
#     for x in invite_namelist:
#         print(x.title() + ' is my guest.')
#     del invite_namelist[0]
#     del invite_namelist[0]
#     print(invite_namelist)
#
# invite()

# desired_travelplace = ['chengdu','sanya','singapore','hongkong','newyork']
# print(desired_travelplace)
# print(sorted(desired_travelplace))
# print(desired_travelplace)
# print(sorted(desired_travelplace,reverse=True))
# print(desired_travelplace)
# desired_travelplace.reverse()
# print(desired_travelplace)
# desired_travelplace.reverse()
# print(desired_travelplace)
# desired_travelplace.sort()
# print(desired_travelplace)
# desired_travelplace.sort(reverse=True)
# print(desired_travelplace)

# x = 1
# list = []
# while x < 1000:
#     print(x)
#     list.append(x)
#     x = x+1
# print(list)
#

# pizza_list = ['haixian','shuangping','peigen']
# for pizza in pizza_list:
#     print('I like '+pizza+'Pizza.')

# for number in range(1,21):
#     print(number)
#
# m_number = [value for value in range(1,1000001)]
# print(min(m_number)),print(max(m_number))
# print(sum(m_number))
#
# eve_numbers = [value for value in range(1,21,2)]
# print(eve_numbers)
# for number in eve_numbers:
#     print(number)

# tripple = [value*3 for value in range(1,10)]
# print(tripple)

# cube = []
# for x in range(1,11):
#     data =  x**3
#     cube.append(data)
# print(cube)
#
# cube = [value for value in range(1,11)]
# print('the first three item in the list are:'+str(cube[-3:]))


# alien_color = 'red'
# if alien_color == 'green':
#     print('Congratulation!You have win 5 points!')
# elif alien_color == 'red':
#     print('You have won 15 points')
# else:
#     print('You have won 10 points!')
#
# input_age = True
# while input_age:
#     age = input('Pls input your age,if you want to exit,pls enter\'no\':')
#     if age == 'no':
#         break
#     elif int(age) < 2:
#         print('You are a Baby')
#     elif int(age) < 4:
#         print('You are studing running')
#     elif int(age) < 13:
#         print('You are a children')
#     elif int(age) < 20:
#         print('You are a yang man')
#     elif int(age) < 65:
# #         print('You are a adult')
# #     else:
# #         print('You are an old man')
#
# favorite_fruits = ['apple','pineapple','watermelon','pear','orange']
# for x in range(30):
#     favorite_fruit = input('pls input a fruit:')
#     if favorite_fruit in favorite_fruits:
#         print('you really like '+favorite_fruit)
#     else:print('I don\'t find it')
#

#
# user_names = ['zhangsan','lishi','wangwu','zhaoliu','admin']
# while True:
#     user_name = input('Pls enter your username:')
#     if user_name in user_names:
#         if user_name == 'admin':
#             print('Hello admin,would you like to see a status report?')
#         else:
#             print('Hello %s,thank you for logging in again!' %(user_name))
#     if user_name == '':
#         print('We need to find some users!')

# current_users = ['zhangsan','lishi','wangwu','zhaoliu','Admin']
# current_userslower = [item.lower() for item in current_users]
# new_users = ['Zhangsan','jianxin','penghu','enbing','admin']
# for new_user in new_users:
#     if new_user.lower() in current_userslower:
#         print('%s has been used!' %(new_user))
#     else:
#         print('%s has not been used!' %(new_user))

#
# current_users = ['zhangsan','lishi','wangwu','zhaoliu','Admin']
# new_users = ['Zhangsan','jianxin','penghu','enbing','admin']
# for new_user in new_users:
#     if new_user.lower() in [item.lower() for item in current_users]:
#         print('%s has been used!' %(new_user))
#     else:
#          print('%s has not been used!' %(new_user))
#
# my_dict = {'zhangsan':'zhanggsan','lishi':'lishi'}
# from pprint import pprint
# pprint(my_dict)
# print(my_dict)

#
# number_list = [item for item in range(1,11)]
# for number in number_list:
#     if number == 2:
#         print('%snd' %(number))
#     elif number == 3:
#         print('%srd' %(number))
#     else:
#         print('%sth' %(number))

#
# contacts = {
#     'chen':'first_name',
#     'ganggang':'last_name',
#     '35':'age',
#     'fuzhou':'city',
# }
# print(contacts['chen'])

# vocu_lists = {
#     'list':'一连串有顺序的值',
#     'set':'一连串的值，不可重复',
#     'dict':'一串字符的组合',
#     'triple':'一组数值，不可再修改',
#     'loop':'可循环的方法'
#     }
#
# for k,v in vocu_lists.items():
#     print(str(k)+'means:'+str(v))
#
# rivers = {
#     'nile':'egypt',
#     'huang river':'china',
#     'amazon river':'sa',
#     }
# for river,country in rivers.items():
#     print(river.title() + 'runs through '+country.title())
# #
#
# survey_lists = {
#     'jen':'python',
#     'sara':'c',
#     'susan':'java',
#     'phi':'ruby',
#     }
#
# name_lits = ['ken','sara','jacky','daney']
# for name in name_lits:
#     if name in survey_lists.keys():
#         print(name + ':thanks for your attend!')
#     else:print(name + 'welcome to suvery!')


# contacts = {
#     'chen':'first_name',
#     'ganggang':'last_name',
#     '35':'age',
#     'fuzhou':'city',
# }
# print(contacts['chen'])
# contacts['gulou'] = 'region'
# print(contacts)

# jack ={
#     'first_name':'chen',
#     'last_name':'gang',
#     'age':'33',
#     }
#
# zhang ={
#     'first_name':'zhang',
#     'last_name':'jack',
#     'age':'33',
#     }
#
# gang ={
#     'first_name':'liu',
#     'last_name':'gang',
#     'age':'33',
#     }
#
# peoples = [jack,zhang,gang]
# # for people in peoples:
# #     print(people)
#
# favorite_places = {
#     'zhangsan':'chengdu',
#     'lishi':'xizhang',
#     'wangwu':'guangdong',
# }
#
# cities = {
#     'newyork':
#         {
#             'countury': 'usa',
#             'peoples': '13M',
#             'event': 'morden',
#         },
#     'beijing':
#         {
#             'countury':'china',
#             'peoples':'130M',
#             'event':'old',
#         },
#     'hongkong':
#         {
#         'countury':'hongkong SAR',
#         'peoples':'1M',
#         'event':'1997',
#         },
#     }
#
#
# for city,detail in cities.items():
#     print('The City is:'+ city.title())
#     print('Its belong to:'+detail['countury']+'\npopulation is :'+detail['peoples']+'\n'+detail['event'])
#
#
#
#


##7-4

# active = True
# while active:
#     material = input('pls input your material:')
#     print('We have add' + material)
#
# active = True
# while active:
#     age = input('pls enter your age:')
#     if int(age) < 3:
#         print('you are free!')
#     elif int(age) < 12:
#         print('charge you $10')
#     elif:print('charge you $15')

#7-8

# sandwich_orders = ['cake','buff','egg']
# finished_sandwich = []
# while sandwich_orders:
#     working_sandwich = sandwich_orders.pop()
#     print('I made your %s sandwich' %(working_sandwich))
#     finished_sandwich.append(working_sandwich)
# print('\nYou sandwich have been done:')
# for item in finished_sandwich:
#     print(item)

#7-9
# sandwich_orders = ['pastrami','egg','pastrami','egg''cake','buff','pastrami','egg']
# print('Pastrami sandwich have sold out!')
# sold = 'pastrami'
# while sold in sandwich_orders:
#     sandwich_orders.remove(sold)
# print(sandwich_orders)

#7-10
# Suvery = True
# fav_places = []
# while Suvery:
#     fav_place = input('If you could visit one place in the world,where you want to go:')
#     fav_places.append(fav_place)
#     repeat = input('do you want to continue?(yes/no)')
#     if repeat == 'no':
#         Suvery = False
# print(fav_places)

#8-1
# def display_message():
#     print('you are learning hanshu')
#
# display_message()

#8-2
# def favorite_book(book_title):
#     print('One of you favorite book is %s.' %(book_title))
#
# favorite_book('python')

#8-3
# def make_shirt(size,descrtption):
#     print('This T-shirt is %s and print %s' %(size,descrtption))
#
# make_shirt('32','Java')

#8-4
# def make_shirt(size,descrtption='I love Python'):
#     print('This T-shirt is %s and print %s' %(size,descrtption))
#
# make_shirt('Big')
# make_shirt('Middle','I love Java')

#8-5
# def describe_city(city,countury='China'):
#     print('%s is in %s' %(city,countury))
#
# describe_city('fuzhou','china')

# import math
#
# def quadratic(a, b, c):
#     x1 = (-b + math.sqrt((math.pow(b,2)-4*a*c)))/2*a
#     x2 = (-b - math.sqrt((math.pow(b,2)-4*a*c)))/2*a
#     return x1,x2
#
# x1,x2 = quadratic(2,3,1)
# print(x1,x2)



























