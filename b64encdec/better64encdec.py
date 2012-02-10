debug_val = False
def debug(string):
    if debug_val:
        print string

base64dic = {62: "+", 63: "/"}
for cap_letter_ord in range(ord("A"), ord("Z") + 1):
    base64dic[cap_letter_ord - ord("A")] = chr(cap_letter_ord)

for lower_letter_ord in range(ord("a"), ord("z") + 1):
    base64dic[lower_letter_ord - ord("a") + 26] = chr(lower_letter_ord)

for digit in range(10):
    base64dic[digit + 52] = str(digit)

rev_base64dic = dict([(value, key) for key, value in base64dic.iteritems()])

def ord64(char):
    return rev_base64dic[char]

def byte_to_bits(byte, num_bits):
    ret = ["0"] * num_bits
    idx = -1
    while byte:
        if byte % 2:
            ret[idx] = "1"

        byte /= 2
        idx -= 1

    return ''.join(ret)

def bits_to_ord(bit_string):
    ret = 0

    idx = 0
    for char in reversed(bit_string):
        if char == '1':
            ret += 2**idx
        idx += 1

    return ret

def get_chunks(bit_string, chunk_size):
    ret = []
    idx = 0

    while idx + chunk_size < len(bit_string):
        ret.append(bit_string[idx: idx+chunk_size])
        idx += chunk_size

    ret.append(bit_string[idx:])
    return ret


def bytes_to_base64(byte_string):
    debug(byte_string)
    if not byte_string:
        return ""

    ord_list = map(ord, byte_string)
    debug(str(ord_list))

    bit_str_list = map(lambda x: byte_to_bits(x, num_bits=8), ord_list)
    debug(bit_str_list)

    bit_string = ''.join(bit_str_list)
    debug(bit_string)

    six_bit_chunks = get_chunks(bit_string, 6)
    debug(six_bit_chunks)
    num_extra_bits = (6 - len(six_bit_chunks[-1]))
    debug(num_extra_bits)
    padding = "=" * (3 - len(six_bit_chunks[-1]) / 2)

    six_bit_chunks[-1] += "0" * num_extra_bits
    debug(six_bit_chunks)

    six_bit_ord_list = map(bits_to_ord, six_bit_chunks)
    debug(six_bit_ord_list)

    base64_char_list = map(lambda x: base64dic[x], six_bit_ord_list)
    debug(base64_char_list)

    return ''.join(base64_char_list) + padding

debug_val = True
print bytes_to_base64("s")
print bytes_to_base64("su")
print bytes_to_base64("sur")

def base64_to_bytes(base64_string):
    ord64_list = map(ord64, base64_string.rstrip("="))
    debug(str(ord64_list))

    bit_str_list = map(lambda x: byte_to_bits(x, num_bits=6), ord64_list)
    debug(bit_str_list)

    bit_string = ''.join(bit_str_list)
    debug(bit_string)

    eight_bit_chunks = get_chunks(bit_string, 8)
    eight_bit_chunks = filter(lambda x: len(x) == 8, eight_bit_chunks)
    debug(eight_bit_chunks)

    eight_bit_ord_list = map(bits_to_ord, eight_bit_chunks)
    debug(eight_bit_ord_list)

    ascii_char_list = map(chr, eight_bit_ord_list)
    return ''.join(ascii_char_list)

#debug_val = True

#print base64_to_bytes("cw==")
#print base64_to_bytes("c3U=")
#print base64_to_bytes("c3Vy")

#print bytes_to_base64("")
