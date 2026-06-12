import cv2

def draw_area(image, area):

    x,y,w,h = area

    cv2.rectangle(
        image,
        (x,y),
        (x+w,y+h),
        (0,0,255),
        3
    )

    return image