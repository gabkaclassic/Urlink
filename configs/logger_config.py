import logging

logging.basicConfig(
    level=logging.WARNING,
    filename='logs/error.log',
    filemode='w',
    format="%(levelname)s |--| %(asctime)s |--| %(message)s"
)



