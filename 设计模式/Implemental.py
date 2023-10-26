import Algorithm


class Subject(object):
    '''主题类。
       保存所有观察者实例的引用，
       每个主题都可以有很多观察者,可以增加和删除观察者
    '''

    def __init__(self):
        self.obs = []

    def Attach(self, ob):
        self.obs.append(ob)

    def Detach(self, ob):
        self.obs.remove(ob)

    def Notify(self):
        for ob in self.obs:
            ob.Update()


class Observer(object):
    '''抽象观察者类。
       当主题发生变化时通知它
    '''

    def __init__(self, subject):
        self.subject = subject
        subject.Attach(self)

    def Update(self):
        pass


class Data(Subject):
    '''具体的主题
       设置所需修改实现功能
    '''

    def __init__(self):
        self.data = None
        Subject.__init__(self)

    def __str__(self):
        return "Decimal String: {}".format(self.GetState())

    # 修改更新数据
    def ChangeState(self, newValue):
        self.data = newValue
        self.Notify()

    # 读数据
    def GetState(self):
        return self.data


class HexFormatter(Observer):
    '''十六进制具体观察者'''

    def Update(self):
        print("Hex String: " + hex(self.subject.GetState()))


class BinaryFormatter(Observer):
    '''二进制具体观察者'''

    def Update(self):
        print("Binary String: " + bin(self.subject.GetState()))


class BigNumFormatter(Observer):
    '''大数进制具体观察者'''

    def Update(self):
        print("BigNum String: " + BigNumFormatter(self.subject.GetState()))


def main():
    '''测试'''
    expression = input()
    df = Data()
    # print(df)
    # print()
    result = Algorithm.main(expression)
    hf = HexFormatter(df)
    bf = BinaryFormatter(df)
    df.ChangeState(int(float(result)))
    print(df)


if __name__ == '__main__':
    main()
