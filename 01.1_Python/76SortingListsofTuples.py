#using sorted >>>>>>>>>
#sorting will take place by
#comparison of the keys only without looking at the values
d={'a':10, 'b':1, 'c':22}
d.items()

sorted=sorted(d.items())
for k,v in sorted:
    print(k,v)