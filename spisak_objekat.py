# Ovo je moj spisak za kupovinu
spisakkupovine = ['jabuka', 'mango', 'sargarepa', 'banana']
print('Ja imam', len(spisakkupovine), 'stvari da kupim.')
print('Te stvari su:', end = ' ')
for stvar in spisakkupovine:
    print(stvar, end = ', ')
print('\nJa takodje treba da kupim i pirinac.')
spisakkupovine.append('pirinac')
print('Moj spisak za kupovinu je sad', spisakkupovine)
print('Sada cu da sortiram moj spisak.')
spisakkupovine.sort()
print('Sortirana lista je', spisakkupovine)
print('Prva stvar koju cu kupiti je', spisakkupovine[0])
starastvar = spisakkupovine[0]
del spisakkupovine[0]
print('Kupio sam', starastvar)
print('Moj spisak za kupovinu je sada', spisakkupovine)
