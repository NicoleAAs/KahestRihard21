def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas


def salvesta_failisse(f,text):
    fail=open(f,"a",encoding="utf-8-sig")
    fail.write+(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas
def tolkimine(f):
    pass
rus=loe_failist("rus.txt")
eng=loe_failist("eng.txt")
print(rus)
print(eng)


while True:
    g=input("1 перевод,2 Новое слово,3 испровление ошибок,4 Проверка знаний") 
    if g=="1":
        tolkimine()
    elif g=="2":
        rus_sana=input("введи слово на руском:")
        ang_sona=("write words on English:")
        rus_listsalvista_failisse("rus.txt",rus_sona)
