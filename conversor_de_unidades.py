import os
import time

def limpar():
    os.system("clear")
def espera():
    time.sleep(2)
    
def color(cor):
    cores = {
             "azul": "\033[96m",
             "vermelho": "\033[31m",
             "amarelo": "\033[33m",
             "verde": "\033[92m",
             "ciano": "\033[36m"
    }
    return cores.get(cor.lower(), "\033[0m")

def notcolor():
    return "\033[0m"

def convert_dist():
    while True:
        limpar()
        print(f"=== {color('azul')}Conversor de distância{notcolor()} ===")
        print(f"\n1 - {color('amarelo')}Km{notcolor()} para {color('amarelo')}M{notcolor()}")
        print(f"2 - {color('amarelo')}M{notcolor()} para {color('amarelo')}Km{notcolor()}")
        print(f"3 - {color('amarelo')}M{notcolor()} para {color('amarelo')}Cm{notcolor()}")
        print(f"4 - {color('amarelo')}Cm{notcolor()} para {color('amarelo')}M{notcolor()}")
        print(f"5 - {color('amarelo')}Voltar{notcolor()}")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "":
            print(f"{color('vermelho')}\nInsira uma opção!{notcolor()}")
            espera()
        elif opcao not in ["1", "2", "3", "4", "5"]:
            print(f"{color('vermelho')}\nOpção inválida!{notcolor()}")
            espera()
        elif opcao == "1":
            limpar()
            km = input("\nQuilômetros: ")
            try:
                km = float(km)
                if km.is_integer():
                    km = int(km)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                m = km * 1000
                print(f"\n{color('verde')}{km} Km{notcolor()} = {color('ciano')}{m} m{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "2":
            limpar()
            m = input("\nMetros: ")
            try:
                m = float(m)
                if m.is_integer():
                    m = int(m)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                km = m / 1000
                print(f"\n{color('verde')}{m} m{notcolor()} = {color('ciano')}{km} Km{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "3":
            limpar()
            m = input("\nMetros: ")
            try:
                m = float(m)
                if m.is_integer():
                    m = int(m)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                cm = m * 100
                print(f"\n{color('verde')}{m} m{notcolor()} = {color('ciano')}{cm} Cm{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "4":
            limpar()
            cm = input("\nCentimetros: ")
            try:
                cm = float(cm)
                if cm.is_integer():
                    cm = int(cm)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                m = cm / 100
                print(f"\n{color('verde')}{cm} Cm{notcolor()} = {color('ciano')}{m} m{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "5":
            break       
                
def convert_peso():
    while True:
        limpar()
        print(f"=== {color('azul')}Conversor de Peso (massa){notcolor()} ===")
        print(f"\n1 - {color('amarelo')}Kg{notcolor()} para {color('amarelo')}G{notcolor()}")
        print(f"2 - {color('amarelo')}G{notcolor()} para {color('amarelo')}Kg{notcolor()}")
        print(f"3 - {color('amarelo')}Kg{notcolor()} para {color('amarelo')}Lb{notcolor()}")
        print(f"4 - {color('amarelo')}Lb{notcolor()} para {color('amarelo')}Kg{notcolor()}")
        print(f"5 - {color('amarelo')}Voltar{notcolor()}")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "":
            print(f"\n{color('vermelho')}\nInsira uma opção!{notcolor()}")
            espera()
            continue
        elif opcao not in ["1", "2", "3", "4", "5"]:
            print(f"{color('vermelho')}\nOpção inválida{notcolor()}")
            espera()
            continue
        elif opcao == "1":
            limpar()
            kg = input("\nQuilogramas: ")
            try:
                kg = float(kg)
                if kg.is_integer():
                    kg = int(kg)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                g = kg * 1000
                print(f"\n{color('verde')}{kg} Kg{notcolor()} = {color('ciano')}{g} g{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "2":
            limpar()
            g = input("\nGramas: ")
            try:
                g = float(g)
                if g.is_integer():
                    g = int(g)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                kg = round(g / 1000, 2)
                print(f"\n{color('verde')}{g} g{notcolor()} = {color('ciano')}{kg} Kg{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "3":
            limpar()
            kg = input("\nQuilogramas: ")
            try:
                kg = float(kg)
                if kg.is_integer():
                    kg = int(kg)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                lb = round(kg * 2.20462, 2)
                print(f"\n{color('verde')}{kg} Kg{notcolor()} = {color('ciano')}{lb} Lb{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "4":
            limpar()
            lb = input("\nLibras: ")
            try:
                lb = float(lb)
                if lb.is_integer():
                    lb = int(lb)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                kg = round(lb / 2.20462, 2)
                print(f"\n{color('verde')}{lb} Lb{notcolor()} = {color('ciano')}{kg} Kg{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "5":
            break

def convert_temp():
    while True:
        limpar()
        print(f"=== {color('azul')}Conversor de temperatura{notcolor()} ===")
        print(f"\n1 - {color('amarelo')}Celsius{notcolor()} para {color('amarelo')}Fahrenheit{notcolor()}")
        print(f"2 - {color('amarelo')}fahrenheit{notcolor()} para {color('amarelo')}Celsius{notcolor()}")
        print(f"3 - {color('amarelo')}Celsius{notcolor()} para {color('amarelo')}Kelvin{notcolor()}")
        print(f"4 - {color('amarelo')}Voltar{notcolor()}")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "":
            print(f"{color('vermelho')}\nInsira uma opção!{notcolor()}")
            espera()
            continue
        elif opcao not in ["1", "2", "3", "4"]:
            print(f"{color('vermelho')}\nOpção inválida{notcolor()}")
            espera()
            continue
        elif opcao == "1":
            limpar()
            c = input("\nCelsius: ")
            try:
                c = float(c)
                if c.is_integer():
                    c = int(c)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                f = round((c * 9/5) + 32, 1)
                print(f"\n{color('verde')}{c}°C{notcolor()} = {color('ciano')}{f}°F{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "2":
            limpar()
            f = input("\nFahrenheit: ")
            try:
                f = float(f)
                if f.is_integer():
                    f = int(f)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                c = round((f - 32) * 5/9, 1)
                print(f"\n{color('verde')}{f}°F{notcolor()} = {color('ciano')}{c}°C{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "3":
            limpar()
            c = input("\nCelsius: ")
            try:
                c = float(c)
                if c.is_integer():
                    c = int(c)
            except ValueError:
                print(f"\n{color('vermelho')}Digite apenas números!{notcolor()}")
                espera()
            else:
                k = round(c + 273.15, 1)
                print(f"\n{color('verde')}{c}°C{notcolor()} = {color('ciano')}{k}°K{notcolor()}")
                input("\nAperte enter para voltar")
        elif opcao == "4":
            break
                 
def menu():
    while True:
        limpar()
        print(f"=== {color('azul')}Conversor de unidades{notcolor()} ===")
        print(f"\n1 - {color('amarelo')}Converter{notcolor()} Distância")
        print(f"2 - {color('amarelo')}Converter{notcolor()} Peso")
        print(f"3 - {color('amarelo')}Converter{notcolor()} Temperatura")
        print(f"4 - {color('amarelo')}Sair{notcolor()}")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "":
            print(f"{color('vermelho')}\nInsira uma opção!{notcolor()}")
            espera()
            continue
        elif opcao not in ["1", "2", "3", "4"]:
            print(f"{color('vermelho')}\nOpção inválida!{notcolor()}")
            espera()
            continue
        elif opcao == "1":
            convert_dist()
        elif opcao == "2":
            convert_peso()
        elif opcao == "3":
            convert_temp()
        elif opcao == "4":
            limpar()
            print("encerrando...")
            break

menu()