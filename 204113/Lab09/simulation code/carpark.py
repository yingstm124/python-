import simpy
#สร้างข้อมูลจำลองการจอดรถและขับรถออกในช่วง 15 หน่วยเวลา
def car(env):
     while True:
         print('Start parking at %d' % env.now)
         parking_duration = 5
         yield env.timeout(parking_duration)
         print('Start driving at %d' % env.now)
         trip_duration = 2
         yield env.timeout(trip_duration)

if __name__ == '__main__':
    env = simpy.Environment()
    env.process(car(env))
    #start the simulation and passing an end time
    env.run(until=60)