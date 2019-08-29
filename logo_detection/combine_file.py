from moviepy.editor import*


combined_filename = "render_test.mp4"

def getClipFilename(i):
    return str(i) + ".mp4"
for i in range(0, 82):
    if i == 0:
        combined_file = VideoFileClip(getClipFilename(i))
    else:
        clip = VideoFileClip(getClipFilename(i))
        combined_file = concatenate_videoclips([combined_file, clip])
        combined_file.write_videofile(combined_filename)
