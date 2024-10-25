# 作业二 Python变量和列表

- 班级： 22物联1班

- 学号： B20220305131

- 姓名： 黄志宇

---

## 第1题：求离整数n最近的平方数（Find Nearest square number）

难度：8kyu

你的任务是找到一个正整数n的最近的平方数
例如，如果n=111，那么nearest_sq(n)（nearestSq(n)）等于121，因为111比100（10的平方）更接近121（11的平方）。
如果n已经是完全平方（例如n=144，n=81，等等），你需要直接返回n。
代码验证地址
<https://www.codewars.com/kata/5a805d8cafa10f8b930005ba>

```python
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
```

## 第2题：偶数或者奇数（Even or Odd）

难度：8kyu

创建一个函数接收一个整数作为参数，当整数为偶数时返回”Even”当整数为奇数时返回”Odd”。
代码验证地址：
<https://www.codewars.com/kata/53da3dbb4a5168369a0000fe>

```python
def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
```

## 第三题：括号匹配（Valid Braces）

难度：6kyu

写一个函数，接收一串括号，并确定括号的顺序是否有效。如果字符串是有效的，它应该返回True，如果是无效的，它应该返回False。
例如：

```python
"(){}[]" => True 
"([{}])" => True
 "(}" => False
 "[(])" => False 
"[({})](]" => False
```

**提示：
python中没有内置堆栈数据结构，可以直接使用`list`来作为堆栈，其中`append`方法用于入栈，`pop`方法可以出栈。**

代码验证地址
<https://www.codewars.com/kata/5277c8a221e209d3f6000b56>

```python
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
```
