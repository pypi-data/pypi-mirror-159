import insights_python_client
from insights_python_client import Configuration

from python_sdk_client.libs.abstract_client import AbstractClient
from python_sdk_client.libs.batch_processor import handle
from python_sdk_client.libs.client_cfg import InsightServiceCfg
from python_sdk_client.clients_enum import EnvType

"""
Insights Service Client
-----------------------

class to validate the inputs and set the env, endpoint and other env specific details.
"""


class InsightServiceClient(AbstractClient):
    """
    Initialising the env and base url
    """

    def __init__(self, tenant: str, username: str, password: str, env: EnvType) -> None:
        super(InsightServiceClient, self).__init__(tenant, username, password, env)

        self.tenant_type = 'SMARTFARM_PLUS'
        if env == EnvType.PROD:
            self.base_url = InsightServiceCfg.PROD_BASE_URL
        elif env == EnvType.QA:
            self.base_url = InsightServiceCfg.QA_BASE_URL

        self.configuration = Configuration()
        # set base url
        self.configuration.host = self.base_url
        # set auth token
        self.configuration.api_key['Authorization'] = self.token

    """
    Validate input for fetching plot details
    """

    def get_plot_details(self, plot_ids: str, **kwargs):

        boundary_api = insights_python_client.PlotApi(insights_python_client.ApiClient(self.configuration))
        plot_ids_resp = handle(boundary_api.list_all3, plot_ids, self.tenant_type, self.x_api_key, self.org_id,
                               batch_size=InsightServiceCfg.BATCH_SIZE, **kwargs)
        return plot_ids_resp

    """
    Validate inputs for satellite details
    """

    def get_satellite_details(self, plot_ids: str, **kwargs):

        metrics_api = insights_python_client.MetricsApi(insights_python_client.ApiClient(self.configuration))
        plot_ids_resp = handle(metrics_api.list_all2, plot_ids, self.tenant_type, self.x_api_key, self.org_id,
                               batch_size=InsightServiceCfg.BATCH_SIZE, **kwargs)
        return plot_ids_resp

    """
    Validate inputs for weather details
    """

    def get_weather_details(self, plot_ids: str, **kwargs):

        weather_api = insights_python_client.WeatherApi(insights_python_client.ApiClient(self.configuration))
        weather_api_resp = handle(weather_api.list_all1, plot_ids, self.tenant_type, self.x_api_key, self.org_id,
                                  batch_size=InsightServiceCfg.BATCH_SIZE, **kwargs)
        return weather_api_resp

    """ 
    Validate inputs for yield details
    """

    def get_yield_details(self, plot_ids: str, **kwargs):
        yield_api = insights_python_client.YieldApi(insights_python_client.ApiClient(self.configuration))
        yield_api_resp = handle(yield_api.list_all, plot_ids, self.tenant_type, self.x_api_key, self.org_id,
                                batch_size=InsightServiceCfg.BATCH_SIZE, **kwargs)
        return yield_api_resp

    """
    Validate inputs for download plot image
    """

    def download_image(self, plot_id: str, image_name, image_type, date):
        download_api = insights_python_client.FileApi(insights_python_client.ApiClient(self.configuration))
        file_response = download_api.get_plot_image_for_satellite_and_health_indices(self.tenant_type, self.x_api_key,
                                                                                     org_id=self.org_id,
                                                                                     image_type=image_type,
                                                                                     image_name=image_name, _date=date,
                                                                                     boundary_id=plot_id)
        return file_response
