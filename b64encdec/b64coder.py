import base64
import binascii

# encoding dictionary for base64. Keys are binary values, values correspond to base64 encoded character
base64dic = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z', 26:'a', 27:'b', 28:'c', 29:'d', 30:'e', 31:'f', 32:'g', 33:'h', 34:'i', 35:'j', 36:'k', 37:'l', 38:'m', 39:'n', 40:'o', 41:'p', 42:'q', 43:'r', 44:'s', 45:'t', 46:'u', 47:'v', 48:'w', 49:'x', 50:'y', 51:'z', 52:'0', 53:'1', 54:'2', 55:'3', 56:'4', 57:'5', 58:'6', 59:'7', 60:'8', 61:'9', 62:'+', 63:'/'}

# decoding dictionary from base64 to binary value
rev_base64dic = dict((v,k) for k,v in base64dic.iteritems())


# takes single character from a string as inpput and returns two-digit hex value
def char_to_bin(char):
    hex = char.encode('hex')
    return hex_to_bin(hex)

# takes a two-digit hex value as input and returns binary padded with zeros to make 8 bits
def hex_to_bin(x):
    binary = bin(int(x, 16))[2:].zfill(8)
    return binary

# loops through characters in a string using char_to_bin to return a concatenated string of binary
def str_to_bin(string):
    binary_string = ''
    for i in string:
        tmp = char_to_bin(i)
        binary_string += tmp
    return binary_string

# last mile -  bin encoding function. Checks for correct padding, then converts binary to base64
def bin_to_base64(binary_string):
    binstart = '0b'
    b64string = ''
    missingpad = len(binary_string) % 3
    if missingpad == 1:
        padnum = 1
    elif missingpad == 2:
        padnum = 2
    else:
        padnum = 0
    for i in range(0, len(binary_string), 6):
        if len(binary_string[i:]) < 6:
            # the group of bits sometimes needs to be padded (with 0s) to be read correctly
            tmp = binary_string[i:i+6] + "0"*(6-len(binary_string[i:]))
        else:
            tmp = binary_string[i:i+6]
        val = int(binstart + tmp, 2)
        b64string += base64dic[val]
    return b64string + "=" * padnum

# main encoding funciton takes python string and returns base64 encoded string
def str_to_base64(oldstring):
    binarystring = str_to_bin(oldstring)
    newstring = bin_to_base64(binarystring)
    return newstring

test = "oQDZ"

output = str_to_base64(test)

print output

print "python -> " + str(base64.b64encode(test))

# decoding


def base64_to_string(b64_string):
    binstring = ""
    binstart = "0b"
    finalstring = ""
    stripped = b64_string.replace("=","")
    for i in range(0, len(stripped)):
        tmp = rev_base64dic[stripped[i]]
        bintmp = bin(tmp)[2:].zfill(6)
        binstring += bintmp
    for i in range(0, len(binstring), 8):
        newtmp = binstring[i:i+8]
        if len(newtmp) < 8:
            continue
        val = int(binstart + newtmp, 2)
        finalstring += chr(val)
    return finalstring

grdecode = base64_to_string("oQDZ")
pydecode = base64.b64decode("oQDZ")

print repr(grdecode)
print "python ----> " + str(repr(pydecode))


