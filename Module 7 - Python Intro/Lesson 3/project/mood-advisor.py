
name = input("Hello ! I am your personal mood advisor, I would like to start by getting your name ")
mood = input(f"Welcome {name} ! How are you feeling today ? ")

if mood.lower() == "good" or mood.lower() == "happy" :
  reason = input(f"Wow ! Thats great to hear, Can you tell me what is making you feel {mood} today ? ")
elif mood.lower() == "bad" or mood.lower() == "sad" :
  reason = input(f"Im sorry to hear that, i hope you feel better soon ! Would you like to tell me why you are feeling {mood} today ? ")
elif mood.lower() == "angry" or mood.lower() == "grumpy" :
    reason = input(f"Im sorry that you're angry, Take a moment to calm down. Would you like to tell me why you feel {mood} today ? ")
else :
   reason = input(f"I see, Would you like to tell me why you're feeling {mood} today ?")

print(f"that sounds like a {mood} day !")
print("Thank You for Using mood advisor")