from OOPDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.first_num + self.addition()


obj = ChildImpl()
print(obj.getCompleteData())
