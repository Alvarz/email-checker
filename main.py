#!/usr/bin/env python3
import os
from email.header import decode_header
from check_email import CheckEmail
from process_attachments import ProcessAttachments
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv('EMAIL')
APP_PASSWORD = os.getenv('APP_PASSWORD')


if __name__ == '__main__':
    print("Starting email monitor - Checking last 5 emails every 30 minutes")
    email_checker = CheckEmail(EMAIL, APP_PASSWORD)
    email_checker.check_email()
    # email_checker.email_monitor()

    pa = ProcessAttachments()
    pa.get_files()