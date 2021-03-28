from argparse import ArgumentParser
import serial

parser = ArgumentParser(description='Arguments')
parser.add_argument('--serial-port', type=str, help='Serial port')
parser.add_argument('--baudrate', type=int, help='Communication baudrate')
args = parser.parse_args()

ser = serial.Serial(port = args.serial_port, baudrate=args.baudrate)

while(ser.readline() != b'echo:SD card ok\n'):
    while(ser.readline() != b'echo:SD card ok\n'):
        pass

while True:
    sentence = input('Command: ')

    if(sentence == ''):
        ser.close()
        quit()
        
    ser.write(str.encode(sentence + '\n'))
    print(ser.readline())