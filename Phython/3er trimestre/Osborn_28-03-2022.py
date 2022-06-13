print("Welcome to Osborn!")
input()
print("Dr. Osborn: In this game you will have the opportunity to choose between 3 characters")

input()

print("Dr. Osborn: Remember, you need to be careful, each character has a different power and a different weakness")
print("Your mission is to save Osborn")


input()
print("Kirby")
print("Powers:Fast")
print("Weakness:Eating cake") 
print("Map: Dragon city mobile")

input()
print("Nathan Drake")
print("Powers: Super Strength")
print("Weakness: Spider bite") 
print("Map: Drake's treasure")


input()
print("Ken")
print("Powers:Fireballs and good at fighting") 
print("Weakness:Face punching ")
print("Map: Street")


input()
print("Dr.Osborn: Now, you have to be wise from this point on. After reading this you already have the opportunity to choose your avatar that has caught your attention the most")

#escojer personaje y mapa
character=input("Choose your character: ")
character=character.capitalize()

#KIRBY
while(character=="Kirby"):
  print("You have choosen kirby")
  print("Your map is Dragon city mobile")
  print("Dr.Osborn:Kirby is an entity of a magical place that has magical powers which, has been recruited for an important mission, both for Osborn, and for all humanity.")
  input()
  
  print("Read carefully and be careful with your decisions, one of the best things from kirby is that he is always cute, but when he gets mad, be careful, it is a very different thing ")
  input()
  print("Just keep in mind that if Kirby finds a cake and eats it, it will be the end.")
 
#empieza el juego de Kirby
#1er nivel
  print("Dr.Osborn: Good! Let's start")
  input("Press enter to start")
  print("As you saw before, your map is Dragon city mobile, this means that you will be discovering a magical place")
  print("This will not be that easy, but remember, you have all the power")
  print("Use your powers wisely and enjoy the game")
  print("To start follow the steps and read carefuly")
  
  #variables
  way1=input("You have to choose between 2 ways, a or b:")

  
  if (way1=="a"):
   print("In this way, you can go without any preocupation for now")
   print("You will find an elixir, if you take it and drink it, you will be recovered")
   print("Press enter to take the elixir")
   input()
   print("Nice! You have took the elixir")
   print("Now, press enter to drink it")
   input()
   print("You drank the elixir, now keep walking")
   input()
   print("STOP")
   print("There is a mysterious men in front of you")
   print("He is offering you a cake")
   print("You take it or you leave it")
   opi=input("Press 'c' to take it or press 'd' to leave it: ")
   
   if(opi=="c"):
      print("Great! You accepted the cake")
      print("The cake is mysterious")
      print("Press enter to eat it")
      input()
      print("Bad luck!")
      print("You lost, remember that Kirby can't eat cake")
      print("However, there is a elixir in front of you that can heal you")
      print("Press enter to take it")
      input()
      print("Press enter to drink it")
      input()
      print("Now you are healed")
      print("Great!, You have passed the 1st level")
      print("Be prepared for the next level")
      
   
   if(opi=="d"):
       print("You didn't take the cake")
       print("That was an amazing idea")
       print("Remember that Kirby's weakness are the cakes")
       print("Now, you can continue")
       print("Great!, You have passed the 1st level")
       print("Be prepared for the next level")
       

    
  #way b
  if(way1=="b"):
     print("In this way, you will find a man that wants to kill you")
     print("You decide how to continue")  
     print("Remember that you are super fast")
     #aq
     opo=input("Press 'c' to kick him or press 'd' to run:")
     if(opo=="c"):
        print("You have kicked the man once, however yo have to kick him twice to kill him")
        print("Press enter to kill him again")
        input()
        print("That's nice, you have killed him")
        print("Now, you can continue")
        print("This is a long way, you have passed the 1st level")
        print("Be prepared for the next level")
     if(opo=="d"):
         print("You have started running, however, if you want to survive you have to kick the man twice")
         print("To kick the man twice, press the enter button twice")
         input()
         input()
         print("That's nice, you have killed the man")
         print("Now, you can continue")
         print("This is a long way, you have passed the 1st level")
         print("Be prepared for the next level")
  input("Press enter to pass to the 2nd level")
  
  #2do nivel
  print("Now you are on the second level")
  print("In this level, there is no escape from fighting")
  input()
  print("This is the last level, make your best effort")
  print("In this level you will have to save osborn")
  print("It will not be easy, but remember that you have all the power to save osborn")
  print("Lets start")
  print("Press enter to start")
  input()

  #variables
  way2=input("You have to choose between 2 ways, a or b: ")
  if (way2=="a"):
    print("You have choosen way a")
    print("You have started walking")
    print("There is a magical tool in front of you, press enter to take it")
    input()
    print("You took the magical tool, now keep walking")
    print("...")
    input()
    print("STOP")
    print("There is a fighter in front of you ")
    print("You have the option to choose if you kick him or you use the magical tool against him")
    opi=input("Press 'c' to use the magical tool or press 'd' kick: ")
    if(opi=="c"):
      print("Great! You used the magical tool correctly")
      print("Now he is dead, you can continue")
    if(opi=="d"):
       print("You have kicked him once, but remember you need to kick him twice to kill")
       print("Press enter to kick him again")
       input()
       print("Great! You have killed him")
       print("Now, you can continue")

  
  if (way2=="b"):
      print("You have choosen way b")
      print("You have started walking")
      print("In this way you will not have any support, guns or other things are not allowed")
      print("In this way you will have the power to use your speed and your own hands")
      input()
      print("STOP")
      print("In front of you there is a fighter")
      opi=input("Press 'c' to throw your speed or press 'd' to use your magical power's : ")
      if(opi=="c"):
        print("Great! You have done it correctly")
        print("Now he is dead, you can continue")
      if(opi=="d"):
         print("You have used your magical powers  him once, but remember you need to kick him twice to kill")
         print("Press enter to kick him again")
         input()
         print("Great! You have killed him")
         print("Now, you can continue")
  break
 


 #NATHAN DRAKE
