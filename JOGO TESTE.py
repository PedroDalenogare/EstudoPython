print('-=-' * 20)
print('BEM VINDO AO MEU PRIMEIRO JOGO USANDO O BÁSICO EM PYTHON!!!')
print('-=-' * 20)
start = input('Deseja começar ? ').upper()
if start == 'SIM':
    print('\nJá que você decidiu começar eu vou explicar um pouco sobre a mecânica do jogo, esse é um jogo de sobrevivência')
    print('totalmente focado nas suas escolhas e nas consequências que elas traram, lembre-se que seu objetivo é sobreviver')
    print('e se possível se salvar, para isso você deverá ficar de olho na sua vida e fome, também deverá ter cautela nas')
    print('suas escolhas pois um simples erro pode acabar te levando a morte, bom jogo e divirta-se.')
else:
    print('Que sem graça que você é!!!')
    print('O JOGO COMEÇA MESMO ASSIM')
    print('Eu vou explicar um pouco sobre a mecânica do jogo, esse é um jogo de sobrevivência')
    print('totalmente focado nas suas escolhas e nas consequências que elas traram, lembre-se que seu objetivo é sobreviver')
    print('e se possível se salvar, para isso você deverá ficar de olho na sua vida e fome, também deverá ter cautela nas')
    print('suas escolhas pois um simples erro pode acabar te levando a morte, bom jogo e divirta-se.')
    print('\nVocê é Alan Silva, tem 28 anos e trabalha como contador em um escritório no centro da cidade e no dia 14/03/2032')
    print('você acorda e vê que algo não está certo, olha pela janela do seu quarto e vê diversos zumbis andando pelas ruas,')
    print('como estamos em 2032 todo mundo sabe o que é um zumbi e com você não é diferente, então você rapidamente fecha')
    print('as janelas em casa e toma a decisão de...')

print('-=-' * 20)
print('O JOGO COMEÇA')
print('-=-' * 20)
if start == 'SIM':
    print('\nVocê é Alan Silva, tem 28 anos e trabalha como contador em um escritório no centro da cidade e no dia 14/03/2032')
    print('você acorda e vê que algo não está certo, olha pela janela do seu quarto e vê diversos zumbis andando pelas ruas,')
    print('como estamos em 2032 todo mundo sabe o que é um zumbi e com você não é diferente, então você rapidamente fecha')
    print('as janelas em casa e toma a decisão de...')
