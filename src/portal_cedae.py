from lxml.html import fromstring
import requests


class Cedae:
    _url_root = "https://cedae.com.br"
    _url_principal = _url_root + '/Noticias'
    _xpath_noticias = '/html/body/form/article/div/div/div[2]/div/div[1]/div/div/div[1]//div/div/h3/a'
    _xpath_titulo = '/html/body/form/article/div/div/div[2]/div/div[1]/div/div/div[1]/h4/span'
    _xpath_corpo_noticia = '/html/body/form/article/div/div/div[2]/div/div[1]/div/div/div[2]/span/child::*'

    def coletar_links(self):
        lista = []
        result = requests.get(self._url_principal)
        soup = fromstring(result.text)

        elements = soup.xpath(self._xpath_noticias)

        for element in elements:
            lista.append(element.get('href'))

        return [self._url_root + i for i in lista]

    def coletar_texto(self, link):
        result = requests.get(link)
        soup = fromstring(result.text)

        elements_titulo = soup.xpath(self._xpath_titulo)
        elements_corpo_noticia = soup.xpath(self._xpath_corpo_noticia)

        texto_final = ''
        for item in elements_titulo:
            if isinstance(item.text, str):
                texto_final += item.text
        
        texto_final += '\n'

        for item in elements_corpo_noticia:
            if isinstance(item.text, str):
                texto_final += item.text

        return texto_final
