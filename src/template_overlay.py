from PIL import Image

def overlay_template(
        image_path,
        template_path):

    base = Image.open(image_path).convert("RGBA")

    template = Image.open(
        template_path
    ).convert("RGBA")

    template=template.resize(base.size)

    combined = Image.alpha_composite(
        base,
        template
    )

    return combined