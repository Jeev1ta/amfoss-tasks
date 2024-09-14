{:ok, input} = File.read("input.txt")
{:ok, output} = File.open("output.txt", [ :write])
IO.write(output, input)
File.close(output)