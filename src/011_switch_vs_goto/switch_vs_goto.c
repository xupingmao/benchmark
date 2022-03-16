#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>

enum OP {
    /* 开始占位符 */
    OP_START = 0,

    LD_NUM,
    LD_LOC,
    ST_LOC,
    ADD,
    MUL,
    RET,

    /* 结束标记符 */
    EOP, 
};

#define N 5000000
#define true 1

typedef void (*Func)();

typedef struct opcode_t {
    int code;
    int a;
} OpCode;

typedef struct runtime_t {
    OpCode* opcodes;
    int* locals;
    int* stack;
    int loops;
} Runtime;


void switchFunc (Runtime* rt) {    
    OpCode* op = rt->opcodes;
    int *locals = rt->locals;
    int *stack  = rt->stack;
    int top = 0;
    int loops = rt->loops;
    
    // instructions count
    int count = 5;

    for (int i = 0; i < loops; i++) {
        top = 0;
        while (true) {
            switch(op->code) {
                case LD_NUM:
                    top ++;
                    stack[top] = op->a;
                    break;
                case LD_LOC:
                    top ++;
                    stack[top] = locals[op->a];
                    break;
                case ST_LOC:
                    locals[op->a] = stack[top];
                    top--;
                    break;
                case ADD: {
                    int a = stack[top];
                    top--;
                    int b = stack[top];
                    stack[top] = a + b;
                    break;
                }

                case MUL: {
                    int a = stack[top];
                    top--;
                    int b = stack[top];
                    stack[top] = a * b;
                    break;
                }
                case OP_START:
                    break;
                case EOP:
                    top = 0;
                    return;
            }

            op++;
        }
    }
}

#define DISPATCH(op) op++; goto *opcode_targets[op->code];
#define TARGET(opname) TARGET_##opname:

void gotoFunc(Runtime *rt) {
    OpCode* op = rt->opcodes;
    int *locals = rt->locals;
    int *stack  = rt->stack;
    int top = 0;
    int loops = rt->loops;
    
    // instructions count
    int count = 5;

    // 参考Python源码的
    static void *opcode_targets[] = {
        &&TARGET_OP_START,
        &&TARGET_LD_NUM,
        &&TARGET_LD_LOC,
        &&TARGET_ST_LOC,
        &&TARGET_ADD,
        &&TARGET_MUL,
        &&TARGET_RET,
        &&TARGET_EOP
    };

    for (int i = 0; i < loops; i++) {
        top = 0;
        while (true) {
            TARGET(OP_START)
                DISPATCH(op)

            TARGET(LD_NUM)
                top ++;
                stack[top] = op->a;
                DISPATCH(op);
            
            TARGET(LD_LOC)
                top ++;
                stack[top] = locals[op->a];
                DISPATCH(op);

            TARGET(ST_LOC)
                locals[op->a] = stack[top];
                top--;
                DISPATCH(op);

            TARGET(ADD) {
                int a = stack[top];
                top--;
                int b = stack[top];
                stack[top] = a + b;
                DISPATCH(op);
            }

            TARGET(MUL) {
                int a = stack[top];
                top--;
                int b = stack[top];
                stack[top] = a * b;
                DISPATCH(op);
            }

            TARGET(RET) {
                DISPATCH(op);
            }

            TARGET(EOP)
                top = 0;
                return;
        }
    }
}

void timeit(Func func, void* ctx) {
    int t1 = clock();
    func(ctx);
    int t2 = clock();

    double cost_time = (double)(t2-t1) / CLOCKS_PER_SEC * 1000.0f;
    printf("cost_time:%lfms\n", cost_time);
}

int main(int argc, char* argv[]) {
    Runtime rt;
    OpCode opcodes[] = {
        {OP_START, 0},
        {LD_NUM, 3}, 
        {LD_NUM, 4},
        {MUL, 0},
        {ST_LOC, 0},
        {EOP, 0}
    };

    int locals[] = {1,2,3,4,5,6,7,8,9};
    int stack[] = {0,0,0,0,0};

    rt.opcodes = opcodes;
    rt.locals = locals;
    rt.stack =  stack;
    rt.loops = N;

    printf("Run switchFunc\n");
    timeit(switchFunc, &rt);

    printf("Run gotoFunc\n");
    timeit(gotoFunc, &rt);
    return 0;
}