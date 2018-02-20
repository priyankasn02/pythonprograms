class ccd:
    
    coffee_rate=10
    tea_rate=5
    milk_rate=15
    
    total_num_bvg_frm_all_branches=0
    total_num_coffe_frm_all_branches=0
    total_num_tea_frm_all_branches=0
    total_num_milk_frm_all_branches=0
    
    total_amount_frm_all_branches=0
    total_amount_of_coffe_frm_all_branches=0
    total_amount_of_tea_frm_all_branches=0
    total_amount_of_milk_frm_all_branches=0
    
    def __init__(self,name):
        
        self.name = name
        
        self.total_bvg_sold=0
        self.total_coffe_sold=0
        self.total_tea_sold=0
        self.total_milk_sold=0
        
        self.total_income=0
        self.total_coffe_income=0
        self.total_tea_income=0
        self.total_milk_income=0
        
    def sell(self,brev,num):
        self.brev=brev
        self.num=num
        
        if self.brev == 'C':
            
            self.total_num_bvg_frm_all_branches+=self.num
            self.total_num_coffe_frm_all_branches+=self.num
            self.total_amount_of_coffe_frm_all_branches+=self.coffee_rate
            self.total_amount_frm_all_branches+=self.coffee_rate
            
            self.total_bvg_sold+=self.num
            self.total_coffe_sold+=self.num
            self.total_income+=self.coffee_rate
            self.total_coffe_income+=self.coffee_rate
        
        if self.brev == 'T':
            
            self.total_num_bvg_frm_all_branches+=self.num
            self.total_num_tea_frm_all_branches+=self.num
            self.total_amount_of_tea_frm_all_branches+=self.tea_rate
            self.total_amount_frm_all_branches+=self.tea_rate
            
            self.total_bvg_sold+=self.num
            self.total_tea_sold+=self.num
            self.total_income+=self.tea_rate
            self.total_tea_income+=self.tea_rate
         
        if self.brev == 'M':
            
            self.total_num_bvg_frm_all_branches+=self.num
            self.total_num_milk_frm_all_branches+=self.num
            self.total_amount_of_milk_frm_all_branches+=self.milk_rate
            self.total_amount_frm_all_branches+=self.milk_rate
            
            self.total_bvg_sold+=self.num
            self.total_milk_sold+=self.num
            self.total_income+=self.milk_rate
            self.total_milk_income+=self.milk_rate   
            
            def rate_change(cls,b,r):
                b=
        
             
            
