import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint


def send_email(self, report, title, email, description):
    admin_email = os.environ.get("ADMIN_EMAIL")

    # Configure API key authorization: api-key
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.environ.get("sendinblue-api-key")

    # Create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))

    # Set the sender and recipient details
    sender = sib_api_v3_sdk.SendSmtpEmailSender(name="Customer", email=email)
    recipient = sib_api_v3_sdk.SendSmtpEmailTo(
        email=admin_email, name="CV-VMA")
    to = [recipient]

    # Create the email object
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        sender=sender,
        to=to,
        html_content=f"<html><head></head><body><h1>Report Type: {report}</h1> \n <h3>Title: {title}</h3> \n <h3>Feedback:</h3> <p>{description}</p>",
        subject=report
    )

    # Send the email
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
        return True
    except ApiException as e:
        print(f"Exception when calling SMTPApi->send_transac_email: {e}\n")
        return False
