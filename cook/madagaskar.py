# encoding: utf8

k=734/1000.
print k*.150
print

ingridients = [
['Грудинка с ребрышками - ',1,'кг'],
['Лук белый - ',150,' г '],#(2 штуки)'
['Морковь - ',150,'г '],#(1 крупная)'
['Чернослив - ',150,' г '],#( 2 жмени )'
['Бульон (вода) - ',1,' стакан'],
['Вино красное сухое - ',1,' стакан'],
['Томатная паста - ',2,' ст.л (маленькая баночка 70 грамм)'],
['Растительное масло для обжарки ',5,' ст.л,'],
['соль крупная ',2,' ч.л. ,'],
['перец черный молотй ',0.5,' чл,'],
['мускатный орех ',1./2,' чл,'],
['лавровый лист ',4,' штушка,'],
['розмарин.',-1,''],
['чеснок ',6,' зубчиков'],
['Мука',-1,'']
]

for i in ingridients: print i[0],i[1]*k,i[2]