while(character=="Nathan drake"):
  print("You have choosen Nathan Drake")
  print("Your map is Drake's treasure")
  print("Dr.Osborn:Nathan, the best guy to search about treasures and value things which, has been recruited for an important mission, both for Osborn, and for all humanity.")
  input()
  
  print("Read carefully and be careful with your decisions, one of the best of skills is that he is always assertive with his movements when searching for the Drake's treasure and when saving Osborn ")
  input()
  print("Just keep in mind that if Nathan  receives any spider bite even, we are gonna be sorry player, but your game will be over.")
 
#empieza el juego de Nathan Drake
#1er nivel
  print("Dr.Osborn: Good! Let's start")
  input("Press enter to start")
  print("As you saw before, your map is Drake's treasure, this means that you will be discovering some of values things like gold")
  print("This will not be that easy, but remember, you have all the power")
  print("Use your super strenght wisely and enjoy the game")
  print("To start follow the steps and read carefuly")
  
  #variables
  way1=input("You have to choose between 2 ways, a or b:")

  
  if (way1=="a"):
   print("In this way, you can go without any preocupation for now")
   print("You will find a barrel, if you break it, you will find some value coins")
   print("Press enter to break the barrel")
   input()
   print("Nice! You have broken the barrel, now you're having the coins ")
   print(" In the way you are, in front of you, you will find a gun")
   print("Press enter to take it")
   input()
   print("You took the gun, now keep walking until you listen some voices")
   input()
   print("STOP")
   print("There are some enemies like 15 meters  in front of you")
   print("Remember that you have a gun, if you shoot hem, you will kill him and pass to the next level, don't lose your coins")
   print("Or you also have the option of kicking him to kill him")
   opi=input("Press 'c' to shoot or press 'd' kick: ")
   
   if(opi=="c"):
      print("Great! You shooted them correctly")
      print("Now they are dead, you can continue")
      print("This is a long way, you have passed the 1st level")
      print("Be prepared for the next level")
      input("Press enter to pass to the 2nd level")
   
   if(opi=="d"):
       print("You have kicked them once, but remember you need to kick five times to kill each one of the enemies")
       print("Press enter to kick them again")
       input()
       print("Great! You have killed them")
       print("Now, you can continue")
       print("This is a long way, you have passed the 1st level")
       print("Be prepared for the next level")
       

    
  #way b
  if(way1=="b"):
     print("In this way, you will find like ten mans and some spiderwebs with a lot of poisonous spiders, be careful with the spiders")
     print("You need to kill them to avoid the punches and to dodge the bullets, remember that if a spider bites you, the game is over")  
     opo=input("Press 'c' to take risk and super strenght or press 'd' to take a lot of risk and shoot them:")
     if(opo=="c"):
        print("You have taken the risk, however you have to kick them like five times to kill them")
        print("Press enter to hit one last time and kill them")
        input()
        print("That's nice, you have killed all of them")
        print("Now, you can continue")
        print("This is a long way, you have passed the 1st level")
        print("Be prepared for the next level")
     if(opo=="d"):
         print("You have started shoot them, however, if you want to survive you need to kill the poisonous spiders that are infront of you")
         print("To kill the spiders, press the enter button twice")
         input()
         input()
         print("That's nice, you have killed the most of the spiders")
         print("Now, you can continue")
         print("This is a long way, you have passed the 1st level")
         print("Be prepared for the next level")
  input("Press enter to pass to the 2nd level")
  
  #2do nivel
  print("Now you are on the second level")
  print("In this level, there is no escape from spiders")
  input()
  print("This is the last level, make your best effort")
  print("In this level you will have to save osborn and to get the Drake's treasure")
  print("It will not be easy, but remember that you have super strength and a lot of guns with a lot of bullets to save osborn and to save yourself")
  print("Lets start")
  print("Press enter to start")
  input()

  #variables
  way2=input("You have to choose between 2 ways, a or b: ")
  if (way2=="a"):
    print("You have choosen way a")
    print("You have started walking carefuly")
    print("There is a machine gun and a and a protective equipment that helps you cover your body from spider bites, but unfortunately it will only last thirty seconds, press enter to take the machine gun and the equipment")
    print("You took the machine gun and you have already the equipment in your body, now keep walking")
    print("...")
    input()
    print("STOP")
    print("There are like 50 cocoons of spiders in front of you ")
    #aqui
    print("You have the option to choose if you shoot and spend the two hundred bullets in the gun or twenty seconds to run out of there")
    opi=input("Press 'c' to shoot or press 'd' to run: ")
    if(opi=="c"):
      print("Great! You shooted them correctly")
      print("Now the spiders are dead, you can continue")
    if(opi=="d"):
       print("You have run out of there with a spider bite in your arm, in front of you there is an antidote to recover from the spider bite, you have fifteen seconds to take it or you die")
       print("Press enter to take the antidote")
       input()
       print("Great! Now you are save thanks to the antidote")
       print("Now, you can continue")

  
  if (way2=="b"):
      print("You have choosen way b")
      print("You have started walking")
      print("In this way you will nothave any support, guns or other things are not allowed")
      print("In this way you will have the power to use your body and skills like super strenght and parkour")
      input()
      print("STOP")
      print("In front of you there are like twenty enemies with guns, equipment and bombs")
      opi=input("Press 'c' silently knock out each of them or press 'd' to kick them on their faces : ")
      if(opi=="c"):
        print("Great! You have done it correctly")
        print("Now they're dead because you knocked them out too hard , you can continue")
      if(opi=="d"):
         print("You have kicked them once, but remember you need to kick them like five times to kill each of them")
         print("Press enter to kick them again")
         input()
         print("Great! You have killed them")
         print("Now, you can continue")

     
       
    
    
  break
    

