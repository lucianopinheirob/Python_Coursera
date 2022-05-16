seg = int(input("Por favor, entre com o número de segundos que deseja converter:"))

a = seg//86400
b = (seg%86400)//3600
c = ((seg%86400)%3600)//60
d = (((seg%86400)%3600)%60)

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
