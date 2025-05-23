from abc import ABC, abstractmethod

class Observer(ABC):
    """Interface para Observadores."""
    
    @abstractmethod
    def update(self, mensagem: str):
        pass

class Subject:
    """Classe base para Subjects que gerenciam observadores."""
    
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, mensagem: str):
        for observer in self._observers:
            observer.update(mensagem)
