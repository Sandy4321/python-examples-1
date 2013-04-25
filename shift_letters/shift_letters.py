# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    if letter == ' ':
        return letter
    alpha_ord = [x for x in range(ord('a'), ord('z') + 1)]
    pos = alpha_ord.index(ord(letter))
    if pos + n > len(alpha_ord) - 1:
        pos = (pos + n) % len(alpha_ord)
    else:
        pos += n

    return chr(alpha_ord[pos])

def rotate(t, n):
    # Your code here
    out = ''
    for c in t:
        out += shift_n_letters(c, n)
    return out

#print rotate ('sarah', 13)
#>>> 'fnenu'
#print rotate('fnenu',13)
#>>> 'sarah'
#print rotate('dave',5)
#>>>'ifaj'
#print rotate('ifaj',-5)
#>>>'dave'
#print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
#                "sv rscv kf ivru kyzj"),-17)

