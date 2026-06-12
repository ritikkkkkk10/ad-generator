import cv2
import numpy as np

def find_text_area(mask):

    mask_u8 = (
        mask.astype(np.uint8)
        * 255
    )

    contours, _ = cv2.findContours(
        mask_u8,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    best = None
    best_score = 0

    for c in contours:

        x, y, w, h = cv2.boundingRect(c)

        area = w * h

        if area < 5000:
            continue

        aspect = w / max(h, 1)

        # Prefer wide rectangles
        score = area * min(aspect, 3)

        if score > best_score:

            best_score = score
            best = (
                int(x),
                int(y),
                int(w),
                int(h)
            )

    if best is None:

        return (
            20,
            20,
            250,
            150
        )

    return best