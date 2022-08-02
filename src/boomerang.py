import cv2
import os
from shutil import rmtree
from vid_to_img import Vid2Img

class Boomerang:
    def __init__(self, path, filename, out_path, fps, output_name, video_extension, create_frames, loop):
        self.frame_path = path + "frames/"
        self.img_extension = ".jpg"
        self.fps = fps
        self.out_path = out_path
        self.output_name = output_name
        self.video_extension = video_extension
        self.loop = loop

        self.frames = self.setFrames(path, filename, create_frames)

    def setFrames(self, vid_path, filename, create_frames):
        # Create frames
        if create_frames:
            vid_to_img = Vid2Img(vid_path, filename, self.video_extension, self.img_extension)
            vid_to_img.run()

        os.chdir(self.frame_path)

        frames = [img for img in os.listdir(self.frame_path) if img.endswith(self.img_extension)]
        frames.sort()

        # Create Boomerang effect
        for i in range (len(frames) - 2, 0, -1):
            frames.append(frames[i])

        # Loop video
        out_frames = []
        for j in range (self.loop):
            for i in range (len(frames) - 1):
                out_frames.append(frames[i])

        return out_frames

    def run(self):
        print(self.frames)

        frame = cv2.imread(os.path.join(self.frames[0]))
        height, width, layers = frame.shape

        os.chdir(self.out_path)

        video = cv2.VideoWriter(self.output_name + self.video_extension, cv2.VideoWriter_fourcc(*'DIVX'), self.fps, (width, height))

        for frame in self.frames:
            video.write(cv2.imread(os.path.join(self.frame_path, frame)))


        cv2.destroyAllWindows()
        video.release()

        # Delete frame directory to save space
        try:
            rmtree(self.frame_path)
        except OSError as e:
            print("Error: %s : %s" % (self.frame_path, e.strerror))
