#Level 2 - Analyze the picture and find the ascii code

![Image](https://github.com/frodopwns/python-examples/blob/master/image_analysis/PNG.png?raw=true "PNG file for Level 2 test")

The pixels in the above image are numbered 0..99 for the first row, 100..199 for the second row etc. White pixels represent ascii codes. The ascii code for a particular white pixel is equal to the offset from the last white pixel. For example, the first white pixel at location 65 would represent ascii code 65 ('A'), the next at location 131 would represent ascii code (131 - 65) = 66 ('B') and so on.

The text contained in the image is the answer encoded in Morse, where "a test" would be encoded as ".- / - . ... -"

You have 15 seconds time to send the solution.

For this challenge I saved the image manually by right-clicking.  I then scanned the image for white pixels using the offset formula provided to find the hidden message which is encoded in morse code.  I then translate the morse code to ascii text and set the value in my clipboard for easy pasting.
