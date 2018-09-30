#!/usr/bin/python3
import argparse
from bitarray import bitarray
def bits_from_int(number, size=8):
    a = bitarray(bin(number).replace('0b', ''))
    while len(a) < size:
        a.insert(0, 0)
    return a

def int_from_bits(bits):
    return int(bits.to01(), 2)

def compress(text):
    dict_size = 256
    dictionary = {bits_from_int(i).to01(): i for i in range(dict_size)}
    result = bitarray()
    w = bitarray()
    code_size = 8
    for c in text:
        wc = bitarray()
        wc.extend(w)
        wc.extend(bits_from_int(int(c)))
        if wc.to01() in dictionary:
            w = bitarray()
            w.extend(wc)
        else:
            result.extend(bits_from_int(dictionary[w.to01()], code_size))
            dictionary[wc.to01()] = dict_size
            dict_size += 1
            code_size = dict_size.bit_length()
            w = bitarray()
            w.extend(bits_from_int(int(c)))
    if len(w) > 0 and len(text) > 0:
        result.extend(bits_from_int(dictionary[w.to01()], code_size))
    return result

def power_of_two(value):
    init_value = 1
    while init_value < value:
        init_value *= 2
        if init_value == value:
            return True
    return False

def decompress(text):
    dict_size = 256
    dictionary = {i: bits_from_int(i).to01() for i in range(dict_size)}
    w = bitarray()
    w.extend(text[:8])
    result = bitarray()
    result.extend(text[:8])
    pos = 8
    code_size = 9
    while pos + code_size <= len(text):
        k = int_from_bits(text[pos:pos + code_size])
        pos += code_size
        if k in dictionary:
            entry = bitarray()
            entry.extend(dictionary[k])
        elif k == dict_size:
            entry = bitarray()
            entry.extend(w)
            entry.extend(w[:8])
        else:
            print('Bad compressed k: %s' % k)
            exit()
        result.extend(entry)
        tmp = bitarray()
        tmp.extend(w)
        tmp.extend(entry[:8])
        dictionary[dict_size] = tmp.to01()
        dict_size += 1
        if power_of_two(dict_size + 1):
            code_size += 1
        w = bitarray()
        w.extend(entry)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LZW algorithm utility.')
    parser.add_argument('path', help='Path to file for compression.')
    parser.add_argument('--d', help='decomress', action='store_true')
    args = parser.parse_args()
    text = None
    if args.d:
        with open(args.path, 'rb') as file:
            text = bitarray()
            text.fromfile(file)
        text = decompress(text)
        with open(args.path + '.decompress', 'wb') as file:
            text.tofile(file)
    else:
        with open(args.path, 'rb') as file:
            text = file.read()
        text = compress(text)
        with open(args.path + '.lzw', 'wb') as file:
            text.tofile(file)
