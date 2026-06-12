import re

def style_text(headline, subheadline, cta):

    highlight = None

    # detect percentages
    match = re.search(r'\d+(\.\d+)?%', headline)

    if match:
        highlight = match.group()

    return {
        "headline": headline,
        "subheadline": subheadline,
        "cta": cta,
        "highlight": highlight
    }