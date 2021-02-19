import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)                    #pregatirea placii

TRIG = 23                              ##macro-uri
ECHO = 24
LED = 25

print("Masurarea distantei in desfasurare")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
def calcul_distanta():
  GPIO.output(TRIG, False)
  GPIO.output(LED, False)
  print("Se asteapta 3 secunde pentru calibrarea senzorului")
  time.sleep(3)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)  ##10 us
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance=pulse_duration * 17150
  distance=round( distance, 2)

  if distance > 2 and distance < 400:
    print("Distanta este de :",distance - 0.5,"cm")
    GPIO.output(LED, True)
    time.sleep(1)
    return distance
  else:
    print("In afara razei")

GPIO.cleanup