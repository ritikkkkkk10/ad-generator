from PIL import Image
import numpy as np

def get_safe_mask(template_path):

    template = Image.open(
        template_path
    ).convert("RGBA")

    alpha = np.array(template)[:,:,3]

    safe = alpha < 10

    return safe