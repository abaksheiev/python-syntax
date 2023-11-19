class iPhone6:
    def home(self):
        print('Home button is pressed')
    
class iPhoneX(iPhone6):
    def home(self):
        print('Home is touched')
        super().home() # only in this way we could call method from parent

i6 = iPhone6()
i6.home()

ix = iPhoneX()
ix.home()

# Result
#Home button is pressed
#Home is touched
#Home button is pressed