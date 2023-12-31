import wave
import struct

k = int(input())
source = wave.open("in.wav", mode="rb")
dest = wave.open("out.wav", mode="wb")
dest.setparams(source.getparams())
frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))

newdata = []
for i in data:
    value = i * k
    if value > 32767:
        value = 32767
    if value < -32768:
        value = -32768
    newdata.append(int(value))

newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
dest.writeframes(newframes)
source.close()
dest.close()