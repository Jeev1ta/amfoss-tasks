num = File.read("input.txt")
num = num.to_i
star = " "*num
for i in 1..num do
    star = star[1..-1]
    star += " *"
    File.write("output.txt", star, mode: "a")
end
for j in 1..num do
    star = star[0..-3]
    star = " " + star
    File.write("output.txt", star, mode: "a")
end