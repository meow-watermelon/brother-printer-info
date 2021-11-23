# Brother Printer Information Collector

## Intro

This is a small tool to get the Brother printer status information.

## Python Module Dependencies

Following Python modules are needed to run this utility:

```
argparse
csv
io
requests
sys
```

## Usage

```
$ ./brother-printer-info.py -h
usage: brother-printer-info.py [-h] --printer PRINTER

Brother Printer Information Collector

optional arguments:
  -h, --help         show this help message and exit
  --printer PRINTER  Printer IP or Hostname
```

## Example

```
$ ./brother-printer-info.py --printer brother-printer.internal
Node Name: BRW5C61XXXXXXXX
Model Name: Brother HL-L2390DW
Location: 
Contact: 
IP Address: 192.168.0.53
Serial No.: U64967XXXXXXXXX
Main Firmware Version: V
Memory Size: 64
Page Counter: 18
Average Coverage: 2.92
% of Life Remaining(Drum Unit): 100
% of Life Remaining(Toner): 100
A4/Letter: 16
Legal/Folio: 0
B5/Executive: 2
Envelopes: 0
A5: 0
Others: 0
Plain/Thin/Recycled: 18
Thick/Thicker/Bond: 0
Envelopes/Env. Thick/Env. Thin: 0
Label: 0
Hagaki: 0
Total: 18
Total 2-sided Print: 2
Copy: 2
Copy 2-sided Print: 0
Print: 16
Print 2-sided Print: 2
Others 2-sided Print: 0
Flatbed Scan: 11
Scan Page Count: 9
Replace Count(Toner): 0
Replace Count(Drum Unit): 0
Total Paper Jams: 0
Jam Tray 1: 0
Jam Inside: 0
Jam Rear: 0
Jam 2-sided: 0
Error1: No Drum Unit
Error2: 
Error3: 
Error4: 
Error5: 
Error6: 
Error7: 
Error8: 
Error9: 
Error10: 
Error Count 1: 0
Error Count 2: 0
Error Count 3: 0
Error Count 4: 0
Error Count 5: 0
Error Count 6: 0
Error Count 7: 0
Error Count 8: 0
Error Count 9: 0
Error Count 10: 0
```

Any thoughts and suggestions are welcome, Thanks!
