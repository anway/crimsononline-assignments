#!/usr/bin/python
import sys
def swapchar(str):
  charslist=[str[0]]
  numslist=[0]
  found=0
  for c in str:
    for i in range(len(charslist)):
      if (charslist[i]==c):
        numslist[i]=numslist[i]+1;
        found=1;
    if (found==0):
      charslist.append(c);
      numslist.append(1);
    found=0;
  maxindex=0
  minindex=0
  for i in range(len(numslist)):
    if (numslist[i]>numslist[maxindex]):
      maxindex=i;
    if (numslist[i]<numslist[minindex]):
      minindex=i;
  maxchar=charslist[maxindex]
  minchar=charslist[minindex]
  for c in str:
    if (c==maxchar):
      sys.stdout.write(minchar);
    elif (c==minchar):
      sys.stdout.write(maxchar);
    else:
      sys.stdout.write(c);
  sys.stdout.write('\n');
swapchar("There were a lot of escopeoples in the elevator on Tuesday.");
    
      
