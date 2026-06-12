import numpy as np

def find_text_position(mask):

    ys,xs=np.where(mask)

    x=int(np.mean(xs))
    y=int(np.mean(ys))

    return x,y