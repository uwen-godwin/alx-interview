#!/usr/bin/python3
"""
This module contains the canUnlockAll function.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of lists): List of lists where each sublist represents keys in a box.
    
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    opened = [False] * len(boxes)
    opened[0] = True
    keys = boxes[0]
    
    while keys:
        key = keys.pop()
        if key < len(boxes) and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])
    
    return all(opened)
