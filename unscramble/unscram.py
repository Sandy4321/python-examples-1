"""Unscramble the given list of words"""

import gtk


def getClipboard():
    """
    Returns the text copied from the browser to the clipboard
    """
    return gtk.Clipboard().wait_for_text()

def setClipboard(text):
    """
    Sets a new value to the clipboard for easy pasting
    """
    cb = gtk.Clipboard()
    cb.set_text(text)
    cb.store()
  
def main():
    """
    Unscramble list of scrambled words from clipboard then cmopare 
    with list of possible words to find matches.
    """
    #open words.txt and append contents to testList
    with open("words.txt", "r") as mywords:
        testList = [x.strip("\r\n") for x in mywords.readlines()]
    scramIn = getClipboard()
    #split input by tab then strip newlines
    scrambled = [x.strip() for x in scramIn.split("\t")]
    for code in  scrambled:
        codeLen = len(code)
        codeSort = sorted(code)
        for word in testList:
            if (len(word) == codeLen):
                if (sorted(word) == codeSort):
                    results.append(word)
    setClipboard( ",".join(results))
                

if __name__ == '__main__':
    main()






