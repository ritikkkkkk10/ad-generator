import cv2
from PIL import Image

from detector import detect_objects
from image_adjuster import smart_resize

from safe_area import get_safe_mask
from text_safe_area import remove_objects_from_safe_area
from find_text_area import find_text_area
from text_renderer import render_text

image_path = "assets/images/sample.jpg"
template_path = "assets/templates/template1.png"

boxes = detect_objects(image_path)

img = cv2.imread(image_path)

template = Image.open(template_path)

template_w, template_h = template.size

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

base = Image.open(
    "output/adjusted.jpg"
).convert("RGBA")

template = template.convert("RGBA")

final = Image.alpha_composite(
    base,
    template
)

safe_mask = get_safe_mask(
    template_path
)

safe_mask = remove_objects_from_safe_area(
    safe_mask,
    boxes
)

area = find_text_area(
    safe_mask
)

print("TEXT AREA =", area)

text_data = {
    "headline":"HOME LOAN",
    "subheadline":"Get home loans with rates starting at 8.25 percent and fast approval process",
    "cta":"APPLY NOW"
}

final = render_text(
    final,
    area,
    text_data
)

final.save(
    "output/final.png"
)

print("DONE")