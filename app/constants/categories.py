from models.domain.category import CategoryType
from typing import List, Dict
from uuid import UUID, uuid4

CATEGORIAS = [
    'SALARIO', 
    'RENDA_EXTRA', 
    'TRANSFERENCIA_RECEBIDA', 
    'REEMBOLSO',
    'MORADIA',
    'ALIMENTACAO',
    'TRANSPORTE',
    'SAUDE',
    'EDUCACAO',
    'LAZER',
    'PESSOAL',
    'NAMORADA',
    'RENDA_FIXA',
    'RENDA_VARIAVEL',
    'FUNDOS_IMOBILIARIOS',
    'PREVIDENCIA',
    'CRIPTOMOEDAS',
    'OUTROS_INVESTIMENTOS',
    'TRANSFERENCIA'
]

CATEGORIA_TIPOS = {
    'SALARIO': CategoryType.INCOME,
    'RENDA_EXTRA': CategoryType.INCOME,
    'TRANSFERENCIA_RECEBIDA': CategoryType.INCOME,
    'REEMBOLSO': CategoryType.INCOME,
    'MORADIA': CategoryType.EXPENSE,
    'ALIMENTACAO': CategoryType.EXPENSE,
    'TRANSPORTE': CategoryType.EXPENSE,
    'SAUDE': CategoryType.EXPENSE,
    'EDUCACAO': CategoryType.EXPENSE,
    'LAZER': CategoryType.EXPENSE,
    'PESSOAL': CategoryType.EXPENSE,
    'NAMORADA': CategoryType.EXPENSE,
    'RENDA_FIXA': CategoryType.INVESTMENT,
    'RENDA_VARIAVEL': CategoryType.INVESTMENT,
    'FUNDOS_IMOBILIARIOS': CategoryType.INVESTMENT,
    'PREVIDENCIA': CategoryType.INVESTMENT,
    'CRIPTOMOEDAS': CategoryType.INVESTMENT,
    'OUTROS_INVESTIMENTOS': CategoryType.INVESTMENT,
    'TRANSFERENCIA': CategoryType.TRANSFER
}

DEFAULT_CATEGORIES = [
    {
        "name": "SALARIO",
        "type": CategoryType.INCOME,
        "description": "Receitas provenientes de salário"
    },
    {
        "name": "RENDA_EXTRA",
        "type": CategoryType.INCOME,
        "description": "Receitas extras além do salário principal"
    },
    {
        "name": "TRANSFERENCIA_RECEBIDA",
        "type": CategoryType.INCOME,
        "description": "Transferências recebidas de terceiros"
    },
    {
        "name": "REEMBOLSO",
        "type": CategoryType.INCOME,
        "description": "Valores reembolsados de despesas anteriores"
    },
    {
        "name": "MORADIA",
        "type": CategoryType.EXPENSE,
        "description": "Despesas relacionadas à moradia (aluguel, condomínio, IPTU)"
    },
    {
        "name": "ALIMENTACAO",
        "type": CategoryType.EXPENSE,
        "description": "Despesas com alimentação (mercado, restaurantes, delivery)"
    },
    {
        "name": "TRANSPORTE",
        "type": CategoryType.EXPENSE,
        "description": "Despesas com transporte (combustível, transporte público, apps)"
    },
    {
        "name": "SAUDE",
        "type": CategoryType.EXPENSE,
        "description": "Despesas médicas e relacionadas à saúde"
    },
    {
        "name": "EDUCACAO",
        "type": CategoryType.EXPENSE,
        "description": "Despesas com educação e cursos"
    },
    {
        "name": "LAZER",
        "type": CategoryType.EXPENSE,
        "description": "Despesas com entretenimento e lazer"
    },
    {
        "name": "PESSOAL",
        "type": CategoryType.EXPENSE,
        "description": "Despesas pessoais diversas"
    },
    {
        "name": "NAMORADA",
        "type": CategoryType.EXPENSE,
        "description": "Despesas relacionadas ao relacionamento"
    },
    {
        "name": "RENDA_FIXA",
        "type": CategoryType.INVESTMENT,
        "description": "Investimentos em renda fixa (CDB, LCI, LCA, Tesouro)"
    },
    {
        "name": "RENDA_VARIAVEL",
        "type": CategoryType.INVESTMENT,
        "description": "Investimentos em renda variável (ações, ETFs)"
    },
    {
        "name": "FUNDOS_IMOBILIARIOS",
        "type": CategoryType.INVESTMENT,
        "description": "Investimentos em Fundos Imobiliários (FIIs)"
    },
    {
        "name": "PREVIDENCIA",
        "type": CategoryType.INVESTMENT,
        "description": "Investimentos em planos de previdência"
    },
    {
        "name": "CRIPTOMOEDAS",
        "type": CategoryType.INVESTMENT,
        "description": "Investimentos em criptomoedas"
    },
    {
        "name": "OUTROS_INVESTIMENTOS",
        "type": CategoryType.INVESTMENT,
        "description": "Outros tipos de investimentos"
    },
    {
        "name": "TRANSFERENCIA",
        "type": CategoryType.TRANSFER,
        "description": "Transferências entre contas próprias"
    }
]

