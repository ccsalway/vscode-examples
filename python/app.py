import logging
import os
import time
import boto3

logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().handlers[0].setFormatter(
    logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s", "%Y-%m-%dT%H:%M:%S.%sZ"))
logging.Formatter.converter = time.gmtime  # utc time


sts = boto3.client('sts')


def main(name):
    # for k, v in os.environ.items():
    #     print(f"{k}={v}")
    logging.info(f"Hello, {name}!")
    logging.info(sts.get_caller_identity())


if __name__ == "__main__":
    main("World")
