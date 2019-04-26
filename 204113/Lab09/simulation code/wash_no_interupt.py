import simpy
class Car(object):
    def __init__(self, env):
    	self.env = env
    	self.action = env.process(self.run())
         #start the run process an instance is created.
    def run(self):
    	while True:
            print('Start parking and washing at %d' % self.env.now)
            wash_duration = 5
 
            yield self.env.process(self.wash(wash_duration))
 # We yield the process that returns to wait for it to finish.
 # The wash process has finished and we can start driving again.
            print('Start driving at %d' % self.env.now)
            trip_duration =  2
            yield self.env.timeout(trip_duration)

    def wash(self, duration):
            yield self.env.timeout(duration)



def main():
    env = simpy.Environment()
    car = Car(env) 
    car.run()
    env.run(until=60)

if __name__ == '__main__':
	main()
