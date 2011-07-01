import os
def crop(fname):
 ofname=fname+"_crop"
 get_info = "convert %s -virtual-pixel edge -colorspace gray -blur 0x15 -fuzz 10%% -trim info: > out" % (fname+".png")
 os.system(get_info)
 a=open("out").read().split()
 new_bound = map(float,a[2].split("x"))
 new_bound += map(float,a[3].split("+")[-2:])

 exp_bound = new_bound[:]
 exp_bound[0] *= 1.3
 exp_bound[1] *= 1.3
 exp_bound[2] *= 0.8
 exp_bound[3] *= 0.75
 new_bound = map(int,exp_bound)

 crop="convert %s -crop %dx%d+%d+%d +repage %s" % (fname+".png",new_bound[0],new_bound[1],new_bound[2],new_bound[3],ofname+".png")
 os.system(crop)

if(__name__=="__main__"):
 import sys
 crop(sys.argv[1])
