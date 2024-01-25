choices =input("Enter your Computer choice (stone/paper/scissors): ")
user_choice = input("Enter your Human choice  (stone/paper/scissors): ")
if choices == user_choice:
     print("Its Tie")

if user_choice=="stone":
    if choices =="paper":
      print("user Win!")

if choices == "paper":
    if user_choice =="scissors":
        print("user win")

if choices == "scissors":
    if user_choice=="stone":
        print("user win")



else:
     print("Computer Win! ...YOU LOSE BETTER LUCK NEXT TIME")
