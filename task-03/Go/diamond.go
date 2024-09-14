package main
import (
	"fmt"
	"strings"
)
func main() {
	var num int
	fmt.Scan(&num)
	var stars string
	stars = strings.Repeat(" ", num)
	for i := 0; i < num; i++ {
		stars = stars[1:]
		stars += " *"
		fmt.Println(stars)
	}
	for j := 0; j < num; j++ {
		stars = stars[:len(stars)-2]
		stars = " " + stars
		fmt.Println(stars)
	}
}