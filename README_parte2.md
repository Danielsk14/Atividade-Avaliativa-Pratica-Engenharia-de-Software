**1. Padrão Arquitetural e Justificativa**

**O padrão arquitetural escolhido é a Arquitetura Cliente-Servidor.**

**Justificativa:** Este padrão é simples e ideal para separar as responsabilidades de interface (interação com o usuário) e processamento centralizado. No nosso contexto de domínio, ele se adapta perfeitamente às histórias de usuário ao dividir o sistema em nós claros: o aplicativo no smartphone atua como o Cliente principal, enquanto o sistema central em nuvem atua como o Servidor. O diferencial prático aqui é que o hardware no carro funciona como um "Cliente Embarcado" (IoT) que também pode receber comandos diretos do aplicativo (via Bluetooth) quando o Servidor estiver inacessível, atendendo diretamente ao requisito de Autenticação Offline.


**2. Representação dos Componentes e Relacionamentos:**

[Aplicativo Mobile] <=======(Bluetooth local)=======> [Módulo Veicular]
    (Cliente)                                        (Cliente Embarcado)
        |                                                     |
        |                                                     |
    (Internet 4G/Wi-Fi)                               (Rede Celular/IoT)
        |                                                     |
        +------------------> [Servidor Web] <-----------------+
                            (API & Banco de Dados)


**3. Principais Componentes e Responsabilidades**
**Aplicativo Mobile (Frontend/Cliente):** Responsável por prover a interface com o motorista. Suas atribuições incluem solicitar a biometria, ativar o Modo Manobrista e estabelecer comunicação local segura (Bluetooth) com o veículo para envio de chaves (tokens) de destravamento.

**Módulo Veicular (Hardware Embarcado):** O cérebro físico dentro do carro. Responsável por atuar nos relés de ignição e injeção eletrônica, validar tokens de segurança locais recebidos do aplicativo e acionar sensores (como corte progressivo e buzina).

**Servidor Web (Backend e Banco de Dados):** Centralizador das regras de negócio globais. Responsável por autenticar o cadastro inicial do usuário, sincronizar o histórico de partidas quando houver internet e gerenciar o envio de notificações push em caso de tentativas de furto.

**4. Limitação ou Trade-off da Arquitetura**

**A Limitação (Sincronização):** Como o veiculo pode ser destravado offline (via Bluetooth), o Servidor em Nuvem não saberá imediatamente que o carro foi acessado. Isso cria um estado de "inconsistência temporária" até que o App ou o Carro recuperem o sinal de internet para avisar a nuvem sobre o que aconteceu.

**O Custo (Trade-off):** A equipe precisará investir muito mais tempo e esforço em segurança do que em um app comum. Será necessário implementar criptografia assimétrica complexa no Bluetooth para evitar Replay Attacks (quando um hacker clona o sinal do Bluetooth do dono para abrir o carro depois). A facilidade do modo offline cobra um preço alto na engenharia de segurança de software embarcado.

**Minha Reflexão:** Escolhendo o padrão Cliente-Servidor busca tornar o desenvimento e manutenção do sofware mais simples, além de se encaixar bem com a proposta e toda a ER realizada enteriormente.
 A principio, a ideia é ter 3 componentes e responsabilidades principais, o Aplicativo mobile, um servidor com banco de dados para os clientes, e um modulo ou algo do tipo, que será instalado dentro do veiculo para se cominicar a chave (aparelho que ira destravar o veiculo).
 Apesar de optar por escolhar de desenvolvimento relativamente simples em relação as variadades existentes, já é possivel visualizar algum possiveis problemas, como: a falta de sincronização quando o veiculo for destravado offline (via bluetooh) ele não vai conseguir sincronizar com a rede naquele momento, mas pode ser feito algo como um comparativo dos dados locais e os dados salvos na numvem, e verificar qual tem os dados mais recentem, claro, no desenvovimento deve ser pensados metodos de segurança em relação a essa implementação. Pois de fato o blueetooth é uma otima ideia, reduzindo os impecilos de rede wifi/4g/5g... e ainda ampliando os aparehos suportados, como por exemplo um smartchwatch com bluetooth conectado ao celular, fazendo intermediação.
E claro, deve ser feito um orçamento sobre o custo do projeto e possiveis retornos.

**Padrão 1: State**
**Categoria: Comportamental.**



[ModuloVeicular] 
        | (Contexto)
        v
  [EstadoMotor (Interface)] <-------------------------+
        |                                             |
        +-- dar_partida(modulo)                       |
        +-- bloquear(modulo)                          |
                                                      |
    +-------------------+-------------------+---------+
    |                   |                   |
[Bloqueado]       [Desbloqueado]    [EmFuncionamento]

**Onde foi aplicado no código:** A interface base é a classe abstrata EstadoMotor, cujas implementações concretas (Bloqueado, Desbloqueado, EmFuncionamento) gerenciam o comportamento da função dar_partida(). O contexto fica na classe ModuloVeicular.


**Padrão 2: Observer
Categoria: Comportamental.**

[SensorProximidade]                          [Observador (Interface)]
    | (Subject)                                      | 
    +-- observadores: List[Observador]               +-- atualizar(distancia)
    +-- adicionar_observador(obs)                    ^
    +-- set_distancia(d)                             | (Implementa)
    +-- _notificar() -----------------------> [ModuloVeicular]


**Onde foi aplicado no código:** No arquivo codigo/sistema_veicular.py. A classe SensorProximidade atua como o sujeito observado. A classe ModuloVeicular implementa a interface Observador através do método atualizar(), recebendo notificações sempre que o celular se afasta.


**Revisão Critica:**
