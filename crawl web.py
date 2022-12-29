import re
import subprocess

yd = "01068"

def inn(yd):
    try:
        result = subprocess.check_output('curl -F "SoBaoDanh='+yd+'" diemthi.hcm.edu.vn/Home/Show')

        def Loc(result):
    
            mu = result.decode()
            chu = str(mu)

            ls = chu.split("\r\n")
            return ls 

        ym = Loc(result)

        ls = []
        for i in range(len(ym)):
            if "<" in ym[i]:
                ym[i] = ""
        for i in ym :
            if i != "" :
                ls.append(i)

        lsm1 = []
        for i in ls:
            for a in i:
                 if a != " ":
                     lsm1.append(i)
                     break
                 else:
                     pass
 
        line1 = lsm1[-2]
        line2 = lsm1[-1]

        print(line1)
        print(line2)

        def hecc(st):                       ### HEC to Unicode
             lin = []
             lin4 = []
             lin5 = ""
             lin3=st
             chec = ""
             for i in range(len(st)):
                  lin2 = lin
                  if st[i] == "#":
                      chec = st[i+1:i+4]

                      new = str(chr(int(chec))) 
                      lin.append(new)
             for i in lin3:
                  lin4.append(i)
     
             for new in lin:
                 for i in range(len(lin4)):
                      if lin4[i] == "#":
                          lin4[i-1] = ""
                          lin4[i] = new
                          lin4[i+1] =""
                          lin4[i+2] =""
                          lin4[i+3] =""
                          lin4[i+4] =""
                          break
                      else:
                          pass
             for i in lin4:
                  lin5+=i
               
             return lin5
              

        line1 = hecc(line1)         
        line2 = hecc(line2)
        print(line1)
        print(line2)
        mun1 = line2.split(":")
        poi0 = mun1[0][:-7]              #Subject
        mun = []
        for i in mun1:
                mo = re.sub(r"\s+", "", i, flags=re.UNICODE)
                mun.append(mo)
        print(mun)
        
        poi1 = mun[1][:-5]
        poi2 = mun[2][:-4]

        if "Chínhthức" in mun[3]:
            poi3 = mun[3][:-9]
            poi4 = "Chính thức"
        elif "Dựbị" in mun [3]:
            poi3 = mun[3][:-4]
            poi4 = "Dự bị"
        else:
            poi3 = mun[3]
            poi4 = ""
      
        def Loc2(st):            ### " " to ""
             for i in st:
                 if i == " ":
                     st = st[1:]
                 else:
                     return st
        line1 = Loc2(line1)
        poi0 = Loc2(poi0)

        def Loc3(st):            ### Capital
             st1 = st.split(" ")
             nu = len(st1)
             for i in range(nu):
                  st1[i] = st1[i].lower()
                  st1[i] = st1[i].capitalize()
             st2 = st1[0]
             for i in range(1,nu):
                  st2 += " "+ st1[i]
             return st2

        line1 = Loc3(line1) 

        lsna = yd+","+line1+","+poi0+","+poi1+","+poi2+","+poi3+","+poi4
        print(lsna)
        return lsna
        

    except:
        return

#####################################################

with open("Name.csv","w" ,encoding = "utf-8") as na:
      sp = "SBD,Name,Subject,Point1,Point2,Total,Status\n"
      na.write(sp)
for i in range(1000,9999):
    try:
        st = inn("0"+str(i))
        with open("Name.csv","a" ,encoding = "utf-8") as na:
              na.write(st+"\n")
    except:
        continue

for i in range(10000,11100):
    try:
        st = inn(str(i))
        with open("Name.csv","a" ,encoding = "utf-8") as na:
              na.write(st+"\n")
    except:
        continue
