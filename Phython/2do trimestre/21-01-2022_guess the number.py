while True:
  x=int(input("Guess the number:"))
  number=10
  if x>8:
    print('less')
  if x<8:
    print('more')
  if x==8:
    print('You got it')
  