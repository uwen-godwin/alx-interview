#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF  # Only consider the least significant 8 bits

        if num_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False  # Must be a 1-byte character, hence MSB must be 0
        else:
            # Check if the byte is a continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
