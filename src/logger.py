import logging
import os

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.v2.model.http_log import HTTPLog
from datadog_api_client.v2.model.http_log_item import HTTPLogItem


class DataDogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.dd: ApiClient = ApiClient(Configuration(
            api_key={
                "apiKeyAuth": os.environ['DD_API_KEY'],
                "appKeyAuth": os.environ['DD_APP_KEY']
            },
            server_variables={
                "site": "datadoghq.eu"
            }
        ))
        self.log = LogsApi(self.dd)

    def emit(self, record):
        log_entry = self.format(record)
        body = HTTPLog(
            [
                HTTPLogItem(
                    ddsource="automatic-turret-gut",
                    ddtags="env:prod",
                    hostname="pi",
                    message=log_entry,
                    service="automatic-turret-gut",
                    status=record.levelname,
                ),
            ]
        )
        response = self.log.submit_log(body=body)
        if len(response) > 0:
            print(response)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
data_dog_handler = DataDogHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
data_dog_handler.setFormatter(formatter)
logger.addHandler(data_dog_handler)

