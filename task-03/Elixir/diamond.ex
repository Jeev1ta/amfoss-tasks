defmodule LoopModule do
  def upper_half(_star, 0) do
  end
  def upper_half(star, num) do
    star_new = String.slice(star, 1..-1)
    IO.puts(star_new)
    star_new = star_new <> " *"
    upper_half(star_new, num-1)
  end
  def lower_half(_star, 0) do
  end
  def lower_half(star, num) do
    IO.puts(star)
    star_new = String.slice(star, 0..-3)
    star_new = " " <> star_new
    lower_half(star_new, num-1)
  end
end

num = IO.gets("Enter num:")
num = String.to_integer(num)
star = String.duplicate(" ", num)
LoopModule.upper_half(star, num)
lower = String.duplicate("* ", num)
LoopModule.lower_half(lower, num)