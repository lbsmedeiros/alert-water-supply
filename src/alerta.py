from twilio.rest import Client

from src.keys import keys


class Alert:
    client = Client(keys.account_sid, keys.auth_token)

    def __init__(self, numero):
        self.numero = numero

    def enviar_alerta(self, lista):
        message = self.client.messages.create(
            body='\n'.join(lista),
            from_=keys.twilio_phone,
            to=self.numero
        )
