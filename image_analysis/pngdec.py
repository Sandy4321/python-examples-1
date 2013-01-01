"""Analyze the Image"""

from PIL import Image
import gtk

#Dictionary used for translating the morse code to english    
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

def setClipboard(text):
    """
    Sets the answer in the system clipboard
    """
    cb = gtk.Clipboard()
    cb.set_text(text)
    cb.store()
    
  
def main():
    """
    Opens and parses the encoded iamge.
    """
    file = 'PNG.png'
    im = Image.open(file)
    picture = im.load()
    #start at row 0 with no offset
    y, offset = 0, 0
    #max width is given but height is not so we search until there is nothing to search
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
    setClipboard("".join(translated))


if __name__ == '__main__':
    main()
