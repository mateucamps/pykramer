import serial
import sys
import argparse
from kramer import paquet

parser = argparse.ArgumentParser()
parser.add_argument('-p', type=str, help="Device serial port (ex. COM3)", required=True)
parser.add_argument('-i', type=int,  help="Input channel", required=True)
parser.add_argument('-o', type=int,  help="Output channel", required=True)

args = parser.parse_args()

ser = serial.Serial(args.p, 9600)
print('Port: ' + ser.name)
print('Baud: ' + str(9600))

cmd = paquet(args.i, args.o)
nbytes = ser.write(cmd)

print('Input: ' + str(args.i))
print('Output: ' + str(args.o))

print('Bytes written: ' + str(nbytes))
ser.close()
