import pyaudio
import wave
import contextlib
import time


def playAudio(filename):
    CHUNK = 1024
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)
    start_time = time.time()
    while countAudioSec(filename) > time.time() - start_time + 0.2:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    p.terminate()


def countAudioSec(filename):
    with contextlib.closing(wave.open(filename, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


filename = 'audio.wav'
playAudio(filename)
