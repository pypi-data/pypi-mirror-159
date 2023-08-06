#!/usr/bin/env python
# encoding: utf-8
#
# Copyright 2022 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import os
import pathlib
import sys
import threading
import time
from contextlib import contextmanager
from typing import Iterator, Optional, Union

TF_LOG_LEVEL_KEY = "TF_CPP_MIN_LOG_LEVEL"
TF_LOG_LEVEL_NO_WARNINGS_VALUE = "3"
s_print_lock = threading.Lock()
OUTPUT_EMOJIS = {
    "MIDI": "💅",
    "MODEL_OUTPUT_NPZ": "💁‍♀️",
    "MIDI_SONIFICATION": "🎧",
    "NOTE_EVENTS": "🌸",
}


def generating_file_message(output_type: str) -> None:
    """Print a message that a file is being generated

    Args:
        output_type: string indicating which kind of file is being generated

    """
    print(f"\n\n  Creating {output_type.replace('_', ' ').lower()}...")


def file_saved_confirmation(output_type: str, save_path: Union[pathlib.Path, str]) -> None:
    """Print a confirmation that the file was saved succesfully

    Args:
        output_type: The kind of file that is being generated.
        save_path: The path to output file.

    """
    print(f"  {OUTPUT_EMOJIS[output_type]} Saved to {save_path}")


def failed_to_save(output_type: str, save_path: Union[pathlib.Path, str]) -> None:
    """Print a failure to save message

    Args:
        output_type: The kind of file that is being generated.
        save_path: The path to output file.

    """
    print(f"\n🚨 Failed to save {output_type.replace('_', ' ').lower()} to {save_path} \n")


@contextmanager
def no_tf_warnings() -> Iterator[None]:
    """
    Supress tensorflow warnings in this context
    """
    tf_logging_level = os.environ.get(TF_LOG_LEVEL_KEY, TF_LOG_LEVEL_NO_WARNINGS_VALUE)
    os.environ[TF_LOG_LEVEL_KEY] = TF_LOG_LEVEL_NO_WARNINGS_VALUE
    yield
    os.environ[TF_LOG_LEVEL_KEY] = tf_logging_level


@contextmanager
def entertaining_waiting(operation_name: Optional[str] = None) -> Iterator[None]:
    """
    Display a jazzy loading animation in the commandline for the duration of this context

    Args:
        operation_name: the name of the operation contained in this context to be displayed in
        the commandline
    """
    if operation_name is None:
        operation_name = f"Running Command: '{inspect.stack()[2].function}'"

    loading = True
    loading_states = ["🥁", "🎷", "🎸", "🎻", "🎹", "🪘", "🪗", "🎺", "🪕"]
    blank_message = " " * (len(loading_states) * 2 + len(operation_name))

    def animate() -> None:
        emoji_index = 0
        while loading:
            if emoji_index >= len(loading_states):
                emoji_index = 0
                loading_message = blank_message
            else:
                loading_message = "".join(loading_states[0:emoji_index])

            s_flush()
            s_print(f"\r{operation_name}...  " + loading_message)
            emoji_index += 1
            time.sleep(0.3)

    t = threading.Thread(target=animate)
    t.start()

    yield
    loading = False


def s_print(msg: str) -> None:
    """
    Thread safe print function

    Args:
        msg: the text to be printed to stdout
    """
    with s_print_lock:
        sys.stdout.write(msg)


def s_flush() -> None:
    """
    Thread safe flush function
    """
    with s_print_lock:
        sys.stdout.flush()
