from colorama import Fore,init,Style
import os
import platform    
import subprocess
class Colors():
    def __init__(self):
        # Para resetear los colores de la shell
        init()
      

    def red(self,text,center=True,is_input=False):
        
        colored_text = Fore.RED  +text
        if center:    
            width = os.get_terminal_size().columns
            if is_input:
                input("\n".join(line.center(width)  for line in colored_text.split("\n")))    
            else:
                print("\n".join(line.center(width)  for line in colored_text.split("\n")))
            
        else:  
            if is_input:
                input(colored_text)
            else:   
                print(colored_text)
        print(Style.RESET_ALL)

    def yellow(self,text, center=True,is_input=False):
        colored_text = Fore.YELLOW +text
        if center:    
            width = os.get_terminal_size().columns
            if is_input:
                out = input("\n".join(line.center(width)  for line in colored_text.split("\n")))
                return out
            else:
                print("\n".join(line.center(width)  for line in colored_text.split("\n")))
            
        else:
            if is_input:     
                out = input(colored_text)
                return out 
            else:
                print(colored_text)

        print(Style.RESET_ALL)

    def green(self,text, center=True,is_input=False):
        colored_text = Fore.GREEN +text
        if center:    
            width = os.get_terminal_size().columns
            if is_input:
                out = input("\n".join(line.center(width)  for line in colored_text.split("\n"))) 
                print(Style.RESET_ALL)   
                return out
            else:
                print("\n".join(line.center(width)  for line in colored_text.split("\n")))
            
        else:  
            if is_input:
                out = input(colored_text)
                print(Style.RESET_ALL)
                return out
            else:   
                print(colored_text)
        print(Style.RESET_ALL)
     
    def blue(self,text, center=True,is_input=False):
        colored_text = Fore.BLUE +text
        if center:    
            width = os.get_terminal_size().columns
            if is_input:
                out = input("\n".join(line.center(width)  for line in colored_text.split("\n")))    
                return out
            else:
                print("\n".join(line.center(width)  for line in colored_text.split("\n")))
            
        else:  
            if is_input:
                out = input(colored_text)
                return out
            else:   
                print(colored_text)
        print(Style.RESET_ALL)

    def magenta(self,text, center=True,is_input=False):
        colored_text = Fore.MAGENTA +text
        if center:    
            width = os.get_terminal_size().columns
            if is_input:
                out = input("\n".join(line.center(width)  for line in colored_text.split("\n")))    
                return out
            else:
                print("\n".join(line.center(width)  for line in colored_text.split("\n")))
            
        else:  
            if is_input:
                out = input(colored_text)
                return out
            else:   
                print(colored_text)
        print(Style.RESET_ALL)

    def cyan(self,text, center=True,is_input=False):
        colored_text = Fore.CYAN +text
        if center:    
            width = os.get_terminal_size().columns
            if is_input:
                out = input("\n".join(line.center(width)  for line in colored_text.split("\n")))    
                return out
            else:
                print("\n".join(line.center(width)  for line in colored_text.split("\n")))
            
        else:  
            if is_input:
                out = input(colored_text)
                return out
            else:   
                print(colored_text)
        print(Style.RESET_ALL)

    def white(self,text, center=True,is_input=False):
        colored_text = Fore.WHITE +text
        if center:    
            width = os.get_terminal_size().columns
            if is_input:
                out = input("\n".join(line.center(width)  for line in colored_text.split("\n")))    
                return out
            else:
                print("\n".join(line.center(width)  for line in colored_text.split("\n")))
            
        else:  
            if is_input:
                out = input(colored_text)
                return out
            else:   
                print(colored_text)
        print(Style.RESET_ALL)


def clear():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command =  os.system('cls') if platform.system().lower()=="windows" else os.system('clear')

    # Action
    return command
                    

