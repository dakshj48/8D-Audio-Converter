import numpy as np
from tqdm import tqdm
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from pydub import AudioSegment
from argparse import ArgumentParser


def convert(inputfile, outputfile, period):
    if period < 0:
        period = period*(-1)
    audio = AudioSegment.from_file(inputfile, format='mp3')
    audio = audio + AudioSegment.silent(duration=150)
    fileinfo = MP3(inputfile, ID3=EasyID3)

    eightD = AudioSegment.empty()
    pan = 0.9*np.sin(np.linspace(0, 2*np.pi, period))
    chunks = list(enumerate(audio[::100]))

    for i, chunk in tqdm(chunks, desc='Converting', unit='chunks', total=len(chunks)):
        if len(chunk) < 100:
            continue
        newChunk = chunk.pan(pan[i % period])
        eightD = eightD + newChunk

    eightD.export(outputfile, format='mp3', bitrate=str(fileinfo.info.bitrate), tags=tags(fileinfo))


def tags(info):
    ret = dict()
    ret['title'] = info['title'][0]
    ret['album'] = info['album'][0]
    ret['artist'] = info['artist'][0]
    ret['genre'] = info['genre'][0]
    return ret


if __name__ == '__main__':
    parser = ArgumentParser(description='Convert to 8D.')
    parser.add_argument('-i', type=str, required=True, help='input file')
    parser.add_argument('-o', type=str, default=parser.parse_args().i[:-4] + ' - 8D.mp3',
                        help='output file (default: fileName - 8D.mp3)')
    parser.add_argument('-period', type=int, default=200, help='panning period (default: 200)')
    args = parser.parse_args()

    convert(args.i, args.o, args.period)
