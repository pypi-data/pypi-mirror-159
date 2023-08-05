import logging

import cv2
import numpy as np

from smb3_eh_manip.settings import config


class OpencvComputer:
    def __init__(
        self,
        player,
        start_frame_image_path,
        video_capture_source=config.getint("app", "video_capture_source"),
        show_capture_video=config.getboolean("app", "show_capture_video"),
    ):
        self.player = player
        self.start_frame_image_path = start_frame_image_path
        self.video_capture_source = video_capture_source
        self.show_capture_video = show_capture_video
        self.autoreset = config.getboolean("app", "autoreset")
        self.current_frame = -1

    def compute(self):
        self.player.reset()
        reset_template = cv2.imread(config.get("app", "reset_image_path"))
        template = cv2.imread(self.start_frame_image_path)
        cap = cv2.VideoCapture(self.video_capture_source)
        if not cap.isOpened():
            logging.info("Cannot open camera")
            exit()
        while True:
            ret, frame = cap.read()
            if not ret:
                logging.info("Can't receive frame (stream end?). Exiting ...")
                break
            if self.player.playing:
                self.current_frame += 1
            if (
                self.autoreset
                and self.player.playing
                and list(OpencvComputer.locate_all_opencv(reset_template, frame))
            ):
                self.player.reset()
                logging.info(f"Detected reset")
            if not self.player.playing:
                results = list(OpencvComputer.locate_all_opencv(template, frame))
                if self.show_capture_video:
                    for x, y, needleWidth, needleHeight in results:
                        top_left = (x, y)
                        bottom_right = (x + needleWidth, y + needleHeight)
                        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 5)
                if results:
                    self.player.reset()
                    self.player.set_playing(True)
                    self.current_frame = 0
                    logging.info(f"Detected start frame")
            if self.show_capture_video:
                frame = cv2.putText(
                    frame,
                    f"Frame: {self.current_frame}",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2,
                    cv2.LINE_AA,
                )
                cv2.imshow("capture", frame)
            self.player.render()
            cv2.waitKey(1)
        cap.release()
        cv2.destroyAllWindows()

    @classmethod
    def locate_all_opencv(
        cls,
        needleImage,
        haystackImage,
        limit=10000,
        region=None,
        step=1,
        confidence=float(config.get("app", "confidence")),
    ):
        """
        TODO - rewrite this
            faster but more memory-intensive than pure python
            step 2 skips every other row and column = ~3x faster but prone to miss;
                to compensate, the algorithm automatically reduces the confidence
                threshold by 5% (which helps but will not avoid all misses).
            limitations:
            - OpenCV 3.x & python 3.x not tested
            - RGBA images are treated as RBG (ignores alpha channel)
        """

        confidence = float(confidence)

        needleHeight, needleWidth = needleImage.shape[:2]

        if region:
            haystackImage = haystackImage[
                region[1] : region[1] + region[3], region[0] : region[0] + region[2]
            ]
        else:
            region = (0, 0)  # full image; these values used in the yield statement
        if (
            haystackImage.shape[0] < needleImage.shape[0]
            or haystackImage.shape[1] < needleImage.shape[1]
        ):
            # avoid semi-cryptic OpenCV error below if bad size
            raise ValueError(
                "needle dimension(s) exceed the haystack image or region dimensions"
            )

        if step == 2:
            confidence *= 0.95
            needleImage = needleImage[::step, ::step]
            haystackImage = haystackImage[::step, ::step]
        else:
            step = 1

        # get all matches at once, credit: https://stackoverflow.com/questions/7670112/finding-a-subimage-inside-a-numpy-image/9253805#9253805
        result = cv2.matchTemplate(haystackImage, needleImage, cv2.TM_CCOEFF_NORMED)
        match_indices = np.arange(result.size)[(result > confidence).flatten()]
        matches = np.unravel_index(match_indices[:limit], result.shape)

        if len(matches[0]) == 0:
            return

        # use a generator for API consistency:
        matchx = matches[1] * step + region[0]  # vectorized
        matchy = matches[0] * step + region[1]
        for x, y in zip(matchx, matchy):
            yield (x, y, needleWidth, needleHeight)
