import queue
import sounddevice as sd

from vosk import KaldiRecognizer
from scripts.DownloadModel import model


q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print()
    q.put(bytes(indata))


def ResultWord():
    resultat = ""
    try:
        with sd.RawInputStream(samplerate=42000, blocksize = 8000, device=sd.default.device,
                dtype="int16", channels=1, callback=callback):

            rec = KaldiRecognizer(model, 42000)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    res = rec.FinalResult()
                    resultat = res[14:len(res)-3]
                    return resultat
                
                # else:
                #     print(rec.PartialResult())

    except KeyboardInterrupt:
        print("\nDone")


  

