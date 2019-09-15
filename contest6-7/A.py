import sys


class ExtendedList(list):

    def __init__(self, my_list):
        super().__init__(my_list)
        self.my_list = super().__self__

    @property
    def reversed(self):
        return list(reversed(self.my_list))

    R = reversed

    @property
    def size(self):
        return len(self.my_list)

    @size.setter
    def size(self, value):
        if value < len(self.my_list):
            new_my_list = self.my_list[:value]
            self.__init__(new_my_list)
        else:
            new_my_list = self.my_list
            for i in range(value - len(self.my_list)):
                new_my_list.append(None)

    S = size

    @property
    def first(self):
        return self.my_list[0]

    @first.setter
    def first(self, value):
        self.my_list[0] = value

    F = first

    @property
    def last(self):
        return self.my_list[len(self.my_list) - 1]

    @last.setter
    def last(self, value):
        self.my_list[len(self.my_list) - 1] = value

    L = last


exec(sys.stdin.read())
