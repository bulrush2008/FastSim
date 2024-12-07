"""
1, "P-": Preconditioning
  read the vtk file (.vtm, .vtr), converting to structured data;
2, "S-": Save/Store
  build the hdf5 file to save matrix data. The data would be directly read by
  both the FNN and GAN model;
3, "P-": Postprocessing
  read the matrix data, and then convert it to VTK format, which can be
  displayed by Paraview

@author       @date         @aff          @version
Xia, S        2024.11.7     Simpop.cn     v1.0
"""

from pathlib import Path
from ReadVTM import ReadVTM
from idxList import idxList
from ReadVTR import ReadVTR

import numpy as np

# register all cases names to a list

# case indexes
commonPath = Path("../FSCases")


# number of cases
numOfCases = len(idxList)

# parameterization inputs: [inlet temperature, inlet velocity, heat flux]
paraInList = [[438.15, 2.511048614, 458333.3333],\
              [458.15, 2.511048614, 458333.3333],\
              [478.15, 2.511048614, 458333.3333],\
              [438.15, 2.064639971, 458333.3333],\
              [458.15, 2.064639971, 458333.3333],\
              [478.15, 2.064639971, 458333.3333],\
              [438.15, 1.618231329, 458333.3333],\
              [458.15, 1.618231329, 458333.3333],\
              [478.15, 1.618231329, 458333.3333],\
              [438.15, 2.511048614, 291666.6667],\
              [458.15, 2.511048614, 291666.6667],\
              [478.15, 2.511048614, 291666.6667],\
              [438.15, 2.064639971, 291666.6667],\
              [458.15, 2.064639971, 291666.6667],\
              [478.15, 2.064639971, 291666.6667],\
              [438.15, 1.618231329, 291666.6667],\
              [458.15, 1.618231329, 291666.6667],\
              [478.15, 1.618231329, 291666.6667],\
              [438.15, 2.511048614, 125000.],\
              [458.15, 2.511048614, 125000.],\
              [478.15, 2.511048614, 125000.],\
              [438.15, 2.064639971, 125000.],\
              [458.15, 2.064639971, 125000.],\
              [478.15, 2.064639971, 125000.],\
              [438.15, 1.618231329, 125000.],\
              [458.15, 1.618231329, 125000.],\
              [478.15, 1.618231329, 125000.]]

# register each case name to a list of strings
caseNames = []  # e.g "Case003" or "Case115"
for i in range(numOfCases):
  s = "%03d"%idxList[i]
  caseNames.append("C"+s)

# assertain each case's path
casePaths = []
for i in range(numOfCases):
  path = commonPath.joinpath(caseNames[i]) 
  casePaths.append(path)
  #print(casePaths[i])

# loop over each case
for i in range(numOfCases):
  VTMFileName = Path("case" + "%d"%idxList[i] + "_point.002000.vtm")
  VTMFilePath = casePaths[i].joinpath(VTMFileName)

  # assertain each vtm file is alive
  #alive = VTMFilePath.exists()
  #print(alive)

  numOfBlock, VTRFilePath = ReadVTM(VTMFilePath, i)

  # For certain case, loop all its vtr files, each of which relates to a block
  for j in range(numOfBlock):
    theVTRFile = casePaths[i].joinpath(VTRFilePath[j].decode("ASCII"))

    fieldP, fieldU, fieldV, fieldW, fieldT, coordsX, coordsY, coordsZ\
      = ReadVTR(theVTRFile)

    if i==0: print(coordsZ)

