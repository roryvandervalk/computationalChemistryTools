#!/bin/python3

from computationalChemistryTools.utility.vec3 import vec3
from math import sqrt

def ReadAnimations(f):
  # Assuming f in open and all is well
  while True:
    l = f.readline()
    if not l:
      break
    n = int(l) # Atom count
    l = f.readline().split() # "q [0, 0, 0] , b 1 , f -0.005 (generated by Phonopy)"
    frequency = float(l[9])
    atoms = []
    for i in range(n):
      atoms.append(f.readline().split())
    # For starters just print out
    #Frequency Atom with largest displacement
    # Atoms displacement length
    maxlen = -1e9
    maxindex = 0
    disp = []
    for i in range(len(atoms)):
      displacement = vec3(atoms[i][4:]).Length()
      if displacement > maxlen:
        maxlen = displacement
        maxindex = i
      disp.append([atoms[i][0], displacement])
    with open("ParsedEnergy.txt", 'a') as o:
      o.write("Frequency: {0: <10.3f} Max Displacement: {1:<2} {2: <10.3f}\n".
      format(frequency, atoms[maxindex][0], maxlen))
      for i in disp:
        o.write("\t{0:<2} {1: <10.3f}\n".format(i[0], i[1]))

def ReadAnime(args):
  if len(args) == 1:
    print("Reads a anime.xyz_jmol file to parse out energy contributions of vibrations.")
    print("Get an anime.xyz_jmol file from phonopy.")
    print("Input: anime.xyz_jmol filename.")
    print("Output: ParsedEnergy.txt.")
    return
  else:
    f = open("ParsedEnergy.txt", 'w')
    f.close()
    with open(args[1], 'r') as f:
      ReadAnimations(f)
    print("Good Day.")

if __name__ == "__main__":
  import sys
  ReadAnime(sys.argv)

