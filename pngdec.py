import sys
from PIL import Image
import gtk


###############
### Helpers ###
###############
    
codex = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
}
    
def setcbtext(text):
    cb = gtk.Clipboard()
    cb.set_text(text)
    cb.store()
    
######################
### Core Functions ###
######################


                
############
### Main ###
############
  
def main():

    file = 'PNG.png'
    im = Image.open(file)
    picture = im.load()
    y, offset, characters = 0, 0, []
    while True:
        try:
            for x in range(100):
                if picture[x,y]:
                    z = x
                    if y:
                        z = y * 100 + x
                    characters.append(chr(z - offset))
                    offset = z
            y += 1
        except IndexError:
            break
        
    phrase = "".join(characters)
    translated = [codex[x] for x in phrase.split()]
    setcbtext("".join(translated))

    

if __name__ == '__main__':
    main()
