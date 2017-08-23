# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import os
import codecs

parser = argparse.ArgumentParser()
parser.add_argument('--training_txt', default='data/tiny-shakespeare.txt')
parser.add_argument('--input_txt', default='data/tiny-shakespeare.txt')
parser.add_argument('--output_txt', default='data/tiny-shakespeare.h5')
parser.add_argument('--quiet', action='store_true')
parser.add_argument('--encoding', default='utf-8')
args = parser.parse_args()


if __name__ == '__main__':
  if args.encoding == 'bytes': args.encoding = None

  # First go the training file and build a set of lines
  lines = set()
  total_size = 0
  with codecs.open(args.training_txt, 'r', args.encoding) as f:
    for line in f:
      total_size += 1
      lines.add(line)

  if not args.quiet:
    print('Total lines in file: %d' % total_size)

  # Go through the input file and remove any lines
  filtered = set()
  with codecs.open(args.input_txt, 'r', args.encoding) as f:
    for line in f:
      if line not in lines:
        filtered.add(line)

  # Create a text file for the unique lines
  with codecs.open(args.output_txt, 'w', args.encoding) as f:
    f.writelines(list(filtered))
