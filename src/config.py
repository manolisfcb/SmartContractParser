import os
from dotenv import load_dotenv, find_dotenv
from urllib.parse import quote


# carrega .env.local caso exista
base_path = os.path.abspath(os.path.dirname(__file__))
local_env_path = os.path.join(base_path, '.env')
if os.path.isfile(local_env_path):
    load_dotenv(find_dotenv(local_env_path))
else:
    load_dotenv(find_dotenv())


class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "xxx"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = os.getenv("DEBUG")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    ENV = os.getenv("ENV")
    TESTING = False

    # caminhos padrão
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    MINUTA_PATH = os.path.join(BASE_PATH, 'docs', 'arquivos_modelo','qualificacao.txt')
    RESOURCES_PATH = os.path.join(BASE_PATH, 'resources')
    
    PATH_TO_ZIP = os.path.join(BASE_PATH, 'database', 'ia_contratos_paragrafos.zip')
    PATH_TO_CSV = os.path.join(BASE_PATH, 'database')
    
    ASPOSE_LICENSE = os.path.join(BASE_PATH, 'Aspose.Words.Python.NET.lic')
    NLTK_DATA_PATH = os.path.join(BASE_PATH, 'nltk_data')
    DEBENTURE_DATA_PATH = os.path.join(BASE_PATH, 'resources', 'debentures_data')
    STORAGE_PATH = os.path.join(RESOURCES_PATH, 'storage')
    
    NER_MODEL = os.path.join(BASE_PATH, 'ner_model', 'pt_core_news_sm-3.4.0')
    SUBPRODUTO_MODEL = os.path.join(BASE_PATH, 'ml-models', 'modelo-subproduto-RF.joblib')
    PRODUTO_MODEL = os.path.join(BASE_PATH, 'ml-models', 'modelo-produto-RF.joblib')
    CLASSIFICATION_MODEL = os.path.join(BASE_PATH, 'ml-models', 'class-model')
    

    CACHE_DIR = os.path.join(BASE_PATH, 'ml-models')
    AMOSTRA_PARAGRAFOS = os.path.join(BASE_PATH, 'resources', 'helpers', 'similaridade', 'paragrafos_validados.pkl')
    
    RETRAIN_ESTRUTURA_MODEL = os.path.join(BASE_PATH, 'data_retrain_classif_estrutura/classificador_estructura.csv')
    RETRAIN_CLASSIFICATION_MODEL = os.path.join(BASE_PATH, 'data_to_retrain_linearsvc_topicos')
    API_NAME = 'api-ia-contratos'
    #GRAYLOG_HOST = os.getenv("GRAYLOG_HOST")
    
    # aws
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    REGION_NAME = os.getenv("REGION_NAME")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
    AWS_PREFIX = os.getenv("AWS_PREFIX")
    
    # caminho para salvar os arquivos
    DOCX_UPLOADS = os.path.join(RESOURCES_PATH, 'storage', 'arquivos')
    ARQUIVOS_MODIF = os.path.join(RESOURCES_PATH, 'storage', 'arquivos_modificados')
    TMP_DIR = os.path.join(BASE_PATH, 'temp')
    ARQUIVOS_PERMITIDOS = ["DOCX", "docx", "Docx"]  # extenções permitidas para fazer upload

    SQLALCHEMY_DATABASE_URI =  f'mysql+pymysql://{os.getenv("API_IA_CONTRATOS_DB_USERNAME")}:%s@{os.getenv("API_IA_CONTRATOS_DB_HOST")}:3306/{os.getenv("API_IA_CONTRATOS_DB_DATABASE")}' % quote(f'{os.getenv("API_IA_CONTRATOS_DB_PASSWORD")}')
    #SQLALCHEMY_DATABASE_URI =  f"sqlite:///{os.path.join(BASE_PATH, 'database', 'sqlite.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SESSION_COOKIE_SECURE = False

    # api armazenamento
    API_ARMAZENAMENTO_URL = os.getenv("API_ARMAZENAMENTO_URL")
    
    # keycloak
    KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
    KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")
    KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
    KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")
    #KEYCLOAK_CLIENT_SECRET = 'GIAef0wSJ1rpIwnih3ci5x4bi4qCTkMD'
    #KEYCLOAK_URL ='https://keycloak.dev.otfin.tools/'
    #KEYCLOAK_REALM='Restrito'
    #KEYCLOAK_CLIENT_ID='api-contratos'   
    
    KEYCLOAK_ACCESS_TOKEN_URL = f'{KEYCLOAK_URL}auth/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token' 
    #print(f"{KEYCLOAK_ACCESS_TOKEN_URL}")
    #print(f"{KEYCLOAK_CLIENT_ID} ===== {KEYCLOAK_CLIENT_SECRET}")
    LOG_SERVER_HOST= 'graylogotrj01.scot.oliveiratrust.com'
    LOG_SERVER_PORT=3435
    LOG_SERVER_PROTOCOL= 'udp'
    
    # flags
    CALLBACK_SUCCESS = True
    TEM_QUE_RETREINAR = False
    LAST_RESPONSE = []
class TestingConfig(Config):
    TESTING = True
