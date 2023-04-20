import pandas

read_file = pandas.read_excel ("Test.xlsx")
  
read_file.to_csv ("Test.csv", index = None, header=True)
    
df = pandas.DataFrame(pandas.read_csv("Test.csv"))
