def valid_braces(s):
    """确定括号的顺序是否有效"""
    
    #用于存储左括号
    stack = []
    
    #存储右括号与左括号的配对关系
    matching_braces = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    #遍历输入字符串 s
    for char in s:
        #左括号将其加入到 stack
        if char in matching_braces.values():
            stack.append(char)
        #右括号则检查 stack 的顶部是否有匹配的左括号
        elif char in matching_braces:
            if stack and stack[-1] == matching_braces[char]:
                stack.pop()
            else:
                return False
     
    #最后检查 stack 是否为空     
    return not stack