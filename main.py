import random
from emoji import logo

k = 1
user = 0
pc = 0
userend = 0
pcend = 0
play_continue = ""
while True:
  i, j = 0, 0
  if k == 1:
    print(f"{k}-o'yiningiz {logo}")
  elif userend > pcend:
    print(f"{k}-o'yiningiz hozircha hisob {userend}-{pcend} siz oldindasiz {logo}")
  elif userend < pcend:
    print(f"{k}-o'yiningiz hozircha hisob {userend}-{pcend} men oldindaman {logo}")
  else:
    print(f"{k}-o'yiningiz hozircha hisob {userend}-{pcend} durrang {logo}")
  if play_continue != "ha":
    level = input("qiyinlik darajasini tanlang easy/normal/hard: ")
  if level == "easy":
    i, j = 15, 15
  elif level == "normal":
    i, j = 10, 10
  else:
    i, j = 7, 7
  print(f"1 dan 100 gacha bo'lgan sonlar ichidan birini tanladim topolasizmi? \nSizda {i} ta imkon bor")
  computer_number = random.randrange(1, 101)
  user_number = 0
  while computer_number != user_number:
    user_number = int(input("son kiriting: "))
    user += 1
    if computer_number > user_number:
      i -= 1
      if i > 0:
        print(f"{user_number} dan katta son kiriting, sizda {i} ta imkon qoldi")
      else:
        print("imkoniyatingiz qolmadi")
        break
    elif computer_number < user_number:
      i -= 1
      if i > 0:
        print(f"{user_number} dan kichik son kiriting, sizda {i} ta imkon qoldi")
      else:
        print("imkoniyatingiz qolmadi")
        break
    else:
      print(f"Ha men {computer_number} sonini o'ylagandim, siz {user} ta urinishda topdingiz")
  computer_number = 0
  user_number = int(input("1 dan 100 gacha bo'lgan sonlar ichidan birini tanlang va men topshishga xarakat qilaman: "))
  a, b = 1, 101
  while computer_number != user_number:
    computer_number = random.randrange(a, b)
    pc += 1
    if computer_number > user_number:
      j -= 1
      if j > 0:
        print(f"{computer_number} dan kichikroqmi, menda {j} ta imkon qoldi")
      else:
        print(f"{computer_number} ham emasmi, imkoniyatim qolmadi")
        break
      b = computer_number
    elif computer_number < user_number:
      j -= 1
      if j > 0:
        print(f"{computer_number} dan kattaroqmi, menda {j} ta imkon qoldi")
      else:
        print(f"{computer_number} ham emasmi, imkoniyatim qolmadi")
        break
      a = computer_number + 1
    else:
      print(f"{computer_number} ni o'yladingizmi? men {pc} ta urinishda topdim")
  if i > j:
    print("Siz yutdingiz Tabriklaymiz!!!")
    userend += 1
  elif i < j:
    print("Yutdim ureee!!!")
    pcend += 1
  else:
    if i == 0:
      print("Ikkalamiz ham o'ldik")
    else:
      print("Durrang bo'ldi")
      userend += 1
      pcend += 1
  play_continue = input("yana o'ynaysizm? ha/yo'q: ")
  if play_continue == "ha":
    pc = 0
    user = 0
    k += 1
  else:
    break
