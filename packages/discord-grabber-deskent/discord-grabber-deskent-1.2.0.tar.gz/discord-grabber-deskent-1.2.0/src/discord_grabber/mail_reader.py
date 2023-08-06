import re
import imaplib

import email
import datetime
import base64

from email.header import decode_header


def b64padanddecode(b):
    """Decode unpadded base64 data"""
    b += (-len(b) % 4) * '='  # base64 padding (if adds '===', no valid padding anyway)
    return base64.b64decode(b, altchars='+,', validate=True).decode('utf-16-be')


def imaputf7decode(s):
    """Decode a string encoded according to RFC2060 aka IMAP UTF7.

Minimal validation of input, only works with trusted data"""
    lst = s.split('&')
    out = lst[0]
    for e in lst[1:]:
        u, a = e.split('-', 1)  # u: utf16 between & and 1st -, a: ASCII chars folowing it
        if u == '':
            out += '&'
        else:
            out += b64padanddecode(u)
        out += a
    return out


def imaputf7encode(s):
    """"Encode a string into RFC2060 aka IMAP UTF7"""
    s = s.replace('&', '&-')
    iters = iter(s)
    unipart = out = ''
    for c in s:
        if 0x20 <= ord(c) <= 0x7f:
            if unipart != '':
                out += '&' + base64.b64encode(unipart.encode('utf-16-be')).decode('ascii').rstrip('=') + '-'
                unipart = ''
            out += c
        else:
            unipart += c
    if unipart != '':
        out += '&' + base64.b64encode(unipart.encode('utf-16-be')).decode('ascii').rstrip('=') + '-'
    return out


def decodemailtext(text):
    print('decode', text)
    text = re.sub(r'\?=\s+=\?UTF\-8\?B\?', '', text, re.IGNORECASE)
    if re.search(r'=\?(UTF\-8|windows\-1251|koi8\-r)+\?', text, re.IGNORECASE):
        text = decode_header(text)
        text = text[0][0].decode(text[0][1])
    return text


class MailReader:
    def __init__(self, email, password, server, logger=None):
        self.login = email
        self.password = password
        self.server = server
        self.logger = logger

    def reader_login(self):
        self.imap = imaplib.IMAP4_SSL(self.server)
        self.imap.login(self.login, self.password)

    def reader_logout(self):
        self.imap.logout()

    def read_folder(self, folder):
        print(folder, '\n', imaputf7encode(folder))
        self.imap.select(imaputf7encode(folder))
        result, self.data = self.imap.uid('search', None, 'ALL')
        if self.data:
            self.data = self.data[0].split()
            self.data = self.data[::-1]
        print('result', result)

    def get_link_from_last_email(self):
        self.logger.debug('read folder...')
        self.read_folder('inbox')
        new_count = 0
        for uid in self.data:
            self.logger.info(f'Starting work for uid: {uid} ')
            try:

                uid = int(uid.decode('utf-8'))
                new_count += 1

                result, msg = self.imap.uid('fetch', str(uid), '(RFC822)')

                if not msg[0]:
                    self.logger.info(f' message {msg}')
                    continue

                mail = email.message_from_bytes(msg[0][1])

                dt = datetime.datetime.strptime(' '.join(mail['Date'].split(' ')[1:4]), '%d %b %Y')
                subj = mail['Subject']
                self.logger.info(f'{mail["From"]}, {mail["Content-Type"]}')
                self.logger.info(f'mail to {mail["To"]} data {dt}, subject {subj}')

                if mail.is_multipart():
                    for payload in mail.get_payload():
                        if payload.get_content_maintype() == 'text':
                            body = payload.get_payload(decode=True).decode('utf-8', 'ignore')

                else:
                    body = mail.get_payload(decode=True).decode('utf-8', 'ignore')

                search = re.search(r'<a href="(https://click\.discord\.com.[^"]*?)".[^>]*?>([^<:]*?)</a>', body)

                return search.group(1)
            except Exception as err:
                self.logger.error(err)

    def start(self):
        self.reader_login()
        link: str = self.get_link_from_last_email()
        self.reader_logout()

        return link


if __name__ == '__main__':
    SERVER = "imap.rambler.ru"
    EMAIL = 'iajnajysy@rambler.ru'
    PASSWORD = 'X27WENQQK'
    r = MailReader(EMAIL, PASSWORD, SERVER)
    link = r.start()
    print(link)
    exit()
