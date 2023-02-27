from PIL import Image
import cv2
import csv
import moviepy.editor as mpe

"""
Resize the video to LED Matrix resolution:

clip = mpe.VideoFileClip("Bad Apple!!.mp4")
clip_resized = clip.resize(newsize=(64, 48))
clip_resized.write_videofile("bad apple resized.mp4")
"""

vid = cv2.VideoCapture("bad apple resized.mp4")
ret, frame = vid.read()

frame_count = 0
x = 0
y = 0

with open("rgb_data.csv", "w", encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["frame, white_pixels"])

    while ret:
        ret, frame = vid.read()

        pil_image = Image.fromarray(frame)

        pix = pil_image.load()

        for y in range(47):
            for x in range(63):
                if pix[x, y] != [0, 0, 0]:
                    writer.writerow([frame_count, x, y])

        frame_count += 1

        print(frame_count)
