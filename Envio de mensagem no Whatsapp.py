# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import pyautogui as pat
import pyperclip
import time

pat.PAUSE = .5

pat.click("chrome.PNG")
for i in range(326): #número de repetições
    pat.click("novaaba.PNG")
    pyperclip.copy("wa.me/55")
    pat.hotkey('Ctrl','V')
    pat.click("excel.PNG")
    pat.keyDown('ctrl')
    pat.press('c')
    pat.keyUp('ctrl')  
    pat.click("chrome.PNG")
    pat.moveTo(1145,402)
    pat.hotkey('Ctrl','V')
    pat.press('Enter')
    time.sleep(2)
    pronto = pat.locateOnScreen("pronto.PNG")
    semzap = pat.locateOnScreen("semzap.PNG")
    while semzap is None and pronto is None:
        pronto = pat.locateOnScreen("pronto.PNG")
        semzap = pat.locateOnScreen("semzap.PNG")  
        print("Esperando Semzap e Pronto")
    if semzap is not None:
        pat.click("semzap.PNG")
        pat.click("excel.PNG")
        pat.press('right')
        pat.write('Nao Enviado')
        pat.press('Enter')
        pat.press('left')
        pat.click("chrome.PNG")   
        pat.hotkey('Ctrl', 'w')
    else:
        print("Debugando")
        pronto = pat.locateOnScreen("pronto.PNG")
        while pronto == None:
            print("Esperando Pronto")
            pronto = pat.locateOnScreen("pronto.PNG")
        if pronto is not None:
            pyperclip.copy("Prezado (a) verificamos que foi feito o cadastro no simulador, mas a migração não foi efetivada, caso ainda tenha alguma dúvida, pedimos que entre em contato conosco pelo telefone 21 3282-8260 / 3282-8160 ou pelo whatsapp 21 99163-8180. Favor não retornar por esse número, utilizar os contatos informados acima. Fique atento ao prazo.") # Mensagem a ser enviada
            pat.hotkey('Ctrl','V')
            time.sleep(1)
            pat.press('Enter')
            pat.click("excel.PNG")
            pat.press('right')
            pat.write('Enviado')
            pat.press('Enter')
            pat.press('left')
            pat.click("chrome.PNG")  
            pat.hotkey('Ctrl', 'w')
    
    
    
    
