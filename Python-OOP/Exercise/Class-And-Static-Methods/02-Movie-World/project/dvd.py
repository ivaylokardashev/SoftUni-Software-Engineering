from datetime import date

class DVD:

    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, _id: int, name: str, _date: str, age_restriction: int):
        day, month, year = [int(x) for x in _date.split('.')]
        date_obj = date(year, month, day)  # Without this line
        month_full_name = date_obj.strftime('%B')  # month_name = calendar.month_name[month] -> Full month name => '%B'

        return cls(name, _id, year, month_full_name, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"

