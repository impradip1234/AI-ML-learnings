astr='Pradip';
try:
    print('hello mittar')
    istr=int(astr)
    print('first',istr)             # this line will not work as the previous 
    print('kyu hill dala na.');     # line has error,it will be directed to except 
                                    # and will not comeback for these lines.
except:
    print('gad bad ho gya mittar');