a = "Piyush Sharma "
print(a)
print(type(a))

##replicate a string
print(5*a)

##string length
print(len(a))

#string slicing
print(a[-2])
print(a[0:])

print(a.lower())
print(a.upper())

#string stripping
print(' piyush   '.strip())

#string replacing
print(a.replace('h','-'))

#count
print(a.count('s'))

print(len(a))

#string find

print(a.find('P'))

#string check 
print('istrue'.isalpha())
print('123'.isalpha())
print('piyush'.islower())
print('sharma'.islower())

#string capitalization
print('piyush'.capitalize())
print('piyush sharma'.title())

#check for start and end
print('piyush sharma'.startswith('piy'))
print('piyush sharma'.endswith('sh'))

print('piyush sharma'.center(20,'*'))
print('piyush sharma'.ljust(20,'*'))
print('piyush sharma'.rjust(20,'*'))