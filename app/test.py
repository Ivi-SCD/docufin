from constants.categories import classify_by_description

transactions = [
    {"date": "15/03/2025", "amount": 5000.00, "id": "a87c4d31-9f65-42e1-8b23-5a9876dc1234", "description": "Salário Empresa XYZ Ltda"},
    {"date": "17/03/2025", "amount": 750.00, "id": "b12e3f56-78a9-40b1-c234-5d6789e01f23", "description": "Freela design website Cliente ABC"},
    {"date": "18/03/2025", "amount": 325.50, "id": "c23f4g67-8h90-41i2-j345-6k7890l12m34", "description": "Transferência recebida pelo Pix - MARIA SILVA"},
    {"date": "19/03/2025", "amount": -1200.00, "id": "d34g5h78-9i01-42j3-k456-7l8901m23n45", "description": "Aluguel Apartamento Março"},
    {"date": "20/03/2025", "amount": -450.75, "id": "e45h6i89-0j12-43k4-l567-8m9012n34o56", "description": "Mercado Compras da Semana"},
    {"date": "21/03/2025", "amount": -120.00, "id": "f56i7j90-1k23-44l5-m678-9n0123o45p67", "description": "Uber viagens trabalho"},
    {"date": "22/03/2025", "amount": -350.00, "id": "g67j8k01-2l34-45m6-n789-0o1234p56q78", "description": "Consulta médica Dr. Santos"},
    {"date": "23/03/2025", "amount": -99.90, "id": "h78k9l12-3m45-46n7-o890-1p2345q67r89", "description": "Netflix anual e Spotify"},
    {"date": "24/03/2025", "amount": -250.00, "id": "i89l0m23-4n56-47o8-p901-2q3456r78s90", "description": "Roupas e calçados shopping"},
    {"date": "25/03/2025", "amount": -180.00, "id": "j90m1n34-5o67-48p9-q012-3r4567s89t01", "description": "Presente aniversário namorada"},
    {"date": "26/03/2025", "amount": -2000.00, "id": "k01n2o45-6p78-49q0-r123-4s5678t90u12", "description": "Aplicação CDB Banco XYZ 110%"},
    {"date": "27/03/2025", "amount": -1500.00, "id": "l12o3p56-7q89-50r1-s234-5t6789u01v23", "description": "Compra de ações PETR4 e VALE3"},
    {"date": "28/03/2025", "amount": -800.00, "id": "m23p4q67-8r90-51s2-t345-6u7890v12w34", "description": "Compra de FII - HGLG11 e XPLG11"},
    {"date": "29/03/2025", "amount": -500.00, "id": "n34q5r78-9s01-52t3-u456-7v8901w23x45", "description": "Aporte PGBL Bradesco"},
    {"date": "30/03/2025", "amount": -1000.00, "id": "o45r6s89-0t12-53u4-v567-8w9012x34y56", "description": "Compra Bitcoin Exchange"},
    {"date": "31/03/2025", "amount": -700.00, "id": "p56s7t90-1u23-54v5-w678-9x0123y45z67", "description": "Investimento em ouro"},
    {"date": "01/04/2025", "amount": -2500.00, "id": "q67t8u01-2v34-55w6-x789-0y1234z56a78", "description": "Transferência entre contas - Nubank para Inter"},
    {"date": "02/04/2025", "amount": 210.50, "id": "r78u9v12-3w45-56x7-y890-1z2345a67b89", "description": "Reembolso despesas viagem trabalho"},
    {"date": "03/04/2025", "amount": -295.00, "id": "s89v0w23-4x56-57y8-z901-2a3456b78c90", "description": "Curso online de programação"},
    {"date": "04/04/2025", "amount": -98.20, "id": "t90w1x34-5y67-58z9-a012-3b4567c89d01", "description": "Farmácia remédios mês"}
]

for transaction in transactions:
    category = classify_by_description(transaction["description"])
    print(f"Transação: {transaction['description']}")
    print(f"Categoria identificada: {category}")
    print("-" * 50)