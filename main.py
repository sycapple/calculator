import csv


class CalculationError(Exception):
    pass


def karatsuba(num1, num2):
    num1Str, num2Str = str(num1), str(num2)
    if int(num1) != num1:
        num1f = '0.' + num1Str.split('.')[1]
        num1Str = num1Str.split('.')[0]
    else:
        num1f = '0'
    if int(num2) != num2:
        num2f = '0.' + num2Str.split('.')[1]
        num2Str = num2Str.split('.')[0]
    else:
        num2f = '0'
    if num1Str[0] == '-': return -karatsuba(-num1, num2)
    if num2Str[0] == '-': return -karatsuba(num1, -num2)

    if num1 < 10 or num2 < 10: return num1 * num2

    maxLength = max(len(num1Str), len(num2Str))
    num1Str = ''.join(list('0' * maxLength)[:-len(num1Str)] + list(num1Str))
    num2Str = ''.join(list('0' * maxLength)[:-len(num2Str)] + list(num2Str))

    splitPosition = maxLength // 2
    high1, low1 = int(num1Str[:-splitPosition]), int(num1Str[-splitPosition:])
    high2, low2 = int(num2Str[:-splitPosition]), int(num2Str[-splitPosition:])
    z0, z2 = karatsuba(low1, low2), karatsuba(high1, high2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    return z2 * 10 ** (2 * splitPosition) + (z1 - z2 - z0) * 10 ** (splitPosition) + z0 + eval(num1f) * eval(num2f)


def Add_large_numbers(num1, num2):
    output = ''
    num1Str, num2Str = str(num1), str(num2)
    precision1, precision2 = 0, 0
    if '.' in num1Str: precision1 = len(num1Str) - num1Str.find('.') - 1
    if '.' in num2Str: precision2 = len(num2Str) - num2Str.find('.') - 1
    max_precision = max(precision1, precision2)
    if precision1 != 0:
        num1Str = num1Str + '0' * (max_precision - precision1)
    else:
        num1Str = num1Str + '.' + '0' * (max_precision - precision1 - 1)
    if precision2 != 0:
        num2Str = num2Str + '0' * (max_precision - precision2)
    else:
        num2Str = num2Str + '.' + '0' * (max_precision - precision2 - 1)
    length1, length2 = len(num1Str), len(num2Str)
    carry = 0
    min_length = min(length1, length2)
    for i in range(min_length):
        i = -(i + 1)
        if num1Str[i] == '.':
            output = '.' + output
            continue
        result = str((eval(num1Str[i]) + eval(num2Str[i]) + carry) % 10)
        carry = (eval(num1Str[i]) + eval(num2Str[i]) + carry) // 10
        output = result + output
    if length1 < length2:
        longer_num = num2Str
    else:
        longer_num = num1Str
    font_num = longer_num[:-min_length]
    if font_num:
        output = font_num[:-1] + str(eval(font_num[-1]) + carry) + output
    return output


def mine_large_numbers(num1, num2):
    output = ''
    num1Str, num2Str = str(num1), str(num2)
    precision1, precision2 = 0, 0
    if '.' in num1Str: precision1 = len(num1Str) - num1Str.find('.') - 1
    if '.' in num2Str: precision2 = len(num2Str) - num2Str.find('.') - 1
    max_precision = max(precision1, precision2)
    if precision1 != 0:
        num1Str = num1Str + '0' * (max_precision - precision1)
    else:
        num1Str = num1Str + '.' + '0' * (max_precision - precision1 - 1)
    if precision2 != 0:
        num2Str = num2Str + '0' * (max_precision - precision2)
    else:
        num2Str = num2Str + '.' + '0' * (max_precision - precision2 - 1)
    length1, length2 = len(num1Str), len(num2Str)
    carry = 0
    min_length = min(length1, length2)
    flag = 0
    if length1 == length2:
        for i in range(min_length):
            if num1Str[i] == '.':
                continue
            if eval(num1Str[i]) < eval(num2Str[i]):
                flag = -1
    if flag == -1 or length1 < length2:
        flag = -1
        mid = num1Str
        num1Str = num2Str
        num2Str = mid
        length1 = length1 + length2
        length2 = length1 - length2
        length1 = length1 - length2
    for i in range(min_length):
        i = -(i + 1)
        if num1Str[i] == '.':
            output = '.' + output
            continue
        result = str((eval(num1Str[i]) - eval(num2Str[i]) + carry + 10) % 10)
        carry = (lambda a: 0 if a >= 0 else -1)(eval(num1Str[i]) - eval(num2Str[i]) + carry)
        output = result + output
    if length1 < length2:
        longer_num = num2Str
    else:
        longer_num = num1Str
    font_num = longer_num[:-min_length]
    if font_num:
        for i in range(len(font_num)):
            result = str((eval(font_num[i]) + carry + 10) % 10)
            carry = (lambda a: 0 if a >= 0 else -1)(eval(font_num[i]) + carry)
            output = result + output
    if flag == -1:
        output = '-' + output
    return output


def and_minus(expression):
    try:
        while '+' in expression or '-' in expression[1:]:
            op_index = min(expression[1:].find('+') if expression[1:].find('+') != -1 else 999,
                           expression[1:].find('-') if expression[1:].find('-') != -1 else 999) + 1
            op = expression[op_index]
            start = op_index - 1
            while start > 0 and expression[start].isdigit():
                start -= 1
                if start == 0:
                    break
                if expression[start] == '.':
                    start -= 1
            end = op_index + 1
            while end < len(expression) and expression[end].isdigit():
                end += 1
                if end == len(expression):
                    break
                if expression[end] == '.':
                    end += 1
            if op == '+':
                result = str("{0:.6f}".format(
                    Add_large_numbers(eval(expression[start:op_index]), eval(expression[op_index + 1:end]))))
            else:
                result = str("{0:.6f}".format(
                    mine_large_numbers(eval(expression[start:op_index]), eval(expression[op_index + 1:end]))))
            if start == 0:
                font = expression[:start] + result
            else:
                font = expression[:start + 1] + result
            if end < len(expression) - 1:
                expression = font + expression[end:]
            else:
                expression = font
        return expression
    except Exception as e:
        raise CalculationError(f"{e}")


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
                    karatsuba(eval(expression[start:op_index] if start == 0 else expression[start + 1:op_index]), eval(
                        expression[op_index + 1:end])))
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


def square(expression):
    try:
        while '^' in expression:
            op_index = expression.find('^')
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
            result = "{0:.6f}".format(
                eval(expression[start:op_index] if start == 0 else expression[start + 1:op_index]) ** eval(
                    expression[op_index + 1:end])
            )
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


def parenthesis(expression):
    try:
        while '(' in expression:
            start = expression.rfind('(')
            end = expression.find(')', start)
            result = calculate(expression[start + 1: end])
            expression = expression[:start] + str(result) + expression[end + 1:]
        return expression
    except Exception as e:
        raise CalculationError(f"Error occurred when calculating {expression}: {e}")


def filter_minus(expression):
    try:
        expression = expression.replace('+-', '-')
        expression = expression.replace('-+', '-')
        return expression
    except Exception as e:
        raise CalculationError(f"{e}")


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
    except Exception as e:
        raise CalculationError(f"{e}")


if __name__ == '__main__':
    print(calculate('6123949.3*9280.7'))
