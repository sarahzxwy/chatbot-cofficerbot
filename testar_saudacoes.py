import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.robo = configurar_robo()
        return super().setUpClass()
    
    def testar_01_saudacoes_gerais(self):
        self.assertIsNotNone(self.robo)

        saudacoes = [
            "oi", "olá", "tudo bem?", "como vai?",
            "oi, tudo bem?", "olá, tudo bem?",
            "oi, como vai?", "olá, como vai?",
            "como você está?", "oi, como você está?",
            "tudo certo?", "oi, tudo certo?",
            "tudo tranquilo?", "oi, tudo tranquilo?",
        ]

        for saudacao in saudacoes:
            resposta = self.robo.get_response(saudacao)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Olá! Sou o COFFICERBot, seu assistente corporativo. Como posso ajudar?".lower(),
                resposta.text.lower()
            )

    def testar_02_bom_dia(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "bom dia", "olá, bom dia", "oi, bom dia",
            "bom dia, tudo bem?", "bom dia, tudo certo?"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Bom dia! Sou o COFFICERBot, seu assistente corporativo. Como posso ajudar nesta manhã?".lower(),
                resposta.text.lower()
            )

    def testar_03_boa_tarde(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "boa tarde", "olá, boa tarde", "oi, boa tarde",
            "boa tarde, tudo bem?", "boa tarde, tudo certo?"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Boa tarde! Sou o COFFICERBot, seu assistente de escritório corporativo. O que posso fazer por você?".lower(),
                resposta.text.lower()
            )

    def testar_04_boa_noite(self):
        self.assertIsNotNone(self.robo)

        mensagens = [
            "boa noite", "olá, boa noite", "oi, boa noite",
            "boa noite, tudo bem?", "boa noite, tudo certo?"
        ]

        for msg in mensagens:
            resposta = self.robo.get_response(msg)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "Boa noite! Sou o COFFICERBot, seu assistente corporativo. Como posso te ajudar agora?".lower(),
                resposta.text.lower()
            )

unittest.main()
