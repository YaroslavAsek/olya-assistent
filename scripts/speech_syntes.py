import os
import torch
import winsound
import warnings


def makeSound(text: str):
    device = torch.device('cpu')
    torch.set_num_threads(8)
    local_file = 'model.pt'
    warnings.filterwarnings("ignore", category=UserWarning, module="torch")

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v5_ru.pt',
                                    local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    sample_rate = 48000
    speaker='baya'

    audio_paths = model.save_wav(text=text,
                                speaker=speaker,
                                sample_rate=sample_rate)
    

    winsound.PlaySound("test.wav", winsound.SND_ASYNC)