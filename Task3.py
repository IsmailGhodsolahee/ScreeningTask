# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:33:47 2020

@author: Rtyeuwki
"""
def Replacement(InputFileName,OutputFileName):
    fi=open(InputFileName,'r')
    fo=open(OutputFileName,'w')
    Conte=fi.readline()
    leng=6;Ncont="";
    while leng<len(Conte) and Conte[leng]!="#":
        Ncont=Ncont+Conte[leng]
        leng+=1
    for i in range(0,int(Ncont)):
        Conte=fi.readline()
        Nconte=""
        if "cnot" in Conte or "CNOT" in Conte:
            Conte=Conte.strip();
            leng=5
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            leng+=1
            Nconte=""
            while leng<len(Conte) and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var2=Nconte
            fo.write("Rzt (0.5*pi) "+var1+"\n"+"Rxt (0.5*pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n"+"c-z "+var1+","+var2+"\n"+"Rzt (0.5*pi) "+var1+"\n"+"Rxt (0.5*pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n")
        elif "c-z" in Conte or "C-Z" in Conte:
            Conte=Conte.strip();
            leng=4
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            leng+=1
            Nconte=""
            while leng<len(Conte) and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var2=Nconte
            fo.write("c-z "+var1+","+var2+"\n")
        elif "rzt" in Conte or "RZT" in Conte or "Rzt" in Conte:
            Conte=Conte.strip();
            leng=0
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write(var1+"\n")
        elif "ryt" in Conte or "RYT" in Conte or "Ryt" in Conte:
            Conte=Conte.strip();
            leng=5
            Nconte=""
            while Conte[leng]!=")" and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            leng+=1
            Nconte=""
            while leng<len(Conte) and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var2=Nconte
            fo.write("Rzt ("+var1+") "+var2+"\n"+"Rxt ("+var1+") "+var2+"\n")
        elif "rxt" in Conte or "RXT" in Conte or "Rxt" in Conte:
            Conte=Conte.strip();
            leng=0
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write(var1+"\n")
        elif "i " in Conte or "I " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (0) "+var1+"\n")  
        elif "x " in Conte or "X " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (0.5*pi) "+var1+"\n"+"Rxt (pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n") 
        elif "z " in Conte or "Z " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (0.5*pi) "+var1+"\n"+"Rzt (pi) "+var1+"\n"+"Rzt (1.5*pi) "+var1+"\n") 
        elif "y " in Conte or "Y " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (1.5*pi) "+var1+"\n"+"Rxt (pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n") 
        elif "h " in Conte or "H " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (0.5*pi) "+var1+"\n"+"Rxt (0.5*pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n") 

    fo.close();
    fi.close();


def Simplfication(InputFileName,OutputFileName):
    fi=open(InputFileName,'r')
    fo=open(OutputFileName,'w')
    Conte=fi.readline()
    leng=6;Ncont="";
    while leng<len(Conte) and Conte[leng]!="#":
        Ncont=Ncont+Conte[leng]
        leng+=1
    for i in range(0,int(Ncont)):
        Conte=fi.readline()
        Nconte=""
        if "cnot" in Conte or "CNOT" in Conte:
            Conte=Conte.strip();
            leng=5
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            leng+=1
            Nconte=""
            while leng<len(Conte) and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var2=Nconte
            fo.write("Rzt (0.5*pi) "+var1+"\n"+"Rxt (0.5*pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n"+"c-z "+var1+","+var2+"\n"+"Rzt (0.5*pi) "+var1+"\n"+"Rxt (0.5*pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n")
        elif "c-z" in Conte or "C-Z" in Conte:
            Conte=Conte.strip();
            leng=4
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            leng+=1
            Nconte=""
            while leng<len(Conte) and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var2=Nconte
            fo.write("c-z "+var1+","+var2+"\n")
        elif "rzt" in Conte or "RZT" in Conte or "Rzt" in Conte:
            Conte=Conte.strip();
            leng=0
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write(var1+"\n")
        elif "ryt" in Conte or "RYT" in Conte or "Ryt" in Conte:
            Conte=Conte.strip();
            leng=5
            Nconte=""
            while Conte[leng]!=")" and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            leng+=1
            Nconte=""
            while leng<len(Conte) and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var2=Nconte
            fo.write("Rzt ("+var1+") "+var2+"\n"+"Rxt ("+var1+") "+var2+"\n")
        elif "rxt" in Conte or "RXT" in Conte or "Rxt" in Conte:
            Conte=Conte.strip();
            leng=0
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write(var1+"\n")
        elif "i " in Conte or "I " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (0) "+var1+"\n")  
        elif "x " in Conte or "X " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (0.5*pi) "+var1+"\n"+"Rxt (pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n") 
        elif "z " in Conte or "Z " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (pi) "+var1+"\n")
        elif "y " in Conte or "Y " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (1.5*pi) "+var1+"\n"+"Rxt (pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n") 
        elif "h " in Conte or "H " in Conte:
            Conte=Conte.strip();
            leng=2
            Nconte=""
            while Conte[leng]!="," and Conte[leng]!="#" and Conte[leng]!="\t":
                Nconte=Nconte+Conte[leng]
                leng+=1
            var1=Nconte
            fo.write("Rzt (0.5*pi) "+var1+"\n"+"Rxt (0.5*pi) "+var1+"\n"+"Rzt (0.5*pi) "+var1+"\n") 

    fo.close();
    fi.close();
        
Replacement("Circuit1.qcirc","Circuit1Compiled.qcirc")             #for Compilation
Simplfication("Circuit1.qcirc","Circuit1CompiledSimplified.qcirc") #for Simplify