import copy
import time
from io import BytesIO
from typing import Iterable, Union

import pygame
from gtts import gTTS

"""
This is a simple implementation of text-to-speech (TTS) assistant, which helps time push up workouts.
Several parameters can be set for preference in do_push_up function, e.g., 
In one push up, the duration of "up" movement: 'up_duration_in_one_push_up_in_seconds'; 
In one push up, the duration of "hold-on" movement: 'hold_on_duration_in_one_push_up_in_seconds';
In one push up, the duration of "duration" movement: 'down_duration_in_one_push_up_in_seconds';
Total number of circles of push up: 'total_circles'
"""


def call_out(text: Iterable[str], repeat_times: int,
             minimum_seconds_per_call_out: Union[int, float] = 1):
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
        while time.time() - time_start < minimum_seconds_per_call_out:
            continue
        else:
            time_start = time.time()
        while True:
            if not pygame.mixer.music.get_busy():
                break
    pygame.quit()


def do_push_up(up_duration_in_one_push_up_in_seconds: int = 7,
               hold_on_duration_in_one_push_up_in_seconds: int = 1,
               down_duration_in_one_push_up_in_seconds: int = 8,
               total_circles: int = 50):
    one_circle = [str(i) for i in range(1, up_duration_in_one_push_up_in_seconds + 1)] + \
                 [str(i) for i in range(1, hold_on_duration_in_one_push_up_in_seconds + 1)] + \
                 [str(i) for i in range(down_duration_in_one_push_up_in_seconds, 0, -1)]
    call_out(one_circle, total_circles)


if __name__ == '__main__':
    do_push_up(total_circles=3)
