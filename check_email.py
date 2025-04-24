import os
import imaplib
import email
from email.header import decode_header
import time
from datetime import datetime



class CheckEmail:
    def __init__(self, email :str, app_password: str, num_emails=10, interval=1800):
        self.email = email
        self.app_password = app_password
        self.num_emails = num_emails
        self.interval = interval

    def _process_email(self, email_message):
        """Your custom email processing logic"""
        subject = decode_header(email_message['Subject'])[0][0]
        if isinstance(subject, bytes):
            subject = subject.decode()
        from_ = email_message['From']
        date = email_message['Date']
        print(f"\nNew email received at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"From: {from_}")
        print(f"Date: {date}")
        print(f"Subject: {subject}")
        # Add your script trigger logic here

    def _check_recent_emails(self):
        """Check the last N emails in the inbox"""
        self.mail.select('inbox')
        
        # Search for all emails and get their IDs
        status, messages = self.mail.search(None, 'ALL')
        if status != 'OK':
            print("No messages found!")
            return
        
        # Get the last N message IDs
        message_ids = messages[0].split()
        last_n_ids = message_ids[-self.num_emails:] if len(message_ids) >= self.num_emails else message_ids
        
        print(f"\nChecking last {len(last_n_ids)} emails at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        for num in reversed(last_n_ids):  # Process from newest to oldest
            status, data = self.mail.fetch(num, '(RFC822)')
            if status == 'OK':
                email_message = email.message_from_bytes(data[0][1])
                self._process_email(email_message)

    def email_monitor(self):
        """Check inbox every X seconds for last N emails"""
        while True:
            try:
                # Connect to server
                self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
                self.mail.login(self.email, self.app_password)
                
                self._check_recent_emails()
                
                self.mail.close()
                self.mail.logout()
                
                print(f"\nNext check in {self.interval//60} minutes...")
                time.sleep(self.interval)
                
            except Exception as e:
                print(f"Error occurred: {str(e)}")
                print("Reconnecting in 5 minutes...")
                time.sleep(300)  # Wait 5 minutes before reconnecting
