#!/usr/bin/python

def sortcat(num, *args):
  mylist=[]
  result=""
  for i in args:
    mylist.append(i);
  mylist.sort(key=lambda str: -1*len(str))
  if (num<0):
    num=len(mylist);
  result="".join(mylist[0:num]);
  print result;

sortcat(1,'abc','bc');
sortcat(2,'bc','c','abc');
  
