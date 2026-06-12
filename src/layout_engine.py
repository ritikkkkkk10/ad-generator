from PIL import ImageFont, ImageDraw
import textwrap

FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"
FONT_REGULAR = "C:/Windows/Fonts/arial.ttf"


def fit_text_block(draw, area, text_data):

    x, y, w, h = area

    headline = text_data["headline"]
    subheadline = text_data["subheadline"]
    cta = text_data["cta"]

    for headline_size in range(80, 20, -2):

        headline_font = ImageFont.truetype(
            FONT_BOLD,
            headline_size
        )

        headline_bbox = draw.textbbox(
            (0, 0),
            headline,
            font=headline_font
        )

        headline_w = headline_bbox[2]

        if headline_w > w - 30:
            continue

        for sub_size in range(40, 14, -2):

            sub_font = ImageFont.truetype(
                FONT_REGULAR,
                sub_size
            )

            wrapped = textwrap.wrap(
                subheadline,
                width=max(10, int(w / 12))
            )

            sub_height = 0

            for line in wrapped:

                bbox = draw.textbbox(
                    (0, 0),
                    line,
                    font=sub_font
                )

                sub_height += (
                    bbox[3] - bbox[1]
                ) + 8

            cta_font = ImageFont.truetype(
                FONT_BOLD,
                max(18, sub_size)
            )

            cta_bbox = draw.textbbox(
                (0, 0),
                cta,
                font=cta_font
            )

            cta_h = cta_bbox[3] - cta_bbox[1]

            total_height = (
                (headline_bbox[3] - headline_bbox[1])
                + 20
                + sub_height
                + 30
                + cta_h
                + 40
            )

            if total_height <= h - 20:

                return {
                    "headline_font": headline_font,
                    "sub_font": sub_font,
                    "cta_font": cta_font,
                    "wrapped_lines": wrapped
                }

    return None