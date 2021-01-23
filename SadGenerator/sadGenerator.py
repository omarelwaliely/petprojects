import cv2 as cv
import numpy as num
import sys
import random

caption = ""
image = cv.imread("image.jpg")
BWimage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imwrite("BW.jpg", BWimage)
BWimage = cv.imread("BW.jpg")
ask = input("Put a default (d) or enter caption: ")
if ask == 'd' or ask == 'D':
    random.seed()
    num = int(random.uniform(0, 15))
    if num == 1:
        caption = "Crying alone does not show that you are weak but it shows that you are strong."
    if num == 2:
        caption = "Wipeout your own tears, because if people come to you they will come for a deal."
    if num == 3:
        caption = "When you feel the pain, just remember its the signal that your sins are getting less."
    if num == 4:
        caption = "Never compare yourself with others because they dont know your bad time and you dont know about theirs."
    if num == 5:
        caption = "Finding true love is not difficult but to maintain it is very difficult."
    if num == 6:
        caption = "If you ever get rejected by anyone, dont worry the problem is not in you but in that person."
    if num == 7:
        caption = "After every dark night, there is a brighter day waiting for you."
    if num == 8:
        caption = "I was not myself but yet nobody ever noticed."
    if num == 9:
        caption = "Tears are words that cant be explained."
    if num == 10:
        caption = "You can wipe out someones tear but not their memory."
    if num == 11:
        caption = "Its better to leave early rather than to feel the pain all the time."
    if num == 12:
        caption = "Sorrow"
    if num == 13:
        caption = "I wish I could lose this memory as fast as I lost you."
    if num == 14:
        caption = "I dont cry when you leave me, I cry when you dont come."
    if num == 15:
        caption = "Its terrible to lose someone we love, but its even worse to lose ourselves while loving them."
else:
    caption = ask
font = cv.FONT_HERSHEY_TRIPLEX
height, width, channels = image.shape


if int(len(caption)) > 30:
    size = 0.5
else:
    size = 1
cv.putText(BWimage, caption, (20, (height-20)),
           font, size, (0, 0, 255), 2)
cv.imwrite("BW.jpg", BWimage)
cv.waitKey(1)
cv.destroyAllWindows()
for i in range(1, 5):
    cv.waitKey(1)
