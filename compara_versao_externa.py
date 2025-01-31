
from flask_restful import Resource
from flask import request, current_app, jsonify, make_response
from resources.services.api_armazenamento import Api_armazenamento
from resources.jobs.JobCreator import CompararVersaoExternaJob, JobManager

import io

from app import logger
class CompararVersaoExterna(Resource):
    def get(self):
        try:
            logger.info('Iniciando comparación de versiones externas')
            success = False  
            payload = request.get_json()
            callback_url = payload.get('callback_url', None)      
            uid_antigo = payload['antigo_armazenamento_uid']
            uid_novo = payload['novo_armazenamento_uid']  
            aditivo = payload['aditivo']

            if current_app.config['ENV'] != 'prod':
                token = request.headers.get('Authorization') # Obter token do header se não estiver em produção
            else:
                token = None # Se estiver em produção, não enviar token
            
            job_type = CompararVersaoExternaJob(
                info = {'callback_url': callback_url,
                        'uid_antigo': uid_antigo,
                        'aditivo': aditivo,
                        'armazenamento_uid': uid_novo}, 
                uid_armazenamento= uid_novo)
            
            new_job = JobManager().create_job(job_type)
            new_job.run_job(token)
            return make_response(jsonify({'message': f'Job  criado', 'success': True, 'data': []}), 200)
        except Exception as e:
            return make_response(jsonify({'message': 'Não foi possivel fazer a comparação','motivo': f'{str(e)}', 'success': False}), 400)
