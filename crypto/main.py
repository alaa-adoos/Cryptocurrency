from printy import printy
from crypto.crypto import crypto


'''
 - we used printy to style the texts 
 - the app is about Cryptocurrency , the user can explore information for coins by input it's symbol 
 - Cryptocurrency funciton used to start the app 
'''
def Cryptocurrency():
          print('''

░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░
██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗
██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║
██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░
''')
          printy('''[bD]  
        █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
        ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄@   ''')

          print("\n")

          printy("(≖_≖ ) \t   to quit any time, type [bD]\"quit\"@ \t(≖_≖ )")
          

          
          
          symbol1() 
          printy("[bD]*********************************************** " )
          print("**        to price type           \"1\"        **" )
          print("**        to max_supply type      \"2\"        **" )
          print("**        to categories type      \"3\"        **" )
          print("**        to rank type            \"4\"        **" )
          printy("**   to selecet anthor coin type  [y]\"5\"@        **" )
          printy("[bD]*********************************************** " )
      
          while(True):
            '''
            while statment used to return options for user , for example  option 1 for  coin price 
            
            '''    

            Number=(input(">"))
            if Number=="1":
                    print(f"Price: {crypto.get_price()}💲")
                  
            
            elif Number=="2":
                print(f"Max supply :{crypto.get_max_supply()}")
                
            
            elif Number=="3":
                print(f"Catagories :{crypto.get_categories()}")
     

            elif Number=="4":
                 print(f"Rank:{crypto.get_rank()}")
                  

            elif Number=="5":
                symbol1() 

            elif Number=="quit":
                printy(''' ☻/  bye
/▌ [r]♥♥''')           
                printy("/ \ [r]♥♥ ")

                break        
            

            else:
                symbol=input("Enter a number from 1-4->")
      

def symbol1():
          '''
          - symbol function used to validate the symbol  if is exist or not
          - if symbole not exist we used recursion to make user retype anthor symbol
    
          '''

          printy("(≖_≖ )  Enter a symbol Coin \"[bD]for example :btc@\"  (≖_≖ )")  
          symbol=input("👉  ").upper()
          if symbol=="QUIT":
                printy(''' ☻/  bye
/▌ [r]♥♥''')           
                printy("/ \ [r]♥♥ ")
                exit()
              
          else:  
              crypto.set_symbol(symbol)
              crypto.get_data()
              var=crypto.get_coin()      
              if var==None:
                 print("wrong symbol")
                 symbol1()
        
         
         
    
           
          print (f"Coin Name 👉  :{crypto.get_name()}")

 

Cryptocurrency()