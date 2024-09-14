package main
import (
	"fmt"
	"os"
	"strconv"
	"strings"
)
func main() {
	data, _ := os.ReadFile("input.txt")
	output, _ := os.OpenFile("output.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY)
	defer output.Close()
	num, _ := strconv.Atoi(str(data))
	var stars string
	stars = strings.Repeat(" ", num)
	for i := 0; i < num; i++ {
		stars = stars[1:]
		stars += " *"
		output.WriteString(stars + "\n")
	}
	for j := 0; j < num; j++ {
		stars = stars[:len(stars)-2]
		stars = " " + stars
		output.WriteString(stars + "\n")
	}
}