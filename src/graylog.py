import logging
import json
from gelfclient import UdpClient

class GraylogHandler(logging.Handler):
    def __init__(self, host, port, hostname, facility):
        super().__init__()
        self.gelf_client = UdpClient(host, port)
        self.hostname = hostname
        self.facility = facility
    
    def emit(self, record):
        try:
            message = self.format(record)
            gelf_message = {
                'version': '1.1',
                'host': self.hostname,
                'short_message': message,
                'timestamp': record.created,
                'level': self.map_log_level(record.levelno),
                'facility': self.facility
            }
            self.gelf_client.log(**gelf_message)
        except Exception as e:
            self.handleError(record)

    def map_log_level(self, level):
        # Mapeia os níveis de log do Python para os níveis de log GELF
        if level >= logging.CRITICAL:
            return 2
        elif level >= logging.ERROR:
            return 3
        elif level >= logging.WARNING:
            return 4
        elif level >= logging.INFO:
            return 6
        else:
            return 7


def configura_logger(graylog_host, graylog_port, graylog_hostname, facility):

# Configuração do logger
    logger = logging.getLogger('graylog_logger')
    logger.setLevel(logging.INFO)

    # Configuração do manipulador GELF
    gelf_handler = GraylogHandler(graylog_host, graylog_port, graylog_hostname, facility)
    gelf_handler.setFormatter(logging.Formatter('%(message)s'))  # Formato GELF
    
        
    # Adiciona o manipulador ao logger
    logger.addHandler(gelf_handler)
    logger.info(f'CONECTANDO AO GRAYLOG facility: {facility} hostname: {graylog_hostname} host: {graylog_host} port: {graylog_port}')

    return logger