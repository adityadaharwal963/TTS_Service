# import torch
# import torchaudio as ta
# from chatterbox.tts import ChatterboxTTS

# device = "mps" if torch.backends.mps.is_available() else "cpu"
# map_location = torch.device(device)

# torch_load_original = torch.load
# def patched_torch_load(*args, **kwargs):
#     if 'map_location' not in kwargs:
#         kwargs['map_location'] = map_location
#     return torch_load_original(*args, **kwargs)

# torch.load = patched_torch_load
# # import required modules

# def wav_to_text(wav):
#     """
#     Converts a WAV audio file to MP3 format.

#     Args:
#         input_wav_path (str): The file path of the input WAV file.

#     Returns:
#         str: The file path of the converted MP3 file.
#     """



# def text_to_speech(text):
#     """
#     Generate a MP# audio file from given text.

#     Args:
#         text (str): The text to convert to speech.

#     Returns:
#         str: The file path of the converted MP3 file.
#     """
#     model = ChatterboxTTS.from_pretrained(device=device)
#     AUDIO_PROMPT_PATH = "test.wav"
#     wav = model.generate(
#     text, 
#     audio_prompt_path=AUDIO_PROMPT_PATH,
#     exaggeration=1.0,
#     cfg_weight=0.8
#     )
#     #tesnor_to_mp3
#     ta.save("test1.mp3", wav, model.sr)
