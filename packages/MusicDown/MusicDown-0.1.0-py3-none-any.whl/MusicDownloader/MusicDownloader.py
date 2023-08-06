# You must have the ffmpeg in the 
# https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z

from __future__ import unicode_literals
import os
import unicodedata
import youtube_dl
import glob
import re
import shutil
import concurrent.futures

# Write the links of the songs which was unable to download in the file 
# fail : Is the list of the faild links
# file : Filename of the file for the faild songs
def write_fail_to_text(fail,file):
    with open(file, 'w') as filehandle:
        filehandle.writelines("%s" % place for place in fail)
    filehandle.close()

class MusicDownloader:
    
    def download(urls,download_path,faild_file):
        """
        Download every url video as mp3 file.
        
        :param urls: The urls to go through
        :type number: list of strings
        
        :param download_path: The folder to move the files after the download.
        :type download_path: string
        
        :param download_path: The file to save the links which was unable to download.
        :type faild_file: string
        """
        
        #Options for the youtube_dl 
        ydl_opts={
            'format' : 'bestaudio/best',
            'postprocessors': [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192', # 192 is the best quality for mp3 files
            }],
        }
        
        fail=[] #List of the faild to download files
        replace_list = ['|','/',':','*','"','?','<','>'] # List of characters to be replaced if it is in the songs name (because Windows does not support)
        
        #if folder songs does not exist create one
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        print(download_path)
        
        # Loop to run the download prosses if it is more songs tho be download
        for x in urls:
            if x[0] != "h":#"https://" not in x or "http://" not in x:
                print(x)
                #pass # If it is bad link skip it
            else:
                try:
                    url = x
                    info_dict = youtube_dl.YoutubeDL(ydl_opts).extract_info(url, download=False) # It is all the info for the song
                    video_title = info_dict.get('title', None) # Video Title
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        video_id = info_dict.get("id", None) # Video ID for further use (To be removed from the download song name)
                        
                        #print(video_title)
                        
                        # FROM HERE
                        title = video_title+".mp3"
                        title = title.replace("-"+video_id, '')
                        
                        for i in replace_list:
                            title = title.replace(i, '')
                        # TO HERE 
                        # Prepare the filename of the song
                        download_path = download_path+"\\"
                        # If the song exist in the folder print exist and skip it
                        if not os.path.exists(download_path+title):
                            ydl.download([url]) # Download the song
                                
                            list_of_files = glob.glob('*.mp3') # Find all the mp3 files
                            latest_file = max(list_of_files, key=os.path.getctime) # Find the song
                            
                            original = latest_file #The song with the current title
                            target = r''+download_path+title #The better titile for the song (Without the Videos ID)
                            shutil.move(original,target) # The "rename" command
                        else:
                            print(title+" exists")

                except Exception as e:
                    # IF an error oqure print it and put the link in the faild list
                    print(str(e))
                    fail.append(x)
                except KeyboardInterrupt:
                    # If the prosses interrupted from the user write the faild song into the file and exit the programme
                    write_fail_to_text(fail,faild_file)
                    sys.exit()
                    return fail
        
        # Write the faild song ONLY if there is any
        if len(fail) != 0:
            write_fail_to_text(fail,faild_file)
