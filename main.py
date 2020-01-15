import serial
import sys
import argparse
from kramer import paquet

parser = argparse.ArgumentParser()
parser.add_argument('-p', type=str, help="Port sèrie del dispositiu (ex. COM3)", required=True)
parser.add_argument('-b', type=int,  help="Baud rate (ex. 9600)", required=True)
parser.add_argument('-i', type=int,  help="Canal entrada", required=True)
parser.add_argument('-o', type=int,  help="Canal sortida", required=True)

args = parser.parse_args()

ser = serial.Serial(args.p, args.b)
print('Port: ' + ser.name)
print('Baud: ' + str(ser.baudrate))

cmd = paquet(args.i, args.o)
nbytes = ser.write(cmd)

print('Entrada: ' + str(args.i))
print('Sortida: ' + str(args.o))

print('Bytes escrits: ' + str(nbytes))
ser.close()
