# GCODE CLI sender for marlin

Tested on Tevo Tornado with marlin 1.1.8

### 1 - Usage:

```
usage: cli.py [-h] [--serial-port] [--baudrate]

arguments:
  -h, --help
  --serial-port STRING
  --baudrates INT
```

### 2 - Examples:

##### Windows :

```
python main.py --serial-port COM4 --baudrate 250000
Command: M105
b'ok T:19.92 /0.00 B:20.55 /0.00 @:0 B@:0\n'
```

##### Linux :

```
python main.py --serial-port /dev/ttyUSB0 --baudrate 250000
Command: M105
b'ok T:19.92 /0.00 B:20.55 /0.00 @:0 B@:0\n'
```