#KEN
while(character=="Ken"):
  print("You have choosen ken")
  print("Your map is Street")
  print("Dr.Osborn:Ken, the best fighter   of street fights, which, has been recruited for an important mission, both for Osborn, and for all humanity.")
  input()
  
  print("Read carefully and be careful with your decisions, one of the best of skills is that he is always assertive with his movements when fighting")
  input()
  print("Just keep in mind that if Ken receives even one hit to the face, we are sorry player, but your game will be over.")
 
#empieza el juego de Ken
#1er nivel
  print("Dr.Osborn: Good! Let's start")
  input("Press enter to start")
  print("As you saw before, your map is street, this means that you will be discovering a street")
  print("This will not be that easy, but remember, you have all the power")
  print("Use your powers wisely and enjoy the game")
  print("To start follow the steps and read carefuly")
  
  #variables
  way1=input("You have to choose between 2 ways, a or b:")

  
  if (way1=="a"):
   print("In this way, you can go without any preocupation for now")
   print("You will find a barrel, if you break it, you will find food")
   print("Press enter to break the barrel")
   input()
   print("Nice! You have broken the barrel ")
   print(" In the way you are, in front of you, you will find a gun")
   print("Press enter to take it")
   input()
   print("You took the gun, now keep walking")
   input()
   print("STOP")
   print("There is a fighter in front of you")
   print("Remember that you have a gun, if you shoot him, you will kill him and pass to the next level")
   print("Or you also have the option of kicking him to kill him")
   opi=input("Press 'c' to shoot or press 'd' kick: ")
   
   if(opi=="c"):
      print("Great! You shooted him correctly")
      print("Now he is dead, you can continue")
      print("This is a long way, you have passed the 1st level")
      print("Be prepared for the next level")
      input("Press enter to pass to the 2nd level")
   
   if(opi=="d"):
       print("You have kicked him once, but remember you need to kick him twice to kill")
       print("Press enter to kick him again")
       input()
       print("Great! You have killed him")
       print("Now, you can continue")
       print("This is a long way, you have passed the 1st level")
       print("Be prepared for the next level")
       

    
  #way b
  if(way1=="b"):
     print("In this way, you will find a man that wants to kill you")
     print("You need to kill him to avoid that he punches your face, remember that if he punches you in the face, the game is over")  
     opo=input("Press 'c' to kick him or press 'd' to run:")
     if(opo=="c"):
        print("You have kicked the man once, however yo have to kick him twice to kill him")
        print("Press enter to kill him again")
        input()
        print("That's nice, you have killed him")
        print("Now, you can continue")
        print("This is a long way, you have passed the 1st level")
        print("Be prepared for the next level")
     if(opo=="d"):
         print("You have started running, however, if you want to survive you have to kick the man twice")
         print("To kick the man twice, press the enter button twice")
         input()
         input()
         print("That's nice, you have killed the man")
         print("Now, you can continue")
         print("This is a long way, you have passed the 1st level")
         print("Be prepared for the next level")
  input("Press enter to pass to the 2nd level")
  
  #2do nivel
  print("Now you are on the second level")
  print("In this level, there is no escape from fighting")
  input()
  print("This is the last level, make your best effort")
  print("In this level you will have to save osborn")
  print("It will not be easy, but remember that you have all the power to save osborn")
  print("Lets start")
  print("Press enter to start")
  input()

  #variables
  way2=input("You have to choose between 2 ways, a or b: ")
  if (way2=="a"):
    print("You have choosen way a")
    print("You have started walking")
    print("There is a gun in front of you, press enter to take it")
    print("You took the gun, now keep walking")
    print("...")
    input()
    print("STOP")
    print("There is a fighter in front of you ")
    print("You have the option to choose if you kick him or you shoot him")
    opi=input("Press 'c' to shoot or press 'd' kick: ")
    if(opi=="c"):
      print("Great! You shooted him correctly")
      print("Now he is dead, you can continue")
    if(opi=="d"):
       print("You have kicked him once, but remember you need to kick him twice to kill")
       print("Press enter to kick him again")
       input()
       print("Great! You have killed him")
       print("Now, you can continue")

  
  if (way2=="b"):
      print("You have choosen way b")
      print("You have started walking")
      print("In this way you will nothave any support, guns or other things are not allowed")
      print("In this way you will have the power to use your fireballs and your own hands")
      input()
      print("STOP")
      print("In front of you there is a fighter")
      opi=input("Press 'c' to throw your fireball or press 'd' to kick: ")
      if(opi=="c"):
        print("Great! You have done it correctly")
        print("Now he is dead, you can continue")
      if(opi=="d"):
         print("You have kicked him once, but remember you need to kick him twice to kill")
         print("Press enter to kick him again")
         input()
         print("Great! You have killed him")
         print("Now, you can continue")

     
       
    
    
  break


  

