#!C:\Users\SamRayaneh\Desktop\project\video\myvevn\Scripts\python.exe

import os
import cv2

input_file = r"C:\Users\SamRayaneh\Desktop\project\video\sample_video.mp4"

video = cv2.VideoCapture(input_file)

frame_number = 0

frame_interval = 10

while True :
    ret , frame = video.read()

    if not ret :
        break

    if frame_number % frame_interval == 0 :
        output_path = r'C:\Users\SamRayaneh\Desktop\project\video\save_directory\frame_{}.jpg'.format(frame_number)
    cv2.imwrite(output_path , frame)

    frame_number += 1

video.release()


folder_path = r"C:\Users\SamRayaneh\Desktop\project\video\save_directory"
video_path = r"C:\Users\SamRayaneh\Desktop\project\video\sample_video.mp4"
