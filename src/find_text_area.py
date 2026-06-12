import numpy as np

print("NEW FIND_TEXT_AREA LOADED")

def find_text_area(mask):

    rows, cols = mask.shape

    heights = [0] * cols

    best_area = 0
    best_rect = None

    for r in range(rows):

        for c in range(cols):

            if mask[r, c]:
                heights[c] += 1
            else:
                heights[c] = 0

        stack = []

        c = 0

        while c <= cols:

            current_height = (
                heights[c]
                if c < cols
                else 0
            )

            if (
                not stack
                or current_height >= heights[stack[-1]]
            ):

                stack.append(c)
                c += 1

            else:

                top = stack.pop()

                h = heights[top]

                w = (
                    c
                    if not stack
                    else c - stack[-1] - 1
                )

                area = h * w

                if area > best_area:

                    best_area = area

                    x = (
                        0
                        if not stack
                        else stack[-1] + 1
                    )

                    y = r - h + 1

                    best_rect = (
                        int(x),
                        int(y),
                        int(w),
                        int(h)
                    )

    print("BEST RECT =", best_rect)

    return best_rect