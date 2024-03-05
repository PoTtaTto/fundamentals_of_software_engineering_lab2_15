#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: No file name!')
    else:
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for _ in range(10):
                    line = file.readline().strip()
                    if not line:
                        break
                    print(line)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
