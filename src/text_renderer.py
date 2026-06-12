from PIL import ImageDraw

from layout_engine import fit_text_block


def render_text(
        image,
        area,
        text_data):

    draw = ImageDraw.Draw(image)

    layout = fit_text_block(
        draw,
        area,
        text_data
    )

    if layout is None:
        return image

    x, y, w, h = area

    headline_font = layout["headline_font"]
    sub_font = layout["sub_font"]
    cta_font = layout["cta_font"]

    headline = text_data["headline"]
    lines = layout["wrapped_lines"]
    cta = text_data["cta"]

    current_y = y + 15

    draw.text(
        (x + 15, current_y),
        headline,
        fill=(0, 0, 0),
        font=headline_font
    )

    headline_bbox = draw.textbbox(
        (x + 15, current_y),
        headline,
        font=headline_font
    )

    current_y = headline_bbox[3] + 15

    for line in lines:

        draw.text(
            (x + 15, current_y),
            line,
            fill=(60, 60, 60),
            font=sub_font
        )

        bbox = draw.textbbox(
            (x + 15, current_y),
            line,
            font=sub_font
        )

        current_y = bbox[3] + 5

    current_y += 10

    cta_bbox = draw.textbbox(
        (0, 0),
        cta,
        font=cta_font
    )

    tw = cta_bbox[2] - cta_bbox[0]
    th = cta_bbox[3] - cta_bbox[1]

    padding = 12

    draw.rounded_rectangle(
        (
            x + 15,
            current_y,
            x + 15 + tw + padding * 2,
            current_y + th + padding * 2
        ),
        radius=10,
        fill=(0, 51, 255)
    )

    draw.text(
        (
            x + 15 + padding,
            current_y + padding
        ),
        cta,
        fill=(255, 255, 255),
        font=cta_font
    )

    return image