from .base_task import BaseTask

class Task3(BaseTask):
    def __init__(self, config_service):
        super().__init__(config_service)
        
    def run(self):
        ...