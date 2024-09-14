num = gets
num = num.to_i
star = " "*num
for i in 1..num do
    star = star[1..-1]
    star += " *"
    puts star
end
for j in 1..num do
    star = star[0..-3]
    star = " " + star
    puts star
end