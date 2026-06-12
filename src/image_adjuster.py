import cv2
import numpy as np

def smart_resize(
        image,
        template_w,
        template_h,
        important_boxes):

    h, w = image.shape[:2]

    target_ratio = template_w / template_h
    image_ratio = w / h

    # ----------------------------------
    # Build one bounding box containing
    # all important objects
    # ----------------------------------

    if important_boxes:

        min_x = min(box[0] for box in important_boxes)
        min_y = min(box[1] for box in important_boxes)

        max_x = max(box[2] for box in important_boxes)
        max_y = max(box[3] for box in important_boxes)

    else:

        min_x = 0
        min_y = 0
        max_x = w
        max_y = h

    # add some margin around people

    margin_x = int(0.15 * (max_x - min_x))
    margin_y = int(0.20 * (max_y - min_y))

    min_x = max(0, min_x - margin_x)
    min_y = max(0, min_y - margin_y)

    max_x = min(w, max_x + margin_x)
    max_y = min(h, max_y + margin_y)

    important_w = max_x - min_x
    important_h = max_y - min_y

    # ----------------------------------
    # determine crop size
    # ----------------------------------

    crop_w = important_w
    crop_h = crop_w / target_ratio

    if crop_h < important_h:

        crop_h = important_h
        crop_w = crop_h * target_ratio

    # ----------------------------------
    # center crop around important area
    # ----------------------------------

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    left = int(center_x - crop_w / 2)
    right = int(center_x + crop_w / 2)

    top = int(center_y - crop_h / 2)
    bottom = int(center_y + crop_h / 2)

    # keep crop inside image

    if left < 0:
        right -= left
        left = 0

    if top < 0:
        bottom -= top
        top = 0

    if right > w:
        left -= (right - w)
        right = w

    if bottom > h:
        top -= (bottom - h)
        bottom = h

    left = max(0, left)
    top = max(0, top)

    cropped = image[top:bottom, left:right]

    scale_x = template_w / cropped.shape[1]
    scale_y = template_h / cropped.shape[0]

    scale = max(scale_x, scale_y)

    new_w = int(cropped.shape[1] * scale)
    new_h = int(cropped.shape[0] * scale)

    resized = cv2.resize(
        cropped,
        (new_w, new_h)
    )

    x = (new_w - template_w) // 2
    y = (new_h - template_h) // 2

    final = resized[
        y:y+template_h,
        x:x+template_w
    ]

    return final