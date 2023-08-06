from slack import WebClient
from slack.errors import SlackApiError


class SlackClient:
    def __init__(self, slack_channel, slack_token):
        self.slack_channel = slack_channel
        self.slack_token = slack_token

    def post_data_to_slack(self, data):
        """
        Posts the messages for APIs added, deleted and updated based on the \
        input data

        Inputs
        ----------
            data : list of strings pertaining to APIs added, deleted and \
updated
        """
        try:
            slack_web_client = WebClient(
                # Add the slack access token here
                token=self.slack_token
            )

            response_true_cnt = 0
            for x in data:
                if x is not None and len(x) > 0:
                    message = {
                        "channel": self.slack_channel,
                        "blocks": [
                            {
                                "type": "section",
                                "text": {"type": "plain_text", "text": x},
                            }
                        ],
                    }
                    response = slack_web_client.chat_postMessage(**message)

                    if response:
                        response_true_cnt += 1
        except SlackApiError as e:
            return e

        return response_true_cnt
