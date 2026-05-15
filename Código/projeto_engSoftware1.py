from abc import ABC, abstractmethod

# ==========================================
# PADRÃO OBSERVER: Sensor de Proximidade
# ==========================================
class Observador(ABC):
    @abstractmethod
    def atualizar(self, distancia: float):
        pass

class SensorProximidade:
    def __init__(self):
        self._observadores = []
        self._distancia = 0.0

    def adicionar_observador(self, obs: Observador):
        self._observadores.append(obs)

    def set_distancia(self, distancia: float):
        self._distancia = distancia
        print(f"[Hardware: Sensor] Sinal Bluetooth detectado a {distancia} metros.")
        self._notificar()

    def _notificar(self):
        for obs in self._observadores:
            obs.atualizar(self._distancia)

# ==========================================
# PADRÃO STATE: Estados da Ignição/Motor
# ==========================================
class EstadoMotor(ABC):
    @abstractmethod
    def dar_partida(self, modulo):
        pass
    
    @abstractmethod
    def bloquear(self, modulo):
        pass

class Bloqueado(EstadoMotor):
    def dar_partida(self, modulo):
        print("[Motor] Acesso negado. Motor bloqueado. Faça autenticação no App.")
    
    def bloquear(self, modulo):
        # Já está bloqueado, não faz nada
        pass

class Desbloqueado(EstadoMotor):
    def dar_partida(self, modulo):
        print("[Motor] Partida autorizada! O motor está ligado. (Vrum vrum)")
        modulo.set_estado(EmFuncionamento())

    def bloquear(self, modulo):
        print("[Motor] Bloqueando ignição preventivamente.")
        modulo.set_estado(Bloqueado())

class EmFuncionamento(EstadoMotor):
    def dar_partida(self, modulo):
        print("[Motor] O veículo já encontra-se ligado.")
    
    def bloquear(self, modulo):
        print("[Motor] ALERTA: Iniciando corte de combustível e travando veículo!")
        modulo.set_estado(Bloqueado())

# ==========================================
# CONTEXTO: O Módulo Principal do Veículo
# ==========================================
class ModuloVeicular(Observador):
    def __init__(self):
        self._estado = Bloqueado()

    def set_estado(self, estado: EstadoMotor):
        self._estado = estado

    # Implementação da História 1: Autenticação Principal
    def autenticar_app(self, sucesso: bool):
        if sucesso:
            print("[App] Autenticação biométrica válida. Desbloqueando ignição.")
            self.set_estado(Desbloqueado())
        else:
            print("[App] Falha na biometria.")

    def acionar_ignicao(self):
        self._estado.dar_partida(self)

    # Implementação da História 2: Reação ao distanciamento
    def atualizar(self, distancia: float):
        if distancia > 10.0:
            print("\n[Segurança] ALERTA: Autenticador fora de alcance (>10m). Possível roubo em andamento!")
            self._estado.bloquear(self)


# ==========================================
# SIMULAÇÃO (Execução do Protótipo)
# ==========================================
if __name__ == "__main__":
    carro = ModuloVeicular()
    sensor_bluetooth = SensorProximidade()
    sensor_bluetooth.adicionar_observador(carro)

    print("\n--- CENÁRIO A: Tentativa de furto (Sem celular) ---")
    carro.acionar_ignicao()

    print("\n--- CENÁRIO B: Dono no veículo (História 1) ---")
    carro.autenticar_app(sucesso=True)
    carro.acionar_ignicao()

    print("\n--- CENÁRIO C: Roubo no semáforo (História 2) ---")
    # Ladrão levou o carro e o dono ficou para trás com o celular
    sensor_bluetooth.set_distancia(2.0)  # Carro arranca
    sensor_bluetooth.set_distancia(5.5)  # Afastando
    sensor_bluetooth.set_distancia(15.0) # Passou de 10 metros, ativa o bloqueio!