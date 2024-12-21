-- package.path = package.path .. ";../utils/?.lua"
local utils = require("src.utils.utils")

local rand_str = utils.rand_str
local timeit = utils.timeit
local len = utils.len

local function test_random_gen(n)
    print("test_random_gen: n=" .. n)
    for i = 1, n do
        rand_str(5)
    end
end

local function test_dict_set(n)
    print("test_dict_set: n=" .. n)
    local d = {}
    for i = 1, n do
        local key = utils.rand_str(5)
        d[key] = 1
    end

    print("len(dict)=" .. len(d))
end

local function test_dict_get(n)
    print("test_dict_get: n=" .. n)
    local d = {}
    for i = 1, n do
        local key = rand_str(5)
        d[key] = 1
    end
    print("len(dict)=" .. len(d))
end

timeit("test_random_gen", test_random_gen, 100000)
print("")
timeit("test_dict_set", test_dict_set, 100000)
print("")
timeit("test_dict_get", test_dict_get, 100000)
