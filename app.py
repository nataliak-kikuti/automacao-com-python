import pyautogui
from time import sleep

pyautogui.click(987,543, duration=2)
pyautogui.write('nome')

pyautogui.click(971,572, duration=2)
pyautogui.write('senha')

pyautogui.click(846,614, duration=2)

with open('produtos.txt','r') as file:
    for linha in file:
        produto = linha.split(',')[0]  
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(642,532 )
        pyautogui.write(produto)

        pyautogui.click(629,560)
        pyautogui.write(quantidade)

        pyautogui.click(621,595)
        pyautogui.write(preco)

        pyautogui.click(518,785)
        sleep(1)