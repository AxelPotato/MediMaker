from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path

filepath = Path(__file__).resolve().parent

file1 = Path.joinpath(filepath, "test1.mp3")
file2 = Path.joinpath(filepath, "test2.mp3")

sound1 = AudioSegment.from_mp3(file1)
sound2 = AudioSegment.from_mp3(file2)

silence_duration_minutes_1 = 0.1
silence_duration_minutes_2 = 0.2

silence_duration = 1000 * 60 * silence_duration_minutes_1 - len(sound1)
silence_duration2 = 1000 * 60 * silence_duration_minutes_2 - len(sound2)

output = AudioSegment.empty()


silent_segment1 = AudioSegment.silent(duration=silence_duration)
silent_segment2 = AudioSegment.silent(duration=silence_duration2)  # duration in milliseconds

output += sound1
output += AudioSegment.silent(duration=silence_duration)
output += sound2
output += AudioSegment.silent(duration=silence_duration2)

output.export('Blok Sida.mp3', format="mp3", tags={'artist': 'Givin School'})
