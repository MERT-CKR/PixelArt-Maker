import os
import subprocess



line1=f""
line2=f""
line3=f""
line4=f""
line5=f""
line6=f""

def main():
    global line1,line2,line3,line4,line5,line6,input1
    print("use only english letters")
    input1= input("yazdırmak istediğiniz metni girin: ")
    for i1 in input1:
        i1=i1.lower()
        line1+=f"{i1}[1]"
        line2+=f"{i1}[2]"
        line3+=f"{i1}[3]"
        line4+=f"{i1}[4]"
        line5+=f"{i1}[5]"
        line6+=f"{i1}[6]"
            
main()

#add comma between items except last one
line1 = line1.replace("]","],")[:-1]
line2 = line2.replace("]","],")[:-1]
line3 = line3.replace("]","],")[:-1]
line4 = line4.replace("]","],")[:-1]
line5 = line5.replace("]","],")[:-1]
line6 = line6.replace("]","],")[:-1]




def makeScript(fileName, icerik):
    with open(fileName+".py", 'w',encoding="UTF-8") as dosya:
        dosya.write(icerik)


icerik = f"""
with open("characters.txt", "r", encoding="utf-8") as dosya:
        metinler = dosya.read().split("\\n\\n\\n")


for x1 in range(25):
        metinler[x1]=metinler[x1].split("\\n")        

a = metinler[0]
b = metinler[1]
c = metinler[2]
d = metinler[3]
e = metinler[4]
f = metinler[5]
g = metinler[6]
h = metinler[7]
i = metinler[8]
j = metinler[9]
k = metinler[10]
l = metinler[11]
m = metinler[12]
n = metinler[13]
o = metinler[14]
p = metinler[15]
q = metinler[16]
r = metinler[17]
s = metinler[18]
t = metinler[19]
u = metinler[20]
v = metinler[21]
w = metinler[22]
x = metinler[23]
y = metinler[24]
z = metinler[25]
a=['']+a
print({line1})
print({line2})
print({line3})
print({line3})
print({line4})
print({line5})
print({line6})
input()
"""

makeScript(input1, icerik)

current_dir = os.getcwd()
input1=input1+".py"
subprocess.run(["python", os.path.join(current_dir, input1)])