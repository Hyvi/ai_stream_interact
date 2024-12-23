import os
import cv2
import threading


class Streamer:
    def __init__(self, cam_index: int) -> None:
        """Streams video from a USB camera."""
        self._cam_index = cam_index
        self.cap = cv2.VideoCapture("rtmp://47.xx.53.xxx/live/7CTDM3D00BV272_165-0-7?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9kdWN0X2lkIjoiNzEzNTE5ZmIxYjRlNDRiYTlkMjdkMDJhOGRlZDk5NGQiLCJjaGFubmVsX25hbWUiOiI3Q1RETTNEMDBCVjI3Ml8xNjUtMC03IiwiYWN0aW9uIjoicGxheSIsInVpZCI6MjAwMCwiZXhwIjoxNzMyMzUwMzA1LCJuYmYiOjE3MzIzNDY3MDUsImlhdCI6MTczMjM0NjcwNX0.gS-OhVh9C45zqJaVGOsi1u6J9sSPm7SjfdCdZONU2z8")
        self._success, self._frame = self.cap.read()
        self._video_stream_is_stopped = True

    def start_video_stream(self) -> None:
        threading.Thread(target=self._run, args=()).start()

    def _run(self) -> None:
        self._video_stream_is_stopped = False
        while not self._video_stream_is_stopped:
            if not self._success:
                self._stop_video_stream()
            else:
                self._ret, self._frame = self.cap.read()
#                cv2.imshow("video", self._frame)
                if cv2.waitKey(1) == ord("q") & 0xFF:
                    self.stop_video_stream()
                    self.cap.release()
                    cv2.destroyWindow("video")
                    os._exit(1)

    def stop_video_stream(self) -> None:
        self._video_stream_is_stopped = True
