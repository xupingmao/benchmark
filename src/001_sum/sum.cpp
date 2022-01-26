#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define N 500000

typedef void (*Func)();

void benchFunc() {
    int64_t result = 0;
    for (int i = 0; i < N; i++) {
        result += i;
    }
    printf("loops=%d\n", N);
    printf("result=%lld\n", result);
}

void timeit(Func func) {
    int t1 = clock();
    func();
    int t2 = clock();
    double cost_time = (double)(t2-t1) / CLOCKS_PER_SEC * 1000.0f;
    printf("cost_time:%lfms\n", cost_time);
}

int main(int argc, char* argv[]) {
    timeit(benchFunc);
    return 0;
}