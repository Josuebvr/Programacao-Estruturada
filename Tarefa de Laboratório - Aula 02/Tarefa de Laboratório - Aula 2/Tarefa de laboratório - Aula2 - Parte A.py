
var_febre = input("Você está com febre? (sim/não) ")
tem_febre = var_febre == "sim"
sem_febre = var_febre == "não"
print(tem_febre)

var_tosse = input("Você tem tosse?")
tem_tosse = var_tosse == "sim"
sem_tosse = var_tosse == "não"
print(tem_tosse)

var_ar = input("Você está com dificuldade para respirar?")
tem_falta_ar = var_ar == "sim"
sem_ar = var_ar == "não"
print(tem_falta_ar)

covid = (tem_febre) and (tem_tosse) and (tem_falta_ar)

if (covid):
    print("Provavelmente você tem Covid")
else:
    print("Provavelmente você não tem Covid")
