import cv2
import imutils
import numpy
from typing import Any, Iterator


class CV2Capture:
    def __init__(self, video_input: int | str, windows_name: str = "F"):
        self.input = video_input
        self.playing: bool = False
        self.window_name: str = windows_name
        self.first_frame: bool = False

    def __iter__(self) -> Iterator[numpy.ndarray]:
        self.playing = True
        while self.playing:
            ret, self.frame = self.capture.read()
            yield self.frame

    def show(self, frame: numpy.ndarray | None = None):
        if frame is None:
            frame = self.frame
        if (key := cv2.waitKey(25)) & 0xFF == ord("q") or key in [27, 1048603]:
            self.playing = False
        if cv2.getWindowProperty(self.window_name, cv2.WND_PROP_VISIBLE) == 0.0:
            if not self.first_frame:
                self.first_frame = True
            else:
                self.playing = False

        cv2.imshow(self.window_name, frame)

    def __enter__(self):
        self.capture: cv2.VideoCapture = cv2.VideoCapture(self.input)
        return self

    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any):
        self.playing = False
        self.capture.release()
        cv2.destroyAllWindows()
