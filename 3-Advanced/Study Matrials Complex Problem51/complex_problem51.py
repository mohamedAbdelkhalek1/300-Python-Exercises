from pydub import AudioSegment
from pydub.playback import play
audio = AudioSegment.from_wav("au.wav")
play(audio)