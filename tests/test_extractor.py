import unittest
from src.core.extractor import Extractor

class TestExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = Extractor()

    def test_extract_text(self):
        # Test case for extracting text from a paywalled article
        url = "http://example.com/paywalled-article"
        expected_text = "This is the expected text from the article."
        extracted_text = self.extractor.extract_text(url)
        self.assertEqual(extracted_text, expected_text)

    def test_extract_images(self):
        # Test case for extracting images from a paywalled article
        url = "http://example.com/paywalled-article"
        expected_images = ["http://example.com/image1.jpg", "http://example.com/image2.jpg"]
        extracted_images = self.extractor.extract_images(url)
        self.assertListEqual(extracted_images, expected_images)

    def test_invalid_url(self):
        # Test case for handling an invalid URL
        url = "http://invalid-url"
        with self.assertRaises(ValueError):
            self.extractor.extract_text(url)

if __name__ == '__main__':
    unittest.main()