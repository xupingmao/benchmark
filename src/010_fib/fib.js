
function fib(n) {
    if (n == 1 || n == 2) {
        return 1;
    }
    return fib(n-1) + fib(n-2)
}


function timeit(funcName, func, args) {
    var t1 = new Date().getTime();
    var result = func.apply(this, args)
    var t2 = new Date().getTime();
    console.log(funcName + "(" + args + ")=" + result);
    console.log("cost", t2-t1, "ms");
}

timeit("fib", fib, [30]);
