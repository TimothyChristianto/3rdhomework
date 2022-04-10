class Output1:
    def writeNo1(self):
        f = open("question_no1", "w")
        n = int(input("Masukan nilai N : "))
        arrno1 = []*n
        i = 1
        while(i<=n):
            j=0
            strtampung = ""
            while(j<=n):
                if(j<i):
                    strtampung += "*"
                j+=1
            arrno1.append(strtampung)
            i+=1
        print("Isi array :")
        print(arrno1)
        i = 0
        while(i<len(arrno1)):
            f.write(arrno1[i])
            f.write("\n")
            i+=1
        print("Input No 1 Successful, bacanya difile read ato difilenya")
        f.close()
        
    def readNo1(self):
        f = open("question_no1", "r")
        tampung = f.read()
        print("Isi dari output question_no1 : ")
        print(tampung)
        f.close()

Output1.writeNo1(Output1)
Output1.readNo1(Output1)

    