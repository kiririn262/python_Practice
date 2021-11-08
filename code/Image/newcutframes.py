# coding: utf-8

import os
import shutil
import cv2
import numpy as np
import pandas as pd



def delete_and_make_directory(dir_path='D:/python/image_dir/'):
	# Delete the entire directory tree if it exists.
	if os.path.exists(dir_path):
		shutil.rmtree(dir_path)  
	
	# Make the directory if it doesn't exist.
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)


def video_2_frames(video_file='./%s.mp4', image_dir='D:/python/image_dir/', image_file='img_%s.png'):
	# Delete the entire directory tree if it exists.
	if os.path.exists(image_dir):
		shutil.rmtree(image_dir)  
	
	# Make the directory if it doesn't exist.
	if not os.path.exists(image_dir):
		os.makedirs(image_dir)

	# Video to frames
	i = 0
	cap = cv2.VideoCapture(video_file)
	while(cap.isOpened()):
		flag, frame = cap.read()  # Capture frame-by-frame
		if flag == False:  # Is a frame left?
			break
		cv2.imwrite(image_dir+image_file % str(i).zfill(6), frame)  # Save a frame
		print('Save', image_dir+image_file % str(i).zfill(6))
		i += 1

	cap.release()  # When everything done, release the capture


def get_target_files(dir_path='./image_dir/', cond='.png'):
	files = [f for f in os.listdir(dir_path) if f[-4:]=='.png']

	return files


def make_df_from_list_and_array():
	col1 = [0,1,2,3,4] 
	col2 = np.array([5,6,7,8,9])
	
	df = pd.DataFrame({'col_list':col1, 'col_array':col2})
	print(df)