package main

import "fmt"

func main() {
	names := [...]string{"eko", "kurniawan", "khannedy", "joko", "budi", "nugraha"}

	slice := names[4:6]
	fmt.Println(slice)

	slice1 := names[:3]
	fmt.Println(slice1)

	slice2 := names[3:]
	fmt.Println(slice2)

	slice3 := names[:]
	fmt.Println(slice3)
}