import concrete_Calculate
import Implemental


class Algorithm:
    '''策略接口
       定义了算法的接口，具体的策略类需要实现这个接口
    '''

    def do_operation(self, expression):
        pass


class Addition(Algorithm):
    '''加法策略'''

    def do_operation(self, expression):
        return concrete_Calculate.and_minus(expression)


class Subtract(Algorithm):
    '''减法策略'''

    def do_operation(self, expression):
        return concrete_Calculate.and_minus(expression)


class Multiply(Algorithm):
    '''乘法策略'''

    def do_operation(self, expression):
        return concrete_Calculate.multiply_divide(expression)


class Divide(Algorithm):
    '''乘法策略'''

    def do_operation(self, expression):
        return concrete_Calculate.multiply_divide(expression)


class Square(Algorithm):
    '''次方策略'''

    def do_operation(self, expression):
        return concrete_Calculate.square(expression)


class Caculator:
    '''策略上下文
       持有一个策略类的引用，并且在需要时调用策略类中的算法。
    '''

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def execute_algorithm(self, expression):
        return self.algorithm.do_operation(expression)


def main(expression):
    '''使用示例'''
    try:
        # 去除空格
        expression = expression.replace(' ', '')
        # 统一符号
        expression = concrete_Calculate.filter_minus(expression)
        # 判断是否为大数

        if '+' in expression:
            # 加法
            algorithm = Addition()
        elif '-' in expression:
            # 减法
            algorithm = Subtract()
        elif '*' in expression:
            # 乘法
            algorithm = Multiply()
        elif '/' in expression:
            # 除法
            algorithm = Divide()
        elif '^' in expression:
            # 次方
            algorithm = Square()
        # 通过上下文引用计算结果并输出
        context = Caculator(algorithm)
        result = context.execute_algorithm(expression)
        print(expression + f" = {result}")
        # Implemental.main(result)

    except Exception as e:
        raise main.CalculationError(f"{e}")

    return result
