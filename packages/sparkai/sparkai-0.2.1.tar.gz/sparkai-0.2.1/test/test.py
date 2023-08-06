#!/usr/bin/env python3

from sparkai import SparkAIClient
import unittest
import os
import sys
import uuid
import tempfile
import urllib
import json

IMAGE_URL = "https://picsum.photos/640/480"
VIDEO_URL = "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"

api_key = os.environ["SPARKAI_API_KEY"]
os.environ["SPARKAI_HOST"] = "http://localhost:3100"
client = SparkAIClient(api_key=api_key)
engagement_id = None


# HELPER FUNCTIONS


def is_valid_uuid(test_uuid):
    try:
        uuid.UUID(test_uuid)
        return True
    except:
        return False


def get_bytes_from_url(url):
    return urllib.request.urlopen(url).read()


class TestSimple(unittest.TestCase):
    def test_create_annotation(self):
        annotation = client.create_annotation([{"x": 1, "y": 1}], "dot", "point", {"test": 1})
        print(annotation)
        self.assertEqual(annotation["vertices"][0]["x"], 1)
        self.assertEqual(annotation["vertices"][0]["y"], 1)
        self.assertEqual(annotation["type"], "dot")
        self.assertEqual(annotation["label"], "point")
        self.assertEqual(annotation["metadata"]["test"], 1)
        self.assertIsNone(annotation["image_idx"])

    def test_create_annotation(self):
        annotation = client.create_annotation([{"x": 1, "y": 1}], "dot", "point", {"test": 1}, image_idx=4)
        print(annotation)
        self.assertEqual(annotation["vertices"][0]["x"], 1)
        self.assertEqual(annotation["vertices"][0]["y"], 1)
        self.assertEqual(annotation["type"], "dot")
        self.assertEqual(annotation["label"], "point")
        self.assertEqual(annotation["metadata"]["test"], 1)
        self.assertEqual(annotation["image_idx"], 4)

    def test_create_engagement_from_image_url(self):
        resp = client.create_engagement_from_image_url(IMAGE_URL)
        self.assertTrue(is_valid_uuid(resp["token"]))

    def test_create_engagement_from_video_url(self):
        resp = client.create_engagement_from_video_url(VIDEO_URL)
        self.assertTrue(is_valid_uuid(resp["token"]))

    def test_create_engagement_from_file_with_image(self):
        with tempfile.NamedTemporaryFile("wb", suffix=".jpg") as temp_file:
            results = get_bytes_from_url(IMAGE_URL)
            temp_file.write(results)
            resp = client.create_engagement_from_file(temp_file.name)
            self.assertTrue(is_valid_uuid(resp["token"]))

    def test_create_engagement_from_file_with_video(self):
        global engagement_id
        with tempfile.NamedTemporaryFile("wb", suffix=".mp4") as temp_file:
            results = get_bytes_from_url(VIDEO_URL)
            temp_file.write(results)
            resp = client.create_engagement_from_file(temp_file.name, video=True)
            engagement_id = resp["token"]
            self.assertTrue(is_valid_uuid(resp["token"]))

    def test_get_engagement(self):
        engagements = client.get_engagements(engagement_id=engagement_id)
        self.assertEqual(engagements[0]["state"], "open")
        self.assertIsNotNone(engagements[0]["date_created"])
        self.assertIsNotNone(engagements[0]["content_location"])
        self.assertEqual(engagements[0]["token"], engagement_id)

    def test_get_engagement_with_query(self):
        engagements = client.get_engagements()
        self.assertEqual(isinstance(engagements, list), True)
        self.assertGreater(len(engagements), 3)

    def test_webhook_signature_validation(self):
        x =  '{"state":"closed"}'

        req_body = json.loads(x)
        req_header = "t=1650901861020,v1=cce8bba61c34ac09d266312e3c12631d576d050c0e9fbbc22dfc2188ba7ef6d1"
        self_secret = "123456789"
        secret_validation = client.validate_webhook_secret(req_header, req_body, self_secret)
        self.assertTrue(secret_validation)