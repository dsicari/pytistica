import sys
from terminaltables import AsciiTable
import matplotlib.pyplot as plt

n = 0
data = []
nClasses = 0
ampClasse = 0
Li = 0

while True:
    print("PYTISTICA - TAB FREQ, HISTOGRAMA, OGIVAS E MUITA DIVERSAO")
    print("[I] Inserir dados brutos")
    print("[A] Calcular") 
    print("[Q] Sair")
    
    opcao = str(input())
    
    if(opcao == "Q"):
        sys.exit()
    elif(opcao == "A"):
        data.sort()
        
            
        print("Limite inferior: ")
        Li = int(input())
        print("Amplitude classe: ")
        ampClasse = int(input())

        
        # Qtde classe se dara pelo incremento da amplitude ate que o ultimo item de data esteja dentro da faixa
        #print("Qtde classes: ")
        #nClasses = int(input())
        somaClasse = Li
        nClasses = 0
        while True:
            somaClasse = somaClasse + ampClasse
            if(data[-1] > somaClasse):
                nClasses = nClasses + 1
            else:
                nClasses = nClasses + 1
                break
        
        print("Quantidade classe(s): " + str(nClasses))

        print("ROL: " + str(data))
        
        countClass = 0
        classeLi = []
        classeLs = []
        pm = []
        classes = []        
        fi = []
        fr = []
        frp = []
        fac = []
        frac = []
        fracp = []

        # Calcula limites classes
        for i in range(0, nClasses):
            classeLi.append(Li + countClass * ampClasse)
            countClass += 1
            classeLs.append(Li + countClass * ampClasse)
        
        # Calcula ponto medio
        for p in range(0, nClasses):
            pm.append((classeLi[p] + classeLs[p])/2)
        
        # Cria classes de frequencia 
        for i in range(0, nClasses):
            classes.append(str(classeLi[i]) + " |--- " + str(classeLs[i]))

        # Calcula fi
        for c in classeLi:
            ocorrencia = 0
            for d in data:
                if(d>=c and d<(c+ampClasse)):
                    ocorrencia += 1
            fi.append(ocorrencia)
        
        # Calcula fr
        for f in fi:
            x = f/n
            x = float("%0.4f"%x)
            fr.append(x)
            x = x * 100
            frp.append(x)
        
        sumFi = 0
        # Calcula fac
        for f in fi:
            sumFi = sumFi + f
            fac.append(sumFi)

        sumFr = 0
        # Calcula frac
        for f in fr:
            sumFr = sumFr + f
            frac.append(sumFr)

        # Calcula fracp
        for f in frac:
            fracp.append(f*100)

        # Printa tabela
        dataPlot = []
        dataPlot.append(['Classes', 'Pm', 'Fi', 'Fr', 'Fr%', 'Fac', 'Frac', 'Frac%'])
        for i in range(0, nClasses):
            dataPlot.append([classes[i], str(float(("%0.2f"%pm[i]))), 
                                         str(fi[i]), 
                                         str(float(("%0.4f"%fr[i]))), 
                                         str(float(("%0.2f"%frp[i]))), 
                                         str(float(("%0.2f"%fac[i]))),
                                         str(float(("%0.4f"%frac[i]))),
                                         str(float(("%0.2f"%fracp[i])))])     
        table = AsciiTable(dataPlot)
        print(table.table)  

        # Plota grafico
        x = []
        for li in classeLi:
            x.append(li)        

        plt.subplot(2, 1, 1)
        plt.title('Pytistica') 
        plt.ylabel('Histograma')        
        plt.bar(x, fi, align='edge', color='blue', edgecolor='black', linewidth=1.1, alpha=0.5, width=ampClasse)
        plt.plot(pm, fi, marker='', color='blue', linewidth=4, alpha=1)#,label='Poligono de frequencia')

        plt.subplot(2, 1, 2)
        plt.ylabel('Ogiva')        
        plt.bar(x, fac, align='edge', color='red', edgecolor='black', linewidth=1.1, alpha=0.5, width=ampClasse)
        plt.plot(pm, fac, marker='', color='red', linewidth=4, alpha=1)
                       
        plt.show()
     
    elif(opcao == "I"):
        print("Insira os dados brutos, separados por espaco")
        bruto = str(input())
        bruto = bruto.split(' ')
        for b in bruto:
            data.append(int(b))
        print("Dados brutos: " + str(data))
        n = len(data)
        print("Tamanho amostra (n): " + str(len(data)))
