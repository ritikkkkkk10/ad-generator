from PIL import ImageDraw, ImageFont
import textwrap

FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"
FONT_REGULAR = "C:/Windows/Fonts/arial.ttf"


def fit_font(draw, text, max_width, start_size=80):

    size = start_size

    while size > 10:

        font = ImageFont.truetype(
            FONT_BOLD,
            size
        )

        bbox = draw.textbbox(
            (0,0),
            text,
            font=font
        )

        width = bbox[2] - bbox[0]

        if width <= max_width:
            return font

        size -= 2

    return ImageFont.truetype(
        FONT_BOLD,
        10
    )


def wrap_text(draw, text, font, max_width):

    words = text.split()

    lines = []
    current = ""

    for word in words:

        test = word if current == "" else current + " " + word

        bbox = draw.textbbox(
            (0,0),
            test,
            font=font
        )

        width = bbox[2] - bbox[0]

        if width <= max_width:

            current = test

        else:

            if current:
                lines.append(current)

            current = word

    if current:
        lines.append(current)

    return lines


def render_text(
        image,
        area,
        text_data):

    draw = ImageDraw.Draw(image)

    x,y,w,h = area

    headline = text_data["headline"]
    highlight = text_data["highlight"]
    subheadline = text_data["subheadline"]
    cta = text_data["cta"]

    headline_font = fit_font(
        draw,
        headline,
        w-20,
        80
    )

    highlight_font = fit_font(
        draw,
        highlight,
        w-20,
        70
    )

    sub_font = ImageFont.truetype(
        FONT_REGULAR,
        24
    )

    cta_font = ImageFont.truetype(
        FONT_BOLD,
        24
    )

    sub_lines = wrap_text(
        draw,
        subheadline,
        sub_font,
        w-20
    )

    current_y = y + 15

    # HEADLINE

    draw.text(
        (x+10,current_y),
        headline,
        fill=(0,0,0),
        font=headline_font
    )

    bbox = draw.textbbox(
        (x+10,current_y),
        headline,
        font=headline_font
    )

    current_y = bbox[3] + 10

    # SUBHEADLINE

    for line in sub_lines:

        draw.text(
            (x+10,current_y),
            line,
            fill=(60,60,60),
            font=sub_font
        )

        bbox = draw.textbbox(
            (x+10,current_y),
            line,
            font=sub_font
        )

        current_y = bbox[3] + 5

    current_y += 5

    # HIGHLIGHT

    draw.text(
        (x+10,current_y),
        highlight,
        fill=(0,51,255),
        font=highlight_font
    )

    bbox = draw.textbbox(
        (x+10,current_y),
        highlight,
        font=highlight_font
    )

    current_y = bbox[3] + 15

    # CTA BUTTON

    cta_bbox = draw.textbbox(
        (0,0),
        cta,
        font=cta_font
    )

    tw = cta_bbox[2] - cta_bbox[0]
    th = cta_bbox[3] - cta_bbox[1]

    pad = 10

    draw.rounded_rectangle(
        (
            x+10,
            current_y,
            x+10+tw+pad*2,
            current_y+th+pad*2
        ),
        radius=10,
        fill=(0,51,255)
    )

    draw.text(
        (
            x+10+pad,
            current_y+pad
        ),
        cta,
        fill=(255,255,255),
        font=cta_font
    )

    return image