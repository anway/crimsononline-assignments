import random
def lookaway(num):
  random.seed;
  numwins=0
  #designate luigi as 1
  for i in range(1,num):
    mario=random.randint(1,5);
    peach=random.randint(1,5);
    wario=random.randint(1,5);
    if ((mario==1)or(peach==1)or(wario==1)):
      numwins=numwins+1;
  return float(numwins)/num;

print lookaway(100);
print lookaway(500);
