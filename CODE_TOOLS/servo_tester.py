import RPi.GPIO as GPIO
import time

servoPIN = 18 # der Servomotor wurde an den GPIO Pin 18 angeschlossen
# moegliche Servopositionen fuer dieses Beispiel
servoPositions = [2.5,5,7.5,10,12.5]

# Funktion zum setzen eines Winkels
# als Parameter wird die Position erwartet
def setServoCycle(p, position):
  p.ChangeDutyCycle(position)
  # eine Pause von 0,5 Sekunden
  time.sleep(0.5)

# versuche
try:
  # damit wir den GPIO Pin ueber die Nummer referenzieren koennen
  GPIO.setmode(GPIO.BCM)
  # setzen des GPIO Pins als Ausgang
  GPIO.setup(servoPIN, GPIO.OUT)

  p = GPIO.PWM(servoPIN, 50) # GPIO als PWM mit 50Hz
  p.start(servoPositions[0]) # Initialisierung mit dem ersten Wert aus unserer Liste

  # eine Endlos Schleife
  while True:
    # fuer jeden Wert in der Liste, mache...
    for pos in servoPositions:
      # setzen der Servopostion
      setServoCycle(p, pos)
      # durchlaufen der Liste  in umgekehrter Reihenfolge
    for pos in reversed(servoPositions):
      setServoCycle(p, pos)
# wenn das Script auf dem Terminal / der Konsole abgebrochen wird, dann...
except KeyboardInterrupt:
  p.stop()
  # alle Pins zuruecksetzen
  GPIO.cleanup()
