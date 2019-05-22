import sys
import numpy as np
from tqdm import tqdm
from pydub import AudioSegment

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Need 1 argument.")
        sys.exit(0)
        
    audio = AudioSegment.from_file(sys.argv[1], format="mp3")
    audio = audio + AudioSegment.silent(duration=150)
    
    eightD = AudioSegment.silent(duration=100)
    pan = np.sin(np.linspace(0, 2*np.pi, 101))

    for i, chunk in tqdm(enumerate(audio[::100])):
        if len(chunk) < 100:
            continue
        newChunk = chunk.pan(pan[i%101])
        eightD = eightD + newChunk

    eightD.export('output.mp3', format="mp3")
