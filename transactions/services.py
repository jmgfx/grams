class DefaultDescription:
    def __init__(self):
        count = str(len(self.assets_transact))

        if self.ttype == '1':
            return count + ' asset(s) is in maintenance.'
        elif self.ttype == '2':
            return 'Transfered ' + count + ' asset(s) from ' + self.branch_origin + ' to ' + self.branch_destination + '.'
        elif self.ttype == '3':
            return 'Recovered ' + count + ' asset(s).'
