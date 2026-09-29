import unittest
import numpy as np
import cv2
from detector import SmokingDetector

class TestSmokingDetector(unittest.TestCase):
    def setUp(self):
        self.detector = SmokingDetector()

    def test_classify_product(self):
        det_phone = {"label": "cell phone", "confidence": 0.85}
        self.assertEqual(self.detector.classify_product(det_phone), "Smart Device")

        det_unknown = {"label": "unknown_item", "confidence": 0.15}
        self.assertEqual(self.detector.classify_product(det_unknown), "Suspected Cigarette")

    def test_estimate_height(self):
        person_det = {"bbox": [100, 50, 200, 450]} # box_h = 400
        height = self.detector.estimate_height(person_det, 600)
        self.assertEqual(height, round(400 * 0.0035, 2))

    def test_detect_blank_frame(self):
        blank_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        detections, people, motion_detected = self.detector.detect(blank_frame)
        self.assertIsInstance(detections, list)
        self.assertIsInstance(people, list)
        self.assertIsInstance(motion_detected, (bool, np.bool_))

    def test_draw_detections(self):
        blank_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        people = [{"bbox": [50, 50, 150, 300], "estimated_height": 1.75}]
        detections = [{"bbox": [80, 100, 100, 120], "label": "cell phone", "confidence": 0.9}]
        mouth_zone = [70, 80, 110, 110]

        output_frame = self.detector.draw_detections(blank_frame.copy(), detections, people, mouth_zone)
        self.assertEqual(output_frame.shape, blank_frame.shape)

if __name__ == '__main__':
    unittest.main()
