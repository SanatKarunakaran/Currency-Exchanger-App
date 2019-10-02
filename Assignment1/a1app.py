"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: SANAT KARUNAKARAN SK3263
Date:   09/27/2019
"""
import introcs
import a1

src=input('Enter source currency: ')
dst=input('Enter target currency: ')
amt=input('Enter original amount: ')

"""src_bool=a1.is_currency(src)
print('Source currency has Error: '+str(src_bool))
dst_bool=a1.is_currency(dst)
print('Destination Currency has Error: '+str(dst_bool))
if src_bool==True:
    print('Please Re-Enter.')
elif dst_bool==True:
    print('Please Re-Enter.')
else:
    a,b=a1.exchange(src,dst,amt)
    print ('You can exchange '+a+' for '+b)"""

while a1.is_currency(src)==True:
    print('Source currency has Error: '+str(a1.is_currency(src)))
    print ('Please Re-Enter')
    src=input('Enter source currency: ')
while a1.is_currency(dst)==True:
    print('Destination Currency has Error: '+str(a1.is_currency(dst)))
    print ('Please Re-Enter')
    dst=input('Enter target currency: ')

while a1.amt_has_error(src,dst,amt)==True:
    print ('Currency amount is not a numerical value. Please Re-Enter.')
    amt=input('Enter original amount: ')
    a1.amt_has_error(src,dst,amt)
    while a1.amt_has_error(src,dst,amt)==False:
        if float(amt)<0:
            print('Currency amount invalid. Please Re-Enter: ')
            amt=input('Enter original amount: ')
        else:
            break

print('Source currency has Error: '+str(a1.is_currency(src)))
print('Destination Currency has Error: '+str(a1.is_currency(dst)))
a,b=a1.exchange(src,dst,amt)
print ('You can exchange '+a+' for '+b)
