// cerner_2^5_2019
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	slice := []int{-364, 482, 514, 265, 527, 610, -467, 392, 121, -37, -47, -329, 477, -873, -103, 403, 489, 477, 248, -392}
	fmt.Println("\n--- Unsorted List ---\n", slice)
	quicksort(slice)
	fmt.Println("\n--- Sorted List ---\n", slice)
}
func quicksort(a []int) []int {
	if len(a) < 2 {
		return a
	}
	left, right := 0, len(a)-1
	pivot := rand.Int() % len(a)
	a[pivot], a[right] = a[right], a[pivot]
	for i := range a {
		if a[i] < a[right] {
			a[left], a[i] = a[i], a[left]
			left++
		}
	}
	a[left], a[right] = a[right], a[left]
	quicksort(a[:left])
	quicksort(a[left+1:])
	return a
}