print('\n-------------Vida = 10               Fome = 10-------------')
a = ('ficar')
b = ('sair')
c = ('gritar')
print('(a) = Ficar em casa')
print('(b) = Sair de casa')
print('(c) = Gritar em pânico')
escolha1 = input('O que você decide fazer ? ').upper()
if escolha1 == 'A':
    print(f'\nEu vou {a} em casa.')
    print('Você firmemente toma a decisão de ficar em casa e procura o maxímo de coisas que possam ajudar na sua sobrevivência,')
    print('infelizmente sua casa não tinha nada além de uma lanterna, algumas facas e uma garrafa de água, e isso dificulta muito')
    print('a sua sobrevivência no longo prazo. Depois de algumas horas você começa a sentir fome e fica sem opções a não ser sair')
    print('dali para não morrer de fome.')
    print('\n-------------Vida = 10               Fome = 6------------')
    a = ('policia')
    b = ('mercado')
    c = ('olhar as casas na vizinhança')
    print('(a) = Ir até a policia em busca de ajuda')
    print('(b) = Ir até o mercado em busca de alimentos')
    print('(c) = Fazer buscar nas casas da vizinhança')
    escolha2 = input('Para onde você decidiu ir ? ').upper()
    if escolha2 == 'C':
        print(f'\nEu vou {c}.')
        print('Você começa a vasculhar as casas ao redor da sua mas parecem estar todas vazias, entrando na quarta casa')
        print('você sente um cheiro estranho mas continua sua procura, pois já tinha arrumado uma lata para comer e uma')
        print('roupa mais confortável e protegida, entrando no quarto você escuta um barulho vindo do armario e decide')
        print('que não pode ignorar e quando abre a porta...SURPRESA um guaxinim pula pra cima de você e te assusta')
        print('e quando você vira para tras... SUPRESA... um zumbi já está pulando por cima de você')
        print('Você tenta lutar com todas as suas forças mas acaba derrubando a sua faca, e é mordido pelo zumbi e devorado.')
        print('\n-------------Vida = 0               Fome = 10-------------')
        print('-=-' * 20)
        print('                     VOCÊ MORREU!!!!')
        print('-=-' * 20)
        print('Lembre-se que você era corretor e não um ninja, por isso tente evite investigar o que não é útil para você.')
    if escolha2 == 'B':
        print(f'\nEu vou até o {b} em busca de suprimentos.')
        print('Você escolhe ir até o mercado pois a sua fome ja era bem grande e não queria arriscar, no caminho você acaba')
        print('dando de cara com um zumbi e consegue elimina-lo facilmente com sua faca, então você segue até o supermercado.')
        print('Chegando lá você entra pela porta da frente e a fecha, tudo parece vazio então você vai até o estoque e por')
        print('sorte você acha algumas latas.')
        print('Como você já tinha achado o que veio procurar você decide abrir uma das latas para satisfazer sua fome e alguns minutos')
        print('depois você decide ir embora dali, mas quando vai até a porta ESTÁ CHEIO DE ZUMBIS, vários deles em toda a frente do')
        print('supermercado eles percebem a sua presença e vem até a porta, você se apavora mas precisa tomar uma decisão...')
        print('\n-------------Vida = 10               Fome = 10------------')
        a = ('fugir pelos fundos')
        b = ('LUTAR!!')
        print(f'(a) = Eu vou {a}.')
        print(f'(b) = Eu vou {b} com eles.')
        escolha3 = input('Qual é a sua decisão? ').upper()
        if escolha3 == 'A':
            print('Você faz uma sabia escolha e consegue fugir dali enquanto os zumbis estão destraídos com o próprio barulho')
            print('como nenhum lugar ali parece seguro você decide simplesmente tentar se afastar ao máximo até que da de frente')
            print('com outro sobrevivente, ele te oferece ajuda diz que tem que ser rápido e entrar no carro dele ou os dois')
            print('morrerão, você precisa ser rápido na decisão...')

        if escolha3 == 'B':
            print('Você fica bravamente em frente aquela horda e enquanto eles quebram as portas e janelas você pensa se realmente')
            print('fez a escolha certa, contudo você luta com unhas e dentes e chega a matar incriveis 3 zumbis mas infelizmente é')
            print('derrubado pelo quarto zumbi e a horda inteiro caí por cima de você te devorando totalemente')
            print('\n-------------Vida = 0               Fome = 10-------------')
            print('-=-' * 20)
            print('                     VOCÊ MORREU!!!!')
            print('-=-' * 20)
            print('Lembre-se que você era corretor e não um ninja, por isso tente evitar fazer esse tipo de loucura.')

    if escolha2 == 'A':
        print(f'\nEu vou até a {a} em busca de ajuda.')
        print('Você consegue ir rapidamente até a delegacia e sem ser percebido por nenhum zumbi já que a delegacia ficava bem')
        print('no caminho do seu antigo serviço, chegando lá você tenta entrar mas percebe que as portas estão trancadas')
        print('então você decide...')
        print('\n-------------Vida = 10               Fome = 4------------')
        a = ('arrombar')
        b = ('dar a volta')
        c = ('ir embora')
        print(f'(a) = Eu vou {a} a porta.')
        print(f'(b) = Eu vou {b} em busca de outra entrada.')
        print(f'(c) = Eu vou {c} daqui.')
        escolha3 = input('Qual é a sua decisão? ').upper()
        if escolha3 == 'A':
            print(f'\nEu vou {a} a porta.')
            print('Você tenta com toda a sua força, até usa um pedaço de ferro para tentar abrir a porta e não consegue, e como')
            print('as janelas tem grades você percebe que seu esforço foi em vão e além disso você atraiu diversos zumbis que estavam')
            print('na região e com isso você...')

        if escolha3 == 'B':
            print('Você tranquilamente e em silêncio decide procurar outra entrada dando a volta no prédio, por sorte a porta dos')
            print('fundos estava aberta, então você sem hesitar entra na delegacia.')
            print('Lá dentro está bem escuro e silencioso algumas coisas parecem ter sido saqueadas mais ainda há muito que você')
            print('poderia aproveitar incluindo uma pistola 9mm com 15 munições.')
            print('Depois de pegar tudo você a vista alguns zumbis na parte da frente...')

        if escolha3 == 'C':
            print('Sem sucesso para entrar na delegacia você simplemente decide que o melhor a fazer era ir embora e no caminho')
            print('Acaba ouvindo o som de um veículo se aproximando você tenta se esconder mas o veículo já tinha te percebido,')
            print('ele para e oferece ajuda, desde que você entre rápido no carro...')


if escolha1 == 'B':
    print(f'\nEu vou {b} de casa.')
    print('Mesmo com todo o seu medo você ainda decidiu sair de casa e pegou uma garrafa de água e um faca para se defender,')
    print('surpreendentemente você conseguiu andar um quarteirão sem ser percebido por nenhum zumbi, mas andando mais um pouco')
    print('você acabou sendo percebido pelo seu primeiro zumbi...')
    print('\n-------------Vida = 10               Fome = 8-------------')



if escolha1 == 'C':
    print(f'\nEu vou {c} em pânico')
    print('Isso com certeza foi uma péssima decisão, vários zumbis ouviram seus gritos e vieram até a sua porta, eles são muitos e chegaram')
    print('muito rápido, tremendo de medo você pega uma faca que achou em sua cozinha e fica em posição de combate enquanto os zumbis quebram a sua porta')
    print('e entram pra dentro da sua casa.')
    print('Na sua cabeça uma luta épica parecia que ia acontecer, mas não foi bem assim, você acertou a cabeça do primeiro zumbi, mas o segundo')
    print('rapidamente o derrubou e os outros o devoraram pedacinho por pedacinho.')
    print('\n-------------Vida = 0               Fome = 10-------------')
    print('-=-' * 20)
    print('                     VOCÊ MORREU!!!!')
    print('-=-' * 20)
    print('Lembre-se que você era corretor e não um ninja, por isso tente evitar fazer esse tipo de loucura.')








