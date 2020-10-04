#!/usr/bin/env python3
from sched import scheduler

f_bb = 0.8  # rychlost 500 Hz


# class SObvod:
#     def __init__(self):
#         #proměnné třídy
#     def run():
#         #obsah metody

class BreadBoard:
    def inp(self, X):
        return bool(int(input(X)))

    def run(self, s, t):
        try:
            # logické funkce, volání metod
            print("ahoj")
        except:
            pass
        finally:
            s.enter(t, 1, bb.run, (s, t))


bb = BreadBoard()
s = scheduler()
s.enter(1 / f_bb, 1, bb.run, (s, 1 / f_bb))
# další zaplánované úlohy
s.run()
