import cv2
import numpy as np

from .model import efficientdet
from .utils import preprocess_image, postprocess_boxes

DEFAULT_PARAMS = {
    'phi': 0,
    'weighted_bifpn': False,
    'image_sizes': (512, 640, 768, 896, 1024, 1280, 1408),
    'image_size': 512,
    'num_classes': 4,
    'score_threshold': 0.3,
}


class Recognition:

    def __init__(self, model_path, build_params=None):
        self.build_params = build_params or DEFAULT_PARAMS
        self.model = self.create_model(
            self.build_params['phi'],
            self.build_params['weighted_bifpn'],
            self.build_params['num_classes'],
            self.build_params['score_threshold'],
            model_path)


    def create_model(self, phi, weighted_bifpn, num_classes, score_threshold, model_path):
        _, model = efficientdet(phi=phi, weighted_bifpn=weighted_bifpn,
                                num_classes=num_classes, score_threshold=score_threshold)
        model.load_weights(model_path, by_name=True)
        return model

    def recognize(self, image_path):
        image = cv2.imread(image_path)
        # BGR -> RGB
        image = image[:, :, ::-1]
        h, w = image.shape[:2]

        image, scale = preprocess_image(
            image, image_size=self.build_params['image_size'])

        # run network
        boxes, scores, labels = self.model.predict_on_batch(
            [np.expand_dims(image, axis=0)])
        boxes, scores, labels = np.squeeze(
            boxes), np.squeeze(scores), np.squeeze(labels)

        boxes = postprocess_boxes(boxes=boxes, scale=scale, height=h, width=w)

        # select indices which have a score above the threshold
        indices = np.where(scores[:] > self.build_params['score_threshold'])[0]

        # select those detections
        boxes = boxes[indices]
        labels = labels[indices]
        return labels, boxes
