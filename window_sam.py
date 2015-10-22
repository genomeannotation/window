#!/usr/bin/env python

# Command line script to break a sam into windows of a given size
# Reads from stdin, writes new sam file to stdout

import sys, argparse, math

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--window-size', '-w', help="Window size", type=int, required=True)
    parser.add_argument('--skip', '-s', help="Length to skip between windows", type=int)
    args = parser.parse_args()
    window_size = args.window_size
    skip = 0
    if args.skip:
        skip = args.skip
    # Read sam file one line at a time
    for line in sys.stdin:
        fields = line.strip().split()
        if len(fields) < 4:
            continue
        seq_id = fields[2]
        position = int(fields[3])
        window_number = int(math.floor(float(position)/(window_size+skip))) 
        window_id = seq_id + "_window_" + str(window_number+1)
        window_position = position - ((window_size+skip) * window_number)
        if window_position <= window_size:
            # Only write the read if it's not in the skip zone
            fields[2] = window_id
            fields[3] = str(window_position)
            sys.stdout.write("\t".join(fields) + "\n")


##########################

if __name__ == "__main__":
    main()
