import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self) -> None:
        response_1 = emotion_detector("I am glad this happened")
        self.assertEqual(response_1['dominant_emotion'], 'joy')

        response_2 = emotion_detector("I am really mad about this")
        self.assertEqual(response_2['dominant_emotion'], 'anger')
        
        response_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response_3['dominant_emotion'], 'disgust')
        
        response_4 = emotion_detector("I am so sad about this")
        self.assertEqual(response_4['dominant_emotion'], 'sadness')
        
        response_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response_5['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
