inicio=input()
inicioMayus=inicio.upper()
inicioFinal=inicioMayus.replace(" ","")
reversa=inicioFinal[::-1]
if inicioFinal==reversa:
  print("Es un palindromo")
else:
  print("NO es un palindromo")