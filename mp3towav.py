import os
from pydub import AudioSegment
root_dir = os.path.join(os.getcwd(), 'sound')
for file in os.listdir(root_dir):
    if file.endswith('.mp3'):
        print(os.path.join(root_dir, file))
        sound = AudioSegment.from_mp3(os.path.join(root_dir, file))
        file = file[:-3] + 'wav'
        print(os.path.join(root_dir, file))
        sound.export(os.path.join(root_dir, file), format="wav")
