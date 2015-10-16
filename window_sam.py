#!/usr/bin/env python

# Command line script to break a sam into windows of a given size
# Reads from stdin, writes new sam file to stdout

import sys, argparse, math

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', '-s', help="Window size", 
            type=int, required=True)
    args = parser.parse_args()
    # Read sam file one line at a time
    for line in sys.stdin:
        fields = line.strip().split()
        if len(fields) < 4:
            continue
        seq_id = fields[2]
        position = int(fields[3])
        window_number = int(math.ceil(float(position)/args.size)) 
        window_id = seq_id + "_window_" + str(window_number)
        window_position = position - (args.size * (window_number - 1))
        fields[2] = window_id
        fields[3] = str(window_position)
        sys.stdout.write("\t".join(fields) + "\n")


##########################

if __name__ == "__main__":
    main()
