local utils = require("src.utils.utils")

local function fib(n)
    if n == 1 or n == 2 then
        return 1
    end
    return fib(n-1) + fib(n-2)
end


utils.timeit("fib", fib, 30)
