#!/bin/python

import sys

try:
    import argparse
except ImportError:
    print "argparse is not installed and is a required dependency" 
    print "  -- Try `easy_install argparse` or `pip install argparse` or search your OS Packag Management System for the Package" 
    sys.exit(1)


def set_args(parser):
    parser.add_argument('-i', '--in', dest='in_file_path', 
        help="File that you would like to have converted to a different format.")
    return parser.parse_args()


def main():
    parser = argparse.ArgumentParser(description="Convert PKCS7 an PKCS12 files to other Certifcate formats.")
    args = set_args(parser)


if __name__ == "__main__":
    main()
