class VerificarTexto:
    _itens = [
        'guandu',
        'colúmbia',
        'pavuna',
        'pedreira',
        'chapadão',
        'almirante',
        'tamandaré',
        'são jose',
        'myron clark',
        'morro união',
        'morro da união',
        'jagunço',
        'nova conquista',
        'barbante',
        'nova olinda',
        'batistinha',
        'vila amaral',
        'sossego-alegria',
        'sossego alegria',
        'beira rio',
        'beira do rio',
        'embaú',
    ]

    def verificar(self, texto):
        for item in self._itens:
            if item in texto.lower():
                return True
        return False
