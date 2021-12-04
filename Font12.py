# A font definition taken from the C code file font12.c that is
# supplied as example code from the Waveshare website.
#
# TODO - add other characters
#
class Font12():

    Height = 12
    Width = 8

    def H(self):
        return [
        0x00, #//
        0xEE, #// ### ###
        0x44, #//  #   # 
        0x44, #//  #   # 
        0x7C, #//  ##### 
        0x44, #//  #   # 
        0x44, #//  #   # 
        0x44, #//  #   # 
        0xEE, #// ### ###
        0x00, #//        
        0x00, #//        
        0x00] #//        

    def e(self):
        return [
        0x00, #//        
        0x00, #//        
        0x00, #//        
        0x38, #//   ###  
        0x44, #//  #   # 
        0x7C, #//  ##### 
        0x40, #//  #     
        0x40, #//  #     
        0x3C, #//   #### 
        0x00, #//        
        0x00, #//        
        0x00] #//        
        
    def l(self):
        return [
        0x00, #//        
        0x30, #//   ##   
        0x10, #//    #   
        0x10, #//    #   
        0x10, #//    #   
        0x10, #//    #   
        0x10, #//    #   
        0x10, #//    #   
        0x7C, #//  ##### 
        0x00, #//        
        0x00, #//        
        0x00] #//        

    o = [
        0x00, #//        
        0x00, #//        
        0x00, #//        
        0x38, #//   ###  
        0x44, #//  #   # 
        0x44, #//  #   # 
        0x44, #//  #   # 
        0x44, #//  #   # 
        0x38, #//   ###  
        0x00, #//        
        0x00, #//        
        0x00] #//        
    