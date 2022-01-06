
import time
def quick_sort(sequence):
	if len(sequence)<=1:
		return sequence
	else:
		pivot=sequence.pop()
	item_great=[]
	item_low=[]
	for item in sequence:
		if item<pivot:
			item_low.append(item)
		else:	
			item_great.append(item)	
	#print(item_great)
	return (quick_sort(item_low)+[pivot]+quick_sort(item_great))



#if __name__=="__main__":

print(quick_sort([3,9,1,5,4,8,98,4,7,43,30,12,70]))		

