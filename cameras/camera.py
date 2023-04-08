''' Module for objects tracking '''
from imutils.video import FPS
from imutils import resize
from typing import Dict, Tuple
import numpy as np
import dlib
import cv2

from utils.trackers import CentroidTracker
from utils.objects import TrackableObject
import config


class Camera:
    ''' Class representing camera and vision functionality '''
    height: int = None
    width: int = None

    status: str = None

    max_width: int = 500
    total_frames: int = 0

    confidence: float = config.Vision.CONFIDENCE.value
    skip_frames: int = config.Vision.SKIP_FRAMES.value
    scale_factor: float = config.Vision.SCALE_FACTOR.value
    mean: float = config.Vision.MEAN.value

    font: int = cv2.FONT_HERSHEY_SIMPLEX
    font_scale: float = 0.5
    font_color: Tuple[int] = config.Colors.WHITE.value
    font_thickness: int = 1

    circle_radius: int = 4
    circle_thickness: int = -1

    def __init__(self, device: int = None, video: str = None):
        if device:
            self.capture = cv2.VideoCapture(device)
            self.video = False
        elif video:
            self.capture = cv2.VideoCapture(video)
            self.video = True
        else:
            raise ValueError('Video capture source was not provided')

        self.tracker = CentroidTracker(max_disappeared=40, max_distance=50)

        self.trackers: list = list()
        self.trackable_objects: Dict[int, TrackableObject] = dict()
        self.fps = FPS().start()

        self.total_up = 0
        self.total_down = 0

        self.net = cv2.dnn.readNetFromCaffe(
            config.Vision.INFO.value,
            config.Vision.MODEL.value
        )

    def activate(self):
        self.active = True

        while self.active:
            frame = self.capture.read()
            frame = frame[1] if self.video else frame

            if self.video and frame is None:
                break

            frame = resize(frame, width=self.max_width)

            self.handler(frame)
            self.display(frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.fps.stop()
        cv2.destroyAllWindows()

    def handler(self, frame):
        self.rects = list()

        self.waiting()
        self.resize(frame)

        rgb: cv2.Mat = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if self.total_frames % self.skip_frames == 0:
            detections = self.detect(frame)
            self.trackers = list()

            for i in np.arange(0, detections.shape[2]):
                confidence = detections[0, 0, i, 1]

                if confidence > self.confidence:
                    index = int(detections[0, 0, i, 1])

                    if not self.is_person(index):
                        break

                    coordinates = self.get_coordinates(detections, i)
                    tracker = self.get_tracker(*coordinates, rgb)

                    self.trackers.append(tracker)

                self.i = i
        else:
            for tracker in self.trackers:
                self.tracking()

                tracker.update(rgb)
                positions = tracker.get_position()

                self.rects.append([int(position) for position in (
                    positions.left(), positions.top(), positions.right(), positions.bottom())])

    def display(self, frame):
        self.draw_line(frame)
        # self.draw_text(frame)
        self.draw_info(frame)

        objects = self.tracker.update(self.rects)

        for object_id, centroid in objects.items():
            trackable_object = self.trackable_objects.get(object_id, None)

            if trackable_object is None:
                trackable_object: TrackableObject = TrackableObject(
                    object_id, centroid)
            else:
                direction = centroid[1] - np.mean([centroid_object[1]
                                                  for centroid_object in trackable_object.centroids])
                trackable_object.centroids.append(centroid)

                if not trackable_object.counted:
                    if direction < 0 and centroid[1] < self.height // 2:
                        self.total_up += 1
                        trackable_object.counted = True
                    elif direction > 0 and centroid[1] > self.height // 2:
                        self.total_down += 1
                        trackable_object.counted = True

            self.trackable_objects[object_id] = trackable_object

            self.draw_tracker(frame, object_id, centroid)
            self.draw_circle(frame, centroid)

        cv2.imshow(config.Graphics.TITLE.value, frame)

        self.total_frames += 1
        self.fps.update()

    def draw_tracker(self, frame, object_id: int, centroid):
        cv2.putText(
            img=frame,
            text=f'ID {object_id}',
            org=(centroid[0] - 10, centroid[1] - 10),
            fontFace=self.font,
            fontScale=self.font_scale,
            color=self.font_color,
            thickness=self.font_thickness
        )

    def draw_circle(self, frame, centroid):
        cv2.circle(
            img=frame,
            center=(centroid[0], centroid[1]),
            radius=self.circle_radius,
            color=config.Colors.WHITE.value,
            thickness=self.circle_thickness
        )

    def draw_line(self, frame):
        center = self.center

        cv2.line(
            img=frame,
            pt1=center[0],
            pt2=center[1],
            color=config.Graphics.LINE_COLOR.value,
            thickness=config.Graphics.LINE_THICKNESS.value
        )

    def draw_info(self, frame):
        info = [
            ("Exit", self.total_up),
            ("Enter", self.total_down),
            ("Status", self.status)
        ]

        for index, (key, value) in enumerate(info):
            cv2.putText(
                img=frame,
                text=f'{key}: {value}',
                org=(10, self.height - ((index * 20) + 20)),
                fontFace=self.font,
                fontScale=self.font_scale,
                color=self.font_color,
                thickness=self.font_thickness
            )

    def get_tracker(self, start_x: int, start_y: int,
                    end_x: int, end_y: int, rgb: cv2.Mat):
        rectangle = dlib.rectangle(start_x, start_y, end_x, end_y)

        tracker = dlib.correlation_tracker()
        tracker.start_track(rgb, rectangle)

        return tracker

    def get_coordinates(self, detections, i):
        box = detections[0, 0, i, 3:7] * \
            np.array([self.width, self.height,
                      self.width, self.height])
        return box.astype('int')

    def detect(self, frame):
        self.detecting()
        self.net.setInput(
            cv2.dnn.blobFromImage(
                image=frame,
                scalefactor=self.scale_factor,
                size=self.size,
                mean=self.mean
            )
        )

        return self.net.forward()

    def resize(self, frame):
        if self.width is None or self.height is None:
            self.height = frame.shape[0]
            self.width = frame.shape[1]

    def waiting(self) -> None:
        self.status = config.Status.WAITING.value

    def detecting(self) -> None:
        self.status = config.Status.DETECTING.value

    def tracking(self) -> None:
        self.status = config.Status.TRACKING.value

    def deactivate(self) -> int:
        self.active = False
        return self.total_up - self.total_down

    def is_person(self, index: int) -> bool:
        return index == config.Vision.CLASSES.value.index('person')

    @property
    def size(self) -> Tuple[int]:
        return (self.width, self.height)

    @property
    def center(self) -> Tuple[int]:
        return ((0, self.height // 2), (self.width, self.height // 2))


if __name__ == '__main__':
    # camera = Camera(video='./video/bus-doors.mp4')
    camera = Camera(video='./video/street-cam.mp4')
    camera.activate()
