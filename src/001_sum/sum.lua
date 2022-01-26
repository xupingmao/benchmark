
function timeit( func )
    local t1 = os.clock()
    func()
    local t2 = os.clock()
    cost_time = (t2-t1) * 1000.0
    print("cost_time:" .. cost_time .. "ms")
end

function sum()
    local N = 500000
    local result = 0
    for i = 0,N-1 do
        result = result + i
    end

    print("result="..result)
end

timeit(sum)