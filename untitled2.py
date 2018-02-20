class ccd():
    coffee_rate=10
    
    total_amount_of_coffee_frm_all_branches=0
    total_num_coffe_frm_all_branches=0
    
    def __init__(self,name):
        
        self.name = name
        
        self.total_bvg_sold=0
        self.total_coffe_sold=0
        
        self.total_income=0
        self.total_coffe_income=0
        
        def sell(self,brev,num):
        self.brev=brev
        self.num=num
        
        if self.brev == 'C':
            
            self.total_num_bvg_frm_all_branches+=self.num
            self.total_num_coffe_frm_all_branches+=self.num
            self.total_amount_of_coffe_frm_all_branches+=self.coffee_rate
            self.total_amount_frm_all_branches+=self.num*coffee_rate