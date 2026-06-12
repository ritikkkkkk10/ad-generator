import cv2
import numpy as np
from PIL import Image

from detector import detect_objects
from image_adjuster import smart_resize

from safe_area import get_safe_mask
from text_safe_area import remove_objects_from_safe_area
from find_candidate_areas import find_candidate_areas

from text_renderer import render_text
from debug_candidates import draw_candidates


# --------------------------
# INPUTS
# --------------------------

image_path = "assets/images/sample.jpg"
template_path = "assets/templates/template1.png"


# --------------------------
# DETECT OBJECTS ON ORIGINAL
# --------------------------

boxes = detect_objects(image_path)

print("ORIGINAL BOXES")
print(boxes)


# --------------------------
# LOAD IMAGE + TEMPLATE
# --------------------------

img = cv2.imread(image_path)

template = Image.open(template_path)

template_w, template_h = template.size


# --------------------------
# SMART RESIZE
# --------------------------

adjusted = smart_resize(
    img,
    template_w,
    template_h,
    boxes
)

cv2.imwrite(
    "output/adjusted.jpg",
    adjusted
)


# --------------------------
# DETECT AGAIN AFTER RESIZE
# --------------------------

adjusted_boxes = detect_objects(
    "output/adjusted.jpg"
)

boxes = adjusted_boxes

print("ADJUSTED BOXES")
print(boxes)


# --------------------------
# DEBUG DETECTION BOXES
# --------------------------

debug_boxes = adjusted.copy()

for x1, y1, x2, y2 in boxes:

    cv2.rectangle(
        debug_boxes,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        3
    )

cv2.imwrite(
    "output/debug_boxes.jpg",
    debug_boxes
)


# --------------------------
# SAFE AREA MASK
# --------------------------

safe_mask = get_safe_mask(
    template_path
)

safe_mask = remove_objects_from_safe_area(
    safe_mask,
    boxes
)

debug_mask = (
    safe_mask.astype(np.uint8)
    * 255
)

cv2.imwrite(
    "output/debug_safe_mask.png",
    debug_mask
)


# --------------------------
# FIND CANDIDATE AREAS
# --------------------------

areas = find_candidate_areas(
    safe_mask
)

print("\nCANDIDATES")

for i, area in enumerate(areas):
    print(i, area)


# --------------------------
# DEBUG CANDIDATES
# --------------------------

debug_candidates = adjusted.copy()

debug_candidates = draw_candidates(
    debug_candidates,
    areas
)

cv2.imwrite(
    "output/debug_candidates.jpg",
    debug_candidates
)


# --------------------------
# PICK BEST AREA
# --------------------------

if len(areas) == 0:

    area = (
        20,
        20,
        250,
        150
    )

else:

    area = areas[0][:4]

print("\nSELECTED AREA")
print(area)


# --------------------------
# OVERLAY TEMPLATE
# --------------------------

base = Image.open(
    "output/adjusted.jpg"
).convert("RGBA")

template = Image.open(
    template_path
).convert("RGBA")

final = Image.alpha_composite(
    base,
    template
)


# --------------------------
# TEXT DATA
# --------------------------

text_data = {
    "headline":"HOME LOAN",
    "subheadline":"Get home loans with fast approval process",
    "highlight":"8.25%",
    "cta":"APPLY NOW"
}


# --------------------------
# RENDER TEXT
# --------------------------

final = render_text(
    final,
    area,
    text_data
)


# --------------------------
# SAVE FINAL
# --------------------------

final.save(
    "output/final.png"
)

print("\nDONE")