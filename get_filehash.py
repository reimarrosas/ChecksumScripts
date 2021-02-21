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

        for result_hash in result_dict:
            print(f"{str.upper(result_hash)}: {result_dict[result_hash]}")
    else:
        print("Invalid Hashing Algorithm/s.")
