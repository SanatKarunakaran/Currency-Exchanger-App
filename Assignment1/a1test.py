"""
Unit test for module a1

When run as a script, this module invokes several procedures that test
the various functions in the module a1.

Author: SANAT KARUNAKARAN SK3263
Date:   09/27/2019
"""
import introcs
import a1

def testA(s):
     """Test procedure for Part A

     sa1='4.502 Euros'
     sa2='icniwunci'
     sa3='' """
     a1.before_space(s)
     a1.after_space(s)

def testB(s):
     """Test procedure for Part B

     sb1='{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }'
     sb2='{ "ok":true, "lhs":"2.5UnitedStatesDollars", "rhs":"64.375CubanPesos", "err":"" }'
     sb3='{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }'
     sb4='{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }' """
     a1.get_lhs(s)
     a1.get_rhs(s)
     a1.has_error(s)

def testC(sc1,sc2,sc3):
     """Test procedure for Part C

     sc1= src=USD, dst=CUP, amt=2.5
     sc2= src=USA, dst=BBB, amt=steve
     sc3= src='', dst='', amt='' """
     a=a1.currency_response(sc1,sc2,sc3)
     print(a)

def testD(sd0,sd1,sd2,sd3):
     """Test procedure for Part D

     sd0:
     'USD'
     'USA'
     'USD'
     ''
     sd1:
     src='USD', dst='CUP', amt=2.5
     src='USA', dst='BBB', amt='steve'
     src='USD', dst='CUP', amt=2.5
     src='', dst='', amt='' """
     a1.is_currency(sd0)
     a1.exchange(sd1,sd2,sd3)

sa1='4.502 Euros'
sa2='icniwunci'
sa3=''
sb1='{ "ok":true, "lhs":"2.5 United States Dollars", "rhs":"64.375 Cuban Pesos", "err":"" }'
sb2='{ "ok":true, "lhs":"2.5UnitedStatesDollars", "rhs":"64.375CubanPesos", "err":"" }'
sb3='{ "ok":false, "lhs":"", "rhs":"", "err":"Source currency code is invalid." }'
sb4='{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'
testA(sa1)
testA(sa2)
testA(sa3)
testB(sb1)
testB(sb2)
testB(sb3)
testB(sb4)
testC('USD','CUP',2.5)
testC('USA','BBB','steve')
testC('','','')
testD('USD','USD','CUP',2.5)
testD('USA','USA','BBB','steve')
testD('USD','USD','CUP',2.5)
testD('','USD','CUP',2.5)
print("Module a1 passed all tests")
