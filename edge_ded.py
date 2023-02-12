import time
from PIL import Image


def main(thrs):
    bl = (0, 0, 0)
    wht = (255 ,255, 255)
    im1 = Image.open("static\\image.jpg")
    iw, ih = im1.size
    t1 = time.time()

    th = thrs
    pix = im1.load()
    print(pix)
    for y in range(ih-1):
        for x in range(iw-1):
            x0, x1, y1 = pix[x,y], pix[x+1, y], pix[x, y+1]
            diffX = ((x0[0]-x1[0])**2)**0.5, ((x0[1]-x1[1])**2)**0.5, ((x0[2]-x1[2])**2)**0.5
            diffY = ((x0[0]-y1[0])**2)**0.5, ((x0[1]-y1[1])**2)**0.5, ((x0[2]-y1[2])**2)**0.5
            if diffX[0] > th or diffX[1] > th or diffX[2] > th:
                pix[x,y] = (255,255,255)
            elif diffY[0] > th or diffY[1] > th or diffY[2] > th:
                pix[x,y] = (255,255,255)
            else:
                pix[x,y] = (0,0,0)

    t2 = time.time()
    im1.save("static\\out.jpg")

    return t2 - t1