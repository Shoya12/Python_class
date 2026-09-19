class Engine:
    def start(self):
        print('Engine started')

class Car:
    def drive(self,engine):
        engine.start()
        print('Car is moving')

e=Engine()
c=Car()
c.drive(e)