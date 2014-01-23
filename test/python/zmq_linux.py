#!/usr/bin/python
from  topology import *
import zmq
import sys
import random

#T = Topology()
#net1 = Network(T, "pyt0")

#h1 = Host(T, net1)
#h2 = Host(T, net1, args="zeromq_prod:")

sleep(1)
raw_input("Press enter to continue ...")
#start(T)

# Zeromq publisher
ctx = zmq.Context()
z = ctx.socket(zmq.PUB)

z.bind("tcp://*:1337")

while True: 
	messagedata = "Hello world!Thhe addition of security mechanisms, the removal of hard-coded connection metadata (socket type and identity) from the greeting, the addition of connection metadata, the addition of commands, and the addition of heartbeating.azertyuiopsdfghjkl"
	print "%d" % len(messagedata)
	print "%s" % (messagedata)
	z.send("%s" % (messagedata))
	time.sleep(1)

# Zeromq part
ctx = zmq.Context()
z = ctx.socket(zmq.SUB)
z.setsockopt(zmq.SUBSCRIBE, "")
z.connect("tcp://169.254.22.5:1337")
print "In the loop..."
while 1:
  if z.poll(20000) == 0:
    print "Timeout!!!"
    cleanup()
    sys.exit(1)
  else:
    msg = z.recv()
    print "Recvd msg len=%d content: %s" % (len(msg), msg)
  sleep(1)



cleanup()
