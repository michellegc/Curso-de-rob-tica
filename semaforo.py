from pyfirmata import Arduino;
import time

board = Arduino("COM4")
rojo = board.get_pin('d:13:o')
amarillo = board.get_pin('d:12:o')
verde = board.get_pin('d:11:o')



rojo.write(1)
time.sleep(5)
amarillo.write(1)
time.sleep(5)
verde.write(1)
time.sleep(5)