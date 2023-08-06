from unittest.mock import patch

from src.slack_client import SlackClient


def test_post_data_to_slack():
    slack_client = SlackClient("sample channel", "123ff")
    with patch("slack.WebClient.chat_postMessage") as mock_slack:
        mock_slack.return_value = True

        data = ["New", "Delete", "Update"]
        response = slack_client.post_data_to_slack(data)

        assert response == 3