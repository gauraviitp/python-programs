import threading

# Below code simulates printing in tandem.
#

semA = threading.Semaphore()
semB = threading.Semaphore()

semB.acquire()


def fooA():
    count = 20
    while count >= 0:
        semA.acquire()
        print('A')
        semB.release()

        count -= 1


def fooB():
    count = 20
    while count >= 0:
        semB.acquire()
        print('B')
        semA.release()

        count -= 1


t = threading.Thread(target=fooA)
t.start()
t2 = threading.Thread(target=fooB)
t2.start()
