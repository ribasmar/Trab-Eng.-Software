import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from .cardapio_utils import (
    gerar_data_aleatoria,
    garantir_cardapio_json,
    mostrar_cardapio
)
from .notifi_utils import obter_notificacoes_formatadas
from .ui_utils import criar_layout_principal
from .observer_utils import Subject
from .notificacao_observer import NotificacaoObserver

class RUAppUTFPRAp(toga.App, Subject):
    """Aplicativo de cardápio do RU da UTFPR com notificações via Observer."""

    def __init__(self):
        toga.App.__init__(
            self,
            formal_name="Cardápio RU UTFPR",
            app_id="br.edu.utfpr.rucardapio",
            app_name="RU UTFPR"
        )
        Subject.__init__(self)

    def startup(self):
        """Configura a interface inicial do aplicativo."""
        garantir_cardapio_json()
        self.data_hoje = gerar_data_aleatoria()
        
        # Adiciona observer
        self.attach(NotificacaoObserver())
        
        # Cria layout principal
        main_box = criar_layout_principal(self)
        
        self.main_window = toga.MainWindow(
            title=self.formal_name,
            size=(400, 600)
        )
        self.main_window.content = main_box
        self.main_window.show()

    def set_data_hoje(self, nova_data):
        """Atualiza a data atual, a UI e notifica observers."""
        self.data_hoje = nova_data
        self.date_label.text = f"📅 {nova_data.strftime('%d/%m/%Y')}"
        
        resultado = mostrar_cardapio(nova_data)
        self.data_display.value = resultado["mensagem"]
        
        self.notify(f"Usuário mudou para o dia {nova_data.strftime('%d/%m/%Y')}.")

    def _mostrar_notificacoes(self, widget):
        """Exibe as notificações recentes."""
        resultado = obter_notificacoes_formatadas(self.data_hoje)
        self.data_display.value = resultado["mensagem"]
    
    def _mostrar_cardapio(self, widget):
        """Exibe o cardápio da data atual."""
        resultado = mostrar_cardapio(self.data_hoje)
        self.data_display.value = resultado["mensagem"]
        self.notify(f"Usuário visualizou o cardápio de {self.data_hoje.strftime('%d/%m/%Y')}.")


def main():
    return RUAppUTFPRAp()
