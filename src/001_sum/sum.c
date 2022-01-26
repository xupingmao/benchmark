#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define N 500000

typedef int64_t (*Func)();

int64_t benchFunc() {
    int64_t result = 0;
    for (int i = 0; i < N; i++) {
        result += i;
    }

    return result;
}

void timeit(Func func) {
    int t1 = clock();
    int64_t result = func();
    int t2 = clock();
    
    // 排除了printf的性能问题，但是运行时间还是远远大于go和cython
    // 运行环境：MacBook Air 2015
    //         1.6 GHz 双核Intel Core i5
    //         4 GB 1600 MHz DDR3
    // C语言耗时： 1.4ms ~ 1.6ms
    //     加上-O2参数耗时缩短到 0.001ms ~ 0.002ms
    // Go语言耗时：0.24ms ~ 0.45ms
    // Cython耗时： 0.054ms ~ 0.057ms
    printf("loops=%d\n", N);
    printf("result=%lld\n", result);

    double cost_time = (double)(t2-t1) / CLOCKS_PER_SEC * 1000.0f;
    printf("cost_time:%lfms\n", cost_time);
}

int main(int argc, char* argv[]) {
    timeit(benchFunc);
    return 0;
}