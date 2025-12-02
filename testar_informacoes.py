import unittest
from robo import *

class TesteInformacoes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.robo = configurar_robo()
        return super().setUpClass()
    
    def testar_01_agendar_reunioes(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "como posso agendar reuniões?",
            "como agendar reunião?",
            "onde agendo reunião?",
            "quero marcar uma reunião",
            "onde marco reunião?"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Você pode agendar reuniões através do assistente virtual corporativo informando data, hora, participantes e local. Também é possível agendar manualmente pelo sistema interno de agendamentos.".lower(),
                resposta.text.lower()
            )

    def testar_02_horarios_funcionamento(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "quais os horários de funcionamento do escritório?",
            "qual o horário de funcionamento?",
            "que horas o escritório abre?",
            "que horas funciona o escritório?",
            "horário de funcionamento",
            "hora de funcionamento"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O escritório funciona de segunda a sexta-feira, das 08h às 18h, exceto feriados.".lower(),
                resposta.text.lower()
            )

    def testar_03_servicos_assistente(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "que serviços o assistente virtual do escritório oferece?",
            "o que o assistente virtual faz?",
            "quais serviços automatizados a empresa oferece?",
            "quais comandos o assistente reconhece?",
            "como funciona o assistente virtual?"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Temos dois assistentes de IA para auxiliar! O assistente virtual do escritório reconhece comandos de voz e controla funções do ambiente corporativo simulado, podendo: ligar ou desligar o projetor; ligar, desligar, acender, apagar ou ajustar a intensidade das luzes; agendar reuniões informando o horário desejado; exibir a agenda do dia; e ativar ou desativar o modo apresentação. Já o chatbot fornece informações internas, orientações sobre processos, ajuda em dúvidas comuns, suporte básico e direcionamento para os sistemas corretos da empresa.".lower(),
                resposta.text.lower()
            )

    def testar_04_solicitacao_manutencao(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "onde faço uma solicitação de manutenção?",
            "como solicitar manutenção?",
            "preciso pedir manutenção",
            "como chamo manuntenção?",
            "quero solicitar manutenção",
            "quero saber como solicitar manutenção"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "As solicitações de manutenção podem ser feitas pelo sistema interno de chamados, na seção 'Manutenção e Infraestrutura'.".lower(),
                resposta.text.lower()
            )

    def testar_05_equipamentos_disponiveis(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "quais equipamentos o escritório disponibiliza?",
            "que equipamentos estão disponíveis?",
            "equipamentos do escritório",
            "quai equipamentos eu posso usar?",
            "quero saber dos equipamentos disponíveis"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O escritório disponibiliza notebooks, monitores, projetores, headsets, impressoras, salas equipadas e estações de trabalho compartilhadas.".lower(),
                resposta.text.lower()
            )

    def testar_06_reserva_sala_reuniao(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "como reservar uma sala de reunião?",
            "onde reservo sala de reunião?",
            "quero reservar uma sala",
            "quero saber como reservar sala",
            "preciso reservar uma sala",
            "reservar sala"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A reserva de salas de reunião pode ser feita pelo sistema interno de agendamentos, escolhendo a sala, horário e duração.".lower(),
                resposta.text.lower()
            )

    def testar_07_localizacao_setores(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "onde ficam os setores do escritório?",
            "mapa do escritório",
            "localização dos setores",
            "quero saber dos setores"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O mapa completo do escritório e a localização dos setores estão disponíveis no portal interno da empresa, na área de 'Infraestrutura'.".lower(),
                resposta.text.lower()
            )

    def testar_08_solicitar_materiais(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "como solicitar materiais de escritório?",
            "preciso de materiais",
            "como peço materiais?",
            "onde solicito materiais?",
            "quero saber como pedir materiais",
            "quero saber como solicitar materiais",
            "quero socilitar materiais"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Materiais de escritório podem ser solicitados através do sistema interno na aba 'Solicitação de Materiais'.".lower(),
                resposta.text.lower()
            )

    def testar_09_receber_visitantes(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "quais são os procedimentos para receber visita no escritório?",
            "como recebo visitantes?",
            "procedimento para visitante",
            "quero receber um cliente",
            "quero receber um fornecedor",
            "quero saber como receber visitantes"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Para receber visitantes, informe previamente o nome completo, empresa e horário de chegada no sistema de visitantes. Eles serão liberados na recepção mediante documento de identificação.".lower(),
                resposta.text.lower()
            )

    def testar_10_calendario_eventos(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "onde encontro o calendário de eventos da empresa?",
            "calendário de eventos",
            "agenda de eventos",
            "quero saber dos eventos"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O calendário de eventos internos está disponível no portal corporativo, na seção 'Eventos e Comunicados'.".lower(),
                resposta.text.lower()
            )

    def testar_11_solicitar_ferias(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "como solicitar férias?",
            "quero pedir férias",
            "onde solicito férias?",
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "A solicitação de férias deve ser feita pelo sistema de RH, na aba 'Gestão de Férias', seguindo o fluxo de aprovação do gestor.".lower(),
                resposta.text.lower()
            )

    def testar_12_auxilio_geral(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "como você pode me auxiliar?",
            "como pode me ajudar?",
            "como pode ajudar?",
            "o que você pode fazer por mim?",
            "o que você faz?"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Posso ajudar com informações do escritório, agendamentos, solicitações internas, orientações, organização de tarefas e suporte básico ao usuário.".lower(),
                resposta.text.lower()
            )

unittest.main()
