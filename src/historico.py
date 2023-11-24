from pathlib import Path

class Historico:
    def ler_historico(self):
        if not Path('verificados.txt').exists():
            return ''
        with open('verificados.txt', 'r') as f:
            return f.read()

    def salvar(self, links):
        ids = [link[int(link.rindex('/'))+1:] for link in links]
        srt_final = '\n'.join(ids) + '\n'
        if Path('verificados.txt').exists():
            metodo = 'a'
        else:
            metodo = 'w'
        with open('verificados.txt', metodo) as f:
            f.write(srt_final)
