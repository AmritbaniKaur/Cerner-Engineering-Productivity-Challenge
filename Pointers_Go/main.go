// cerner_2^5_2019
package main

import "fmt"

func pointerFunction(a *int) {
	// dereferencing
	*a = 748
}

// Main function
func main() {
	var x = 100
	fmt.Printf("The value of x before function call is: %d\n", x)

	var pointerVariable *int = &x
	pointerFunction(pointerVariable)

	fmt.Printf("The value of x after function call is: %d\n", x)
}
