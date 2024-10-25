def nearest_sq(n):
    """计算n的平方根"""
    i = 1
    
    # 迭代找到大于或等于 n 的平方数
    while i * i < n:
        i += 1
        
    # 已经找到的平方数
    upper_sq = i * i
    lower_sq = (i - 1) * (i - 1)
    
    # 比较 n 与 upper_sq 和 lower_sq 之间的差距
    if abs(n - lower_sq) <= abs(n - upper_sq):
        return lower_sq
    else:
        return upper_sq