import cv2

def draw_candidates(
        image,
        areas):

    colors = [
        (0,0,255),
        (0,255,0),
        (255,0,0),
        (255,255,0),
        (255,0,255)
    ]

    for i, area in enumerate(areas[:5]):

        x,y,w,h,_ = area

        color = colors[
            i % len(colors)
        ]

        cv2.rectangle(
            image,
            (x,y),
            (x+w,y+h),
            color,
            3
        )

    return image