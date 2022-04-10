class Output2:
    def writeNo2(self):
        f = open("question_no2", "w")
        n = int(input("Masukan nilai N : "))
        arrno2 = []*n
        i = 0
        while(i<n):
            j=0
            strtampung = ""
            while(j<n):
                if(j<n-i):
                    strtampung += "*"
                j+=1
            arrno2.append(strtampung)
            i+=1
            
        print("Isi array :")
        print(arrno2)
        i = 0
        while(i<len(arrno2)):
            f.write(arrno2[i])
            f.write("\n")
            i+=1
        print("Input No 1 Successful, bacanya difile read ato difilenya")
        f.close()
        
    def readNo2(self):
        f = open("question_no2", "r")
        tampung = f.read()
        print("Isi dari output question_no2 : ")
        print(tampung)
        f.close()

Output2.writeNo2(Output2)
Output2.readNo2(Output2)
    