###############################################################################
#
# Copyright (C) 2014, Tavendo GmbH and/or collaborators. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
###############################################################################

from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError


class AppSession(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):

        # subscribe to new value events
        def on_arduino_value(msg):
            print("Received new value " + msg)
            #yield self.publish("com.java.factory.new_value")

        yield self.register(on_arduino_value, 'com.java.factory.on_arduino_value')


        # REGISTER a procedure for remote calling
        #
        # def add2(x, y):
        #     print("add2() called with {} and {}".format(x, y))
        #     return x + y

        # reg = yield self.register(add2, 'com.example.add2')

        # PUBLISH an event
        
        # yield self.publish('com.example.oncounter', counter)
        # print("published to 'oncounter' with counter {}".format(counter))
        # counter += 1

        # CALL a remote procedure
        
        # try:
        #     res = yield self.call('com.example.mul2', counter, 3)
        #     print("mul2() called with result: {}".format(res))
        # except ApplicationError as e:
        #     # ignore errors due to the frontend not yet having
        #     # registered the procedure we would like to call
        #     if e.error != 'wamp.error.no_such_procedure':
        #         raise e


if __name__ == "__main__":
    runner = ApplicationRunner(url =u"ws://127.0.0.1:8080/ws", realm=u"realm1")
    runner.run(AppSession)