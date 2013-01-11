"""
Using pypy to run this scrypt I was able to complete the 3rd mission in about 30 seconeds.
"""

from hashlib import md5

###############
### Helpers ###
###############

def md5hash(strPassword):
    return md5(str(strPassword)).hexdigest()
    

######################
### Core Functions ###
######################

def evalCrossTotal(strMD5):
    intTotal = 0
    arrMD5Chars = list(strMD5)
    for value in arrMD5Chars:
        intTotal += int(value, 16)
    return intTotal

def encryptString(strString, strPassword):
    strPasswordMD5 = md5hash(strPassword)
    intMD5Total = evalCrossTotal(strPasswordMD5)
    arrEncryptedValues = []
    intStrlen = len(strString)
    count = 0
    while count < intStrlen:
        substr1 = strString[count:count+1]
        substr2 = strPasswordMD5[count%32:count%32+1]
        substr3 = md5hash(strString[0:count+1])[0:16]
        substr4 = md5hash(str(intMD5Total))[0:16]
        arrEncryptedValues.append(ord(substr1) +  int((substr2), 16) -  intMD5Total)
        intMD5Total = evalCrossTotal(substr3 + substr4)
        count +=1

    return arrEncryptedValues

def knownChar(count):
    loc = count % 20
    if loc == 19:
        return "\n"
    elif loc in [3,7,11,15]:
        return "-"
    elif loc == 8:
        return "O"
    elif loc == 9:
        return "E"
    elif loc == 10:
        return "M"
    elif loc == 18 or loc == 16:
        return "1"
    elif loc == 17:
        return "."
    else:
        return False

               
############
### Main ###
############
  

myinput = "-161 -185 -139 -157 -136 -142 -115 -152 -174 -177 -119 -217 -203 -199 -186 -194 -202 -191 -171 -271 -163 -131 -197 -221 -162 -145 -164 -201 -147 -177 -189 -182 -121 -157 -118 -151 -191 -165 -167 -213 -176 -172 -129 -214 -155 -148 -179 -154 -99 -98 -166 -223 -156 -150 -156 -220 -155 -222 -184 -233 -159 -169 -158 -175 -155 -139 -136 -221 -178 -147 -174 -199 -169 -164 -171 -200 -166 -173 -183 -239 -188 -110 -178 -154 -102 -144 -138 -242 -182 -156 -141 -211 -178 -155 -182 -150 -200 -172 -171 -197" 
    
codeArr = myinput.split(' ')
chars = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9' ]
hexchars = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9' ]


def fillMD5Total(str_guess, passhash_guess, previous, times_run):
    return evalCrossTotal(str(md5hash(str_guess[:(times_run+1)]))[0:16] + str(md5hash(previous))[0:16])


def main():
    """
    This function finds every possible combination of Character and password for the first character of the string of serials.
    when it finds a feaisble combination it passes it off to DecruptChar to see if matches can be found for subsequest characters.
    """
    for hchar in hexchars:
        for char in chars:
            for c in range(481):
                if(((ord(char) + int(hchar,16) - c) == int(codeArr[0]))):
                    intTotal = fillMD5Total(char, hchar,c, 1)
                    result = DecryptChar(char,1, str(hchar),intTotal)
                    if(result):
                        print result.split("\n")[-2]
                        return True


def DecryptChar(char_guess,count,hstring,total):
    """
    Recursive function that uses a formula derived from the encryption algorithm to guess and then test subsequest character/hex character password combinations.
    """
    if(count > 99):
        return str(char_guess)
        
    elif(count > 31): 
        if(knownChar(count)):
                intTotal = fillMD5Total(char_guess+knownChar(count), hstring[0:1],total, count+1)
                strDone = DecryptChar(char_guess+knownChar(count),count+1,hstring,intTotal)
                return strDone
        else:    
            for char in chars:
                if((ord(char) + int(hstring[(count%32):(count%32+1)],16) - total) == int(codeArr[count])):
                    intTotal = fillMD5Total(char_guess+char, hstring[0:1],total, count+1)
                    strDone = DecryptChar(char_guess+char,count+1,hstring,intTotal)
                    if(strDone):
                        return strDone
        return False

    else:
        knownval = knownChar(count)
        if(knownval):
            for hchar in hexchars:
                if((ord(knownChar(count)) + int(hchar,16) - total) == int(codeArr[count])):
                    intTotal = fillMD5Total(char_guess+knownChar(count), hstring[0:1],total, count+1)
                    strDone = DecryptChar(char_guess+knownChar(count),count+1,hstring+hchar,intTotal)
                    if(strDone):
                        return strDone
        else:
            for hchar in hexchars:
                for char in chars:
                    if((ord(char) + int(hchar,16) - total) == int(codeArr[count])):
                        intTotal = fillMD5Total(char_guess+char, hstring[0:1],total, count+1)
                        strDone = DecryptChar(char_guess+char,count+1,hstring+hchar,intTotal)
                        if(strDone):
                            return strDone

    return False


#this prevents the code from being run automatically if you decide to import the file from another project
if __name__ == '__main__':
    main()

