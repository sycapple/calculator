import inspect
import linecache

def func():
    print("开始执行func函数")
    for i in range(10):
        frame = inspect.currentframe()
        line = linecache.getline(frame.f_code.co_filename, frame.f_lineno)
        print(f"正在执行第{frame.f_lineno}行，代码为：{line.strip()}")
        # 模拟耗时操作
        for j in range(1000000):
            pass
        print(frame.f_lineno)
    print("结束执行func函数")

func()