//Atharva Nagarkar M 42
def fact(x):						#define function
	f=1						#intialize f
	if x<0:						#negative number enter
		print("Enter a positive number")
	elif x==0:					#number=0
		print("Factorial : 1")
	elif x==1:	`				#number=1
		print("Factorial : 1")
	else:						#some positive number
		while x>1:				#while loop
			f=f*x				#update f
			x=x-1				#decrease counter
	return f					#return factorial
x=int(input("Enter a number : "))			#input from user 
print(fact(x))						#print factorial
