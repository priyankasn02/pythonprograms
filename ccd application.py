# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 11:10:22 2018

@author: Rajath Kumar K S
"""
class ccd():
    
    total_no_of_brv_from_all_branches = 0
    total_no_of_coffee_from_all_branches = 0
    total_no_of_tea_from_all_branches = 0
    total_no_of_milk_from_all_branches = 0
    
    total_income_from_all_the_branches = 0
    total_income_from_all_the_branches_coffee = 0
    total_income_from_all_the_branches_tea = 0
    total_income_from_all_the_branches_milk = 0
    
    def __init__(self,name):
        
        self.name = name
        self.total_brv_sold = 0
        self.total_coffee_sold = 0
        self.total_tea_sold = 0
        self.total_milk_sold = 0
        
        self.total_income = 0
        self.total_income_coffee = 0
        self.total_income_tea = 0
        self.total_income_milk = 0
        
    
    def sell(self,brev,num):
        self.brev = brev
        self.num = num
        if self.brev == 'C':
            ccd.total_no_of_brv_from_all_branches += self.num
            ccd.total_no_of_coffee_from_all_branches += self.num
            ccd.total_income_from_all_the_branches_coffee += self.num * 10
            ccd.total_income_from_all_the_branches += self.num * 10
            
            self.total_brv_sold += self.num
            self.total_coffee_sold += self.num
            self.total_income_coffee += self.num * 10
            self.total_income += self.num * 10
        if self.brev == 'T':
            ccd.total_no_of_brv_from_all_branches += self.num
            ccd.total_no_of_tea_from_all_branches += self.num
            ccd.total_income_from_all_the_branches_tea += self.num * 20
            ccd.total_income_from_all_the_branches += self.num * 20
            
            self.total_brv_sold += self.num
            self.total_tea_sold += self.num
            self.total_income_tea += self.num * 20
            self.total_income += self.num * 20
        if self.brev == 'M':
            ccd.total_no_of_brv_from_all_branches += self.num
            ccd.total_no_of_milk_from_all_branches += self.num
            ccd.total_income_from_all_the_branches_milk += self.num * 15
            ccd.total_income_from_all_the_branches += self.num * 15
            
            self.total_brv_sold += self.num
            self.total_milk_sold += self.num
            self.total_income_milk += self.num * 18
            self.total_income += self.num * 18
            
    def generate_report(self):
        print('Total No. of Breverages Sold in ',self.name,' branch : ',self.total_brv_sold)            
        print('Total No. of Coffees Sold ',self.name,' branch: ',self.total_coffee_sold)
        print('Total No. of Tea\'s Sold ',self.name,' branch: ',self.total_tea_sold)
        print('Total No. of Milks Sold ',self.name,' branch: ',self.total_milk_sold)
    
        print('Total Income from All the Breverages sold by ',self.name,' branch : ',self.total_income)
        print('Total Income from ',self.name,' Branch by Selling Coffee: ',self.total_income_coffee)
        print('Total Income from ',self.name,' Branch by Selling Tea: ',self.total_income_tea)
        print('Total Income from ',self.name,' Branch by Seling Milk: ',self.total_income_milk)
        
            
if __name__ == '__main__':
    yesh = ccd('Yeshwanthpur')
    mall = ccd('Malleshwaram')
    math = ccd('Mathikere')
    
    yesh.sell('C',2)
    yesh.sell('T',2)
    yesh.sell('M',2)
    
    mall.sell('C',5)
    
    math.sell('M',5)
    
#    print('Total No. of Breverages Sold by all the Branches: ',ccd.total_no_of_brv_from_all_branches)            
#    print('Total No. of Coffees Sold by all the Branches: ',ccd.total_no_of_coffee_from_all_branches)
#    print('Total No. of Tea\'s Sold by all the Branches: ',ccd.total_no_of_tea_from_all_branches)
#    print('Total No. of Milks Sold by all the Branches: ',ccd.total_no_of_milk_from_all_branches)
#    
#    print('Total Income from All the Branches: ',ccd.total_income_from_all_the_branches)
#    print('Total Income from All the Branches by Selling Coffee: ',ccd.total_income_from_all_the_branches_coffee)
#    print('Total Income from All the Branches by Selling Tea: ',ccd.total_income_from_all_the_branches_tea)
#    print('Total Income from All the Branches by Seling Milk: ',ccd.total_income_from_all_the_branches_milk)
    
    yesh.generate_report()
    mall.generate_report()
    math.generate_report()
    
    
    
            
    
    
    