# Palavras-chave para classificação automática
CATEGORY_KEYWORDS = {
    "salário": "SALARIO",
    "salario": "SALARIO",
    "pró-labore": "SALARIO",
    "pro-labore": "SALARIO",
    "prolabore": "SALARIO",
    "freela": "RENDA_EXTRA",
    "freelance": "RENDA_EXTRA",
    "extra": "RENDA_EXTRA",
    "bico": "RENDA_EXTRA",
    "adicional": "RENDA_EXTRA",
    "pix recebido": "TRANSFERENCIA_RECEBIDA",
    "transferência recebida": "TRANSFERENCIA_RECEBIDA",
    "transferencia recebida": "TRANSFERENCIA_RECEBIDA",
    "reembolso": "REEMBOLSO",
    "estorno": "REEMBOLSO",
    "devolução": "REEMBOLSO",
    "devolucao": "REEMBOLSO",
    "cashback": "REEMBOLSO",
    "aluguel": "MORADIA",
    "condomínio": "MORADIA",
    "condominio": "MORADIA",
    "iptu": "MORADIA",
    "luz": "MORADIA",
    "energia": "MORADIA",
    "água": "MORADIA",
    "agua": "MORADIA",
    "gás": "MORADIA",
    "gas": "MORADIA",
    "internet": "MORADIA",
    "mercado": "ALIMENTACAO",
    "supermercado": "ALIMENTACAO",
    "restaurante": "ALIMENTACAO",
    "ifood": "ALIMENTACAO",
    "delivery": "ALIMENTACAO",
    "lanche": "ALIMENTACAO",
    "combustível": "TRANSPORTE",
    "combustivel": "TRANSPORTE",
    "gasolina": "TRANSPORTE",
    "estacionamento": "TRANSPORTE",
    "pedágio": "TRANSPORTE",
    "pedagio": "TRANSPORTE",
    "uber": "TRANSPORTE",
    "99": "TRANSPORTE",
    "táxi": "TRANSPORTE",
    "taxi": "TRANSPORTE",
    "metrô": "TRANSPORTE",
    "metro": "TRANSPORTE",
    "ônibus": "TRANSPORTE",
    "onibus": "TRANSPORTE",
    "médico": "SAUDE",
    "medico": "SAUDE",
    "dentista": "SAUDE",
    "psicólogo": "SAUDE",
    "psicologo": "SAUDE",
    "farmácia": "SAUDE",
    "farmacia": "SAUDE",
    "remédio": "SAUDE",
    "remedio": "SAUDE",
    "consulta": "SAUDE",
    "exame": "SAUDE",
    "academia": "SAUDE",
    "plano de saúde": "SAUDE",
    "plano de saude": "SAUDE",
    "escola": "EDUCACAO",
    "faculdade": "EDUCACAO",
    "mensalidade": "EDUCACAO",
    "curso": "EDUCACAO",
    "livro": "EDUCACAO",
    "material escolar": "EDUCACAO",
    "cinema": "LAZER",
    "teatro": "LAZER",
    "show": "LAZER",
    "netflix": "LAZER",
    "spotify": "LAZER",
    "amazon prime": "LAZER",
    "disney": "LAZER",
    "hbo": "LAZER",
    "jogo": "LAZER",
    "game": "LAZER",
    "viagem": "LAZER",
    "hotel": "LAZER",
    "passeio": "LAZER",
    "roupa": "PESSOAL",
    "vestuário": "PESSOAL",
    "vestuario": "PESSOAL",
    "calçado": "PESSOAL",
    "calcado": "PESSOAL",
    "cabelo": "PESSOAL",
    "salão": "PESSOAL",
    "salao": "PESSOAL",
    "celular": "PESSOAL",
    "academia": "PESSOAL",
    "presente": "NAMORADA",
    "namorada": "NAMORADA",
    "encontro": "NAMORADA",
    "jantar romântico": "NAMORADA",
    "jantar romantico": "NAMORADA",
    "cdb": "RENDA_FIXA",
    "tesouro": "RENDA_FIXA",
    "tesouro direto": "RENDA_FIXA",
    "lci": "RENDA_FIXA",
    "lca": "RENDA_FIXA",
    "rdb": "RENDA_FIXA",
    "cri": "RENDA_FIXA",
    "cra": "RENDA_FIXA",
    "debênture": "RENDA_FIXA",
    "debenture": "RENDA_FIXA",
    "poupança": "RENDA_FIXA",
    "poupanca": "RENDA_FIXA",
    "ações": "RENDA_VARIAVEL",
    "acoes": "RENDA_VARIAVEL",
    "ação": "RENDA_VARIAVEL",
    "acao": "RENDA_VARIAVEL",
    "etf": "RENDA_VARIAVEL",
    "bolsa": "RENDA_VARIAVEL",
    "b3": "RENDA_VARIAVEL",
    "fii": "FUNDOS_IMOBILIARIOS",
    "fundo imobiliário": "FUNDOS_IMOBILIARIOS",
    "fundo imobiliario": "FUNDOS_IMOBILIARIOS",
    "previdência": "PREVIDENCIA",
    "previdencia": "PREVIDENCIA",
    "pgbl": "PREVIDENCIA",
    "vgbl": "PREVIDENCIA",
    "aposentadoria": "PREVIDENCIA",
    "bitcoin": "CRIPTOMOEDAS",
    "btc": "CRIPTOMOEDAS",
    "ethereum": "CRIPTOMOEDAS",
    "eth": "CRIPTOMOEDAS",
    "cripto": "CRIPTOMOEDAS",
    "criptomoeda": "CRIPTOMOEDAS",
    "binance": "CRIPTOMOEDAS",
    "ouro": "OUTROS_INVESTIMENTOS",
    "prata": "OUTROS_INVESTIMENTOS",
    "obra de arte": "OUTROS_INVESTIMENTOS",
    "colecionável": "OUTROS_INVESTIMENTOS",
    "colecionavel": "OUTROS_INVESTIMENTOS",
    "nft": "OUTROS_INVESTIMENTOS",
    "transferência": "TRANSFERENCIA",
    "transferencia": "TRANSFERENCIA",
    "ted": "TRANSFERENCIA",
    "doc": "TRANSFERENCIA",
    "depósito": "TRANSFERENCIA",
    "deposito": "TRANSFERENCIA",
    "entre contas": "TRANSFERENCIA",
    "pix enviado": "TRANSFERENCIA"
}


def get_category_type(category_name: str) -> CategoryType:
    """
    Retorna o tipo de uma categoria baseado no seu nome
    """
    return CATEGORIA_TIPOS.get(category_name, CategoryType.EXPENSE)


def classify_by_description(description: str) -> str:
    """
    Classifica uma transação baseada em palavras-chave na descrição
    Retorna o nome da categoria ou None se não encontrar correspondência
    """
    description = description.lower()
    for keyword, category in CATEGORY_KEYWORDS.items():
        if keyword.lower() in description:
            return category
    return None