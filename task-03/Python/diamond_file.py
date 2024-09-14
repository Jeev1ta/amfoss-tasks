string = open("input.txt", "r")
f = open("output.txt", "w")
num = int(string.read())
star = " "*(num)
for x in range(num):
  star = star[1:]
  star += " *"
  f.write(star + "\n")
for i in range(1,num+1):
  star = star[:-2]
  star = " " + star
  f.write(star + "\n")