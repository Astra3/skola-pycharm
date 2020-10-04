from sched import scheduler

f_bb = 5
f_bb2 = 1
from time import sleep


def run(s, t):
    print("ahoj")
    s.enter(t, 1, run, (s, t))


def run2(s, t):
    print("čau")
    s.enter(t, 1, run2, (s, t))
    cerman.run(blocking=False)


cerman = scheduler()
# zluva = scheduler()

cerman.enter(1/f_bb, 1, run, (cerman, 1/f_bb))
cerman.enter(1/f_bb2, 2, run2, (cerman, 1/f_bb2))

# zluva.run()
cerman.run(blocking=False)
print("aaaaaa")
while True:
    sleep(.5)
