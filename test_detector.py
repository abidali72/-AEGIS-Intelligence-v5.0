import unittest
from detector import SmokingDetector

class TestSmokingDetector(unittest.TestCase):
    def setUp(self):
        self.detector = SmokingDetector()

    def test_classify_product(self):
        self.assertEqual(self.detector.classify_product({'label': 'cell phone', 'confidence': 0.8}), 'Smart Device')
        self.assertEqual(self.detector.classify_product({'label': 'unknown', 'confidence': 0.8}), 'Unidentified Object')
        self.assertEqual(self.detector.classify_product({'label': 'cell phone', 'confidence': 0.15}), 'Suspected Cigarette')

    def test_estimate_height(self):
        person = {'bbox': [0, 0, 100, 200]}
        self.assertEqual(self.detector.estimate_height(person, 480), 0.7)

    def test_get_contextual_event_empty(self):
        event, status, mouth_zone = self.detector.get_contextual_event([], [], False)
        self.assertIsNone(event)
        self.assertEqual(status, 'Static/Empty')

    def test_get_contextual_event_smoking(self):
        people = [{'bbox': [100, 100, 200, 300], 'estimated_height': 1.7}]
        # Mouth zone for person:
        # pw = 100, ph = 200
        # mx1 = 100 + 35 = 135, my1 = 100 + 30 = 130
        # mx2 = 100 + 65 = 165, my2 = 100 + 70 = 170
        detections = [{'label': 'cell phone', 'confidence': 0.15, 'bbox': [140, 140, 150, 150]}]
        event, status, mouth_zone = self.detector.get_contextual_event(detections, people, True)
        self.assertIsNotNone(event)
        self.assertEqual(event['category'], 'SMOKING')
        self.assertEqual(event['product'], 'Cigarette')

if __name__ == '__main__':
    unittest.main()
