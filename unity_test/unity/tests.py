from rest_framework import status
from rest_framework.test import APITestCase

from .models import EmailSubscription


class EmailSubscriptionTestCase(APITestCase):
    def setUp(self):
        EmailSubscription.objects.create(
            email="first@test.com",
            is_subscribed=True
        )
        EmailSubscription.objects.create(
            email="second@test.com"
        )
        EmailSubscription.objects.create(
            email="third@test.com",
            is_subscribed=True
        )

    def test_get_all_email_subscriptions(self):
        """
        Ensure we can get all email subscriptions.
        """
        response = self.client.get("/api/v1/unity/subscribe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_one_email_subscription(self):
        """
        Ensure we can get one email subscription.
        """
        email = "first@test.com"
        response = self.client.get(f"/api/v1/unity/subscribe?email={email}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], email)

    def test_create_email_subscription(self):
        """
        Ensure we can create an email subscription.
        """
        data = {
            "email": "test@test.com"
        }
        response = self.client.post("/api/v1/unity/subscribe",
                                    data=data,
                                    format="json"
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_email_subscription(self):
        """
        Ensure we can update an email subscription.
        """
        data = {
            "email": "second@test.com",
            "is_subscribed": True
        }

        response = self.client.put("/api/v1/unity/subscribe",
                                   data=data,
                                   format="json"
                                   )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_email_subscription(self):
        """
        Ensure we can delete an email subscription.
        """
        email = "third@test.com"
        data = {
            "email": email
        }
        response = self.client.delete("/api/v1/unity/subscribe",
                                      data=data,
                                      format="json"
                                      )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_email_subscription_not_found(self):
        """
        Ensure we get a 400 if email subscription is not found.
        """
        email = "test@test.com"
        response = self.client.get(f"/api/v1/unity/subscribe?email={email}")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_email_subscription_already_exists(self):
        """
        Ensure we get a 400 if email subscription already exists.
        """
        data = {
            "email": "first@test.com"
        }
        response = self.client.post("/api/v1/unity/subscribe",
                                    data=data,
                                    format="json"
                                    )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_email_subscription_not_found(self):
        """
        Ensure we get a 400 if email subscription is not found.
        """
        data = {
            "email": "test@test.com",
            "is_subscribed": True
        }
        response = self.client.put("/api/v1/unity/subscribe",
                                   data=data,
                                   format="json"
                                   )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_email_subscription_not_found(self):
        """
        Ensure we get a 400 if email subscription is not found.
        """
        email = "test@test.com"
        data = {
            "email": email
        }
        response = self.client.delete("/api/v1/unity/subscribe",
                                      data=data,
                                      format="json"
                                      )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_email_subscription_invalid_email(self):
        """
        Ensure we get a 400 if email is invalid.
        """
        data = {
            "email": "test"
        }
        response = self.client.post("/api/v1/unity/subscribe",
                                    data=data,
                                    format="json"
                                    )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
