from loguru import logger
import argparse
import etl


def main():
    logger.debug("starting")
    logger.warning(f"version: {etl.get_version()}")
    logger.warning(f"version metadata: {etl.get_version_metadata()}")
    logger.debug("finished")


def display_version():
    print(f"{etl._package_name_}")
    print(f"version: {etl.get_version()}")
    print(f"version metadata: {etl.get_version_metadata()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', help="display version", action="store_true")

    args = parser.parse_args()
    if args.version:
        display_version()
    else:
        main()