print("now you countinue to the final stretch of these game")
print("remember that is not going to be easy")
print("You are going to fight with the craquen at the bottom of the sea")
print("no matter who are you,you can beat it")
print("now you are going to continue walking until you see the craquen")
print("press enter to walk")
input()
input()
input()
input()
input()
print("the time has arrived the kraken is in front of you")
print("use your powers to beat it")
fin=input("Press 'a' if you are kirby, press 'b' if you are Nathan Drake or press 'c' if you are Ken")
if(fin=="a"):
  print("Kirby, use your magical powers to kill him")
  print("get into a tentacle and then throw your elixir into his face, with that you will kill him")
  print("press enter to get into the tentacle")
  input()
  print("Now you are in the tentacle")
  print("Press enter to throw the elixir")
  input()
  print("You failed the shoot")
  print("Press enter until you kill him")
  input("------")
  input("------")
  input("------")
  input("------")
  input("------")
  print("Nice! You killed him")
  print("But wait, your mission was to save dr. Osborn")
  print("Where is he?")
  print("Look for him, maybe he is behind the kraken or inside of it")
  print("Keep walking until you find him")
  input()
  print("STOP")
  print("You found Dr. Osborn")
  print("now you can take him to a safe place")
  print("Dr.Osborn: Thank you for saving me from the beast")
  ptint("Now you are free")
  print("****GAME OVER****")

