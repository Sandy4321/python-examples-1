import win32clipboard, sys, optparse, Image

###############
### Options ###
###############

#option callback for printing clipboard input
def clip_callback(option, opt_str, value, parser):
    clipboard = getClipIn()
    print clipboard

###############
### Helpers ###
###############
    

    
######################
### Core Functions ###
######################


                
############
### Main ###
############
  
def main():
    parser = optparse.OptionParser()
    parser.add_option('--clip', help="Print the contents of the clipboard", action="callback", callback=clip_callback)
    #parser.add_option('--clip', action="callback", callback=clip_callback)
    
    if (len(sys.argv) > 1):
        print 'Options used: ', sys.argv[1]
        parser.parse_args()
        sys.exit()
        # Command line args are in sys.argv[1], sys.argv[2] ..
        # sys.argv[0] is the script name itself and can be ignored

    img = Image.open(filename)
    im = img.load()
    

if __name__ == '__main__':
    main()