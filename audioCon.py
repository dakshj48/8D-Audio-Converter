import sys
import numpy as np
from tqdm import tqdm
from pydub import AudioSegment
from argparse import ArgumentParser


def convert(inputfile, outputfile, period):
    audio = AudioSegment.from_file(inputfile, format="mp3")
    audio = audio + AudioSegment.silent(duration=150)

    eightD = AudioSegment.silent(duration=100)
    pan = 0.9*np.sin(np.linspace(0, 2*np.pi, period))
    chunks = list(enumerate(audio[::100]))

    for i, chunk in tqdm(chunks, desc='Converting', unit='chunks', total=len(chunks)):
        if len(chunk) < 100:
            continue
        newChunk = chunk.pan(pan[i % period])
        eightD = eightD + newChunk

    eightD.export(outputfile, format="mp3")


if __name__ == '__main__':
    parser = ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', type=str, help='input file')
    parser.add_argument('-o', type=str, default='output.mp3', help='output file (default: output.mp3)')
    parser.add_argument('-period', type=int, default=200, help='panning period (default: 200)')
    args = parser.parse_args()

    convert(args.i, args.o, args.period)
