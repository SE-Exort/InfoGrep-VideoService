import os

class FFMPEG:
    
    def __init__(self, save_path):
        self.save_path: str = save_path

    @staticmethod
    def run(command: str):
        os.system(command)
        
    def create_frame(self, audio_path, image_path, vfilter=None):
        vfilter = vfilter or "pad=ceil(iw/2)*2:ceil(ih/2)*2"
        command = f"ffmpeg -i {image_path} -i {audio_path} -vf \"{vfilter}\" {self.save_path}"
        print(f"Running {command} for FFMPEG")
        FFMPEG.run(command)

    def concat(self, frames_path): 
        command = f"ffmpeg -f concat -safe 0 -i {frames_path} {self.save_path}"
        FFMPEG.run(command)