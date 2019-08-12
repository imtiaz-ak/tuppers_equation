#Take an input of K
#Plot the graph of the tuppers equation

from math import floor as floor


#1/2 < floor(mod(floor(y/17)*2^(-17*floor(x)-mod(floor(y), 17)),2))

def equation(y): #the equation returns a list of values of x for each value of y
	
	list_of_x = []
	for x in range(107): #value of x is limited to 106 as the grid size is 17*106

		exponent = ( (-17*floor(x)) - (floor(y)%17) )
		number = floor(y/17) * (2**exponent)
		if 1/2 < floor(number%2):			
			list_of_x.append(x)
		return list_of_x


#This is the value of k for whice the equation itself is graphed in the graph
k = int("960 939 379 918 958 884 971 672 962 127 852 754 715 004 339 660 129 306 651 505 519 271 702 802 395 266 424 689 642 842 174 350 718 121 267 153 782 770 623 355 993 237 280 874 144 307 891 325 963 941 337 723 487 857 735 749 823 926 629 715 517 173 716 995 165 232 890 538 221 612 403 238 855 866 184 013 235 585 136 048 828 693 337 902 491 454 229 288 667 081 096 184 496 091 705 183 454 067 827 731 551 705 405 381 627 380 967 602 565 625 016 981 482 083 418 783 163 849 115 590 225 610 003 652 351 370 343 874 461 848 378 737 238 198 224 849 863 465 033 159 410 054 974 700 593 138 339 226 497 249 461 751 545 728 366 702 369 745 461 014 655 997 933 798 537 483 143 786 841 806 593 422 227 898 388 722 980 000 748 404 719".replace(" ",""))






#for each value of y from k to k+17, find the list of the values of x

co_ordinates = []
for y in range(k,k+18):
	list_of_x = equation(y)
	co_ordinates.append([y,list_of_x])

print(co_ordinates)





#ISSUES:
#1)Floor returns a float?? and the float is too large. Or maybe the modulus returns a float but that doesnt make any sense.