# Import the datetime module to work with date and time data
import datetime

# Define a DateConverter class that contains static methods to convert between date and string representations
class DateConverter:
    # Static method to convert a date string (YYYY-MM-DD) to a date object
    @staticmethod
    def convert_to_date(date_str):
        # Check if the input date string is not empty
        if date_str:
            try:
                # Attempt to convert the date string to a date object using the specified format
                date = datetime.datetime.strptime(str(date_str), '%Y-%m-%d').date()
            except ValueError:
                # If the date string is not in the correct format, set date to None (invalid date)
                date = None
            # Return the date object or None if conversion fails
            return date
        else:
            # If the input date string is empty, return None (invalid date)
            return None

    # Static method to convert a date object to a string representation(YYYY-MM-DD)
    @staticmethod
    def convert_to_str(date):
        # Check if the input date object is not empty
        if date:
            # Convert the date object to a string using the specified format
            date_str = date.strftime('%Y-%m-%d')
            # Return the string representation of the date
            return date_str
        else:
            # If the input date object is empty (None), return an empty string
            return ''
