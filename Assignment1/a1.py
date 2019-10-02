"""
Functions for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: SANAT KARUNAKARAN SK3263
Date:   09/27/2019
"""
import introcs
def before_space(s):
    """Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space"""
    try:
        result=s[:s.find(' ',s.index(' ')-1)]
        return result
    except ValueError as e:
        print('This is an error')

def after_space(s):
    """Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space"""
    try:
        result=s[s.index(' ')+1:]
        return result
    except ValueError as e:
        print('This is an error')

def first_inside_quotes(s):
    """Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes"""
    try:
        result=s[s.index('"')+1:s.find('"',s.index('"')+1)]
        return result
    except ValueError as e:
        print ('This is a ', type(e))

def get_lhs(json):
    """Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    lhs=json[json.index('lhs')+6:json.find('"',json.index('lhs')+6)]
    return lhs

def get_rhs(json):
    """Returns the rhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "rhs". For example, if the JSON is

    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'

    then this function returns '9916.0137 Euros' (not
    '"9916.0137 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    rhs=json[json.index('rhs')+6:json.find('"',json.index('rhs')+6)]
    return rhs

def has_error(json):
    """Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "ok". For example,
    if the JSON is

    '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    a=json[json.index('ok')+4:json.find(',',json.index('ok')+4)]
    if a=="false":
        return True
    else:
        return False

def currency_response(src="USD", dst="EUR", amt=2.5):
    """Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the
    currency dst. The response should be a string of the form

    '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "ok" will be followed by the value false (and "err" will have
    an error message).

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float"""
    json=introcs.urlread('http://cs1110.cs.cornell.edu/2019fa/a1?src='+str(src)+'&dst='+str(dst)+'&amt='+str(amt))
    return json

def is_currency(code):
    """Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces."""
    json=currency_response(code)
    bool=has_error(json)
    return bool

def exchange(src, dst, amt):
    """Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency
    src to the currency dst. The value returned represents the
    amount in currency dst.

    The value returned has type float.

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float"""
    json=currency_response(src,dst,amt)
    rhs=get_rhs(json)
    lhs=get_lhs(json)
    return lhs,rhs

def amt_has_error(src,dst,amt):
    """Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "ok". For example,
    if the JSON is

    '{ "ok":false, "lhs":"", "rhs":"", "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    temp=introcs.urlread('http://cs1110.cs.cornell.edu/2019fa/a1?src='+str(src)+'&dst='+str(dst)+'&amt='+str(amt))
    a=temp[temp.index('err')+6:temp.find('"',temp.index('err')+6)]
    if a=="Currency amount is invalid.":
        return True
    else:
        return False
