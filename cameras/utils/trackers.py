''' Module for centroid tracking of objects '''
from scipy.spatial import distance as dist
from collections import OrderedDict

import numpy as np


class CentroidTracker:
    def __init__(self, max_disappeared: int = 50, max_distance: int = 50):
        self.next_object_id = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()

        self.max_disappeared = max_disappeared
        self.max_distance = max_distance

    def register(self, centroid):
        self.objects[self.next_object_id] = centroid
        self.disappeared[self.next_object_id] = 0
        self.next_object_id += 1

    def deregister(self, object_id):
        del self.objects[object_id]
        del self.disappeared[object_id]

    def update(self, rects):
        if len(rects) == 0:
            for object_id in list(self.disappeared.keys()):
                self.disappeared[object_id] += 1

                if self.disappeared[object_id] > self.max_disappeared:
                    self.deregister(object_id)

            return self.objects

        input_centroids = np.zeros((len(rects), 2), dtype="int")

        for (index, (start_x, start_y, end_x, end_y)) in enumerate(rects):
            x = int((start_x + end_x) / 2.0)
            y = int((start_y + end_y) / 2.0)
            input_centroids[index] = (x, y)

        if len(self.objects) == 0:
            for index in range(0, len(input_centroids)):
                self.register(input_centroids[index])

        else:
            object_ids = list(self.objects.keys())
            object_centroids = list(self.objects.values())

            distance = dist.cdist(np.array(object_centroids), input_centroids)

            rows = distance.min(axis=1).argsort()
            cols = distance.argmin(axis=1)[rows]

            used_rows = set()
            used_cols = set()

            for (row, col) in zip(rows, cols):
                if row in used_rows or col in used_cols:
                    continue

                if distance[row, col] > self.max_distance:
                    continue

                object_id = object_ids[row]
                self.objects[object_id] = input_centroids[col]
                self.disappeared[object_id] = 0

                used_rows.add(row)
                used_cols.add(col)

            unused_rows = set(
                range(0, distance.shape[0])).difference(used_rows)
            unused_cols = set(
                range(0, distance.shape[1])).difference(used_cols)

            if distance.shape[0] >= distance.shape[1]:
                for row in unused_rows:
                    object_id = object_ids[row]
                    self.disappeared[object_id] += 1

                    if self.disappeared[object_id] > self.max_disappeared:
                        self.deregister(object_id)
            else:
                for col in unused_cols:
                    self.register(input_centroids[col])
        return self.objects
