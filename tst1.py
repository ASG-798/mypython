hours = int(input('Enter Hours: '))
rate = int(input('Enter Rate: '))

if hours > 40:
  extra_time = float(hours) - 40
else:
  extra_time = 0

extra_pay = 0.5 * float(rate) * extra_time

pay = float(hours) * float(rate) + extra_pay

print ('Pay: '),
print( pay)



error_msg_numeric = "Error, please enter numeric input"

hours = int(input('Enter Hours: '))
try:
  float(hours)>=0
except:
  print (error_msg_numeric)
  # ideally you would want this whole "check for valid input" in a while loop. This is a beginner's course, so here is a get-out-of-jail-free implementation.
  hours = int(input('Enter Hours: '))

rate = int(input('Enter Rate: '))
try:
  float(rate) >=0
except:
  print (error_msg_numeric)
  rate = raw_input('Enter Rate: ')

hours = float(hours)
rate = float(rate)

if hours > 40:
  extra_time = hours - 40
else:
  extra_time = 0

extra_pay = 0.5 * rate * extra_time

pay = hours * rate + extra_pay

print ('Pay: '),
print (pay)



error_msg_invalid = "ERROR: Invalid input."
input_score = raw_input('Enter a score between 0.0 and 1.0: ')
try:
  if (float(input_score) >= 0) and ( float(input_score) <= 1 ):
    print('valid input, thanks!')
  else:
    print (error_msg_invalid)
    input_score = raw_input('Enter a score between 0.0 and 1.0: ')
except:
  print (error_msg_invalid)
  input_score = raw_input('Enter a score between 0.0 and 1.0: ')

input_score = float(input_score)

if input_score < 0.6:
  print ('F')
  #break
elif input_score >= 0.9:
  print ('A')
  #break
elif input_score >= 0.8:
  print ('B')
  #break
elif input_score >= 0.7:
  print('C')
  #break
elif input_score >= 0.6:
  print('D')
  #break
else:
  print ('hmmmm.')
