import seqlog
import logging

seqlog.log_to_seq(
   server_url="http://seq:5341",
   level=logging.INFO,
   batch_size=10,
   auto_flush_timeout=1,  # seconds
   override_root_logger=True,
)

def info(str):
    logging.info(str)
    
def error(str):
    logging.error(str)
    
def exception(str):
    logging.exception(str)

def warn(str):
    logging.warning(str)