import csv


class CalculationError(Exception):
    pass


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
                result = str("{0:.6f}".format(eval(expression[start:op_index]) + eval(expression[op_index + 1:end])))
            else:
                result = str("{0:.6f}".format(eval(expression[start:op_index]) - eval(expression[op_index + 1:end])))
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
    print(calculate('6949.3/9280.7'))
