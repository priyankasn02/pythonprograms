import datetime
class orion():
    
    def __init__(self,gatename):
        self.gatename=gatename
        
    def calculate_parking_charges(self,no_of_hours_parked, parked_vehical_type):
        self.no_of_hours_parked=no_of_hours_parked
        self.parked_vehical_type=parked_vehical_type
        
        date = datetime.datetime.today().day
        if(date%2==0):
            print('even day')
            if(self.parked_vehical_type==2):
                print("parking fee for bike:",self,no_of_hours_parked*30)
            if(self.parked_vehical_type==4):
                print("parking fee for car:",self,no_of_hours_parked*60)
        else:
            print('odd day')
            if(self.parked_vehical_type==2):
                print("parking fee for bike:",self,no_of_hours_parked*40)
            if(self.parked_vehical_type==4):
                print("parking fee for car:",self.no_of_hours_parked*80)
                
if __name__=='__main__':
    northgate=orion('north gate')
    
    northgate.calculate_parking_fee(2,2)
    northgate.calculate_parking_fee(2,4)
    
                