from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from serial import Serial

class MyComponent(ApplicationSession):
   @inlineCallbacks
   def onJoin(self, details):
      print "Starting..."
      with Serial("/dev/ttyACM0", 9600) as arduino:
         print "Connected to arduino"
         while True:
            val = arduino.readline()
            try:
               yield self.publish(u'com.java.factory.on_arduino_value', val)
               print val
            except Exception as e:
               print("call error: {0}".format(e))

if __name__ == '__main__':
   runner = ApplicationRunner(url =u"ws://localhost:8080/ws", realm=u"realm1")
   runner.run(MyComponent)