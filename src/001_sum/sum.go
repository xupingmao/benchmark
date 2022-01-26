package main

import (
	"fmt"
	"time"
)

func benchFunc() {
	const N int = 500000
	result := 0
	for i:=0;i<N;i++ {
		result += i;
	}
	fmt.Printf("loops=%d\n", N)
	fmt.Printf("result=%d\n", result)
}

func timeit(f func()) {
	t1 := time.Now()
	f()
	cost_time := time.Since(t1)
	
	fmt.Printf("cost_time=%vms\n", float64(cost_time)/float64(time.Millisecond))
}

func main() {
	timeit(benchFunc)
}