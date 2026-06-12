import numpy as np

def remove_objects_from_safe_area(
        safe_mask,
        boxes):

    mask = safe_mask.copy()

    h, w = mask.shape

    for x1, y1, x2, y2 in boxes:

        pad = 40

        x1 = max(0, int(x1 - pad))
        y1 = max(0, int(y1 - pad))

        x2 = min(w, int(x2 + pad))
        y2 = min(h, int(y2 + pad))

        mask[y1:y2, x1:x2] = False

    return mask