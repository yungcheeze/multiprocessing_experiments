import timeit


def an_expensive_task(repeat: int = 1):
    s = """for i in range(int(5e7)): pass """
    print(timeit.timeit(s, number=repeat))


def main():
    an_expensive_task()


if __name__ == '__main__':
    main()
