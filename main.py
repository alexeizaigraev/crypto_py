import os, sys
import shutil
import datetime

class Crypto:
    def __init__(self, fname):
        self.txt = '' #   логи и сообщения
        self.mail1 = 'neya1969@gmail.com'
        self.mail2 = 'vovan@gmail.com'

        self.in_fname = fname # имя файлв в папке in
        self.short_fname = fname.split('/')[-1] # короткое имя файла
        self.arhiv_fname = "arhiv/" + self.short_fname # имя файла в архиве

        self.prefixes = ['f', 'qu-qu'] # шифруемые файлы должны начинаться с префиксов

        self.comand = self.mk_gpg_command() # клманда шифрования

        self.flag_to_arhiv = self.mk_flag_to_arhiv()


    def mk_flag_to_arhiv(self): # определяет нужно ли шифровать
        for prefix in self.prefixes:
            if prefix in self.short_fname[:len(prefix)]:
                return False 
        return True
    

    def mk_gpg_command(self): # строит команду шифрования
        return "gpg --output out/" + self.short_fname + ".gpg --encrypt --recipient " + self.mail1 + " --recipient " + self.mail2 + " in/" + self.short_fname
  

    def nau(self):
        return str(datetime.datetime.now())



    def log_it(self):
        """Записывает текст self.txt в файл с именем logi.txt"""
        with open('logi.txt', 'a', encoding="UTF-8") as out_object:
            out_object.write(self.txt + "\t" + self.nau() + "\n")
        print(self.txt)


    def main(self):
        if self.flag_to_arhiv: # aрхивирует
            self.txt = "to_arhiv " + self.short_fname
            self.log_it()

            try:
                shutil.move(self.in_fname, self.arhiv_fname)
            except:
                pass
    
        else:
            try:
                os.system(self.comand) # выполение шифрования                
                self.txt = self.comand
                self.log_it()            
            except Exception as ex:
                print(ex)
                self.txt = str(ex)
                self.log_it()
            try:
                os.remove(self.in_fname) # удаление файла из входящих
            except:
                pass



fnames = os.listdir("in/")
if fnames:
    #print("______________\n", fnames, "\n______________\n")
    for fname in fnames:
        full_fname = "in/" + fname
        my_file = Crypto(full_fname)
        my_file.main()
    print("\n_____end_____\n")

else:
    print("empty, by-by!")

