from pyfirmata import Arduino
import time 
board = Arduino("COM7")
led_r = board.get_pin('d:13:o')
led_a = board.get_pin('d:12:o')
led_v = board.get_pin('d:11:o')


while True:
    led_r.write(1)
    time.sleep(5)
    led_r.write(0)
    
    led_v.write(1)
    time.sleep(5)
    led_v.write(0)
 
    
    led_a.write(1)
    time.sleep(1)
    led_a.write(0)
    time.sleep(1)
    led_a.write(1)
    time.sleep(1)
    led_a.write(0)
    time.sleep(1)
    led_a.write(1)
    time.sleep(1)
    led_a.write(0)
    
    