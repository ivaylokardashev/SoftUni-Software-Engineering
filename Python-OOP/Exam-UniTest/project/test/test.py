import unittest
from project.social_media import SocialMedia


class TestSocialMedia(unittest.TestCase):
    def test_initialization(self):
        # Test initializing the SocialMedia object with valid parameters
        social_media = SocialMedia("test_user", "Instagram", 1000, "photo")
        self.assertEqual(social_media._username, "test_user")
        self.assertEqual(social_media._platform, "Instagram")
        self.assertEqual(social_media._followers, 1000)
        self.assertEqual(social_media._content_type, "photo")
        self.assertEqual(len(social_media._posts), 0)

        # Test initializing the SocialMedia object with invalid platform
        with self.assertRaises(ValueError):
            SocialMedia("test_user", "Facebook", 1000, "photo")

    def test_platform_property(self):
        # Test setting platform with valid and invalid values
        social_media = SocialMedia("test_user", "Instagram", 1000, "photo")
        social_media.platform = "YouTube"
        self.assertEqual(social_media.platform, "YouTube")

        with self.assertRaises(ValueError):
            social_media.platform = "Facebook"

    def test_followers_property(self):
        # Test setting followers with valid and invalid values
        social_media = SocialMedia("test_user", "Instagram", 1000, "photo")
        social_media.followers = 2000
        self.assertEqual(social_media.followers, 2000)

        with self.assertRaises(ValueError):
            social_media.followers = -500

    def test_create_post(self):
        # Test creating a post with valid content
        social_media = SocialMedia("test_user", "Instagram", 1000, "photo")
        self.assertEqual(social_media.create_post("This is a test post."), "New photo post created by test_user on Instagram.")

        # Test creating a post with empty content
        self.assertEqual(social_media.create_post(""), "New photo post created by test_user on Instagram.")

    def test_like_post(self):
        # Test liking a post with valid index and when the post hasn't reached the maximum likes
        social_media = SocialMedia("test_user", "Instagram", 1000, "photo")
        social_media.create_post("Test post")
        self.assertEqual(social_media.like_post(0), "Post liked by test_user.")

        # Test liking a post with valid index and when the post has reached the maximum likes
        for _ in range(10):
            social_media.like_post(0)
        self.assertEqual(social_media.like_post(0), "Post has reached the maximum number of likes.")

        # Test liking a post with invalid index
        self.assertEqual(social_media.like_post(1), "Invalid post index.")

    def test_comment_on_post(self):
        # Test commenting on a post with valid index and comment length greater than 10
        social_media = SocialMedia("test_user", "Instagram", 1000, "photo")
        social_media.create_post("Test post")
        self.assertEqual(social_media.comment_on_post(0, "This is a long comment."), "Comment added by test_user on the post.")

        # Test commenting on a post with valid index and comment length less than or equal to 10
        self.assertEqual(social_media.comment_on_post(0, "Short."), "Comment should be more than 10 characters.")

        # Test commenting on a post with invalid index
        with self.assertRaises(IndexError):
            social_media.comment_on_post(1, "Invalid post.")

    def test_appending_to_posts(self):
        # Test appending to the _posts list
        social_media = SocialMedia("test_user", "Instagram", 1000, "photo")
        social_media.create_post("Test post")

        # Check if the _posts list contains the newly created post
        self.assertEqual(len(social_media._posts), 1)
        self.assertEqual(social_media._posts[0]['content'], "Test post")

        # Append another post and check if it's added to the _posts list
        social_media.create_post("Another post")
        self.assertEqual(len(social_media._posts), 2)
        self.assertEqual(social_media._posts[1]['content'], "Another post")


if __name__ == '__main__':
    unittest.main()
