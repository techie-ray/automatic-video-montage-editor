# automatic-video-montage-editor
This python program automatically create a music video montage by extracting and combining randomly selected videos. You can specify the duration of the montage and the number of videos contained in the montage.

## PREREQUISITTES
* Install moviepy (see https://pypi.org/project/moviepy/ for installation instructions)
* A folder containing at least __10 video samples__ (mp4 format). You can have any number of video samples of any content __(VIDEO FOLDER)__ 
* A folder containing your music samples (mp3 format). You can have any number of musics samples of any content __(MUSIC FOLDER)__
* Make sure you save the main.py file into the same folder that contains the Video Folder and Music Folder __(PROJECT FOLDER)__

## HOW TO RUN THE PROGRAM
* In your command prompt, navigate to the Project Folder
* The run command is: ```python main.py```
* You can specify the number of samples and duration of montage (in seconds) by adding the arguments: ```python main.py --samples=10 --duration=20```
  * In this example, the program will create a 20 second montage using 10 video samples. 
  * If the ```--samples``` and ```--duration``` are not specified, the default will be 10 video samples and 10 seconds respectively. 
  * __NOTE that the number of samples specified must be lower than or equal to the number of videos in the Video Folder.__ If you have less than 10 video samples in the Video Folder, then you can change the default samples value at line 49.
  
* On execution, the program will ask for the folder address (absolute path) of the Video Folder and the Music Folder.
* Depending on the specified duration, the program will then take around 1 minute to output the montage. The montage will be automatically saved in the Project Folder
 

