import RPi.GPIO as GPIO 
from time import sleep 
import math
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)

int=int(input('n='))
rest=''
vector=[0,1,2,3,4,5,6,7]

for x in range (8):
    r=int%2
    int=int//2
    rest+=str(r)
    vector[x]=r
    
rest=rest[::-1]
print(rest)

if vector[7]==1:
    GPIO.output(12, GPIO.HIGH)
else:
    GPIO.output(12, GPIO.LOW)
    
if vector[6]==1:
    GPIO.output(16, GPIO.HIGH)
else:
    GPIO.output(16, GPIO.LOW)
    
if vector[5]==1:
    GPIO.output(18, GPIO.HIGH)
else:
    GPIO.output(18, GPIO.LOW)
    
if vector[4]==1:
    GPIO.output(22, GPIO.HIGH)
else:
    GPIO.output(22, GPIO.LOW)
    
if vector[3]==1:
    GPIO.output(24, GPIO.HIGH)
else:
    GPIO.output(24, GPIO.LOW)
    
if vector[2]==1:
    GPIO.output(26, GPIO.HIGH)
else:
    GPIO.output(26, GPIO.LOW)
    
if vector[1]==1:
    GPIO.output(32, GPIO.HIGH)
else:
    GPIO.output(32, GPIO.LOW)
    
if vector[0]==1:
    GPIO.output(36, GPIO.HIGH)
else:
    GPIO.output(36, GPIO.LOW)

    
sleep(15)
GPIO.output(12, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(26, GPIO.LOW)
GPIO.output(32, GPIO.LOW)
GPIO.output(36, GPIO.LOW)



