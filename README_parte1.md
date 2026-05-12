Parte 1, Engenharia de Requisitos

Tarefa 1.1, Proposta de Tema

Domínio: Sistema Autenticação e Bloqueio Veicular

• O problema:
Rastreadores convencionais apenas informam a localização após o roubo, falhando em impedir a ação inicial. O sistema resolve isso atuando ativamente no controle do veículo: ele exige validação de identidade (via aplicativo, token ou biometria) para liberar a ignição ou a injeção eletrônica. Sem a identificação positiva, o sistema mantém o motor bloqueado. Talvez também um sensor de proximidade após o desbloqueio.

Hoje em dia é fácil roubar veículos, por exemplo: apenas quebrando a ignição da moto uma moto com alguma ferramenta, se pode sair pilotando ela.

• Quem são os usuários principais
Proprietários de veículos em geral, locadoras e concessionárias.
 
• Por que esse problema é relevante
Reduziria consideravelmente os índices de roubos e furtos de veículos, atuando como uma barreira preventiva de segurança em vez de apenas monitorar.



Tarefa 1.2, Planejamento de Entrevista

Objetivo da entrevista
O objetivo desta entrevista é compreender os hábitos de segurança e a rotina diária de proprietários de veículos, identificando as vulnerabilidades que percebem no uso cotidiano e validando a usabilidade de um sistema ativo de bloqueio por autenticação. Busca-se mapear as falhas das soluções atuais do mercado (como rastreadores passivos e alarmes) e entender como a introdução de uma nova etapa de validação (seja por token, biometria ou proximidade) impactaria a experiência do usuário, garantindo que o sistema ofereça alta segurança sem gerar lentidão ou frustração na hora de dar a partida.

• Pelo menos 8 perguntas, sendo:
- Perguntas abertas voltadas à compreensão do problema:

1. Como você descreve a sua preocupação atual em relação à possibilidade de furtos ou roubos do seu veículo no dia a dia?

2. Na sua visão, quais são as principais brechas de segurança que os criminosos exploram para conseguir levar um veículo estacionado (como quebrar a ignição, por exemplo)?

3. Se você pudesse idealizar o sistema de segurança perfeito para o seu veículo, como ele agiria no momento de uma tentativa de furto?

- Perguntas que exploram fluxos de trabalho ou rotinas do usuário:

4. Poderia me descrever detalhadamente o seu passo a passo, desde o momento em que você se aproxima do veículo até dar a partida e arrancar?

5. Como é a sua rotina quando você precisa repassar a direção do veículo para outra pessoa, como um familiar, um mecânico ou um manobrista?

- Perguntas que investigam frustrações ou limitações com soluções atuais:

6. Você já utilizou (ou utiliza) rastreadores, travas físicas ou alarmes sonoros? Quais foram as suas maiores decepções ou problemas com esses métodos?

7. Pensando em tecnologias de segurança, existe algum tipo de validação (como digitar senha ou usar biometria) que você acharia muito irritante ter que fazer toda vez que fosse usar o veículo?

- Pergunta de encerramento:

8. Baseado no que conversamos, há algum outro detalhe, receio ou ideia sobre a segurança de veículos que não abordamos e que você gostaria de compartilhar?

Minha reflexão:
Atualmente, é muito difícil para os brasileiros adquirirem um veículo, mesmo os modelos mais populares. Diante de todo esse esforço financeiro, ter o bem roubado ou furtado é uma experiência extremamente frustrante e devastadora.

Tendo isso como propósito inicial para o software, as primeiras questões do roteiro buscam verificar se o público-alvo se sente compreendido em relação a essa dor. Além disso, visam identificar se os usuários possuem novos pontos de vista ou vulnerabilidades diárias ainda não mapeadas pelos elaboradores da Engenharia de Requisitos (ER).

Depois disso, é importante investigar a experiência e a percepção deles em relação ao problema, questionando sobre as principais brechas de segurança exploradas por criminosos para levar um veículo, seja ele estacionado (furto) ou mediante abordagem (roubo). Também é essencial entender as expectativas dos usuários sobre como um sistema ideal atuaria para salvá-los nessas situações.

Na sequência, o roteiro foca em levantar os possíveis impedimentos e limitações que a nossa proposta traria para a rotina. Exemplos práticos incluem a dificuldade ao emprestar o veículo para terceiros ou a perda de comodidade (como a obrigação de sempre precisar abrir um aplicativo, destravar pelo celular ou usar um token para dar a partida).

Para eliminar ou mitigar esses atritos, a ideia seguinte é coletar a opinião dos entrevistados sobre o que consideram processos irritantes ou inviáveis, questionando como eles imaginariam a usabilidade perfeita do aplicativo no dia a dia. Por fim, a entrevista é encerrada abrindo espaço para o participante comentar qualquer ideia ou receio que não estivesse no escopo inicial, enriquecendo o levantamento de requisitos.


