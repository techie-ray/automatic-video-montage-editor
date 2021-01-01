from moviepy.editor import *
import os, glob
import random
import argparse

def extract_clip(samples, output_duration):
	extract_duration = output_duration/len(samples)
	extracted_samples = []
	for s in samples:
		start_point = random.uniform(0, s.duration - extract_duration)
		end_point = start_point + extract_duration
		extracted_sample = s.subclip(start_point, end_point)
		extracted_samples.append(extracted_sample)
	return extracted_samples

def combine_clip(samples):
	combined_clip = concatenate_videoclips(samples)
	print('Concatenation done')
	return combined_clip

def select_random_music(music_file_path):
	dir_folder = glob.glob(music_file_path)
	return random.choice(dir_folder)

def main(video_file_path, music_file_path, no_of_videos, output_duration):
	dir_folder = glob.glob(video_file_path)

	#randomly select and load n samples from the dir_folder
	random_sample_paths = random.sample(dir_folder, no_of_videos)
	loaded_samples = [VideoFileClip(x) for x in random_sample_paths]

	#extract and concatenate the samples
	extracted_samples = extract_clip(loaded_samples, output_duration)
	combined_clip = combine_clip(extracted_samples)

	#randomly select music for the montage
	music = select_random_music(music_file_path)
	combined_clip.audio = AudioFileClip(music).subclip(0, output_duration)
	
	#write output
	combined_clip.write_videofile('output.mp4')
	combined_clip.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='video_editor')
	parser.add_argument('--samples', type=int, default=10)
	parser.add_argument('--duration', type=int, default=10)
	args = parser.parse_args()
	video_file_path = input('Enter folder address of video samples: ')
	video_file_path += '\\*'
	music_file_path = input('Enter folder address of music samples: ')
	music_file_path += '\\*'
	main(video_file_path, music_file_path, args.samples, args.duration) 


