from smb3_eh_manip.video_player import VideoPlayer
from smb3_eh_manip.computers import OpencvComputer
from smb3_eh_manip.settings import config


class CalibrationComputer(OpencvComputer):
    def __init__(self):
        super().__init__(
            VideoPlayer(
                "calibrationvideo", config.get("app", "calibration_video_path")
            ),
            config.get("app", "calibration_start_frame_image_path"),
        )
