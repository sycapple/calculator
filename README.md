# 超级计算机

## 待完成的功能

1. [ ]  编写一个科学计算器程序。可以完成加、减、乘、除（运用strategy pattern调用不同算法）、平方、平方根、立方、立方根以及其他（可自行添加）的运算。所有计算代码自行编写（运用adatper pattern调用库）。
2. [ ]  扩展计算器程序，可接受大数（指长度为2个或以上int或double的数）输入；并对大数进行加法、减法、乘法运算（运用bridge pattern/strategy pattern）。
3. [ ]  扩展计算器程序，可用十进制、二进制、十六进制三种方式对计算结果进行显示（运用observer pattern）。

## 已完成功能

* 计算器的主体编写

## 老计算机的介绍

老计算机分为两个部分，分别是测试用例生成和计算器本体，测试用例的部分很简单，这里不以阐述，主要是解释计算器本体的部分

主要思想其实是管道过滤器，就是给定一个字符串表达式以后一步步拆解

```python
def calculate(expression):
    try:
        # 去除空格
        expression = expression.replace(' ', '')
        # 统一符号
        expression = filter_minus(expression)
        # 计算括号
        expression = parenthesis(expression)
        # 平方
        expression = square(expression)
        # 乘除
        expression = multiply_divide(expression)
        # # 加减
        expression = and_minus(expression)
        # 输出结果
        return eval(expression)

```

这个就是主要的函数，可以看到算式在进入计算器之后经历了以下几个流程

* 去除空格
* 统一加减法符号，将-+和+-改为-
* 首先计算括号内的
* 计算平方
* 计算乘除法
* 计算加减法
* 输出结果

想要将这个计算器加以改造的话，其实只需要该里面的平方，乘除和加减的函数就可以了，下面我会以乘除的函数为例，解释一下字符串转变为数据的过程

---

```python
def multiply_divide(expression):
    try:
        while '*' in expression or '/' in expression:
            op_index = min(expression.find('*') if expression.find('*') > 0 else 999,
                           expression.find('/') if expression.find('/') > 0 else 999)
            op = expression[op_index]
            start = op_index - 1
            while start > 0 and expression[start].isdigit():
                start -= 1
                if start == 0:
                    break
                if expression[start] == '.':
                    start -= 1
            end = op_index + 1
            end = end + 1 if expression[end] == '-' else end
            while end < len(expression) and expression[end].isdigit():
                end += 1
                if end == len(expression):
                    break
                if expression[end] == '.':
                    end += 1
            if op == '*':
                result = "{0:.6f}".format(
                    eval(expression[start:op_index] if start == 0 else expression[start + 1:op_index]) * eval(
                        expression[op_index + 1:end]))
            else:
                result = "{0:.6f}".format(
                    eval(expression[start:op_index] if start == 0 else expression[start + 1:op_index]) / eval(
                        expression[op_index + 1:end]))
            if start == 0:
                font = expression[:start] + result
            else:
                font = expression[:start + 1] + result
            if end < len(expression) - 1:
                expression = font + expression[end:]
            else:
                expression = font
            expression = filter_minus(expression)
        return expression
    except Exception as e:
        raise CalculationError(f"{e}")

```

在这个函数中主要经历以下步骤

* 输入形如`3*2`的算式
* 检测里面是否有乘除号
* 找到第一个操作符，索引记为`op`
* 从`op`开始向前找确定数字1
* 从`op`开始向后找确定数字2
* 计算

其他的函数也是大同小异，也就是说，想要改造大数计算只需要改造最后一步计算即可，改造进制转换则是放在`calculate`函数里
