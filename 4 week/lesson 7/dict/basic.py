persone = {'name':'Oleg',
            'age':23,
            'phone':'09798687587',
            'married':False,}
persone.update({'address':'Ukraine','language':'ua'})
# print(persone)
# persone.pop('language')
# print(persone)
oleg = persone.copy()
persone.clear()
oleg['address'] = 'Poltava'
print(oleg)
print(persone)
print(oleg.get('name','anonim'))
print(oleg.get('lang','Python'))