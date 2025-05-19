# 递归实现（适用于小数据，效率较低）
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 迭代实现（效率更高）
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 示例调用
print(fib_iterative(10))  # 输出：55
