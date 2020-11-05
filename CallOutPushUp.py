from typing import List, Union
import pyttsx3
import time

"""
This is a simple implementation of text-to-speech (TTS) assistant, which helps time push up workouts.
Several parameters can be set for preference in do_push_up function, e.g., 
In one push up, the duration of "up" movement: 'up_duration_in_one_push_up_in_seconds'; 
In one push up, the duration of "hold-on" movement: 'hold_on_duration_in_one_push_up_in_seconds';
In one push up, the duration of "duration" movement: 'down_duration_in_one_push_up_in_seconds';
Total number of circles of push up: 'total_circles'
"""


def call_out(text: List[str], repeat_times: int,
             minimum_seconds_per_call_out: Union[int, float] = 1):
    time.sleep(5)
    engine = pyttsx3.init()
    engine.setProperty('rate', int(minimum_seconds_per_call_out * 100))  # setting up new voice rate
    for i in range(repeat_times):
        engine.say(str(text + [f"第{i + 1}个"]))
        engine.runAndWait()


def do_push_up(up_duration_in_one_push_up_in_seconds: int = 3,
               hold_on_duration_in_one_push_up_in_seconds: int = 1,
               down_duration_in_one_push_up_in_seconds: int = 3,
               total_circles: int = 50):
    one_circle = [str(i) for i in range(1, up_duration_in_one_push_up_in_seconds + 1)] + \
                 ['hold'] * hold_on_duration_in_one_push_up_in_seconds + \
                 [str(i) for i in range(down_duration_in_one_push_up_in_seconds, 0, -1)]
    call_out(one_circle, total_circles)


if __name__ == '__main__':
    while True:
        this_total_circle = int(input())
        do_push_up(total_circles=this_total_circle)
