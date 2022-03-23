# creo oggetto CSVFile
class CSVFile():

    def __init__(self, name):
    #Set name
        self.name = name
    # creo metodo  “get_data()” che torni i dati dal file CSV come lista di liste,  [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
    def get_data(self):
        # provo ad aprire il file, se non riesco faccio scrivere a monitor l'errore
        try:
            my_file = open(self.name,'r')
        except Exception as eccezione:
            print('Errore: non trovo il file ...')
            print('Ed ho avuto questo Errore: "{}"'.format(eccezione))
        return
        #inizializzo la lista
        list = []
        #ciclo sulle righe del file
        for line in my_file:   
            # Faccio lo split di ogni riga sulla virgola   
            line = line.strip()   
            #
            line_elements = line.split(',')   # Se NON sto processando l’intestazione... 
                #elements[-1] = elements[-1].strip() # con -1 accedo all'ultimo carattere e tolgo dall'ultimo elemento il newline \n strip toglie le porcherie
            if not line_elements[0].startswith('Date'):        # Setto la data e il valore             
        # Aggiungo alla lista dei valori questo valore         
                   list.append(line_elements) #mettebndo elements invece che [date,value] potrei avere più colonne
        # Chiudo il file
        my_file.close()
        
        return list


############################################################################################

class NumericalCSVFile(CSVFile):
# function per estendere l'oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che converta automaticamente a numero tutte le colonne tranne la prima (data)
    def get_data(self):
          # Chiamo la get_data del padre 
        string_data = super().get_data()
        
        # Preparo lista per contenere i dati ma in formato numerico
        numerical_data = []    
        #ciclo sulle righe del file originale
        for string_line in string_data:   
# Preparo una lista di supporto per salvare la riga
            # in "formato" nuumerico (tranne il primo elemento)
            numerical_row = []
            
            # Ciclo su tutti gli elementi della riga con un
            # enumeratore in modo daavere anche il numero di riga
            for i,element in enumerate(string_row):
                
                if i == 0:
                    # Il primo elemento della riga lo lascio in formato stringa
                    numerical_row.append(element)
                    
                else:
                    # Converto a float tutto gli altri. Ma se fallisco, stampo
                    # l'errore e rompo il ciclo (e poi saltero' la riga).
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                
            # Alla fine aggiungo la riga in formato numerico alla lista
            # "esterna", ma solo se sono riuscito a processare tutti gli
            # elementi. Qui controllo per la lunghezza, ma avrei anche potuto
            # usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        return numerical_data

# Controllo se funziona (su bash)
       
#==============================
#  Main del programma
#==============================
# srtampo a video
csv_file = CSVFile(name='shampoo_sales.csv') #--> nome file corretto, per mandarlo inerrore metto un nome di file che non ho, ad es shampoo:salesbbb.csv
#csv_file = CSVFile('shampoo_salesbbb.csv')
print('Nome del file: "{}"'.format(csv_file.name))
print('Dati contenuti nel file: "{}"'.format(csv_file.get_data()))

#csv_file_numerico = NumericalCSVFile(name='shampoo_sales.csv')
#print(csv_file_numerico.name)
#print(csv_file_numerico.get_data())