if(fin=="b"):
  print("Nathan Drake, use your fist or guns to kill the kraken")
  print("get into a tentacle and then use your fist or guns, with that you will kill him")
  print("press enter to get into the tentacle")
  input()
  print("Now you are in the tentacle")
  print("Press enter to shoot or kick")
  input()
  print("You failed the shoot")
  print("Press enter until you kill him")
  input("------")
  input("------")
  input("------")
  input("------")
  input("------")
  print("Nice! You killed him")
  print("But wait, your mission was to save dr. Osborn")
  print("Where is he?")
  print("Look for him, maybe he is behind the kraken or inside of it")
  print("Keep walking until you find him")
  input()
  print("STOP")
  print("You found Dr. Osborn")
  print("now you can take him to a safe place")
  print("Dr.Osborn: Thank you for saving me from the beast")
  ptint("Now you are free")
  print("****GAME OVER****")

if(fin=="c"):
  print("Ken, use your powers to kill him")
  print("get into a tentacle and then use your powers, with that you will kill him")
  print("press enter to get into the tentacle")
  input()
  print("Now you are in the tentacle")
  print("Press enter to use your powers")
  input()
  print("You failed the shoot")
  print("Press enter until you kill him")
  input("------")
  input("------")
  input("------")
  input("------")
  input("------")
  print("Nice! You killed him")
  print("But wait, your mission was to save dr. Osborn")
  print("Where is he?")
  print("Look for him, maybe he is behind the kraken or inside of it")
  print("Keep walking until you find him")
  input()
  print("STOP")
  print("You found Dr. Osborn")
  print("now you can take him to a safe place")
  print("Dr.Osborn: Thank you for saving me from the beast")
  ptint("Now you are free")
  print("****GAME OVER****")

print(""░░░▄▄
░░░░░░░░░░█░░█
░░░░░░░░░░█░░█
░░░░░░░░░█░░░█
░░░░░░░░█░░░░█
██████▄▄█░░░░░██████▄
▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓█████░░░░░░░░░█
█████▀░░░░▀▀██████▀")