//Atharva Nagarkar M 42
def Arm(num):							#define function	
	sum = 0							#initialize variables
	temp = num					
	while temp > 0:						#while loop		
   		digit = temp % 10				#remainder of number with 10
   		sum += digit ** 3				#update sum by cube of number	
   		temp //= 10					#update number by quotient with 10
	if num == sum:						#compare old and new numbers
	        print(num,"is an Armstrong number")
	else:	
   		print(num,"is not an Armstrong number")
num = int(input("Enter a number: "))				#input from user
