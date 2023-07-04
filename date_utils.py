import datetime

class DateConverter:
    @staticmethod
    def convert_to_date(date_str):
        if date_str:
            try:
                date = datetime.datetime.strptime(str(date_str), '%Y-%m-%d').date()
            except ValueError:
                date = None
            return date
        else:
            return None

    @staticmethod
    def convert_to_str(date):
        if date:
            date_str = date.strftime('%Y-%m-%d')
            return date_str
        else:
            return ''