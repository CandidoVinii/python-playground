print("Bem vindo ao QUIZ")
user_answer = input("Quer começar? (S/N) \n")
points = 0;
if user_answer.lower() != "s" :
  quit()

print("Começando...")
print("Quem ganhu o Major MLG Colombus 2016? \n (A) LG \n (B) NAVI \n (C) FNATIC \n (D) VIRTUS PRO \n")
answer = input("reposta \n")

if answer.lower() == "a":
  points += 10
  print("Correto!")
else: 
  print("Incorreta!")

print("Quem ganhu o ESL One 2016?\n (A) FNATIC \n (B) IMMORTALS \n (C) ASTRALIS \n (D) SK \n")
answer2 = input("reposta \n")

if answer2.lower() == "d":
  points += 10
  print("Correto!")
else: 
  if points > 0 :
    points -= 5
  print("Incorreta!")

if points == 20:
  print(f"Parabéns, você acertou todas as questões!! \n Seu resultado foi de: { points }/20")
else:
  print(f"Sua pontuação final foi de: { points }/20")

  



