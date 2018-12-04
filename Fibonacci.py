//Atharva Nagarkar M 42
def fib(x):							#define funvtion
	l=[0,1]							#innitialize variables ani list
	a=0
	b=1
	if x<0:							#negative number entered
		print("Enter a positive number ")
	elif x==0:						#if number is x=0
		print([0])
	elif x==1:						#if number is x=1
		print([0,1])
	else:							#for some positive number
		for i in range (x-2):				#for number til x-2
			f=a+b					#add 2 numbers
			l.append(f)				#append sum to list
			a=b					#assign new values to variables
			b=f
	return l						#return list
x=int(input("Enter number of terms : "))			#input from user
print(fib(x))							#print output
