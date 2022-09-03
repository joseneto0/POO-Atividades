from abc import ABC, abstractmethod
class CartaoMensagem(ABC):
    def __init__(self, destinatario):
        self.__destinatario = destinatario

    @property
    def destinatario(self):
        return self.__destinatario

    @abstractmethod
    def retornarMensagem(self, remetente):
        pass

class MensagemDiaDosNamorados(CartaoMensagem):

    def __init__(self, destinatario) -> None:
        super().__init__(destinatario)

    def retornarMensagem(self, remetente):
        return f"De: {remetente}, para: {self.destinatario} - Feliz dia dos namorados!"

class MensagemNatal(CartaoMensagem):

    def __init__(self, destinatario) -> None:
        super().__init__(destinatario)

    def retornarMensagem(self, remetente):
        return f"De: {remetente}, para: {self.destinatario} - Feliz natal!"


class MensagemAniversario(CartaoMensagem):

    def __init__(self, destinatario) -> None:
        super().__init__(destinatario)

    def retornarMensagem(self, remetente):
        return f"De: {remetente}, para: {self.destinatario} - Feliz aniversário!"