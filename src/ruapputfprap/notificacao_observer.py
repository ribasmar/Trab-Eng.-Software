from .observer_utils import Observer
from .notifi_utils import adicionar_notificacao

class NotificacaoObserver(Observer):
    """Observer que adiciona notificações ao sistema."""

    def update(self, mensagem: str):
        adicionar_notificacao(mensagem)
