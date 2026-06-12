import numpy as np

def find_candidate_areas(mask):

    rows, cols = mask.shape

    heights = [0] * cols

    rectangles = []

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

                if area < 10000:
                    continue

                x = (
                    0
                    if not stack
                    else stack[-1] + 1
                )

                y = r - h + 1

                rectangles.append(
                    (
                        int(x),
                        int(y),
                        int(w),
                        int(h),
                        int(area)
                    )
                )

    rectangles.sort(
        key=lambda x: x[4],
        reverse=True
    )

    return rectangles[:10]