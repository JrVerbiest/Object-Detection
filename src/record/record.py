""" 
    A script. 
    To get something up and running.
    Record => at time on image => save to file (avi) 
"""

import os
import time
from datetime import date

import argparse

import numpy as np

import pyrealsense2 as rs
import cv2

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

# -------------------------------------------------------------------------------------------------
# parameters

video_fps = 30
frameSize = [640, 480]

# -------------------------------------------------------------------------------------------------

# Text time on image
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_LOCATION = (30,35)
FONT_SCALE = 0.8
FONT_COLOR = (0,0,255) # red color
FONT_THICKNESS = 2

def record(filename):
    today = date.today()

    # Configure color streams
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color,  frameSize[0], frameSize[1], rs.format.bgr8, video_fps)

    # Start streaming
    profile = pipeline.start(config)
    color_sensor = profile.get_device().query_sensors()[1]
    logger.info(color_sensor)

    fourcc = cv2.VideoWriter_fourcc(*'XVID') # fourcc == encoder of the video 
    out = cv2.VideoWriter(filename, fourcc, video_fps, (frameSize[0], frameSize[1]))

    frame_number = 0

    try:
        while True:
            frame = pipeline.wait_for_frames()
            frame_number += 1

            color_frame = frame.get_color_frame()
            color_image = np.asanyarray(color_frame.get_data())

            cv2.imshow('', color_image)
            
            if frame_number == 1:
                starttime_ms = time.time()*1000

            timestamp_ms = round(time.time()*1000 - starttime_ms)

            txt = str(today)+' fr'+str(frame_number)+' t'+str(timestamp_ms)+' ms'
            cv2.putText(color_image,txt,FONT_LOCATION, FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS,cv2.LINE_AA)
            
            out.write(color_image)
            key = cv2.waitKey(1)
            
            logger.info(frame_number)
            if key == ord('q'):
                break

    finally:
        # Stop streaming
        pipeline.stop()
        # out.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Intel Realsense D435i Recorder')

    parser.add_argument("--filename", type=str, default='test', help='filename')
    
    arg = parser.parse_args()

    record(os.path.join(arg.filename+"_"+str(int(time.time()))+'.avi'))