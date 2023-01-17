#!/usr/bin/env python3

from faker import Faker
import os

def main():
    faker = Faker()
    limit = 1 #GB
    unit = 'gb'
    lessThanLimit = True
    filename = 'output.json'
    write(filename, '[')

    while lessThanLimit:
        append(filename, '{')
        address = faker.address().replace("\n", "");
        text = faker.text().replace("\n", "");
        append(filename, f'"name": "{faker.name()}",')
        append(filename, f'"address": "{address}",')
        append(filename, f'"text": "{text}"')
        append(filename, '},')
        size = get_size(filename, unit)
        lessThanLimit = size < limit

    deleteLastChar(filename)
    append(filename, ']')

def write(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def append(filename, text):
    with open(filename, 'a') as f:
        f.write(text)

def deleteLastChar(filename):
    with open(filename, 'rb+') as f:
        f.seek(-1, 2)
        f.truncate()

def get_size(file_path, unit='bytes'):
    file_size = os.path.getsize(file_path)
    exponents_map = {"bytes": 0, "kb": 1, "mb": 2, "gb": 3}
    if unit not in exponents_map:
        raise ValueError("Must select from bytes\
        kb, mb or gb")
    else:
        size = file_size / 1024 ** exponents_map[unit]
        return round(size, 1)

if __name__ == "__main__":
    main()
