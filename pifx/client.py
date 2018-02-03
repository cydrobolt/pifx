import requests

from pifx import util


class LIFXWebAPIClient:
    def __init__(self, api_key, http_endpoint=None):
        if http_endpoint == None:
            self.http_base = "https://api.lifx.com/v1/"
        else:
            self.http_base = http_endpoint

        self.api_key = api_key
        self.headers = util.generate_auth_header(self.api_key)
        self._s = requests.Session()

    def _full_http_endpoint(self, suffix):
        return self.http_base + suffix

    def perform_request(
        self,
        method,
        endpoint,
        endpoint_args=[],
        argument_tuples=None,
        json_body=False,
        parse_data=True
    ):
        http_endpoint = self._full_http_endpoint(
            endpoint.format(*endpoint_args)
        )

        data = None
        if argument_tuples is not None:
            data = util.arg_tup_to_dict(argument_tuples)

        if json_body:
            res = self._s.request(
                method=method, url=http_endpoint, json=data, headers=self.headers)
        else:
            res = self._s.request(
                method=method, url=http_endpoint, data=data, headers=self.headers)

        parsed_response = util.parse_response(res)

        util.handle_error(res)

        if parse_data:
            return util.parse_data(parsed_response)

        return parsed_response
