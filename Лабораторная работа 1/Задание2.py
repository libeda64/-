# TODO Найдите количество книг, которое можно разместить на дискете

page = 100
string = 50
simbol = 25
disc = 1.44

all_simbols = simbol*string*page
bites_book = 4*all_simbols//1024

bites_disc = disc*1024

amount = round(bites_disc/bites_book)

print("Количество книг, помещающихся на дискету:", amount)
