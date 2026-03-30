def generate_mock_data() -> dict:
    """Generate 4 fictional Brazilian legal processes with realistic chunks."""
    return {
        "processes": [
            # ── Process 1: Maria Silva vs. Empresa XYZ Ltda (horas extras) ──
            {
                "name": "Maria Silva vs. Empresa XYZ Ltda",
                "case_type": "trabalhista",
                "parties": {"plaintiff": "Maria Silva", "defendant": "Empresa XYZ Ltda"},
                "status": "sentenciado",
                "sentence_summary": (
                    "Juiz condenou a empresa ao pagamento de horas extras excedentes da 8ª diária e 44ª semanal, "
                    "com adicional de 50%, reflexos em DSR, férias + 1/3, 13º salário e FGTS + 40%. "
                    "Também condenou ao pagamento de 1 hora extra diária pelo intervalo intrajornada suprimido "
                    "e indenização por danos morais de R$ 10.000,00. Valor total da condenação: R$ 120.000,00."
                ),
                "chunks": [
                    {
                        "content": (
                            "A reclamante Maria da Silva, brasileira, solteira, operadora de caixa, portadora do "
                            "CPF nº 123.456.789-00, CTPS nº 12345 série 001-SP, residente na Rua das Flores, nº 456, "
                            "Bairro Jardim Esperança, São Paulo/SP, CEP 01234-567, vem, por intermédio de seus advogados "
                            "(procuração anexa), perante esta MM. Vara do Trabalho, propor a presente RECLAMAÇÃO TRABALHISTA "
                            "em face de EMPRESA XYZ LTDA., pessoa jurídica de direito privado, inscrita no CNPJ sob o "
                            "nº 12.345.678/0001-90, com sede na Av. Industrial, nº 1000, Bairro Centro, São Paulo/SP. "
                            "A reclamante foi admitida em 15/03/2020, exercendo a função de operadora de caixa, com "
                            "salário mensal de R$ 1.800,00 (mil e oitocentos reais), tendo sido dispensada sem justa causa "
                            "em 20/11/2023. Durante todo o período contratual, a reclamante laborou em regime de sobrejornada, "
                            "cumprindo habitualmente jornada das 07h00 às 19h00, com apenas 30 minutos de intervalo para "
                            "refeição, de segunda a sábado, sem receber as horas extras devidas, em flagrante violação aos "
                            "artigos 58 e 71 da CLT."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 1,
                    },
                    {
                        "content": (
                            "DOS FATOS: A reclamante foi contratada pela reclamada em 15 de março de 2020 para exercer "
                            "a função de operadora de caixa no supermercado da rede XYZ, localizado na Av. Paulista, "
                            "nº 2000, São Paulo/SP. Conforme consta na CTPS (doc. 02), o salário contratual era de "
                            "R$ 1.800,00 mensais, com jornada prevista das 08h00 às 17h00, com 1 hora de intervalo. "
                            "Ocorre que, na prática, a reclamante era obrigada a chegar ao estabelecimento às 07h00 "
                            "para participar de reuniões matinais obrigatórias com a gerência, onde eram passadas metas "
                            "de vendas e orientações sobre promoções do dia. Ademais, a reclamante raramente conseguia "
                            "encerrar suas atividades antes das 19h00, pois era responsável pelo fechamento do caixa e "
                            "conferência de valores, atividades que se estendiam além do horário contratual. O intervalo "
                            "para refeição era de apenas 30 minutos, insuficiente para o descanso adequado, em clara "
                            "violação ao art. 71 da CLT que prevê intervalo mínimo de 1 hora para jornadas superiores "
                            "a 6 horas."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 2,
                    },
                    {
                        "content": (
                            "DO DIREITO — DAS HORAS EXTRAS: Nos termos do art. 58 da CLT, a duração normal do trabalho "
                            "não excederá 8 horas diárias e 44 horas semanais. A reclamante, conforme demonstrado, laborava "
                            "habitualmente 12 horas por dia (das 07h00 às 19h00), perfazendo 72 horas semanais (de segunda "
                            "a sábado), ou seja, 28 horas extras semanais. Considerando o salário mensal de R$ 1.800,00, "
                            "o valor da hora normal é de R$ 8,18 (R$ 1.800,00 / 220h). Com o adicional de 50% previsto "
                            "no art. 7º, XVI, da CF/88, a hora extra equivale a R$ 12,27. Multiplicando pelas 28 horas "
                            "extras semanais, tem-se o valor semanal de R$ 343,56, perfazendo aproximadamente R$ 1.487,42 "
                            "mensais em horas extras não pagas. Ao longo dos 44 meses de contrato (março/2020 a novembro/2023), "
                            "o débito acumulado de horas extras atinge aproximadamente R$ 65.446,48, sem considerar reflexos "
                            "e correção monetária."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 3,
                    },
                    {
                        "content": (
                            "DO INTERVALO INTRAJORNADA: Conforme art. 71 da CLT, em qualquer trabalho contínuo cuja duração "
                            "exceda 6 horas, é obrigatória a concessão de um intervalo para repouso ou alimentação de, no mínimo, "
                            "1 hora. A reclamante usufruía de apenas 30 minutos de intervalo, conforme será comprovado por "
                            "testemunhas. A supressão parcial do intervalo intrajornada implica o pagamento do período "
                            "correspondente como hora extra, com acréscimo de 50%, conforme §4º do art. 71 da CLT e "
                            "Súmula 437 do TST. Requer-se, portanto, a condenação da reclamada ao pagamento de 1 hora "
                            "extra diária, referente ao intervalo suprimido, durante todo o período contratual."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 4,
                    },
                    {
                        "content": (
                            "DOS DANOS MORAIS: A submissão da reclamante a jornada extenuante de 12 horas diárias, 6 dias "
                            "por semana, sem o devido pagamento de horas extras e com intervalo reduzido, configura ato "
                            "ilícito do empregador, causando danos à saúde física e mental da trabalhadora. Conforme "
                            "relatório médico anexo (doc. 05), a reclamante desenvolveu síndrome de burnout e problemas "
                            "osteomusculares relacionados ao trabalho (DORT) durante o período contratual. A conduta da "
                            "reclamada viola os princípios da dignidade da pessoa humana (art. 1º, III, CF/88) e do valor "
                            "social do trabalho (art. 1º, IV, CF/88). Pleiteia-se indenização por danos morais no valor "
                            "de R$ 20.000,00, considerando a gravidade da conduta, a capacidade econômica da empresa e "
                            "o caráter pedagógico da condenação. DOS PEDIDOS: Ante o exposto, requer a procedência total "
                            "dos pedidos, condenando a reclamada ao pagamento de horas extras, intervalo intrajornada "
                            "suprimido, reflexos legais e danos morais."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 5,
                    },
                    {
                        "content": (
                            "CONTESTAÇÃO — EMPRESA XYZ LTDA.: A reclamada, por seus advogados, vem apresentar contestação "
                            "à reclamação trabalhista movida por Maria da Silva. PRELIMINARMENTE, impugna-se o valor dado à "
                            "causa, por excessivo e incompatível com a realidade dos fatos. No mérito, a reclamada nega "
                            "veementemente as alegações da inicial. A jornada de trabalho da reclamante sempre foi das 08h00 "
                            "às 17h00, com 1 hora de intervalo, conforme registrado nos cartões de ponto eletrônicos (docs. "
                            "anexos). A reclamante jamais participou de reuniões matinais obrigatórias antes do horário de "
                            "trabalho. As reuniões de equipe ocorriam esporadicamente e sempre dentro do horário contratual. "
                            "A empresa possui sistema eletrônico de controle de jornada, modelo REP-C, homologado pelo MTE, "
                            "e os registros demonstram que a reclamante cumpria regularmente sua jornada contratual."
                        ),
                        "section": "contestacao",
                        "page_number": 6,
                    },
                    {
                        "content": (
                            "A reclamada ressalta que mantém rigoroso controle de jornada e que todos os funcionários são "
                            "orientados a registrar o ponto nos horários corretos de entrada e saída. Eventuais permanências "
                            "além do horário eram esporádicas e devidamente compensadas por meio de banco de horas, conforme "
                            "acordo coletivo firmado com o sindicato da categoria (doc. 08). Quanto ao intervalo intrajornada, "
                            "a empresa disponibiliza refeitório próprio e o intervalo de 1 hora é respeitado, conforme "
                            "demonstram os registros de ponto. A alegação de intervalo de apenas 30 minutos não encontra "
                            "respaldo nos documentos apresentados. Impugna-se o pedido de danos morais, pois a reclamante "
                            "não comprovou nexo causal entre as condições de trabalho e os problemas de saúde alegados. "
                            "O atestado médico apresentado é genérico e não estabelece relação com o trabalho."
                        ),
                        "section": "contestacao",
                        "page_number": 7,
                    },
                    {
                        "content": (
                            "A reclamada destaca que o acordo coletivo de trabalho da categoria (2020/2022 e 2022/2024) "
                            "prevê a possibilidade de banco de horas com compensação em até 6 meses, sendo que a empresa "
                            "sempre respeitou os termos pactuados. A reclamante, durante todo o contrato, nunca apresentou "
                            "reclamação formal à empresa ou ao sindicato sobre a jornada de trabalho. A empresa possui "
                            "canal de denúncias interno e programa de compliance trabalhista, demonstrando boa-fé nas "
                            "relações de trabalho. Requer-se a improcedência total dos pedidos, com a condenação da "
                            "reclamante ao pagamento de honorários advocatícios sucumbenciais de 10% sobre o valor da causa."
                        ),
                        "section": "contestacao",
                        "page_number": 8,
                    },
                    {
                        "content": (
                            "Por fim, subsidiariamente, caso este MM. Juízo entenda por acolher algum dos pedidos, requer "
                            "a limitação das horas extras ao período imprescrito (últimos 5 anos), a aplicação do adicional "
                            "de 50% (e não superior), a compensação com valores já pagos a título de banco de horas, e a "
                            "fixação dos danos morais em valor proporcional e razoável, não superior a R$ 2.000,00. "
                            "Protesta provar o alegado por todos os meios de prova admitidos em direito, especialmente "
                            "documental, testemunhal e pericial."
                        ),
                        "section": "contestacao",
                        "page_number": 9,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA 1ª TESTEMUNHA DA RECLAMANTE — Carlos Eduardo Souza, brasileiro, "
                            "casado, repositor, RG nº 98.765.432-1. Compromissado e advertido, inquirido, respondeu: "
                            "que trabalhou na reclamada de janeiro de 2019 a agosto de 2023; que trabalhava no mesmo "
                            "setor da reclamante; que a jornada habitual era das 07h00 às 19h00, com intervalo de "
                            "aproximadamente 30 minutos; que nos sábados trabalhavam das 07h00 às 14h00; que nunca "
                            "recebeu pagamento de horas extras; que o gerente, Sr. Roberto, exigia que os funcionários "
                            "registrassem o ponto no horário contratual (08h00-17h00), mesmo chegando antes e saindo depois; "
                            "que presenciou a reclamante sendo advertida verbalmente por tentar registrar o ponto no "
                            "horário real de saída; que havia câmeras no estabelecimento que poderiam comprovar os "
                            "horários reais. Nada mais disse."
                        ),
                        "section": "depoimento",
                        "page_number": 10,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA 2ª TESTEMUNHA DA RECLAMANTE — Fernanda Rodrigues Lima, brasileira, solteira, "
                            "caixa, RG nº 45.678.901-2. Compromissada e advertida, inquirida, respondeu: que trabalhou na "
                            "reclamada de março de 2021 a fevereiro de 2023; que era colega de setor da reclamante; que "
                            "confirma a jornada alegada, pois também trabalhava no mesmo horário; que as reuniões matinais "
                            "às 07h00 eram obrigatórias e quem não comparecesse recebia advertência; que o intervalo de "
                            "almoço era de apenas 30 minutos porque a gerência exigia que os caixas voltassem rapidamente "
                            "para evitar filas; que também nunca recebeu horas extras; que saiu da empresa por conta "
                            "própria devido ao excesso de trabalho e cansaço. Nada mais disse."
                        ),
                        "section": "depoimento",
                        "page_number": 11,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA TESTEMUNHA DA RECLAMADA — Roberto Almeida Santos, brasileiro, casado, gerente "
                            "de loja, RG nº 11.222.333-4. Compromissado e advertido, inquirido, respondeu: que é gerente "
                            "da loja desde 2018; que a jornada dos funcionários é das 08h00 às 17h00 com 1 hora de intervalo; "
                            "que as reuniões matinais não eram obrigatórias e ocorriam apenas uma vez por semana; que o sistema "
                            "de ponto eletrônico é fidedigno e registra automaticamente os horários; que nunca exigiu que "
                            "funcionários registrassem ponto em horário diferente do real; que a empresa possui política de "
                            "banco de horas. Contradita pela reclamante: a testemunha é gerente da loja e tem interesse direto "
                            "no resultado da demanda. O juízo manteve o depoimento, valorando-o com as devidas ressalvas."
                        ),
                        "section": "depoimento",
                        "page_number": 12,
                    },
                    {
                        "content": (
                            "SENTENÇA: Processo nº 1234567-89.2023.5.02.0001. Vistos e examinados os autos, "
                            "DECIDE este Juízo: Restou comprovado nos autos, através dos cartões de ponto e depoimentos "
                            "testemunhais, que a reclamante efetivamente laborava em jornada extraordinária, das 07h00 às "
                            "19h00, com intervalo reduzido de apenas 30 minutos, configurando violação ao art. 71, §4º da CLT. "
                            "A reclamada não se desincumbiu do ônus probatório que lhe competia (art. 818, II, CLT c/c "
                            "art. 373, II, CPC), deixando de apresentar controles de ponto fidedignos. Os cartões "
                            "apresentados continham horários britânicos (invariáveis), o que gera presunção relativa de "
                            "veracidade da jornada alegada pela reclamante (Súmula 338, III, TST)."
                        ),
                        "section": "sentenca",
                        "page_number": 13,
                    },
                    {
                        "content": (
                            "O depoimento da testemunha Carlos Eduardo Souza foi coerente e convincente, corroborado pela "
                            "testemunha Fernanda Rodrigues Lima, ambos confirmando a jornada extraordinária e a prática de "
                            "registro irregular de ponto. A testemunha da reclamada, por ser gerente e ter interesse direto "
                            "no resultado, teve seu depoimento valorado com ressalvas, não sendo suficiente para afastar as "
                            "provas produzidas pela reclamante. Os cartões de ponto com horários britânicos (invariáveis) "
                            "constituem prova inválida, gerando presunção relativa de veracidade da jornada alegada pela "
                            "obreira, conforme Súmula 338, III, do TST. Quanto ao banco de horas, a reclamada não comprovou "
                            "a efetiva compensação das horas extras, ônus que lhe incumbia. O simples acordo coletivo prevendo "
                            "a possibilidade de banco de horas não afasta a obrigação de pagamento quando não demonstrada "
                            "a compensação."
                        ),
                        "section": "sentenca",
                        "page_number": 14,
                    },
                    {
                        "content": (
                            "CONDENO a reclamada ao pagamento de: (a) horas extras excedentes da 8ª diária e 44ª semanal, "
                            "com adicional de 50%, conforme art. 7º, XVI, CF/88, e reflexos em DSR, férias + 1/3, "
                            "13º salário e FGTS + 40%; (b) 1 hora extra diária referente ao intervalo intrajornada "
                            "suprimido (art. 71, §4º, CLT); (c) indenização por danos morais no valor de R$ 10.000,00 "
                            "(dez mil reais), pela submissão a jornada extenuante. Custas pela reclamada, no importe de "
                            "R$ 2.400,00, calculadas sobre o valor arbitrado à condenação de R$ 120.000,00. "
                            "Juros e correção monetária na forma da ADC 58 do STF (IPCA-E na fase pré-judicial e taxa SELIC "
                            "a partir do ajuizamento). Honorários advocatícios sucumbenciais de 10% sobre o valor da "
                            "condenação, a cargo da reclamada. Partes intimadas. Nada mais."
                        ),
                        "section": "sentenca",
                        "page_number": 15,
                    },
                ],
            },
            # ── Process 2: João Santos vs. Loja ABC S.A. (demissão sem justa causa) ──
            {
                "name": "João Santos vs. Loja ABC S.A.",
                "case_type": "trabalhista",
                "parties": {"plaintiff": "João Santos", "defendant": "Loja ABC S.A."},
                "status": "sentenciado",
                "sentence_summary": (
                    "Juiz acolheu parcialmente os pedidos. Confirmou o pagamento das verbas rescisórias devidas "
                    "(aviso prévio indenizado, 13º proporcional, férias + 1/3, FGTS + 40%), mas negou o pedido de "
                    "danos morais por ausência de comprovação de conduta ilícita do empregador na dispensa."
                ),
                "chunks": [
                    {
                        "content": (
                            "RECLAMAÇÃO TRABALHISTA — O reclamante João Paulo Santos, brasileiro, casado, vendedor, "
                            "portador do CPF nº 987.654.321-00, CTPS nº 67890 série 002-RJ, residente na Rua Presidente "
                            "Vargas, nº 789, Bairro Centro, Rio de Janeiro/RJ, CEP 20040-020, vem propor a presente "
                            "reclamação trabalhista em face de LOJA ABC S.A., inscrita no CNPJ sob o nº 98.765.432/0001-10, "
                            "com sede na Av. Rio Branco, nº 500, Centro, Rio de Janeiro/RJ. O reclamante foi admitido em "
                            "02/01/2019, exercendo a função de vendedor, com salário base de R$ 2.200,00 mais comissões "
                            "sobre vendas. Foi dispensado sem justa causa em 30/06/2023, após 4 anos e 6 meses de contrato. "
                            "Na rescisão, a empresa não pagou integralmente as verbas rescisórias devidas, deixando de "
                            "quitar o aviso prévio indenizado proporcional ao tempo de serviço (art. 1º da Lei 12.506/2011), "
                            "as comissões do último mês trabalhado e os reflexos das comissões em DSR, férias e 13º salário."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 1,
                    },
                    {
                        "content": (
                            "DO AVISO PRÉVIO PROPORCIONAL: Conforme a Lei 12.506/2011, o aviso prévio será de 30 dias "
                            "acrescidos de 3 dias por ano de serviço. O reclamante laborou por 4 anos e 6 meses, fazendo "
                            "jus a 42 dias de aviso prévio (30 + 12 dias). A empresa pagou apenas 30 dias, deixando de "
                            "quitar os 12 dias adicionais, no valor de R$ 880,00. DAS COMISSÕES: O reclamante recebia "
                            "comissão de 3% sobre o total de vendas realizadas. No último mês (junho/2023), realizou "
                            "vendas no valor total de R$ 85.000,00, gerando comissão de R$ 2.550,00, que não foi incluída "
                            "no TRCT. As comissões possuem natureza salarial (art. 457, §1º, CLT) e devem integrar a base "
                            "de cálculo para DSR, férias + 1/3, 13º salário e FGTS, conforme Súmula 340 do TST. O total "
                            "de reflexos das comissões não pagas atinge aproximadamente R$ 15.000,00 ao longo do contrato."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 2,
                    },
                    {
                        "content": (
                            "DOS DANOS MORAIS: O reclamante alega que foi dispensado de forma vexatória perante os colegas "
                            "de trabalho. Na data da demissão, o gerente regional comunicou a dispensa na frente de todos os "
                            "funcionários da loja, em tom humilhante, dizendo que o reclamante 'não servia mais para a empresa' "
                            "e que 'precisava de gente que trabalhasse de verdade'. Tal conduta configura dano moral, nos "
                            "termos dos arts. 186 e 927 do Código Civil, causando constrangimento e abalo emocional ao "
                            "reclamante, que ficou abalado e precisou de acompanhamento psicológico. Pleiteia-se indenização "
                            "de R$ 15.000,00 por danos morais."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 3,
                    },
                    {
                        "content": (
                            "DOS PEDIDOS: Ante o exposto, requer: (a) diferenças de aviso prévio proporcional (12 dias); "
                            "(b) comissões do último mês trabalhado (R$ 2.550,00); (c) reflexos das comissões em DSR, "
                            "férias + 1/3, 13º salário e FGTS + 40%; (d) indenização por danos morais de R$ 15.000,00; "
                            "(e) multa do art. 477, §8º, da CLT, pelo atraso no pagamento das verbas rescisórias; "
                            "(f) honorários advocatícios sucumbenciais de 15% sobre o valor da condenação. Dá-se à causa "
                            "o valor de R$ 50.000,00. Requer a produção de prova testemunhal, documental e pericial."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 4,
                    },
                    {
                        "content": (
                            "CONTESTAÇÃO — LOJA ABC S.A.: A reclamada reconhece a relação de emprego e a dispensa sem "
                            "justa causa, porém impugna os valores pleiteados. Quanto ao aviso prévio, alega que pagou "
                            "integralmente os 30 dias devidos, conforme TRCT anexo. Desconhecia a obrigação de pagamento "
                            "proporcional, mas, subsidiariamente, não se opõe ao pagamento da diferença de 12 dias caso "
                            "este Juízo entenda devido. Quanto às comissões, alega que foram devidamente quitadas até "
                            "maio/2023 e que as vendas de junho/2023 não foram finalizadas antes da rescisão, gerando "
                            "estorno conforme política interna. Impugna integralmente o pedido de danos morais. A dispensa "
                            "foi comunicada de forma reservada, em sala fechada, com a presença apenas do gerente e do RH. "
                            "A empresa jamais admitiria conduta vexatória de seus gestores, possuindo código de ética e "
                            "canal de denúncias."
                        ),
                        "section": "contestacao",
                        "page_number": 5,
                    },
                    {
                        "content": (
                            "A reclamada junta aos autos cópia de seu código de ética e conduta (doc. 12), registro de "
                            "treinamentos sobre respeito no ambiente de trabalho (doc. 13) e declaração do setor de "
                            "recursos humanos atestando que a dispensa seguiu o protocolo interno (doc. 14). Requer que "
                            "as testemunhas do reclamante sejam ouvidas com cautela, pois podem ter interesse em prejudicar "
                            "a empresa. Subsidiariamente, caso o dano moral seja reconhecido, requer a fixação em valor "
                            "proporcional, não superior a R$ 3.000,00. Quanto à multa do art. 477, a empresa alega que "
                            "pagou as verbas rescisórias dentro do prazo de 10 dias, conforme comprovante de depósito "
                            "bancário (doc. 15). Requer a improcedência dos pedidos."
                        ),
                        "section": "contestacao",
                        "page_number": 6,
                    },
                    {
                        "content": (
                            "A reclamada argumenta ainda que o estorno das comissões de junho/2023 decorre de cláusula "
                            "contratual expressa (doc. 16 — contrato de trabalho, cláusula 8ª) que prevê que comissões "
                            "sobre vendas canceladas ou devolvidas no prazo de 30 dias são estornadas. Das vendas realizadas "
                            "pelo reclamante em junho/2023, no valor de R$ 85.000,00, houve devoluções de R$ 32.000,00, "
                            "restando comissões devidas sobre R$ 53.000,00 (R$ 1.590,00), valor que foi incluído no TRCT. "
                            "Protesta pela improcedência de todos os pedidos."
                        ),
                        "section": "contestacao",
                        "page_number": 7,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA 1ª TESTEMUNHA DO RECLAMANTE — Marcos Vinícius Pereira, brasileiro, solteiro, "
                            "vendedor, RG nº 33.444.555-6. Compromissado e advertido, inquirido, respondeu: que trabalhou "
                            "na reclamada de 2020 a 2023; que estava presente no dia da demissão do reclamante; que a "
                            "comunicação foi feita na área de vendas, na frente de outros funcionários; que ouviu o gerente "
                            "regional dizer em voz alta que o reclamante 'não tinha perfil' para continuar; que não se "
                            "recorda das palavras exatas, mas a situação foi constrangedora; que outros colegas comentaram "
                            "o episódio depois. Nada mais disse."
                        ),
                        "section": "depoimento",
                        "page_number": 8,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA TESTEMUNHA DA RECLAMADA — Patrícia Mendes Carvalho, brasileira, casada, "
                            "analista de RH, RG nº 66.777.888-9. Compromissada e advertida, inquirida, respondeu: que é "
                            "analista de RH da reclamada há 5 anos; que esteve presente na comunicação da dispensa do "
                            "reclamante; que a conversa ocorreu na sala de reuniões, em caráter privado; que apenas ela "
                            "e o gerente estavam presentes; que o gerente comunicou a decisão de forma profissional e "
                            "respeitosa; que o reclamante ficou visivelmente chateado mas saiu da sala normalmente; que "
                            "não houve qualquer manifestação pública sobre a demissão. Contradita pelo reclamante: "
                            "a testemunha é funcionária atual da reclamada. Depoimento mantido com ressalvas."
                        ),
                        "section": "depoimento",
                        "page_number": 9,
                    },
                    {
                        "content": (
                            "SENTENÇA: Processo nº 9876543-21.2023.5.01.0001. Vistos. Analiso os pedidos: "
                            "1) AVISO PRÉVIO PROPORCIONAL: Procedente. A Lei 12.506/2011 é clara ao prever acréscimo de "
                            "3 dias por ano de serviço. O reclamante faz jus a 42 dias (30 + 12). Devidas as diferenças "
                            "de 12 dias. 2) COMISSÕES: Parcialmente procedente. A cláusula contratual de estorno por "
                            "devoluções é válida. Contudo, as vendas efetivadas (R$ 53.000,00) geram comissão de R$ 1.590,00. "
                            "Verifico que o TRCT já contempla este valor. Improcedente a diferença pleiteada. Quanto aos "
                            "reflexos das comissões em DSR, férias e 13º, procedente, pois a empresa não comprovou a "
                            "integração regular das comissões nestas verbas."
                        ),
                        "section": "sentenca",
                        "page_number": 10,
                    },
                    {
                        "content": (
                            "3) DANOS MORAIS: Improcedente. As provas são conflitantes. A testemunha do reclamante afirmou "
                            "que a comunicação ocorreu na área de vendas, mas não recordou as palavras exatas. A testemunha "
                            "da reclamada afirmou que ocorreu em sala reservada. Não há prova robusta de que a dispensa "
                            "tenha ocorrido de forma vexatória. O ônus da prova do dano moral incumbe ao reclamante "
                            "(art. 818, I, CLT), do qual não se desincumbiu satisfatoriamente. 4) MULTA DO ART. 477: "
                            "Procedente. O comprovante de depósito (doc. 15) demonstra pagamento no 12º dia útil após "
                            "a dispensa, quando o prazo legal é de 10 dias. Devida a multa equivalente ao salário base."
                        ),
                        "section": "sentenca",
                        "page_number": 11,
                    },
                    {
                        "content": (
                            "DISPOSITIVO: Julgo PARCIALMENTE PROCEDENTES os pedidos para condenar a reclamada ao pagamento "
                            "de: (a) diferenças de aviso prévio proporcional (12 dias); (b) reflexos das comissões em DSR, "
                            "férias + 1/3, 13º salário e FGTS + 40%; (c) multa do art. 477, §8º, CLT. Improcedentes os "
                            "pedidos de diferenças de comissões de junho/2023 e danos morais. Valor arbitrado à condenação: "
                            "R$ 25.000,00. Custas pela reclamada no importe de R$ 500,00. Juros e correção conforme ADC 58 "
                            "do STF. Honorários sucumbenciais recíprocos: 10% sobre o valor dos pedidos procedentes a cargo "
                            "da reclamada, e 5% sobre o valor dos pedidos improcedentes a cargo do reclamante (suspensa a "
                            "exigibilidade, art. 791-A, §4º, CLT). Partes intimadas."
                        ),
                        "section": "sentenca",
                        "page_number": 12,
                    },
                ],
            },
            # ── Process 3: Ana Oliveira vs. Construtora DEF Ltda (assédio moral) ──
            {
                "name": "Ana Oliveira vs. Construtora DEF Ltda",
                "case_type": "trabalhista",
                "parties": {"plaintiff": "Ana Oliveira", "defendant": "Construtora DEF Ltda"},
                "status": "sentenciado",
                "sentence_summary": (
                    "Juiz condenou a empresa ao pagamento de indenização por danos morais de R$ 50.000,00 por "
                    "assédio moral comprovado. Também condenou ao pagamento de diferenças salariais por desvio "
                    "de função e rescisão indireta do contrato de trabalho com pagamento de todas as verbas rescisórias."
                ),
                "chunks": [
                    {
                        "content": (
                            "RECLAMAÇÃO TRABALHISTA — A reclamante Ana Carolina Oliveira, brasileira, divorciada, "
                            "engenheira civil, CPF nº 456.789.012-34, CTPS nº 11111 série 003-MG, residente na Rua "
                            "Minas Gerais, nº 123, Bairro Funcionários, Belo Horizonte/MG, CEP 30130-150, propõe a "
                            "presente ação em face de CONSTRUTORA DEF LTDA., CNPJ nº 45.678.901/0001-23, com sede na "
                            "Av. Afonso Pena, nº 3000, Centro, Belo Horizonte/MG. A reclamante foi admitida em 01/08/2018 "
                            "como engenheira civil, com salário de R$ 8.500,00 mensais. A partir de janeiro de 2022, passou "
                            "a sofrer assédio moral sistemático por parte de seu superior hierárquico, o diretor de obras "
                            "Sr. Ricardo Ferreira, após ter denunciado irregularidades na execução de uma obra pública "
                            "que poderiam comprometer a segurança estrutural do edifício."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 1,
                    },
                    {
                        "content": (
                            "DO ASSÉDIO MORAL: Após a denúncia interna realizada em dezembro de 2021, a reclamante passou "
                            "a sofrer as seguintes condutas por parte do Sr. Ricardo Ferreira: (a) foi removida de suas "
                            "funções de engenheira e designada para tarefas administrativas básicas, como organização de "
                            "arquivo e atendimento telefônico, configurando desvio de função; (b) foi transferida para "
                            "uma sala isolada, sem janela, no subsolo do escritório, longe dos demais colegas; (c) passou "
                            "a ser excluída de reuniões técnicas das quais sempre participava; (d) teve seu acesso ao "
                            "sistema de projetos revogado; (e) recebeu três advertências injustificadas em um período de "
                            "2 meses, por motivos fúteis como 'atraso de 2 minutos' e 'não uso de crachá no refeitório'; "
                            "(f) foi alvo de comentários depreciativos em reuniões, sendo chamada de 'engenheira de papel' "
                            "e 'delatora' na frente de colegas."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 2,
                    },
                    {
                        "content": (
                            "A conduta do superior hierárquico configura assédio moral organizacional, conforme definido "
                            "pela doutrina e jurisprudência trabalhista: trata-se de conduta reiterada, abusiva, que "
                            "atenta contra a dignidade e integridade psíquica do trabalhador, degradando o meio ambiente "
                            "de trabalho. A reclamante apresentou atestados médicos demonstrando o desenvolvimento de "
                            "quadro depressivo grave e síndrome do pânico (docs. 06 e 07), com necessidade de "
                            "afastamento por 60 dias pelo INSS (CAT emitida em 15/03/2022 — doc. 08). O nexo causal "
                            "entre o assédio e os problemas de saúde é evidente, conforme parecer do médico do trabalho "
                            "Dr. Paulo Mendes (doc. 09), que atestou que o quadro clínico é diretamente relacionado às "
                            "condições de trabalho hostis descritas pela paciente."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 3,
                    },
                    {
                        "content": (
                            "DO DESVIO DE FUNÇÃO: A reclamante foi contratada como engenheira civil (CBO 2142-05) com "
                            "salário de R$ 8.500,00. A partir de janeiro de 2022, passou a exercer funções de auxiliar "
                            "administrativo (CBO 4110-10), cujo piso salarial da categoria é de R$ 1.800,00. A empresa "
                            "manteve o salário de engenheira mas retirou as atribuições técnicas. O desvio de função "
                            "constitui alteração contratual ilícita, vedada pelo art. 468 da CLT. Além disso, a "
                            "manutenção da remuneração não afasta o dano, pois a degradação profissional e o "
                            "esvaziamento de funções configuram humilhação e perda de identidade profissional."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 4,
                    },
                    {
                        "content": (
                            "DA RESCISÃO INDIRETA: As condutas narradas configuram falta grave do empregador, nos termos "
                            "do art. 483, alíneas 'a', 'b' e 'd' da CLT: (a) exigência de serviços alheios ao contrato "
                            "(desvio de função); (b) tratamento com rigor excessivo (advertências injustificadas); "
                            "(d) descumprimento das obrigações do contrato (alteração unilateral ilícita). Requer-se a "
                            "declaração de rescisão indireta com pagamento de todas as verbas rescisórias como se "
                            "dispensa sem justa causa fosse: aviso prévio indenizado, saldo de salário, 13º proporcional, "
                            "férias + 1/3, FGTS + 40%, seguro-desemprego. DOS PEDIDOS: (a) rescisão indireta; "
                            "(b) indenização por danos morais de R$ 100.000,00; (c) diferenças salariais por desvio de "
                            "função; (d) verbas rescisórias integrais. Valor da causa: R$ 200.000,00."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 5,
                    },
                    {
                        "content": (
                            "CONTESTAÇÃO — CONSTRUTORA DEF LTDA.: A reclamada nega categoricamente as alegações de assédio "
                            "moral. O Sr. Ricardo Ferreira é profissional respeitado no mercado, com 25 anos de experiência "
                            "e jamais teve qualquer reclamação trabalhista em sua carreira. A reestruturação de funções "
                            "da reclamante decorreu de reorganização interna do departamento de engenharia, que reduziu "
                            "o número de obras em andamento e necessitou realocar profissionais. A transferência de sala "
                            "foi necessária por obras de reforma no andar principal. As advertências foram legítimas e "
                            "decorrem de infrações disciplinares comprovadas. A empresa não praticou qualquer conduta "
                            "ilícita e a denúncia da reclamante sobre irregularidades na obra foi devidamente apurada "
                            "pelo setor de compliance, que concluiu pela improcedência das alegações."
                        ),
                        "section": "contestacao",
                        "page_number": 6,
                    },
                    {
                        "content": (
                            "A reclamada impugna os atestados médicos apresentados, por serem emitidos por profissional "
                            "particular e não pelo médico da empresa. Requer a realização de perícia médica para aferição "
                            "do nexo causal. Quanto ao pedido de rescisão indireta, alega que não houve falta grave do "
                            "empregador. A reestruturação funcional é prerrogativa do poder diretivo (art. 2º, CLT) e "
                            "não configura alteração contratual ilícita quando mantida a remuneração. As advertências "
                            "estão documentadas e foram aplicadas conforme o regulamento interno. A empresa possui "
                            "programa de integridade e canal de denúncias, nunca tendo sido notificada de reclamações "
                            "contra o Sr. Ricardo Ferreira."
                        ),
                        "section": "contestacao",
                        "page_number": 7,
                    },
                    {
                        "content": (
                            "A reclamada apresenta ainda o relatório de compliance (doc. 20) que analisou a denúncia da "
                            "reclamante sobre irregularidades na obra e concluiu que os procedimentos construtivos "
                            "estavam dentro dos parâmetros técnicos. Alega que a reclamante, ao ter sua denúncia "
                            "considerada improcedente, passou a interpretar as legítimas ações gerenciais como "
                            "retaliação. Subsidiariamente, caso reconhecido algum dano, requer fixação proporcional "
                            "e razoável, não superior a R$ 10.000,00. Impugna o pedido de rescisão indireta e requer "
                            "a improcedência total da ação."
                        ),
                        "section": "contestacao",
                        "page_number": 8,
                    },
                    {
                        "content": (
                            "Ainda em contestação, a reclamada argumenta que o poder diretivo do empregador (art. 2º da "
                            "CLT) lhe confere a prerrogativa de organizar e dirigir a prestação de serviços, incluindo "
                            "a redistribuição de funções em caso de necessidade operacional. A reestruturação do "
                            "departamento de engenharia afetou outros profissionais além da reclamante, conforme "
                            "demonstram os documentos de realocação de pessoal (docs. 21 e 22). Requer a oitiva de "
                            "testemunhas para comprovar que o ambiente de trabalho era respeitoso e profissional."
                        ),
                        "section": "contestacao",
                        "page_number": 9,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA 1ª TESTEMUNHA DA RECLAMANTE — Juliana Martins Costa, brasileira, solteira, "
                            "arquiteta, RG nº 22.333.444-5. Compromissada e advertida, inquirida, respondeu: que trabalhou "
                            "na reclamada de 2019 a 2022; que era colega de departamento da reclamante; que presenciou "
                            "a mudança de tratamento após a denúncia sobre a obra; que o Sr. Ricardo passou a chamar "
                            "a reclamante de 'delatora' em reuniões; que a reclamante foi transferida para o subsolo "
                            "sem justificativa aparente, pois a reforma mencionada pela empresa nunca ocorreu no andar; "
                            "que outros colegas comentavam abertamente o isolamento sofrido pela reclamante; que a "
                            "depoente pediu demissão parcialmente por não concordar com o ambiente hostil que se instalou."
                        ),
                        "section": "depoimento",
                        "page_number": 10,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA 2ª TESTEMUNHA DA RECLAMANTE — Gustavo Henrique Alves, brasileiro, casado, "
                            "engenheiro civil, RG nº 55.666.777-8. Compromissado e advertido, inquirido, respondeu: "
                            "que trabalha na reclamada desde 2017; que era colega de equipe da reclamante; que confirma "
                            "que após a denúncia, a reclamante foi retirada de todos os projetos técnicos; que a sala "
                            "do subsolo era um depósito adaptado, sem ventilação adequada; que as advertências aplicadas "
                            "à reclamante chamaram atenção porque eram por motivos insignificantes que jamais geraram "
                            "advertências para outros funcionários; que não houve 'reestruturação do departamento' — "
                            "os outros engenheiros permaneceram em suas funções normais."
                        ),
                        "section": "depoimento",
                        "page_number": 11,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA 3ª TESTEMUNHA DA RECLAMANTE — Dr. Paulo Roberto Mendes, brasileiro, casado, "
                            "médico do trabalho, CRM-MG 54321. Ouvido como testemunha técnica, respondeu: que atendeu "
                            "a reclamante em março de 2022 quando foi encaminhada pela empresa para perícia; que "
                            "diagnosticou quadro de depressão grave e síndrome do pânico; que em sua avaliação médica, "
                            "o quadro é compatível com estresse ocupacional crônico decorrente de ambiente de trabalho "
                            "hostil; que a reclamante não possuía histórico prévio de transtornos psiquiátricos; que "
                            "emitiu CAT (Comunicação de Acidente de Trabalho) em 15/03/2022."
                        ),
                        "section": "depoimento",
                        "page_number": 12,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA TESTEMUNHA DA RECLAMADA — Luiz Fernando Ribeiro, brasileiro, casado, gerente "
                            "administrativo, RG nº 88.999.000-1. Compromissado e advertido, inquirido, respondeu: que é "
                            "gerente administrativo da empresa há 8 anos; que a reestruturação do departamento de engenharia "
                            "ocorreu porque duas obras foram suspensas; que a transferência de sala foi temporária enquanto "
                            "havia reforma; que as advertências seguiram o regulamento interno; que nunca presenciou "
                            "comentários depreciativos do Sr. Ricardo contra a reclamante; que a empresa tem canal de "
                            "denúncias e política contra assédio. Contradita pela reclamante: a testemunha trabalha em "
                            "departamento diferente e não teria conhecimento do dia a dia do setor de engenharia."
                        ),
                        "section": "depoimento",
                        "page_number": 13,
                    },
                    {
                        "content": (
                            "SENTENÇA: Processo nº 5432109-87.2023.5.03.0001. Vistos e examinados os autos. "
                            "DO ASSÉDIO MORAL: Restou robustamente comprovado nos autos que a reclamante foi vítima de "
                            "assédio moral perpetrado por seu superior hierárquico, Sr. Ricardo Ferreira, em retaliação "
                            "à denúncia de irregularidades em obra. Os depoimentos das testemunhas Juliana e Gustavo "
                            "foram coerentes, detalhados e convergentes, descrevendo com precisão o isolamento, "
                            "o esvaziamento de funções, as advertências desproporcionais e os comentários depreciativos. "
                            "A testemunha da reclamada, por trabalhar em departamento diverso, não possuía conhecimento "
                            "direto dos fatos e seu depoimento não foi suficiente para afastar as provas da reclamante. "
                            "A alegada 'reestruturação' não se sustenta, pois, conforme depoimento do engenheiro Gustavo, "
                            "os demais profissionais mantiveram suas funções inalteradas."
                        ),
                        "section": "sentenca",
                        "page_number": 14,
                    },
                    {
                        "content": (
                            "A conduta configura assédio moral por retaliação (whistleblower retaliation), modalidade "
                            "especialmente grave por atingir não apenas a vítima direta, mas por gerar efeito intimidatório "
                            "sobre demais empregados que eventualmente desejem denunciar irregularidades. O nexo causal "
                            "entre o assédio e os danos à saúde foi confirmado pelo médico do trabalho Dr. Paulo Mendes. "
                            "DA RESCISÃO INDIRETA: Reconheço a rescisão indireta do contrato de trabalho, nos termos do "
                            "art. 483, alíneas 'a', 'b' e 'd' da CLT, com pagamento de todas as verbas rescisórias "
                            "como se dispensa imotivada fosse."
                        ),
                        "section": "sentenca",
                        "page_number": 15,
                    },
                    {
                        "content": (
                            "CONDENO a reclamada ao pagamento de: (a) indenização por danos morais no valor de R$ 50.000,00 "
                            "(cinquenta mil reais), considerando a gravidade da conduta, o caráter retaliatório, a duração "
                            "do assédio (mais de 1 ano), os danos à saúde comprovados e a capacidade econômica da empresa; "
                            "(b) verbas rescisórias integrais da rescisão indireta: aviso prévio indenizado proporcional, "
                            "saldo de salário, 13º proporcional, férias + 1/3, FGTS + 40%, guias para seguro-desemprego; "
                            "(c) diferenças salariais não são devidas, pois o salário de engenheira foi mantido. Porém, "
                            "determino indenização adicional de R$ 5.000,00 pelo dano à identidade profissional decorrente "
                            "do esvaziamento de funções. Valor total da condenação: R$ 150.000,00. Custas de R$ 3.000,00 "
                            "pela reclamada. Honorários de 15% sobre a condenação."
                        ),
                        "section": "sentenca",
                        "page_number": 16,
                    },
                ],
            },
            # ── Process 4: Pedro Lima vs. Indústria GHI S.A. (horas extras — similar to Process 1) ──
            {
                "name": "Pedro Lima vs. Indústria GHI S.A.",
                "case_type": "trabalhista",
                "parties": {"plaintiff": "Pedro Lima", "defendant": "Indústria GHI S.A."},
                "status": "sentenciado",
                "sentence_summary": (
                    "Juiz condenou a empresa ao pagamento de horas extras excedentes da 8ª diária e 44ª semanal, "
                    "com adicional de 50%, reflexos legais e FGTS + 40%. Intervalo intrajornada suprimido também "
                    "reconhecido. Danos morais fixados em R$ 8.000,00. Valor total da condenação: R$ 95.000,00. "
                    "Fundamentação similar ao caso Maria Silva vs. Empresa XYZ (Súmula 338 TST, horários britânicos)."
                ),
                "chunks": [
                    {
                        "content": (
                            "RECLAMAÇÃO TRABALHISTA — O reclamante Pedro Henrique Lima, brasileiro, solteiro, operador "
                            "de máquinas, CPF nº 321.654.987-00, CTPS nº 54321 série 004-SP, residente na Rua São "
                            "João, nº 200, Bairro Liberdade, Campinas/SP, CEP 13015-100, propõe a presente reclamação "
                            "em face de INDÚSTRIA GHI S.A., CNPJ nº 56.789.012/0001-34, com sede na Rod. Anhanguera, "
                            "km 105, Distrito Industrial, Campinas/SP. O reclamante foi admitido em 10/06/2019, exercendo "
                            "a função de operador de máquinas, com salário mensal de R$ 2.500,00. Foi dispensado sem "
                            "justa causa em 15/09/2023. Durante todo o contrato, laborou em regime de sobrejornada "
                            "habitual, cumprindo jornada das 06h00 às 18h00, com apenas 30 minutos de intervalo, de "
                            "segunda a sábado, sem receber horas extras, em violação aos artigos 58 e 71 da CLT."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 1,
                    },
                    {
                        "content": (
                            "DOS FATOS: O reclamante trabalhava no setor de produção da fábrica, operando prensa "
                            "hidráulica e torno CNC. A jornada contratual era das 07h00 às 16h00 com 1 hora de "
                            "intervalo, porém o reclamante era obrigado a chegar às 06h00 para preparar as máquinas "
                            "(setup), verificar calibragem e aquecer os equipamentos, atividades indispensáveis para "
                            "o início da produção. Ao final do turno, o reclamante permanecia até 18h00 realizando "
                            "limpeza das máquinas, preenchimento de relatórios de produção e organização do setor "
                            "para o turno seguinte. O intervalo para almoço era de apenas 30 minutos, pois a "
                            "empresa determinava que os operadores deveriam estar de volta aos postos rapidamente "
                            "para não interromper a linha de produção. Registros de ponto eram marcados pelo "
                            "supervisor no horário contratual, e não no horário real de trabalho."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 2,
                    },
                    {
                        "content": (
                            "DO DIREITO — DAS HORAS EXTRAS: O reclamante laborava 12 horas por dia (das 06h00 às 18h00), "
                            "perfazendo 72 horas semanais, quando o limite legal é de 44 horas (art. 58, CLT). São "
                            "devidas 28 horas extras semanais. Com salário de R$ 2.500,00, a hora normal é de R$ 11,36 "
                            "(R$ 2.500,00 / 220h). Com adicional de 50% (art. 7º, XVI, CF/88), a hora extra vale "
                            "R$ 17,04. O débito mensal de horas extras é de aproximadamente R$ 2.064,84. Ao longo dos "
                            "51 meses de contrato (junho/2019 a setembro/2023), o total não pago atinge cerca de "
                            "R$ 105.306,84, sem reflexos e correção monetária. Requer-se também o pagamento dos "
                            "reflexos das horas extras em DSR, férias + 1/3, 13º salário e FGTS + 40%."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 3,
                    },
                    {
                        "content": (
                            "DO INTERVALO INTRAJORNADA E DANOS MORAIS: Aplica-se o mesmo fundamento: art. 71, §4º, CLT "
                            "e Súmula 437 do TST. Requer-se 1 hora extra diária pelo intervalo suprimido. Quanto aos "
                            "danos morais, a submissão a jornada de 12 horas em atividade de operação de máquinas "
                            "pesadas configura risco adicional à saúde e segurança do trabalhador. A fadiga excessiva "
                            "aumenta exponencialmente o risco de acidentes industriais. O reclamante sofreu um acidente "
                            "leve em agosto de 2022, quando sua mão foi atingida por peça metálica no final de um turno "
                            "de 12 horas, gerando afastamento de 15 dias. Pleiteia-se danos morais de R$ 15.000,00. "
                            "DOS PEDIDOS: horas extras + reflexos, intervalo intrajornada, danos morais. "
                            "Valor da causa: R$ 150.000,00."
                        ),
                        "section": "peticao_inicial",
                        "page_number": 4,
                    },
                    {
                        "content": (
                            "CONTESTAÇÃO — INDÚSTRIA GHI S.A.: A reclamada impugna integralmente os pedidos. Alega que "
                            "a jornada do reclamante era das 07h00 às 16h00 com 1 hora de intervalo, conforme registros "
                            "de ponto (docs. anexos). Não havia necessidade de preparação de máquinas antes do horário, "
                            "pois essa atividade é realizada por equipe específica de manutenção. A limpeza ao final do "
                            "turno é realizada em no máximo 15 minutos e está contemplada dentro do horário contratual. "
                            "Os registros de ponto são eletrônicos (sistema biométrico REP-P) e fidedignos. Eventuais "
                            "horas extras esporádicas foram devidamente pagas, conforme demonstram os contracheques "
                            "anexos (docs. 10 a 60)."
                        ),
                        "section": "contestacao",
                        "page_number": 5,
                    },
                    {
                        "content": (
                            "Quanto ao intervalo, a empresa possui refeitório e sala de descanso, com intervalo de 1 hora "
                            "respeitado. O acidente mencionado pelo reclamante foi devidamente registrado e comunicado "
                            "(CAT emitida), tendo sido causado por descuido do próprio trabalhador ao não utilizar o EPI "
                            "adequado, conforme relatório de investigação do acidente (doc. 61). Impugna os danos morais. "
                            "A empresa investiu R$ 2,5 milhões em segurança do trabalho nos últimos 3 anos, possui CIPA "
                            "atuante e PPRA/PCMSO em dia. Subsidiariamente, requer limitação das horas extras ao período "
                            "imprescrito e fixação de danos morais em valor não superior a R$ 2.000,00."
                        ),
                        "section": "contestacao",
                        "page_number": 6,
                    },
                    {
                        "content": (
                            "A reclamada ressalta que o setor de produção opera com supervisão constante e que os "
                            "funcionários são orientados a registrar corretamente seus horários no ponto biométrico. "
                            "Alega que o reclamante nunca reclamou sobre jornada durante o contrato, nem ao sindicato "
                            "nem à empresa. Requer a improcedência total. Protesta por prova testemunhal e documental."
                        ),
                        "section": "contestacao",
                        "page_number": 7,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA 1ª TESTEMUNHA DO RECLAMANTE — Anderson Luiz de Souza, brasileiro, casado, "
                            "operador de máquinas, RG nº 77.888.999-0. Compromissado e advertido, inquirido, respondeu: "
                            "que trabalhou na reclamada de 2018 a 2023; que trabalhava no mesmo setor do reclamante; "
                            "que a jornada real era das 06h00 às 18h00; que a preparação das máquinas era feita pelos "
                            "próprios operadores, não por equipe de manutenção; que o supervisor mandava registrar o "
                            "ponto apenas no horário contratual; que o sistema biométrico só liberava o registro nos "
                            "horários programados pelo supervisor; que o intervalo de almoço era de 30 minutos porque "
                            "a produção não podia parar; que também não recebia horas extras. Nada mais disse."
                        ),
                        "section": "depoimento",
                        "page_number": 8,
                    },
                    {
                        "content": (
                            "DEPOIMENTO DA TESTEMUNHA DA RECLAMADA — José Carlos Ferreira, brasileiro, casado, supervisor "
                            "de produção, RG nº 44.555.666-7. Compromissado e advertido, inquirido, respondeu: que é "
                            "supervisor de produção há 10 anos; que a jornada dos operadores é das 07h00 às 16h00 com "
                            "1 hora de intervalo; que a preparação de máquinas é feita pela equipe de manutenção no turno "
                            "da noite; que os operadores registram o ponto normalmente pelo sistema biométrico; que "
                            "nunca orientou funcionários a registrar ponto em horário diferente do real; que eventuais "
                            "horas extras são autorizadas por ele e registradas em sistema. Contradita pelo reclamante: "
                            "a testemunha é o supervisor mencionado que supostamente manipulava os registros de ponto. "
                            "Depoimento mantido com ressalvas."
                        ),
                        "section": "depoimento",
                        "page_number": 9,
                    },
                    {
                        "content": (
                            "SENTENÇA: Processo nº 6789012-34.2023.5.15.0001. Vistos. DAS HORAS EXTRAS: A controvérsia "
                            "central reside na jornada efetivamente cumprida pelo reclamante. Os registros de ponto "
                            "apresentados pela reclamada contêm horários invariáveis (britânicos) — entrada sempre às "
                            "07h00 e saída sempre às 16h00, sem qualquer variação ao longo de 51 meses. Aplica-se "
                            "a Súmula 338, III, do TST: os cartões de ponto que demonstram horários de entrada e saída "
                            "uniformes são inválidos como meio de prova, invertendo-se o ônus da prova quanto à jornada "
                            "alegada. A testemunha Anderson Luiz prestou depoimento coerente e detalhado, confirmando "
                            "a jornada das 06h00 às 18h00 e a manipulação do sistema de ponto pelo supervisor. A "
                            "testemunha da reclamada, sendo o próprio supervisor acusado de manipulação, teve seu "
                            "depoimento valorado com severas ressalvas."
                        ),
                        "section": "sentenca",
                        "page_number": 10,
                    },
                    {
                        "content": (
                            "Registro importante: o padrão fático deste caso é notavelmente similar ao processo "
                            "nº 1234567-89.2023.5.02.0001 (Maria Silva vs. Empresa XYZ Ltda), julgado recentemente "
                            "por esta Vara, no qual igualmente se constatou a prática de horários britânicos nos cartões "
                            "de ponto e jornada extraordinária habitual não registrada. A recorrência desse padrão em "
                            "diferentes empresas reforça a necessidade de condenações que efetivamente desestimem a "
                            "prática de fraude nos registros de jornada."
                        ),
                        "section": "sentenca",
                        "page_number": 11,
                    },
                    {
                        "content": (
                            "CONDENO a reclamada ao pagamento de: (a) horas extras excedentes da 8ª diária e 44ª semanal, "
                            "com adicional de 50%, conforme art. 7º, XVI, CF/88, e reflexos em DSR, férias + 1/3, "
                            "13º salário e FGTS + 40%; (b) 1 hora extra diária referente ao intervalo intrajornada "
                            "suprimido (art. 71, §4º, CLT); (c) indenização por danos morais no valor de R$ 8.000,00 "
                            "(oito mil reais), pela submissão a jornada extenuante em atividade de risco com máquinas "
                            "pesadas, contribuindo para o acidente ocorrido. Valor total da condenação: R$ 95.000,00. "
                            "Custas de R$ 1.900,00 pela reclamada. Juros e correção conforme ADC 58 do STF. Honorários "
                            "de 10% sobre a condenação. Partes intimadas."
                        ),
                        "section": "sentenca",
                        "page_number": 12,
                    },
                ],
            },
        ]
    }
