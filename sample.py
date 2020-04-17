from utils import translate_and_compose

input_file = "sample.en.srt"

# Translate the subtitle into Japanese, save both English and Japanese to the output srt file
# In Japanese(Chinese, Korean), words are characters which are NOT separated by space, so space=False (default)
translate_and_compose(input_file, 'sample_en_ja_both.srt', 'en', 'ja')

