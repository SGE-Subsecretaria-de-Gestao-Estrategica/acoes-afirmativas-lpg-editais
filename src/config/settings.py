import os
from pathlib import Path

from dotenv import load_dotenv

# CAMINHO DOS DIRETÓRIOS
ROOT = Path(__file__).resolve().parents[2] # PASTA RAÍZ DO PROJETO
load_dotenv(ROOT / ".env")
load_dotenv(ROOT / "src" / ".env")

DATA_PATH = ROOT / "data"                   # dados (fora do repositório)
INTERIM_DATA_PATH = DATA_PATH / "interim"   # versões intermediárias do pipeline
FINAL_DATA_PATH = DATA_PATH / "final"       # resultados finais


# LPG - LEI PAULO GUSTAVO
LPG_PDF_ROOT = DATA_PATH / 'EDITAIS'            # data/EDITAIS/{Capitais,Estados}/<ente>/*.pdf
LPG_NOVOS_ROOT = DATA_PATH / 'NOVOS'              # editais avulsos: NOVOS/<pasta>/*.pdf (ente pelo nome do arquivo)
LPG_INTERIM = INTERIM_DATA_PATH / 'LPG'
LPG_MD_ROOT = LPG_INTERIM / 'MD'                # editais convertidos para Markdown
LPG_PDF_COMPRIMIDO = LPG_INTERIM / 'PDF_ESCANEADO'  # escaneados recomprimidos para envio
LPG_MANIFESTO = LPG_INTERIM / 'manifesto.csv'   # 1 linha por edital (ente, arquivo, modo, tokens)
LPG_LLM_RAW = LPG_INTERIM / 'llm_raw'           # JSON bruto por edital (cache/retomada)
LPG_GASTOS = LPG_INTERIM / 'gastos.csv'         # gasto real por chamada
LPG_BATCHES = LPG_INTERIM / 'batches.csv'       # batches enviados
LPG_OUTPUT = FINAL_DATA_PATH / 'lpg_editais.xlsx'

# Endereço da pasta 'ações afirmativas' no SharePoint/OneDrive (sem barra no fim), para links absolutos
# na planilha de avaliação. Vazio = links relativos (../editais/...). Definido em src/.env.
SHAREPOINT_PASTA_URL = os.getenv('SHAREPOINT_PASTA_URL', '')

MIN_CHARS_POR_PAGINA = 200  # abaixo disso o PDF é tratado como escaneado

# MODELO
MODEL_ID = 'claude-sonnet-5-5'
EFFORT = 'medium'
MAX_TOKENS = 8000
PROMPT_VERSION = 'lpg-v2'  # v1: piloto; v2: retificações completas = edital, PDFs com vários editais

# ORÇAMENTO (US$) - teto rígido somando todas as etapas
ORCAMENTO_USD = 40.0
PRECOS_USD_POR_MTOK = {  # preço padrão; o Batch API cobra 50%
    'claude-sonnet-5-5': {'input': 2.00, 'output': 10.00},
}
MULT_CACHE = {'escrita': 1.25, 'leitura': 0.10}  # sobre o preço de input
DESCONTO_BATCH = 0.5

# IN MinC nº 5/2023, art. 5º
COTA_MIN = {'negras': 0.20, 'indigenas': 0.10}  # caput: percentual mínimo de vagas por grupo
COTA_TOL = 1e-9  # tolerância para comparar floats (0.2 lido como 0.19999...)


# CÓDIGOS IBGE (preenchem cod_ibge na planilha final)
MAP_ESTADOS_IBGE = {
    "ACRE": "12",
    "ALAGOAS": "27",
    "AMAPA": "16",
    "AMAZONAS": "13",
    "BAHIA": "29",
    "CEARA": "23",
    "DISTRITO FEDERAL": "53",
    "ESPIRITO SANTO": "32",
    "GOIAS": "52",
    "MARANHAO": "21",
    "MATO GROSSO": "51",
    "MATO GROSSO DO SUL": "50",
    "MINAS GERAIS": "31",
    "PARA": "15",
    "PARAIBA": "25",
    "PARANA": "41",
    "PERNAMBUCO": "26",
    "PIAUI": "22",
    "RIO DE JANEIRO": "33",
    "RIO GRANDE DO NORTE": "24",
    "RIO GRANDE DO SUL": "43",
    "RONDONIA": "11",
    "RORAIMA": "14",
    "SANTA CATARINA": "42",
    "SAO PAULO": "35",
    "SERGIPE": "28",
    "TOCANTINS": "17"
}

MAP_CAPITAIS_IBGE = {
    "ARACAJU": "2800308",
    "BELEM": "1501402",
    "BELO HORIZONTE": "3106200",
    "BOA VISTA": "1400100",
    "CAMPO GRANDE": "5002704",
    "CUIABA": "5103403",
    "CURITIBA": "4106902",
    "FLORIANOPOLIS": "4205407",
    "FORTALEZA": "2304400",
    "GOIANIA": "5208707",
    "JOAO PESSOA": "2507507",
    "MACAPA": "1600303",
    "MACEIO": "2704302",
    "MANAUS": "1302603",
    "NATAL": "2408102",
    "PALMAS": "1721000",
    "PORTO ALEGRE": "4314902",
    "PORTO VELHO": "1100205",
    "RECIFE": "2611606",
    "RIO BRANCO": "1200401",
    "SALVADOR": "2927408",
    "SAO LUIS": "2111300",
    "SAO PAULO (CAPITAL)": "3550308",
    "TERESINA": "2211001",
    "VITORIA": "3205309",
    "RIO DE JANEIRO (CAPITAL)": "3304557"
}
