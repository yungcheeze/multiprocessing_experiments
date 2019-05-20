from multiprocessing import Manager, Process
from multiprocessing.managers import BaseManager
from time import sleep


class Stuff:
    def __init__(self):
        self.values = [1, 2, 3, 4]


class MyComplexObject:
    def __init__(self, listeners=[]):
        self._my_stuff = Stuff()
        self._listeners = listeners

    def get_my_stuff(self):
        return self._my_stuff.values

    def update_my_stuff(self, value):
        self._my_stuff.values.append(value)

    def notify_listeners(self):
        for listener in self._listeners:
            listener(self.get_my_stuff())


def update_stuff_forever(complex_object):
    n = 5
    while True:
        complex_object.update_my_stuff(n)
        complex_object.notify_listeners()
        n += 1
        sleep(0.5)


class MyManager(BaseManager):
    pass


MyManager.register("MyComplexObject", MyComplexObject)


def print_my_stuff(stuff):
    print("print_my_stuff():", stuff)


class ProxyListener:
    def __call__(self, stuff):
        print("ProxyListener:", stuff)


def main():
    manager = MyManager()
    manager.start()

    listener_obj = ProxyListener()
    complex_object = manager.MyComplexObject([print_my_stuff, listener_obj])
    job = Process(target=update_stuff_forever, args=(complex_object, ))
    job.start()

    while True:
        sleep(1)


if __name__ == '__main__':
    main()
