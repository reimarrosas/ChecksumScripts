#!/bin/env python3

import sys
import hashlib

if len(sys.argv) < 3:
    print("Invalid number of arguments.")
    sys.exit(1)
else:
    hash_types = set(types.lower() for types in sys.argv[1:-1])

    file_dir = sys.argv[-1]
    calc_hashes = []

    if hash_types.issubset(hashlib.algorithms_available):
        with open(file_dir, "rb") as f:
            file_data = f.read()

            for ht in hash_types:
                h = hashlib.new(ht)
                h.update(file_data)
                calc_hashes.append(h.hexdigest())
        
        result_iter = zip(hash_types, calc_hashes)
        result_dict = dict(result_iter)

        given_hashes = []

        for x in range(0, len(result_dict)):
            given_hashes.append(input("Enter the given hash: "))
        
        for items in result_dict.items():
            if items[1] in given_hashes:
                print(f"{items[0]} verified.")
            else:
                print(f"{items[0]} verification failed.")
                sys.exit(1)
    else:
        print("Invalid Hashing Algorithm/s.")
