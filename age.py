driving = input('Driving experience? ')
if driving != 'yes' and driving != 'no':
	print('Only type yes or no')
	raise SystemExit

age = input('What is your age?')
age = int(age)
if driving == 'yes':
	if age >= 18: 
		print('Pass!')
	else:
		print('So why did you drive?')
elif driving == 'no':
	if age >= 18: 
		print('Time for a driving class!')
	else:
		print('You can start driving after a few years:)')
else:
	print('Hey error, please type in lower case.') 