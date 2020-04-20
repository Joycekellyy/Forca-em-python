from random import choice
Frutas = ['abacaxi', 'mamao', 'laranja', 'acai', 'morango', 'limao', 'tomate','banana','amora', 'abacate', 'cacau', 'caqui', 'carambola', 'cereja', 'coco', 'framboesa', 'goiaba', 'jabuticaba', 'kiwi', 'jaca', 'maca', 'manga', 'maracuja', 'melancia', 'melao', 'pera', 'pessego', 'tangerina', 'uva']

BolsaDeMulher = ['batom', 'espelho', 'cartao-de-credito', 'dinheiro', 'esmalte', 'lixa', 'remedio', 'hidratante', 'batom-de-coco', 'lixo-plastico', 'acetona', 'bala', 'sabao-liquido']

Acampamento = ['barraca', 'colchao-inflavel', 'escova-de-dente', 'pasta-de-dente', 'escova-de-cabelo', 'cobertor', 'fogueira', 'insqueiro', 'comida', 'panela', 'fogo',]

Cores = ['amarelo', 'azul', 'ciano', 'marrom', 'vermelho', 'preto', 'verde', 'castanho', 'laranja', 'roxo', 'dourado', 'caramelo', 'branco', 'rosa', 'cinza', 'fluorecente']

def linha_adaptável(txt):
    oi = len(txt)
    print('┏' + '━' * oi + '┓')
    print(f'  {txt}')
    print('\033[m┗' + '━' * oi + '┛')
def mostra_linha():
    print('\033[1;33m' + '-=-' * 10 + '\033[0;0m')

lista =[Frutas, BolsaDeMulher, Acampamento, Cores]
sorteado1 = choice(lista)
if 'abacaxi' in sorteado1:
    print(' ')
    linha_adaptável('O TEMA É \033[31mFRUTAS')
if 'batom' in sorteado1:
    print(' ')
    linha_adaptável('O TEMA É \033[31mBOLSA DE MULHER')
if 'barraca' in sorteado1:
    print(' ')
    linha_adaptável('O TEMA É \033[31mACAMPAMENTO')
if 'azul' in sorteado1:
    print(' ')
    linha_adaptável('O TEMA É \033[31mCORES')
sorteado = choice(sorteado1)
quantidade = len(sorteado)
chances = len(sorteado)
stop = len(sorteado)
letrasQueJáForam = []
apariçao = []
cont = 0
for c in range(0, quantidade):
    tem = '__ '
    apariçao.append(tem)
print(f'\033[mA sua palavra contém {quantidade} letras.')
print(' ')
try:
    while chances != 0:
        while True:
            palpite = str(input('Digite seu palpite: ')).strip()
            if palpite.isalpha():
                break
            print('\033[1;31mErro: Digite apenas LETRAS.\033[m')
        cont += 1
        print(' ')
        if palpite in letrasQueJáForam:
            while True:
                print(f'A letra "\033[1;31m{palpite}\033[m" já foi digitada.')
                print(' ')
                if palpite in letrasQueJáForam:
                    break
        else:
            letrasQueJáForam.append(palpite.upper())
        if palpite in sorteado:
            print(f'A letra "\033[31m{palpite.upper()}\033[m" \033[32mEXISTE\033[m na \npalavra sorteada.')
            print(f'Chances = \033[32m{chances}\033[m')
            print(f'Tentativas = \033[32m{cont}\033[m')
            print('Letras que já foram = \033[32m', end='')
            for c, item in enumerate(letrasQueJáForam):
                print(f'{item}', end=' ')
            print('\033[m\n')
            for c, item in enumerate(sorteado):
                if palpite in item:
                    apariçao.pop(c)
                    apariçao.insert(c, palpite.upper())
                    quantidade -= 1
            for v in apariçao:
                if v.isalpha():
                    print(f'\033[1;32m{v}\033[m', end=' ')
                else:
                    print(f'\033[1;31m{v}\033[m', end=' ')
            print('\n')
            if quantidade == 0:
                print(f'Você completou a palavra toda!!!')
                break
            mostra_linha()
        else:
            print(f'A letra "\033[31m{palpite.upper()}\033[m" \033[31mNÃO EXISTE\033[m na \npalavra sorteada.')
            chances -= 1
            print(f'Chances = \033[32m{chances}\033[m')
            print(f'Tentativas = \033[32m{cont}\033[m')
            print('Letras que já foram = \033[32m', end='')
            for c, item in enumerate(letrasQueJáForam):
                print(f'{item}', end=' ')
            print('\033[m\n')
            for v in apariçao:
                if v.isalpha():
                    print(f'\033[1;32m{v}\033[m', end=' ')
                else:
                    print(f'\033[1;31m{v}\033[m', end=' ')
            print('\n')
            mostra_linha()
        while True:
            escolha = str(input('\033[34mJÁ SABE A RESPOSTA? \033[31m[S/N] \033[m')).strip().upper()[0]
            if 'S' in escolha or 'N' in escolha:
                break
            print('\033[1;31mErro: Digite apenas S ou N.\033[m')
        if escolha == 'S':
            tentativa = str(input('Sua tentativa: ')).lower().strip()
            if tentativa == sorteado:
                print(f'\033[1;32mVOCÊ ACERTOU!!!\033[m')
                break
            else:
                print('\033[1;31mVOCÊ ERROU!!!\033[m')
                break
except:
    print('Você informou algum item errado acima')
print(f'A palavra sorteada foi \033[1;31m{sorteado.upper()}.\033[m')
mostra_linha()