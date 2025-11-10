# loop

# valor 1 - valor includente
# valor 2 - valor excludente
# valor 3 - valor incremental

# loops for 

for i in range(10):
  print(i)

for i in range(2, 10):
  print(i)

for i in range(0, 10, 3):
  print(i)

# loop for each

for i in "python":
    print(i)

# loop while

count = 0
while (count < 10):
  print(count)

  # IMPORTANTE!!! atualizar o contador!
  count += 1

# loop while + for 

while True:
  user = input("digite algo para ser repetido: ")
  if user == "end":
    print("programa encerrado!")
    break
  print(user)

# ou

end = True
while end == True:
  user = input("digite algo para ser repetido: ")
  if user=="end":
    print("programa encerrado!")
    end = False
  else:
    print(user)

count = 1

# usando while

while count + 1 <= 20:
  if count % 2 == 0:
    print("SKIP")
    count += 1
    continue
  print(count)
  count += 1


# usando for

for i in range (1, 20):
  if i % 5 == 0:
    print("SKIP")
    continue
  print(i)