import logging

from src.pipeline import Pipeline


FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename='result.log', format=FORMAT, level=logging.INFO)


def main():
    pipe = Pipeline()
    pipe.run()


if __name__ == '__main__':
    try:
        main()
        logging.info("OK")
    except Exception as e:
        logging.exception(e)
        logging.info("Erro")
