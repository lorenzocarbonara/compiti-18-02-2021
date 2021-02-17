Nord = int(input("Inserire il fatturato nel nord."))
Centro = int(input("Inserire il fatturato nel centro."))
Sud = int(input("Inserire il fatturato nel sud."))
Isole = int(input("Inserire il fatturato nelle isole."))
fatturato = {'Nord':Nord,
'Centro': Centro,
'Sud ': Sud,
'Isole':Isole}
totale = Nord + Centro + Sud + Isole 
per_Nord = Nord/tot*100
per_Centro = Centro/tot*100
per_Sud = Sud/tot*100
per_Isole = Isole/tot*100

fatturato_per = {'Nord':per_Nord,
'Centro': per_Centro,
'Sud ': per_Sud,
'Isole':per_Isole}
print("Il fatturato è di ",totale," €.")
print("Il fatturato è diviso in questo modo")
print(fatturato)
print("Ed è diviso percentualmente in questo modo")
print(fatturato_per)