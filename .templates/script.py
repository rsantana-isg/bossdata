#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Executable script {{ name }}.
"""

from __future__ import division,print_function

import argparse

def main():
    # Initialize and parse command-line arguments.
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--verbose', action = 'store_true',
        help = 'Provide verbose output.')
    args = parser.parse_args()

if __name__ == '__main__':
    main()
