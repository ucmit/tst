import ffmpeg
process = (
    ffmpeg
    .input('mk.mp3')
    .output("out.mp3")
    .overwrite_output()
    .run_async(pipe_stdin=True)
)
# process.communicate(input=input_data)