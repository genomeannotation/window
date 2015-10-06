#!/usr/bin/env python

# Command line script to break a fasta into windows of a given size
# Writes new fasta file

import sys, argparse, math

def window(header, seq, size):
    """Return a fasta string consisting of windowed sequences based on input"""
    result = ""
    seq_length = len(seq)
    number_of_windows = int(math.ceil(float(seq_length) / size))
    for window_number in range(number_of_windows):
        start_index = window_number * size
        end_index = (window_number + 1) * size
        result += ">" + header + ".window_" + str(window_number) + "\n"
        result += seq[start_index:end_index] + "\n"
    return result

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--fasta', '-f', required=True)
    parser.add_argument('--size', '-s', help="Window size", 
            type=int, required=True)
    args = parser.parse_args()
    # Look at input file to determine output file name
    output_filename = args.fasta + "." + str(args.size) + "_windows"
    # Read fasta one sequence at a time
    current_header = ""
    current_sequence = ""
    with open(args.fasta, 'r') as fasta,\
            open(output_filename, 'w') as outfile:
        for line in fasta:
            if line.startswith(">"):
                # New sequence header
                if current_sequence:
                    new_seqs = window(current_header, current_sequence, args.size)
                    outfile.write(new_seqs)
                current_header = line[1:].strip()
                current_sequence = ""
            else:
                # Sequence line
                current_sequence += line.strip()
        # Process last remaining sequence
        new_seqs = window(current_header, current_sequence, args.size)
        outfile.write(new_seqs)


##########################

if __name__ == "__main__":
    main()
