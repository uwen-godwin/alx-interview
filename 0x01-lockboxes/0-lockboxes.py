#!/usr/bin/python3
"""
Module that determines if all boxes can be unlocked
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Arguments:
    boxes -- list of lists, where each list represents keys in a box
    Returns:
    True if all boxes can be opened, else False
    """
    
    n = len(boxes)
    opened_boxes = [False] * n
    opened_boxes[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened_boxes[key]:
                opened_boxes[key] = True
                keys.append(key)
    
    return all(opened_boxes)
