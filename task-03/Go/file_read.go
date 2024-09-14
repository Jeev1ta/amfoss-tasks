package main
import ("os")
func main() {
	data, _ := os.ReadFile("input.txt")
	_ = os.WriteFile("output.txt",data)
}