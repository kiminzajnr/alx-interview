#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    boxes_unlocked = {}
    pos = 0
    for box in boxes:
        if len(box) == 0 or pos == 0:
            boxes_unlocked[pos] = 0
        for key in box:
            if key < len(boxes) and key != pos:
                boxes_unlocked[key] = key
        if len(boxes_unlocked) == len(boxes):
            return True
        pos += 1
    return False
