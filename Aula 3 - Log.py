import logging

# https://docs.python.org/3/library/logging.html
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="app.log", level=logging.DEBUG, format=LOG_FORMAT) # adicional info
# logging.basicConfig(filename="app.log", level=logging.DEBUG, filemode ="w") #sobrescreve info

log = logging.getLogger()

log.debug("Teste1")
log.info("Teste2")
log.critical("Teste3")
log.error("Teste4")
log.warning("Teste5")
