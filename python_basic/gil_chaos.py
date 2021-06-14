import threading

x = 0  # globally shared value


def abraham():
    global x
    for i in range(100000000):
        x += 1


def bobby():
    global x
    for i in range(100000000):
        x -= 1


t1 = threading.Thread(target=abraham)
t2 = threading.Thread(target=bobby)
t1.start()
t2.start()
t1.join()
t2.join()

print(x)
