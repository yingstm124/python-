#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 09
# Problem 4
# 204113 Sec 001

import simpy

def Bank_Teller(env):
     while True:
         print('Deposit %d' % env.now)
         depositing_duration = 3
         yield env.timeout(depositing_duration)
         print('Withdraw %d' % env.now)
         withdraw_duration = 5
         yield env.timeout(withdraw_duration)

if __name__ == '__main__':
    env = simpy.Environment()
    env.process(Bank_Teller(env))
    env.run(until=60)