from datetime import datetime
import logging
import os

def setup_logger():
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'ops-logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, f'fiber_ops_{datetime.now().strftime("%Y%m%d")}.log')
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger('pml-fiber-tracker')
