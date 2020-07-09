from gtts import gTTS
from io import BytesIO
import pygame
import time
from typing import Iterator
import copy


def call_out(text: Iterator[str], repeat_times: int):
    tts_obj_list = [gTTS(text=this_text) for this_text in text]

    bytes_io_obj = []
    for this_tts_obj in tts_obj_list:
        this_bytes_io_obj = BytesIO()
        this_tts_obj.write_to_fp(this_bytes_io_obj)
        this_bytes_io_obj.seek(0)
        bytes_io_obj.append(this_bytes_io_obj)
    bytes_io_obj = tuple(bytes_io_obj * repeat_times)  # shallow copy to repeat bytes_io_obj for repeat_times

    pygame.mixer.init()
    time_start = time.time()
    for i in range(bytes_io_obj.__len__()):
        pygame.mixer.music.load(copy.deepcopy(bytes_io_obj[i]))
        pygame.mixer.music.play()
        while time.time() - time_start < 1:  # At least one second between each call outs
            continue
        else:
            time_start = time.time()
        while True:
            if not pygame.mixer.music.get_busy():
                break
    pygame.quit()


def do_push_up(up_duration_in_seconds: int = 7,
               hold_on_duration_in_seconds: int = 1,
               down_duration_in_seconds: int = 8,
               total_circles: int = 50):
    one_circle = [str(i) for i in range(1, up_duration_in_seconds + 1)] + \
                 [str(i) for i in range(1, hold_on_duration_in_seconds + 1)] + \
                 [str(i) for i in range(down_duration_in_seconds, 0, -1)]
    call_out(one_circle, total_circles)


if __name__ == '__main__':
    do_push_up(total_circles=2)
