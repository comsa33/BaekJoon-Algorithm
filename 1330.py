def compare(self, other):
    if int(self) > int(other):
        return '>'
    elif int(self) < int(other):
        return '<'
    else:
        return '=='