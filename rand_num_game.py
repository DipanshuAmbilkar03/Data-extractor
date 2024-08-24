import random
guessAttempt = 1
print('Guess A Number Game')
print('Enter Your Name')
name = input()
print('Welcome User',name,'. I am generating one random number Between 1 till 13.\nPlease Wait......')
number = random.randint(1,13)
print('Random Number Generated. Please Guess The Number In 4 Attempts')
while guessAttempt<=4:
  print('Enter The Number')
  guess = int(input())

  if guess>number:
    print('Your Guess Is Too High. Please Guess The Smaller Number')

  if guess<number:
    print('Your Guess Is Too Low. Please Guess The Higher Number')

  if guess==number:
    print('Congratulations ! You Won. You Guess The Number In',guessAttempt,'attempts.')
    break

  guessAttempt += 1

if guess!=number:
  print('Game Over. The Correct Number Was',number)