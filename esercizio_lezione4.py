# creo oggetto CSVFile
class CSVFile():

    def __init__(self, name):
    #Set name
        self.name = name
    
# creo metodo  “get_data()” che torni i dati dal file CSV come lista di liste,  [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
    def get_data(self):
        my_file = open(self.name,'r')
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
        return list

# Controllo se funziona (su bash)
       
#==============================
#  Main del programma
#==============================
# srtampo a video
csv_file = CSVFile('shampoo_sales.csv')
print(csv_file.get_data())