Tarefa 1.3, Historias de Usuário


História de Usuário 1: Autenticação Principal
Como proprietário do veículo, quero autenticar minha identidade via biometria no aplicativo do meu celular para desbloquear a ignição e conseguir dar a partida com segurança.

Critérios de aceitação:

O sistema embarcado só deve liberar a injeção eletrônica/ignição após a confirmação biométrica positiva no aplicativo.

Após o desbloqueio via app, o usuário deve ter uma janela de tempo de até 30 segundos para dar a partida; caso contrário, o sistema bloqueia novamente.

O aplicativo deve exibir um retorno visual (ex: tela verde com cadeado aberto) confirmando que o veículo está pronto para a partida.

Prioridade: Alta.

Justificativa: Esta é a funcionalidade central do projeto. Sem essa etapa, o bloqueio do motor não pode ser desfeito pelo usuário legítimo, inviabilizando o uso do veículo.

História de Usuário 2: Sensor de Proximidade (Anti-Roubo em Movimento)
Como motorista, quero que o motor seja bloqueado de forma segura caso o meu celular (autenticado) se afaste do veículo ligado para impedir que criminosos fujam com o carro após uma abordagem armada no trânsito.

Critérios de aceitação:

O sistema deve monitorar constantemente a conexão Bluetooth/NFC entre o smartphone do motorista e o módulo do veículo.

Ao detectar a perda de proximidade (ex: mais de 10 metros), o sistema deve iniciar um corte de combustível progressivo para não causar acidentes bruscos.

Após o bloqueio total, o sistema deve acionar as luzes de alerta e a buzina para chamar a atenção de pessoas próximas.

Prioridade: Alta.

Justificativa: É a principal defesa contra o roubo em andamento, diferenciando o sistema de trancas convencionais. Garante a integridade do condutor (que pode entregar a chave e se afastar) e a recuperação imediata do bem.

História de Usuário 3: Modo Manobrista/Visitante
Como proprietário do veículo, quero ativar um "Modo Manobrista" temporário pelo meu aplicativo para permitir que terceiros (mecânicos, familiares, manobristas) liguem o carro sem precisarem da minha biometria ou do meu celular.

Critérios de aceitação:

O aplicativo deve permitir a configuração de um limite de tempo (ex: 2 horas) ou distância (ex: raio de 2km) para o Modo Manobrista.

O veículo deve dar partida normalmente (sem bloqueio) enquanto os limites estabelecidos não forem ultrapassados.

Se o terceiro ultrapassar os limites de tempo ou distância, o aplicativo deve notificar o dono e o veículo deve ser bloqueado na próxima vez que a ignição for desligada.

Prioridade: Média.

Justificativa: Resolve a principal objeção de usabilidade levantada em entrevistas. Um sistema de segurança engessado impede ações corriqueiras do dia a dia, tornando o "Modo Manobrista" essencial para a viabilidade do produto.

História de Usuário 4: Autenticação Offline
Como motorista, quero validar minha identidade através de uma conexão local segura (Bluetooth) para conseguir desbloquear e ligar meu veículo mesmo em garagens subterrâneas ou regiões rurais sem cobertura de internet.

Critérios de aceitação:

A comunicação entre o aplicativo e a central do veículo não deve depender de requisições a servidores na nuvem no momento da partida.

Os tokens de acesso gerados localmente devem ser criptografados para evitar a clonagem do sinal (ataques de replay).

O aplicativo deve sincronizar o histórico de partidas com o servidor em nuvem assim que o celular recuperar a conexão com a internet.

Prioridade: Alta.

Justificativa: A ausência de sinal de internet (3G/4G/5G) é uma realidade constante. Depender exclusivamente de conectividade faria o dono do carro ficar "preso" na própria garagem, gerando frustração extrema.

História de Usuário 5: Notificação de Tentativa de Furto
Como proprietário do veículo, quero receber uma notificação imediata (push) no celular caso haja uma tentativa forçada de ligar a ignição sem a devida autenticação para que eu possa tomar providências imediatas.

Critérios de aceitação:

O módulo veicular deve detectar tentativas de ligação direta ("mixa") ou giro da chave mecânica sem a liberação prévia via app.

Uma notificação push deve ser enviada para o smartphone do proprietário em no máximo 5 segundos após a detecção do evento.

A notificação deve conter a data, o horário exato e as coordenadas GPS de onde a tentativa ocorreu.

Prioridade: Média.

Justificativa: Embora a ação principal (bloquear) já esteja garantida pelo hardware, alertar o dono fornece consciência situacional, agregando valor perceptível à sensação de segurança proporcionada pelo aplicativo.








