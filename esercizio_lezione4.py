# creo oggetto CSVFile
class CSVFile():

    def __init__(self, name):
    #Set name
        self.name = name

  #  def __str__(self):
  #      return 'CSVFile "{}"'.format(self.name)

#nomefile = CSVFile('shampoo_sales.csv')
#print(nomefile)
# inizializzo con il nome del file csv
    
# creo un attibuto name che contenga il nome del file csv

# creo metodo  “get_data()” che torni i dati dal file CSV come lista di liste,  [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
    def get_data(self):
        list = []
        my_file = open(self.name,'r')
        for line in my_file:   
            # Faccio lo split di ogni riga sulla virgola   
                elements = line.split(',')   # Se NON sto processando l’intestazione... 
                elements[-1] = elements[-1].strip() # con -1 accedo all'ultimo carattere e tolgo dall'ultimo elemento il newline \n strip toglie le porcherie
                if elements[0] != 'Date':        # Setto la data e il valore        
                   date  = elements[0]        
                   value = elements[1]        
        # Aggiungo alla lista dei valori questo valore         
                   line.append(elements) #mettebndo elements invece che [date,value] potrei avere più colonne
        return list

#csvfile = CSVFile('shampoo_sales.csv')
#print(csvfile.get_data())
 