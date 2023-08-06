import logging

logging.basicConfig(level=logging.INFO)  # noqa
# logging.basicConfig(level=logging.DEBUG)  # noqa
LOGGER = logging.getLogger(__name__)

MDS_FILE_ENV_NAME = "MDS_FILE"
MDS_SECTION_ENV_NAME = "MDS_SECTION"
MDS_HOST_ENV_NAME = "MDS_HOST"
MDS_ACCESS_TOKEN_ENV_NAME = "MDS_ACCESS_TOKEN"

MDS_FILE_ENV_DEFAULT_VALUE = "./mds_config.yaml"
MDS_SECTION_ENV_DEFAULT_VALUE = "mds"
MDS_CONFIG_FILE_MDS_HOST = "mds_host"
MDS_CONFIG_FILE_MDS_ACCESS_TOKEN = "mds_access_token"

NUMBER_OF_CONNECTION_ATTEMPTS = 3
SECONDS_OF_SLEEP_BETWEEN_REQUESTS = 5

SIZE_CHUNK_DOWNLOAD_FILE = 1024 ** 2
