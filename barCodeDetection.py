# MARK:- Libs
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# MARK:- Support functions


def hasConnectedComponents(img, r, c):
    # find connected pixel with img[r][c]
    cur_px = img[r][c]  # current pixel
    connected_neighbor = []  # find connected neighbor pixel
    if (img[r][c+1] == cur_px):
        connected_neighbor.append((r, c+1))

    if (img[r][c-1] == cur_px):
        connected_neighbor.append((r, c-1))

    if (img[r+1][c] == cur_px):
        connected_neighbor.append((r+1, c))

    if (img[r+1][c+1] == cur_px):
        connected_neighbor.append((r+1, c+1))

    if (img[r+1][c-1] == cur_px):
        connected_neighbor.append((r+1, c-1))

    if (img[r-1][c] == cur_px):
        connected_neighbor.append((r-1, c))

    if (img[r-1][c+1] == cur_px):
        connected_neighbor.append((r-1, c+1))

    if (img[r-1][c-1] == cur_px):
        connected_neighbor.append((r-1, c-1))

    return connected_neighbor

# MARK:- Read input file


img = cv.imread('barCodesDetection.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

row = len(img) - 1
col = len(img[0]) - 1

# MARK:- Get binary image

j_img = (img < 120) * 1

# MARK:- Find connected components
connected_comps = []
current_comp = []
for r in range(1, row-1):
    for c in range(1, col-1):
        if(j_img[r][c] == 1 and j_img[r][c] not in current_comp):
            current_comp.append((r, c))
            neighbors = hasConnectedComponents(j_img, r, c)

            for (i, j) in neighbors:
                print(i)
                print(j)
                print(j_img[i][j])
                print("===")

for (r, c) in current_comp:
    print(j_img[r][c])
# MARK:- Show output
plt.imshow(j_img, cmap=plt.cm.gray)
plt.show()
# cv.imshow('input', out)
# cv.waitKey(0)
# cv.destroyAllWindows()
