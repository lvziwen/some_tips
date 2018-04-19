from itertools import combinations
# 今天同事找我帮忙，左列数据中随意组合的合等于右列中的某个数
left = [9000,3692,9501,934,1284,15037,6468,2486,2307,7972,6481,4777,2229,7171,4753,981,2444.71]
right = [8485.85,22737.54,123785,7171,554,9011,22131,35062,26172,35632,29786,52234,19630,39880,24292]


len_l = len(left)
len_r = len(right)

i = 2
while i < len_l:
    comb_list = list(combinations(left, i))
    for item in comb_list:
        for r in right:
            if sum(item) == r:
                print item, r
    i += 1
    
