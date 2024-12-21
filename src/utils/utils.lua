
local module = {}

-- print("start load utils.lua ...")

module.timeit = function(func_name, func, ...)
    local t1 = os.clock()
    local ret = func(...)
    print(func_name .. "(" .. (...) .. ")" .. "=" .. tostring(ret))
    local t2 = os.clock()
    print("cost " .. (t2-t1)*1000 .. " ms")
end

math.randomseed(os.time())  -- 设置随机数种子，基于当前时间

-- 定义函数，参数n用于指定生成的随机字符串的长度
module.rand_str = function(n)
    local str = ""
    local char_table = {}
    -- 填充字符表，包含大小写字母和数字
    for i = string.byte('A'), string.byte('Z') do
        table.insert(char_table, string.char(i))
    end
    for i = 1, n do
        local random_index = math.random(#char_table)  -- 随机获取字符表中的索引
        str = str.. char_table[random_index]  -- 拼接字符
    end
    return str
end

module.len = function (t)
    local length = 0
    for _ in pairs(t) do
        length = length + 1
    end
    return length
end

-- for k,v in pairs(module) do
--     print(k,v)
-- end

return module
