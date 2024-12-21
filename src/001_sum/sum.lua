local utils = require("src.utils.utils")
local timeit = utils.timeit


local function sum()
    local N = 500000
    local result = 0
    for i = 0,N-1 do
        result = result + i
    end

    print("result="..result)
end

timeit("sum", sum)