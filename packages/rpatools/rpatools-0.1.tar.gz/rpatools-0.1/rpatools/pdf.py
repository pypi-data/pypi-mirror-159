import pdfplumber as pp
import re
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

class PDF_Doc:
    def __init__(self, filepath):
        self.filepath = filepath

        with pp.open(self.filepath) as doc:
            self.text = doc.pages[0].extract_text()

    def get_doc_date(self):
        date_string = re.findall("Date\s*:\s*(\d{2}\s{1}\w{3}\s{1}\d{4})", self.text)
        if len(date_string) > 0:
            date_string = date_string[0]
            return datetime.strptime(date_string, '%d %b %Y')
        else:
            return None

    def estimate_due_date_from_doc_date(self, offset_month=2):
        doc_date = self.get_doc_date()
        if doc_date is not None:
            return doc_date + relativedelta(months=offset_month)
        else:
            return None

    def get_due_date(self):
        regex = 'If you disagree .*(\d{2} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4})'
        date_string = re.findall(regex, self.text[len(self.text)], re.DOTALL)

        if len(date_string) > 0:
            return datetime.strptime(date_string[0][0], '%d %b %Y')
        else:
            return None

    def valid_iras_statement(self):
        return len(re.findall('CAN00101', self.text)) > 0

    def get_NOA_title(self):
        return re.findall('Notice of Assessment \(.*?\)', self.text)[0]

    def get_year_of_assessment(self):
        return re.findall('Year of Assessment (\d{4})', self.text)[0]

    def get_tax_payable(self):
        regex = 'Tax Payable\s*(.*)'
        return float(re.findall(regex, self.text)[0].replace(",", ""))

    def get_company_name(self, x0=30, y0=50, x1=600, y1=100):
        with pp.open(self.filepath) as doc:
            return doc.pages[0].crop((x0, y0, x1, y1)).extract_text().split("\n")[0]