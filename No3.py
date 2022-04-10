class Output3:
    def writeNo3(self):
        f = open("question_no3", "w")
        n = int(input("Masukan nilai N : "))
        arrno3 = []*n
        i = 1
        
        while(i<=n):
            j=0
            angka = 1
            angka1 = 1
            angka2 = 1
            strtampung = ""
            while(j<=n):
                if(j<i):
                    strtampung+=str(angka1)
                    angka3 = angka1+angka2
                    angka1 = angka2
                    angka2 = angka3
                j+=1
            arrno3.append(strtampung)
            i+=1
        
        print("Isi array :")
        print(arrno3)
        i = 0
        while(i<len(arrno3)):
            f.write(arrno3[i])
            f.write("\n")
            i+=1
        print("Input No 1 Successful, bacanya difile read ato difilenya")
        f.close()
        
    def readNo3(self):
        f = open("question_no3", "r")
        tampung = f.read()
        print("Isi dari output question_no3 : ")
        print(tampung)
        f.close()

Output3.writeNo3(Output3)
Output3.readNo3(Output3)   
