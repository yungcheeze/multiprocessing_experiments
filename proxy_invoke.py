import typing
from multiprocessing import Manager, Process
from multiprocessing.managers import BaseManager
from time import sleep


class Stuff:
    def __init__(self):
        self.values = [1, 2, 3, 4]


class MyComplexObject:
    def __init__(self):
        self._my_stuff = Stuff()

    def get_my_stuff(self):
        return self._my_stuff.values

    def update_my_stuff(self, value):
        self._my_stuff.values.append(value)


def update_stuff_forever(complex_object):
    n = 5
    while True:
        complex_object.update_my_stuff(n)
        n += 1
        sleep(0.5)


class MyManager(BaseManager):
    pass


MyManager.register("MyComplexObject", MyComplexObject)


def main():
    manager = MyManager()
    manager.start()

    complex_object = manager.MyComplexObject()
    job = Process(target=update_stuff_forever, args=(complex_object, ))
    job.start()

    while True:
        print(complex_object.get_my_stuff())
        sleep(1)


if __name__ == '__main__':
    main()
