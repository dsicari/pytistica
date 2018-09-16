from terminaltables import AsciiTable

class Pytistica:

    def Chunks(self, l, n):
        #Yield successive n-sized chunks from l
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def Erase(self):
        self.N = 0
        self.Data = []
        self.NClasses = 0
        self.AmpClasse = 0
        self.Li = 0
        self.CountClass = 0
        self.ClasseLi = []
        self.ClasseLs = []
        self.Pm = []
        self.Classes = []        
        self.Fi = []
        self.Fr = []
        self.Frp = []
        self.Fac = []
        self.Frac = []
        self.Fracp = []
        self.NClasses = 0
        self.SumFi = 0
        self.SumFr = 0
        self.DataPlot = []
        self.SomaClasse = 0
        self.Data = []
        self.N = 0
        self.Li = 0
        self.AmpClasse = 0
        self.Data.sort()
        self.SomaClasse = 0
        self.DataPlot = []

    def Calcular(self, bruto, li, ampClasse):        

        self.N = 0
        self.Data = []
        self.NClasses = 0
        self.AmpClasse = 0
        self.Li = 0
        self.CountClass = 0
        self.ClasseLi = []
        self.ClasseLs = []
        self.Pm = []
        self.Classes = []        
        self.Fi = []
        self.Fr = []
        self.Frp = []
        self.Fac = []
        self.Frac = []
        self.Fracp = []
        self.NClasses = 0
        self.SumFi = 0
        self.SumFr = 0
        self.DataPlot = []
        self.SomaClasse = 0

        bruto = bruto.replace(',','.')
        bruto = bruto.replace('\r',' ')
        bruto = bruto.replace('\n','')
        bruto = bruto.replace('\t','')
        self.Data = []
        print('Dados brutos capturados: ' + bruto)
        for b in bruto:         
            if(b != ' '):
                try:
                    self.Data.append(float(b))
                except:
                    print('Fail to convert str to float')
                    print('Str: {' + b +'}')

        self.N = len(self.Data)
        self.Li = li
        self.AmpClasse = ampClasse
        self.Data.sort()
        self.SomaClasse = self.Li

        while True:
            self.SomaClasse = self.SomaClasse + self.AmpClasse
            if(self.Data[-1] > self.SomaClasse):
                self.NClasses = self.NClasses + 1
            else:
                self.NClasses = self.NClasses + 1
                break

        # Calcula limites classes
        for i in range(0, self.NClasses):
            self.ClasseLi.append(self.Li + self.CountClass * self.AmpClasse)
            self.CountClass += 1
            self.ClasseLs.append(self.Li + self.CountClass * self.AmpClasse)
        
        # Calcula ponto medio
        for p in range(0, self.NClasses):
            self.Pm.append((self.ClasseLi[p] + self.ClasseLs[p])/2)
        
        # Cria classes de frequencia 
        for i in range(0, self.NClasses):
            self.Classes.append(str(self.ClasseLi[i]) + " |--- " + str(self.ClasseLs[i]))

        # Calcula fi
        for c in self.ClasseLi:
            self.Ocorrencia = 0
            for d in self.Data:
                if(d>=c and d<(c+self.AmpClasse)):
                    self.Ocorrencia += 1
            self.Fi.append(self.Ocorrencia)
        
        # Calcula fr
        for f in self.Fi:
            self.x = f/self.N
            self.x = float("%0.4f"%self.x)
            self.Fr.append(self.x)
            self.x = self.x * 100
            self.Frp.append(self.x)        
        
        # Calcula fac
        for f in self.Fi:
            self.SumFi = self.SumFi + f
            self.Fac.append(self.SumFi)
        
        # Calcula frac
        for f in self.Fr:
            self.SumFr = self.SumFr + f
            self.Frac.append(self.SumFr)

        # Calcula fracp
        for f in self.Frac:
            self.Fracp.append(f*100)
    
    def MontarTabelaFrequencia(self):
        if not self.Fi:
            return False
        # Plota tabela
        self.DataPlot = []
        self.DataPlot.append(['Classe', 'Pm', 'Fi', 'Fr', 'Fr%', 'Fac', 'Frac', 'Frac%'])
        for i in range(0, self.NClasses):
            self.DataPlot.append([self.Classes[i], str(float(("%0.2f"%self.Pm[i]))), 
                                         str(self.Fi[i]), 
                                         str(float(("%0.4f"%self.Fr[i]))), 
                                         str(float(("%0.2f"%self.Frp[i]))), 
                                         str(float(("%0.2f"%self.Fac[i]))),
                                         str(float(("%0.4f"%self.Frac[i]))),
                                         str(float(("%0.2f"%self.Fracp[i])))])     
        #self.Table = AsciiTable(self.DataPlot)
        #print(self.Table.table) 

"""
pystt = Pytistica()
bruto = "2000 2012 2034 2345 2456 2546 2678 2390 2908 2512 2999"
li = 2000
ampClasse = 100
pystt.Calcular(bruto, li, ampClasse)
pystt.MontarTabelaFrequencia()
print(pystt.DataPlot)

Table = AsciiTable(pystt.DataPlot)
print(Table.table) 
"""
