# pykramer
Little Python script to switch inputs and outputs of a Kramer VS-162AV Matrix from the command line.

# How to:
1. Download / Clone this repo
2. Download ```python3```
3. ```pip install pyserial```
4. Run the script with: ```py .\main.py -p COM3 -i 4 -o 8```

# Tips:
- You can check the Serial Device Port looking at Windows' Device Manager under ```Ports (COM and LPT)```.
- Kramer VS-162AV is a 16 in / 16 out matrix. If you enter a number outside the range [1, 16] it will return an ```AssertionError```.
