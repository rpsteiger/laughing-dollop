#!/usr/bin/python3
import sys

def generate_offset_file(filename: str, buffer_length: int) -> None:
    with open(filename, "wb") as output_file:
        buffer = b"A"*buffer_length
        output_file.write(buffer)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise ValueError("usage: generate_offset_file.py filename buffer_length")
    generate_offset_file(sys.argv[1], int(sys.argv[2]))
        
