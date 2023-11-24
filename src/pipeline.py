from src.alerta import Alert
from src.portal_cedae import Cedae
from src.historico import Historico
from src.textos import VerificarTexto

class Pipeline:
    cedae = Cedae()
    txt = VerificarTexto()
    hist = Historico()
    alert = Alert('') # phone number with country (including +) and region codes and no spaces

    def coletar_links(self):
        return self.cedae.coletar_links()

    def comparar_com_historico(self, lista):
        retorno = lista.copy()
        conteudo = self.hist.ler_historico()
        for link in lista:
            id = link[int(link.rindex('/'))+1:]
            if id in conteudo:
                retorno.remove(link)
        return retorno

    def coletar_texto(self, link):
        return self.cedae.coletar_texto(link)

    def verificar_texto(self, texto):
        return self.txt.verificar(texto=texto)

    def atualizar_historico(self, lista):
        self.hist.salvar(lista)

    def enviar_alerta(self, lista):
        if lista:
            self.alert.enviar_alerta(lista=lista)

    def run(self):
        informar = []
        links = self.coletar_links()
        links = self.comparar_com_historico(links)
        if links:
            for link in links:
                texto = self.coletar_texto(link=link)
                if self.verificar_texto(texto=texto):
                    informar.append(link)
            self.atualizar_historico(links)
            self.enviar_alerta(informar)
