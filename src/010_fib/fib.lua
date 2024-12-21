local function fib(n)
    if n == 1 or n == 2 then
        return 1
    end
    return fib(n-1) + fib(n-2)
end


function timeit(func_name, func, ...)
    local t1 = os.clock()
    local ret = func(...)
    print(func_name .. "(" .. (...) .. ")" .. "=" .. ret)
    local t2 = os.clock()
    print("cost " .. (t2-t1)*1000 .. " ms")
end

timeit("fib", fib, 30)
