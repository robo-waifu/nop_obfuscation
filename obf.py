#!/usr/bin/python3
import sys

def main():
	path = sys.argv[1]
	with open(path,"r") as f:
	    data = f.read()
	    ref  = ""
	    for i in data:
	            if i is ';':
	                i += "OBF;"
	            ref += i
	    with open(path,"w") as fo:
	    	fo.write(ref)



if __name__ == '__main__':
	main()