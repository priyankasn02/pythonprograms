class parking:
    even_day_charges=20
    odd_day_charges=10
    sunday_charges=40
    sat_charges=40
    
    total_parking_charges=0
    
    def __init__(self,day):
        self.day=day
        self.even_day_charges=0
        self.odd_day_charges=0
        self.sunday_charges=0
        self.sat_charges=0
        
        self.total_parking_charges=0
        
    def income(self,even,odd):
        self.even=even
        self.odd=odd
        
        if self.day==(a%2==0):
            self.even_day+=self.even_day_charges
            print("even_day")
        else:
            print("odd_day")
