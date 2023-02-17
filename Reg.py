class Reg:
    def __init__(self, reg):
        self.reg = str(reg).upper()
        self.EUR = "EUR"
        self.USA = "USA"

        if self.reg == "EUR":
            self.output = self.EUR
        else:
            self.output = self.USA
    def __repr__(self):
        return self.output

