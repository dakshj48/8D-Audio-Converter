import numpy as np
import sys
from pydub import AudioSegment


class Run:

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Need 1 argument.")
        else:
            audio = AudioSegment.from_file(sys.argv[1], format="mp3")
            # mono = AudioSegment(audio).set_channels(1)
            eightD = None
            for i, chunk in enumerate(audio[::1000]):
                newChunk = AudioSegment(chunk).pan(np.sin(i))
                eightD = eightD + newChunk
            eightD.export(format="mp3")
