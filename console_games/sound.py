""'''from playsound import playsound
import multiprocessing
import pyaudio
import wave
import sys

class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

class AudioPlayer:
    def __init__(self):
        """Initialise a sound."""
        self._mute = False
        self._current_sound = None

    def play(self, dir):
        if not self._mute:
            a = AudioFile("test.mp3")
            a.play()
            a.close()

    """
    
    """
    def toggle_mute(self):
        self._mute = not self._mute
        if not self._current_sound == None:

            self._current_sound.terminate()'''""

"proper audio soon"

from pygame import mixer

mixer.init()

class AudioPlayer:
    def __init__(self):
        """Initialise a sound."""
        self._mute = False
        self._current_sound = None

    def play(self, dir):
        mixer.music.load(dir)
        mixer.music.play(1)

    