# 测试环境

```
MacBook Air (13-inch, Early 2015)
1.6 GHz 双核Intel Core i5
4 GB 1600 MHz DDR3
测试时间: 2022/03/16
```

# 测试结果


## leveldb

测试项目 | 测试次数 | 平均QPS
------- | -------|-------
Put     | 100    | 534.17
Put     | 1000   | 673.38
Put     | 10000  | 659.31
Get     | 100    | 13246.57
Get     | 1000   | 20564.46
Get     | 10000  | 22823.50


```
# No.1
Test insert (100) times, cost (189.95)ms, qps (526.46)
Test insert mem (9.47M)->(9.73M)
Test insert (1000) times, cost (1477.11)ms, qps (677.00)
Test insert mem (9.73M)->(11.08M)
Test insert (10000) times, cost (14607.33)ms, qps (684.59)
Test insert mem (11.08M)->(16.04M)
Test query (100) times, cost (9.64)ms, qps (10375.78)
Test query mem (16.04M)->(16.11M)
Test query (1000) times, cost (41.16)ms, qps (24293.68)
Test query mem (16.11M)->(16.11M)
Test query (10000) times, cost (406.02)ms, qps (24629.56)
Test query mem (16.11M)->(16.11M)

# No.2
Test insert (100) times, cost (236.52)ms, qps (422.80)
Test insert mem (9.42M)->(9.71M)
Test insert (1000) times, cost (1449.48)ms, qps (689.90)
Test insert mem (9.71M)->(11.07M)
Test insert (10000) times, cost (15240.08)ms, qps (656.16)
Test insert mem (11.07M)->(16.73M)
Test query (100) times, cost (5.53)ms, qps (18085.91)
Test query mem (16.73M)->(16.94M)
Test query (1000) times, cost (43.68)ms, qps (22894.80)
Test query mem (16.94M)->(16.94M)
Test query (10000) times, cost (364.07)ms, qps (27467.02)
Test query mem (16.94M)->(16.95M)

No.3
Test insert (100) times, cost (153.08)ms, qps (653.25)
Test insert mem (9.46M)->(9.72M)
Test insert (1000) times, cost (1763.82)ms, qps (566.95)
Test insert mem (9.72M)->(11.09M)
Test insert (10000) times, cost (15694.02)ms, qps (637.19)
Test insert mem (11.09M)->(16.16M)
Test query (100) times, cost (8.87)ms, qps (11278.04)
Test query mem (16.16M)->(16.45M)
Test query (1000) times, cost (68.94)ms, qps (14504.93)
Test query mem (16.45M)->(16.45M)
Test query (10000) times, cost (610.73)ms, qps (16373.93)
Test query mem (16.45M)->(16.45M)
```


## sqlite

测试项目 | 测试次数 | 平均QPS
------- | -------|-------
Insert  | 100    | 188.95
Insert  | 1000   | 183.88
Insert  | 10000  | 181.51
Select  | 100    | 11062.84
Select  | 1000   | 15450.56
Select  | 10000  | 16399.47


```
# No.1
Test insert (100) times, cost (496.17)ms, qps (201.54)
Test insert mem (9.46M)->(10.34M)
Test insert (1000) times, cost (5261.84)ms, qps (190.05)
Test insert mem (10.34M)->(11.75M)
Test insert (10000) times, cost (56969.19)ms, qps (175.53)
Test insert mem (11.75M)->(12.43M)
Test query (100) times, cost (8.47)ms, qps (11800.65)
Test query mem (12.43M)->(12.45M)
Test query (1000) times, cost (89.83)ms, qps (11131.65)
Test query mem (12.45M)->(12.45M)
Test query (10000) times, cost (656.11)ms, qps (15241.30)
Test query mem (12.45M)->(12.45M)

# No.2
Test insert (100) times, cost (537.62)ms, qps (186.00)
Test insert mem (9.46M)->(10.36M)
Test insert (1000) times, cost (5496.49)ms, qps (181.93)
Test insert mem (10.36M)->(11.74M)
Test insert (10000) times, cost (54517.91)ms, qps (183.43)
Test insert mem (11.74M)->(9.94M)
Test query (100) times, cost (9.29)ms, qps (10764.01)
Test query mem (9.98M)->(10.02M)
Test query (1000) times, cost (47.21)ms, qps (21180.57)
Test query mem (10.02M)->(10.03M)
Test query (10000) times, cost (608.47)ms, qps (16434.66)
Test query mem (10.03M)->(10.08M)

# No.3
Test insert (100) times, cost (557.64)ms, qps (179.33)
Test insert mem (9.47M)->(10.35M)
Test insert (1000) times, cost (5565.71)ms, qps (179.67)
Test insert mem (10.35M)->(11.77M)
Test insert (10000) times, cost (53886.63)ms, qps (185.57)
Test insert mem (11.77M)->(12.45M)
Test query (100) times, cost (9.41)ms, qps (10623.87)
Test query mem (12.45M)->(12.46M)
Test query (1000) times, cost (71.23)ms, qps (14039.46)
Test query mem (12.46M)->(12.46M)
Test query (10000) times, cost (570.70)ms, qps (17522.47)
Test query mem (12.46M)->(12.47M)
```