
from utils.colors import Colors,clear
from utils.logger import setup_logger
import sys,os,time
import datetime
from config import settings
import logging
class GeneralMenu:
    def __init__(self):
  
        self.color = Colors()
        fecha_archivo = datetime.datetime.today().strftime('%Y_%m_%d_%H')
        print( f'{settings.BASE_DIR}\logs\{fecha_archivo}.log')
        self.logger = setup_logger(name='my_logger',log_file= f'{settings.BASE_DIR}\\logs\\{fecha_archivo}.log',level=logging.ERROR)
        self.choices = {
            1:self.search_file,
            2:self.quit
        }
    def show_menu(self):
        # clear()
        self.color.yellow("""
        =======================
        Menu 
        ========================
        1. Search word in file
        2. Exit
        """)
    def run(self):
        while True:
            self.show_menu()
            choice = int(self.color.green('Select an option: ',is_input=True,center=False))
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print('{0} <-- No es una eleccion valida '.format(choice))

    def search_file(self):
        path = self.color.green("Paste your path:: ",is_input=True,center=False)
        extension = str('.'+self.color.green("Extension to find ex: js (blank for anyone): ",is_input=True,center=False))

        # 
        my_index = 0
        search = self.color.green("Write the exact word to search: ",is_input=True,center=False)
        listOfFiles = list()
        for i,(dirpath, dirnames, filenames) in enumerate(os.walk(path)):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames]
            
        if len(extension)<2:
            self.color.yellow("Maybe some files can't be read")
            time.sleep(5) 
        for i in range(1,len(listOfFiles)):       
            # line.rstrip()
            try:
                if len(extension) > 1:
                    if listOfFiles[i].endswith(extension):
                        js = open(listOfFiles[i], "r", encoding="utf8").readlines()
                else:
                    
                    js = open(listOfFiles[i], "r", encoding="utf8").readlines()
                for index,line in enumerate(js):
                    if search in line:
                    
                        my_index = my_index + 1
                        path_file = listOfFiles[i]
                        fecha_archivo = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M')
                        with open(f'{fecha_archivo}_out.txt','a') as file_txt:
                            file_txt.write(f"{my_index}  {line.split()[1]} LINE:{index +1} --> src{path_file}\n")
                    
                        
                     
            except Exception as e:
                
                exception_type, exception_object, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno
                
                self.logger.error(f"ExecptionType: {exception_type} FILE: {filename} LINE:{ line_number }  {e}")

        with open('out.txt','a') as file_txt:
            file_txt.write(f"FILES ANALIZED {len(listOfFiles)}")
        print("FILES ANALIZED",len(listOfFiles))

                    
        

    def quit(self):
        print('Gracias por usar el demo de proyecto Talent Solution :)')
        exit()
    

        

if __name__ == "__main__":
    GeneralMenu().run()

