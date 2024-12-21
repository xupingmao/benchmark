package main

import (
	"fmt"
	"time"
)


func fib(n int) int {
	if n == 1 || n == 2 {
		return 1
	}
	return fib(n-1) + fib(n-2)
}

func main() {
	t1 := time.Now()
	result := fib(30)
	costTime := time.Since(t1)
	fmt.Printf("fib(%v)=%v\n", 30, result)
	fmt.Printf("cost %v\n", costTime)
}