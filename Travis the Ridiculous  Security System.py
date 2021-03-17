known_users=["Alice","John","Bob", "Calir","David","Elisha","Flora","George"]
print(known_users)

while True:
   print("Hey! My name is Travis")
   name=input("What is your name?: ").strip().capitalize()

   if name in known_users:
        print("Hello {}!".format(name))
        remove=input("Would you like to remove your name from system(y/n)? ").strip().lower()
        if remove=="y":
            known_users.remove(name)
        elif remove=="n":
           print("No problem ! I didn't want you to remove anyway")
                   
   else:
     print("Hmmm..I don't think I have met you yet {}".format(name))
     add_me=input("Would you like to add in system (y/n)?").strip().lower()
     if add_me=="y":
         known_users.append(name)
         print(known_users)
         
     elif add_me=="n":
         print("No worries! See you later")
