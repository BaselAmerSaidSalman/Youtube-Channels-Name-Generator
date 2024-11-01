import time
def Youtube_Channels_Name_Generator():
  print("Welcome to the Youtube Channels Name Generator")
  name = input("What is your nickname?\n")
  print("Nice to meet you " + name + " You should answer next question")
  time.sleep(1)
  topic = input("What is your youtube channel about?\n")
  print("You can name it (" + topic + " with " + name + ")")
  Question = input("Do you want to try again?\n").lower()
  while Question != "yes" and Question != "no":
    print("Please answer with yes or no")
    Question = input("Do you want to try again?\n").lower()
  if Question == "yes":
    Youtube_Channels_Name_Generator()
  elif Question == "no":
    print("Thank you for using our app")
Youtube_Channels_Name_Generator()
