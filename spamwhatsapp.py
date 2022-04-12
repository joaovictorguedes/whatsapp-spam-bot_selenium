from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys

driver = Edge(executable_path=r'C:\Users\Victo\OneDrive\Documentos\Python\Bots\Bot spam do zap\msedgedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input('bota aqui o nome do contato ou grupo EXATAMENTE IGUAL : ')
msg = input('bota a msg parsa : ')
count = int(input('quantas mensage tu quer : '))
choice = str('S').upper()

input('Aperte enter quando fizer login no zap ')

while choice == 'S':

    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        msg_box = driver.find_element_by_class_name('_3uMse')

        for i in range(count):
            msg_box.send_keys(msg)
            msg_box.send_keys('\ue007')
        choice = input('Deseja continuar? [S/N]').upper()

    except:
        print('Você colocou algum dado errado amigo, favor revisar. Próximo erro o programa irá fechar')
        name = input('bota aqui o nome do contato ou grupo EXATAMENTE IGUAL : ')
        msg = input('bota a msg parsa : ')
        count = int(input('quantas mensage tu quer : '))
        
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_class_name('_3uMse')

        for i in range(count):
            msg_box.send_keys(msg)
            msg_box.send_keys('\ue007')
        choice = input(print('Deseja continuar? [S/N]')).upper()
    
        
    