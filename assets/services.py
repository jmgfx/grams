from datetime import datetime, timedelta
from django.utils import timezone

class GetDepreciation:
    def __init__(self, date_acquired):
        self.it_dep_date[0] = date_acquired
        self.it_accrued[0] = self.dep_value
        self.it_balance[0] = self.acquisition_cost


    def is_balance_valid(self):
        if self.balance <= 0:
            self.depreciate = False
            return False
        else:
            self.depreciate = True
            return True
    

    def compute_depreciation(self):
        month = 1
        for month in self.counter:
            self.balance = self.it_balance[month]
            if self.is_balance_valid():
                self.it_dep_date[month] = self.it_dep_date[month-1] + datetime.timedelta(30)
                self.it_accrued[month] = self.it_accrued[month-1] + self.dep_value
                self.it_balance[month] = self.acquisition_cost - self.it_accrued[month]
