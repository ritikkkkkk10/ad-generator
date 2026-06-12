import cv2
import numpy as np

def find_text_area(mask):

    mask_u8 = (
        mask.astype(np.uint8)
        * 255
    )

    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
        mask_u8,
        connectivity=8
    )

    best = None
    best_area = 0

    for i in range(1, num_labels):

        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        area = w * h

        if area < 10000:
            continue

        if area > best_area:
            best_area = area
            best = (x, y, w, h)

    if best is None:

        return (
            50,
            50,
            300,
            200
        )

    return best