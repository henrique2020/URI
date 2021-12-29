dic = {
    'vertebrado':{
        'ave':{
            'carnivoro':'aguia', 
            'onivoro':'pomba'
            }, 
        'mamifero':{
            'onivoro':'homem', 
            'herbivoro':'vaca'
            }
        }, 
    'invertebrado':{
        'inseto':{
            'hematofago':'pulga', 
            'herbivoro':'lagarta'
            }, 
        'anelideo':{
            'hematofago':'sanguessuga', 
            'onivoro':'minhoca'
            }
        }
    }

info1 = input()
info2 = input()
info3 = input()

print(dic[info1][info2][info3])
