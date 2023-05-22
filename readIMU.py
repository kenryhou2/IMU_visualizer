import serial
import time
s = serial.Serial('COM4')
t2 = time.time()

freq = 0
while 1:
    t1 = time.time()
    res = s.readline()
    freq = 1/(t1-t2)
    print(res.decode() + ", Frequency: " + str(freq))
    t2 = t1
