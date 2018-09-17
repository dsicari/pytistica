# -*- coding: utf-8 -*-
# Tracar linha erro na exception
import traceback
# Classe Pytistica
from pytistica import Pytistica
# Componentes flask
from flask import Flask, render_template, request, send_file, make_response, redirect, url_for
# Nao utilizar cache
from nocache import nocache
# Matplot
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
# String de bytes
from io import BytesIO
import base64
# Sys
import sys
# DATE TIME
import datetime
import time
# LOG
import logging
from flask import jsonify

# CONFIG LOG
logger = logging.getLogger('pytistica')
hdlr = logging.FileHandler('pytistica.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)
logger.debug('Flask pytistica started...')

app = Flask(__name__)

@app.route('/pytistica')
def home():
    logger.debug('IP conexao: ' + request.environ['REMOTE_ADDR'] + ' IP Forwarded: ' + request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    return render_template('home.html')

@app.route('/result', methods = ['POST'])
#@nocache # Para nao utilizar cache
def result(): 
    if request.method == 'POST':
        try:
            result = request.form
            logger.debug('Result POST: ' + str(result))   
            pystt = Pytistica()      
            import matplotlib.pyplot as plt
            pystt.Calcular(result["DadosBrutos"], result["LimiteInferior"], result["AmplitudeClasse"])
            pystt.MontarTabelaFrequencia()            
            # Plota grafico
            x = []
            for li in pystt.ClasseLi:
                  x.append(li)
            
            plt.subplot(2, 1, 1)
            #plt.title('Pytistica') 
            plt.ylabel('Histograma')        
            plt.bar(x, pystt.Fi, align='edge', color='blue', edgecolor='black', linewidth=1.1, alpha=0.5, width=pystt.AmpClasse)
            plt.plot(pystt.Pm, pystt.Fi, marker='', color='blue', linewidth=2, alpha=1)            
            plt.subplot(2, 1, 2)
            plt.ylabel('Ogiva')        
            plt.bar(x, pystt.Fac, align='edge', color='red', edgecolor='black', linewidth=1.1, alpha=0.5, width=pystt.AmpClasse)
            plt.plot(pystt.Pm, pystt.Fac, marker='', color='red', linewidth=2, alpha=1) 
            # Para mexer no eixo x. Testar melhor!
            #xmin, xmax = plt.xlim()  
            #plt.xlim(xmax = xmax + 20)              
            #plt.xlim(xmin = xmax - 20)            
            # Transforma plot em string de bytes base64 para enviar ao html      
            figfile = BytesIO()
            plt.savefig(figfile, format='png')
            figfile.seek(0) # Volta ao comeco do arquivo
            
            figdata_png = base64.b64encode(figfile.getvalue())          
            # Limpar plt
            plt.gcf().clear
            plt.close('all')            

            dataParsedForTable = list(pystt.Chunks(pystt.Data, 5))            
            logger.debug("Data for table: " + str(dataParsedForTable))
            logger.debug("DataPlot: " + str(pystt.DataPlot))
            return render_template("result.html",
                                    limiteInferior = pystt.Li,
                                    amplitudeClasse = pystt.AmpClasse, 
                                    tamanhoAmostra = pystt.N,
                                    dataParsedForTable = dataParsedForTable,
                                    dataPlot = pystt.DataPlot, 
                                    imgPlot=figdata_png.decode('utf8'))
        except Exception as e:
            logger.debug("Unexpected error:")
            logger.debug(traceback.format_exc())
            logger.debug(e)

        return render_template("home.html", errorPytistica = "Opa, dados invalidos! Nao envie letras, verifique se os dados brutos possuem apenas espacos entre as amostras e tambem se os numeros reais estao com '.' ou ','.")

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5001)
