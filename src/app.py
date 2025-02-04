from graylog import configura_logger

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from db import db
from models import *
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)


# Configuração do Graylog
graylog_host = app.config['LOG_SERVER_HOST']
graylog_port = app.config['LOG_SERVER_PORT']
graylog_hostname = 'API-IA-CONTRATOS'
graylog_facility = app.config['ENV']
logger = configura_logger(graylog_host, graylog_port, graylog_hostname, graylog_facility)
logger.info('Iniciando API IA Contratos')


cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)
db.init_app(app)

# @app.before_first_request   
# def create_tables():
#     db.create_all()


# nlp = spacy.load(app.config['NER_MODEL'])
from resources.populate_db import PopulateDB
from resources.teste import Teste
from resources.read_docx import LeituraDocx
# from resources.read_docx_paragrafos import LeituraDocxParagrafos
# from resources.read_docx_tabelas import LeituraDocxTabelas
from resources.retrainClassifClauses import retrainStructure
from resources.retrainTopicClassifier import RetrainTopicClassifier
from resources.resumo import Resumo
from resources.StatusController import StatusController
from resources.compara_versao_externa import CompararVersaoExterna
from resources.compara_versao_interna import CompararVersaoInterna
from resources.FileHandler import FileHandler
from resources.obter_env_variaveis import url
from resources.JobsController import JobsController
from resources.ContratoController import ContratosController
# from resources.get_contract_from_api_armazenamento import get_contract
from resources.classifica_subproduto import ClassificaSubProduto
from resources.classifica_produto import ClassificaProduto
from resources.alambic_controller import Alambic
@app.route("/", methods=["GET"])
def Home():
    import socket
    #Get the hostname/IP of the container
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f"Hello World! I am running on  with IP: {ip_address}, and my hostname is: {hostname}! "



api.add_resource(Alambic, '/alambic')
api.add_resource(Teste, '/teste')
api.add_resource(LeituraDocx,'/leitura_docx')
# api.add_resource(LeituraDocxParagrafos,'/leitura_docx_paragrafos')
# api.add_resource(LeituraDocxTabelas,'/leitura_docx_tabelas')
# api.add_resource(get_contract,'/get_contract')
api.add_resource(PopulateDB,'/populate')
api.add_resource(StatusController,'/status')
api.add_resource(JobsController,'/jobs')
api.add_resource(FileHandler,'/file_handler')
api.add_resource(retrainStructure,'/retrain_classificador')
api.add_resource(RetrainTopicClassifier,'/treinar_classificador_topicos')
api.add_resource(Resumo,'/resumo')
api.add_resource(ContratosController,'/contratos')
api.add_resource(CompararVersaoExterna,'/comparar_versao_externa')
api.add_resource(CompararVersaoInterna,'/comparar_versao_interna')
api.add_resource(url,'/url_armazenamento')
api.add_resource(ClassificaSubProduto, '/classificar_subproduto')
api.add_resource(ClassificaProduto, '/classificar_produto')
# api.add_resource(EstruturarDocx,'/estruturar_docx')



import gc
gc.collect()

from flask import jsonify        
from sqlalchemy import text
from resources.jobs.JobCreator import JobManager
from threading import Thread

with app.app_context():
    try:
        status = Status.query.all()
        status = {x.nome: x.status_uid for x in status}
        # Busca todos os jobs que estão em execução
        em_execucao = Jobs.query.\
            filter_by(status_uid_job=status['EM_EXECUCAO']).all() 
        
        if len(em_execucao) > 0:
            # Atualiza o status dos jobs para 'AGUARDANDO_FILA'
            for job in em_execucao:
                logger.info(f'Reiniciando validação do job {job.id}')
                job.status_uid_job = status['AGUARDANDO_FILA']
                db.session.commit()
                print(f'Job {job.id} reiniciado com sucesso!')
            print('Todos os jobs em execução foram reiniciados com sucesso!')
            # Reinicia a validação
            job_manager = JobManager()
            Thread(target=job_manager.run_pending_jobs, args=(None,)).start()
            


        
    except Exception as e:
        print(str(e))
        





# @app.route('/migrate', methods=['POST'])
# def migrate():
#     try:
        
#         # Create index for column classes in paragrafos_validados
#         db.session.execute(text('CREATE INDEX paragrafos_validados_classe_IDX USING BTREE ON api_ia_contratos.paragrafos_validados (classe,similaridade)'))
        
        
#         #eliminar todas as informaçoes da tabela jobs
#         # Jobs.query.delete()
#         # db.session.commit()
        
#         # #eliminar tabela jobs
#         # db.session.execute(text('DROP TABLE IF EXISTS jobs'))
#         # db.create_all()
        
#         # logger.info('Tabela jobs deletada com sucesso!')        
#         # #Ejecuta el comando flask db init
#         # try:
#         #     logger.info('Iniciando init e atualização da base de dados.')
#         #     subprocess.run(['flask', 'db', 'init'])
#         # except:
#         #     pass
        
#         # logger.info('Iniciando migração da base de dados.')
#         # # Ejecuta el comando flask db migrate
#         # subprocess.run(['flask', 'db', 'migrate'])
        
#         # logger.info('Iniciando atualização da base de dados.')

#         # # Ejecuta el comando flask db upgrade
#         # #subprocess.run(['flask', 'db', 'upgrade'])
#         # mess = subprocess.run(['flask', 'db', 'upgrade'], capture_output=True, text=True)
        
#         # print(mess.stdout)
        
#         # logger.info(mess.stdout)
#         return jsonify({'message': 'Migración y actualización de la base de datos completadas exitosamente.'}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)