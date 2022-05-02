#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:46:37 2019

@author: csmk
"""

import numpy as np


def printTypAndValue(ob):
    print("Dieses Objekt ist von Typ :",type(ob),"\n")
    print("Seine Werte sind :\n",ob,"\n")
    
B,C,D,E,a,b,c = np.load('Ueb1.npz').values()
#frage b          
thelist =[B,C,D,E,a,b,c] 
#np.dtype(np.complex128)

A=np.array([[0.,8.,0.,6.,6.],
            [0.,5.,6.,0.,8.],
            [5.,4.,3.,8.,1.],
            [4.,7.,1.,2.,1.],
            [9.,6.,4.,1.,2.]])

print('A type ',type(A))
for x in thelist:
   printTypAndValue(x) 
   
#frage c  A+C, A-C, A+D
print("A+C :",A+C,"\n")
print("A-C :",A-C,"\n")
print("A+D :",A+D,"\n")

#frage d 
#A*C ist das Multiplizieren von zwei Operanden
#A@C ist das Multiplizien von zwei Matrizen
#A/C ist das Teilen vom liken Operand durch rechten Operand
#A@ numpy.linalg.inv(C) ist das Multiplizieren von der Matrix A und die inverse Matrix von C
print("A\n",A,"\nC\n",C,"\n")
print("A*C\n",A*C,"\n")
print("A@C\n",A@C,"\n")
print("A/C\n",A/C,"\n")
print("A @ np.linalg.inv(C)\n",A @ np.linalg.inv(C),"\n")

#frage e
Cmula=C@a
#Cb=C@b nicht möglich, weil die Anzahl von von Spalte von C nicht stimmt mit der Anzahl von Zeile von a
bmulC=b@C
print("C@a :\n",Cmula,"\n")
print("b@C :",bmulC,"\n")

#frage f
BMinD=B-D
Cplsa=C+a
print("B-D :\n",B-D,"\n")
print("C+a :\n",C+a,"\n")

#frage g
A2=A
A[0,0]=42

print("A2 :\n",A2,"\n")

#frage h
#die ersten beiden Spalten
print("die ersten beiden Spalten\n",A[0:,2:])
print("\n",A)

#nur die letzte Zeile
print("nur die letzte Zeile\n",A[4::])
print("\n",A)


#nur jedde 2. Spalte und Zeile
print("nur jedde 2. Spalte und Zeile\n",A[::,::2])
print("\n",A)

#Zeilen in umgekehhrter Reihennfolge
print("Zeilen in umgekeh hrter Reihennfolge\n",A[::,::-1])
print("\n",A,"\n")
    
#frage i
#Erzeuge ein Array, welches 2 mal das Array C enthält
# - Als Tupel (C, C), bes schreiben Si ie was hier passiert.
n1=np.array((C,C))
print("als Tupel ",n1)
print('n1 SHAPE ',n1.shape)
print('C :\n',C,'\nC SHAPE',C.shape)

# - Als ein Array mit dopelter Breite (Tipp: np.append).
n2=np.append(C,C)

# - Als ein Array mit doppelter Höhe.
n3=np.append(C,C*2)
#frage j

##eine "for" Schleife für ein Statement iteriert die Mitglieder einer Sequenz 
##in der Reihenfolge und führt den Block jedes Mal aus

