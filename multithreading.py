from threading import Thread

from expensive_task import an_expensive_task


def main():
    threads = [Thread(target=an_expensive_task) for i in range(12)]

    for t in threads:
        t.start()

    threads[0].join()


if __name__ == '__main__':
    main()
