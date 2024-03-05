#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    with open('test1.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    sentences = content.split('.')
    if len(sentences) < 2:
        print('Not enough sentences for this program!')
        sys.exit(1)

    sentences = sentences[:3]
    [print(sentence.strip()) for sentence in sentences[::-1]]
