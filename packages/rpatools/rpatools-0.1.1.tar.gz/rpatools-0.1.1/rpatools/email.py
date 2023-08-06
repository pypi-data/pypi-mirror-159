import win32com.client as client
from datetime import datetime, timedelta
from time import sleep
import os
import re


class Outlook:
    def __init__(self, account=None, day_first_format=True):
        self.outlook = client.Dispatch("Outlook.Application")
        self.namespace = self.outlook.GetNameSpace("MAPI")
        self.default_inbox = self.namespace.GetDefaultFolder(6)
        self.default_account = self.default_inbox.Parent

        if account is None:
            self.current_account = self.inbox.Parent
        else:
            self.current_account = self.namespace.Folders[account]

        if day_first_format:
            self.date_string = '%d/%m/%Y'
        else:
            self.date_string = '%m/%d/%Y'

    def get_all_accounts_names(self):
        return [acc.DisplayName for acc in self.outlook.Session.Accounts]

    def send_email(self, recipients, subject, text):
        message = self.outlook.CreateItem(0)
        message.To = recipients
        message.Subject = subject
        message.Body = text
        message.Send()

    def subfolder_exist(self, folder_path):
        target_folder = self.get_folder(folder_path)

        if target_folder is None:
            return False
        else:
            return True

    def create_folder(self, folder_path):
        subfolders = folder_path.split("/")
        current_folder = None
        for folder_name in subfolders:
            if current_folder is None:
                try:
                    current_folder = self.current_account.Folders[folder_name]
                except:
                    current_folder = self.current_account.Folders.Add(folder_name)
            else:
                try:
                    current_folder = current_folder.Folders[folder_name]
                except:
                    current_folder = current_folder.Folders.Add(folder_name)

        return current_folder

    def get_folder(self, folder_path):
        subfolders = folder_path.split("/")
        target_folder = self.current_account
        for folder_name in subfolders:
            try:
                target_folder = target_folder.Folders[folder_name]
            except:
                return None

        return target_folder


    def move_email_to_folder(self, message, folder):
        _ = message.Move(folder)


    def get_sender_address(self, msg):
        if msg.SenderEmailType == "EX":
            return msg.Sender.GetExchangeUser().PrimarySmtpAddress
        else:
            return msg.SenderEmailAddress

    def get_recipients_address(self, msg):
        to_address = list()
        cc_address = list()
        for rec in msg.Recipients:
            if rec.AddressEntry.AddressEntryUserType == 30:
                address = rec.Address
            else:
                address = rec.AddressEntry.GetExchangeUser().PrimarySmtpAddress

            if rec.Type == 1:
                to_address.append(address)
            else:
                cc_address.append(address)

        return to_address, cc_address

    def get_all_emails(self, folder):
        return folder.Items

    def get_recent_emails(self, folder, days=1):
        emails = folder.Items
        received_dt = datetime.now() - timedelta(days=days)
        received_dt = received_dt.strftime(self.date_string)

        return emails.Restrict("[ReceivedTime] >= '" + received_dt + "'")

    def get_emails_with_attachments(self, folder):
        return folder.Items.Restrict('@SQL="urn:schemas:httpmail:hasattachment"=1')

    def extract_attachments(self, email, file_extension=None):
        if file_extension is not None:
            attachment_list = list()
            for att in email.Attachments:
                if att.FileName.split(".")[1] == file_extension:
                    attachment_list.append(att)
            return attachment_list
        else:
            return list(email.Attachments)

    def get_filtered_emails(self, folder, sender_name=None, sender_email=None, recent_days=None,
                            date_range=None, unread=False, subject_contains=None, subject_is=None):

        emails = folder.Items

        if sender_name is not None:
            emails = emails.Restrict(f"[SenderName] = '{sender_name}'")

        if sender_email is not None:
            emails = emails.Restrict(f"[SenderEmailAddress] = '{sender_email}'")

        if recent_days is not None:
            received_dt = datetime.now() - timedelta(days=recent_days)
            received_dt = received_dt.strftime(self.date_string)
            emails = emails.Restrict("[ReceivedTime] >= '" + received_dt + "'")

        if date_range is not None:
            emails = emails.Restrict("[ReceivedTime] >= '" + date_range[0] + "'" + \
                                     " and [ReceivedTime] <= '" + date_range[1] + "'")

        if unread:
            emails = emails.Restrict("[Unread] = True")

        if subject_contains is not None:
            emails = emails.Restrict(f"@SQL= \"urn:schemas:httpmail:subject\" like '%{subject_contains}%'")

        if subject_is is not None:
            emails = emails.Restrict(f"[Subject] = {subject_is}")

        return emails

    def create_meeting_invite(self, start=None, end=None, required_recipients=None, optional_recipients=None,
                              subject=None, all_day_event=False, reminder_minutes_befor_start=None,
                              categories=None, location=None, status_as_busy=True, auto_send=True, display_sec=0):

        outlook = client.Dispatch("Outlook.Application")
        meeting = self.outlook.CreateItem(1)
        meeting.MeetingStatus = 1

        if start is not None:
            meeting.Start = start

        if end is not None:
            meeting.End = end

        if required_recipients is not None:
            if isinstance(required_recipients, list):
                for person in required_recipients:
                    recipient = meeting.Recipients.Add(person)
                    recipient.Type = 1
            else:
                recipient = meeting.Recipients.Add(required_recipients)
                recipient.Type = 1

        if optional_recipients is not None:
            if isinstance(optional_recipients, list):
                for person in optional_recipients:
                    recipient = meeting.Recipients.Add(person)
                    recipient.Type = 2
            else:
                recipient = meeting.Recipients.Add(optional_recipients)
                recipient.Type = 2

        if subject is not None:
            meeting.Subject = subject

        if all_day_event:
            meeting.AllDayEvent = True
        else:
            meeting.AllDayEvent = False

        if reminder_minutes_befor_start is not None:
            meeting.ReminderMinutesBeforeStart = reminder_minutes_befor_start

        if status_as_busy:
            meeting.BusyStatus = 2
        else:
            meeting.BusyStatus = 0

        if categories is not None:
            meeting.Categories = categories

        if auto_send:
            meeting.Save()
            meeting.Send()
        else:
            meeting.Display()