# response = post("https://api.mailgun.net/v3/sandbox35cf6a0d8af74abaa6fcd4b3220182e1.mailgun.org/messages",
#                         auth=("api", "c344ee9c65eeef5509157e77b5400c90-915161b7-5bf8c126"),
#                         data={
#                             "from": "pricing service <do-not-reply@sandbox35cf6a0d8af74abaa6fcd4b3220182e1.mailgun.org>",
#                             "to": email,
#                             "subject": subject,
#                             "text": text,
#                             "html": html
#                         })
import os
from typing import List
from requests import Response, post


class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message


class Mailgun:
    FROM_TITLE = 'Pricing service'
    FROM_EMAIL = 'do-not-reply@sandbox35cf6a0d8af74abaa6fcd4b3220182e1.mailgun.org'

    @classmethod
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        api_key = os.environ.get('MAILGUN_API_KEY', None)
        domain = os.environ.get('MAILGUN_DOMAIN', None)

        if api_key is None:
            raise MailgunException('Failed to load Mailgun API key.')

        if domain is None:
            raise MailgunException('Failed to load Mailgun domain')

        response = post(f"{domain}/messages",
                        auth=("api", api_key),
                        data={
                            "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                            "to": email,
                            "subject": subject,
                            "text": text,
                            "html": html
                        })
        if response.status_code != 200:
            raise MailgunException('An error occurred while sending e-mail')
        return response



