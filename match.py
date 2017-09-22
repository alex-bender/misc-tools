#!/usr/bin/env python3
'''Find file matches by hash
'''
import os
import sys
from collections import defaultdict


def build_hash_table(path):
    '''Read filenames from `path' file and calculate hashes.'''

    if os.path.exists(path) and os.path.isfile(path):
        with open(path, 'r') as reference_files:
            file_names = reference_files.readlines()
            if not file_names:
                print('File {} is empty'.format(path))
                sys.exit(1)

            file_counter = 0
            content_read = 0
            hash_table = {}

            number_of_dups = 0
            dups = defaultdict(set)

            for name in file_names:
                name = name.strip()
                file_counter += 1

                file_to_hash = open(name, 'r')
                file_data = file_to_hash.read()

                content_read += len(file_data)
                file_hash = hash(file_data)

                if file_hash in hash_table:
                    number_of_dups += 1
                    dups[file_hash].add(name)
                    dups[file_hash].add(hash_table[file_hash])
                else:
                    hash_table[file_hash] = name

            for hash_item in hash_table:
                print(hash_item, hash_table[hash_item])

            for hash_item in dups:
                print(hash_item)
                for name in dups[hash_item]:
                    print('\t'+name)

            print('Duplicates are: {}'.format(dups))
            print('Hashes are: {}'.format(hash_table))
            print('Files processed: {}'.format(file_counter))
            print('Numbet of duplicated files is: {} (+ one original)'.format(number_of_dups))
            print('Bytes read: {}'.format(content_read))
            print('Time spent: {}'.format('X'))
    else:
        print('File {} does not exist or it is folder'.format(path))
