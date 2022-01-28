#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define N 500000

typedef void (*Func)();

int fib(int n) {
    if (n == 1 || n == 2) {
        return 1;
    }
    return fib(n-1) + fib(n-2);
}
void runFib() {
    int result = fib(30);
    printf("fib(30)=%d\n", result);
}

void timeit(Func func) {
    int t1 = clock();
    func();
    int t2 = clock();

    double cost_time = (double)(t2-t1) / CLOCKS_PER_SEC * 1000.0f;
    printf("cost_time:%lfms\n", cost_time);
}

int main(int argc, char* argv[]) {
    timeit(runFib);
    return 0;
}