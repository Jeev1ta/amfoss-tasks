defmodule LoopModule do
  def upper_half(_star, 0) do
  end
  def upper_half(star, num) do
    star_new = String.slice(star, 1..-1)
    IO.write(output, star_new)
    star_new = star_new <> " *"
    upper_half(star_new, num-1)
  end
  def lower_half(_star, 0) do
  end
  def lower_half(star, num) do
    IO.write(output, star_new)
    star_new = String.slice(star, 0..-3)
    star_new = " " <> star_new
    lower_half(star_new, num-1)
  end
end

{:ok, num} = File.read("input.txt")
{:ok, output} = File.open("output.txt", [ :write])
star = String.duplicate(" ", num)
LoopModule.upper_half(star, num)
lower = String.duplicate("* ", num)
LoopModule.lower_half(lower, num)
File.close(output)