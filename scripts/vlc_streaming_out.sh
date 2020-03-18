
#
# references
#  * https://medium.com/@petehouston/streaming-webcam-to-http-using-vlc-dda7259176c9
#  * ttps://wiki.videolan.org/Documentation:Streaming_HowTo_New/
#

#vlc v4l2:///dev/video0 --sout '#transcode{vcodec=h264,acodec=mp3,ab=128,channels=2,samplerate=44100}:http{dst=localhost:8080/go.mpg}'
#vlc v4l2:///dev/video0 --sout '#transcode{vcodec=mjpg}:http{dst=localhost:8080/go.mpg}'
vlc v4l2:///dev/video0 --sout '#transcode{vcodec=mjpg}:std{access=http,mux=mpjpeg,dst=localhost:8080}'
