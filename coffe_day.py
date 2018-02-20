class ccd:
    total_num_bvg_frm_all_branches=0
    total_num_coffe_frm_all_branches=0
    total_num_tea_frm_all_branches=0
    total_num_milk_frm_all_branches=0
    
    total_amount_frm_all_branches=0
    total_amount_of_coffe_frm_all_branches=0
    total_amount_of_tea_frm_all_branches=0
    total_amount_of_milk_frm_all_branches=0
    
    def __init__(self,name):
        
        self.name=name
        
        self.total_bvg_sold=0
        self.total_coffe_sold=0
        self.total_tea_sold=0
        self.total_milk_sold=0
        
        self.total_incom=0
        self.total_coffe_income=0
        self.total_tea_income=0
        self.total_milk_income=0
        
    def sell(self,bvg,num):
        self.bvg=bvg
        self.num=num
        
        if self.bvg=='C':
            self.total_num_bvg_frm_all_branches+=self.num
            self.total_num_coffe_frm_all_branches+=self.num
            self.total_amount_of_coffe_frm_all_branches+=self.num*10
            self.total_amount_frm_all_branches+=self.num*10
            
            self.total_bvg_sold=self.num
            self.total_coffe_sold=self.num
            self.total_income=self.num*10
            self.total_tea_income=self.num*10
            
         if self.bvg=='T':
            self.total_num_bvg_frm_all_branches+=self.num
            self.total_num_tea_frm_all_branches+=self.num
            self.total_amount_of_tea_frm_all_branches+=self.num*20
            self.total_amount_frm_all_branches+=self.num*20
            
            self.total_bvg_sold=self.num
            self.total_tea_sold=self.num
            self.total_income=self.num*20
            self.total_tea_income=self.num*20
         
        if self.bvg=='M':
            self.total_num_bvg_frm_all_branches+=self.num
            self.total_num_milk_frm_all_branches+=self.num
            self.total_amount_of_milk_frm_all_branches+=self.num*15
            self.total_amount_frm_all_branches+=self.num*15
            
            self.total_bvg_sold=self.num
            self.total_milk_sold=self.num
            self.total_income=self.num*15
            self.total_milk_income=self.num*15    
        
             
            
