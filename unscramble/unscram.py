import sys

import gtk

def getClipboard():
    return gtk.Clipboard().wait_for_text()

def setClipboard(text):
    cb = gtk.Clipboard()
    cb.set_text(text)
    cb.store()


  
def main():
    
    if (len(sys.argv) > 1):
        print 'Options used: ', sys.argv[1]
        sys.exit()
        
    testList = []
    with open("words.txt", "r") as mywords:
        testList = [x.strip("\r\n") for x in mywords.readlines()]
        
    scramIn = getClipboard()
    scrambled = [x.strip() for x in scramIn.split("\t")]
    results = []
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






