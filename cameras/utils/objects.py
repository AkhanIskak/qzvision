''' Module for trackable object classes '''


class TrackableObject:
    def __init__(self, object_id: int, centroid):
        self.object_id = object_id
        self.centroids = [centroid]
        self.counted = False
