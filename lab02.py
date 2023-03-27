# programa para escolha de distribuições Linux

print('Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux.'
      ' Responda a algumas poucas perguntas para ter uma recomendação.')

print('Seu SO anterior era Linux?\n(0) Não\n(1) Sim')
primeira_escolha = int(input())

if primeira_escolha == 1:

    print('É programador/ desenvolvedor ou de áreas semelhantes?\n(0) Não\n(1) Sim\n(2) Sim, realizo testes e '
          'invasão de sistemas')
    segunda_escolha = int(input())

    if segunda_escolha == 2:

        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, '
              'as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.')

    elif segunda_escolha == 1:

        print('Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n(0) Não\n(1) Sim')
        terceira_escolha = int(input())

        if terceira_escolha == 1:

            print('Já utilizou Debian ou Ubuntu?\n(0) Não\n(1) Sim')
            quarta_escolha = int(input())

            if quarta_escolha == 1:

                print('Suas escolhas te levaram a um caminho repleto de desafios, '
                      'para você recomendamos as distribuições: Manjaro, ApricityOS.')

            elif quarta_escolha == 0:

                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, '
                      'as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, '
                      'Ubuntu Mate, Ubuntu.')
            else:
                print('Opção inválida, recomece o questionário.')

        elif terceira_escolha == 0:

            print('Já utilizou Arch Linux?\n(0) Não\n(1) Sim')
            quarta_escolha = int(input())

            if quarta_escolha == 1:

                print('Suas escolhas te levaram a um caminho repleto de desafios,'
                      ' para você recomendamos as distribuições: Gentoo, CentOS, Slackware.')

            elif quarta_escolha == 0:

                print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, '
                      'as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.')

            else:
                print('Opção inválida, recomece o questionário.')
        else:
            print('Opção inválida, recomece o questionário.')

    elif segunda_escolha == 0:

        print('Ao trilhar esse caminho, um novo guru do Linux irá surgir, '
              'as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.')

    else:
          print('Opção inválida, recomece o questionário.')

elif primeira_escolha == 0:

      print('Seu SO anterior era um MacOS?\n(0) Não\n(1) Sim')
      segunda_escolha = int(input())

      if segunda_escolha == 1:

            print('Você passará pelo caminho daqueles que decidiram '
                  'abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.')

      elif segunda_escolha == 0:

            print('Você passará pelo caminho daqueles que decidiram '
                  'abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, '
                  'Kubuntu, Manjaro.')
      else:
            print('Opção inválida, recomece o questionário.')
else:
      print('Opção inválida, recomece o questionário.')