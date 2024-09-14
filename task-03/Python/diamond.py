num = int(input())
star = " "*(num)
for x in range(num):
  star = star[1:]
  star += " *"
  print(star, "\n")
for i in range(num):
  star = star[:-2]
  star = " " + star
  print(star, "\n")