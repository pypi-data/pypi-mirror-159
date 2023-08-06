import requests
import logging
import json


class Client:
	server_url = None
	xsrf_token = None
	logger = logging.getLogger("airbornerf.Client")

	def __init__(self, server_url):
		self.server_url = server_url
		self.session = requests.Session()
		self.logger.setLevel(logging.DEBUG)

	def _response_check(self, response):

		if response.status_code != requests.codes.ok: #pylint: disable=no-member
			self.logger.error("Request failed: HTTP " + str(response.status_code))
			self.logger.error(response.text)
			raise RuntimeError("API request failed: HTTP " + str(response.status_code))

	def _response_check_json(self, response):

		self._response_check(response)
		jesponse = response.json()
		if jesponse['success'] != True:
			self.logger.error("Request failed: success is False")
			self.logger.error(jesponse)
			raise RuntimeError("API request failed: {} ({})".format(jesponse['errorMessage'], jesponse['errorCode']))
		return jesponse

	def subscribe_tile(self, tilespec, service_level, technology, MCC, MNC):

		headers = {
			'X-XSRF-TOKEN': self.xsrf_token,
			'cache-control': "no-cache",
			'Content-Type': "application/json"
		}
		payload = json.dumps({
			"volume": {
				"id": "",
				"type": "tile",
				"tilespec": tilespec
			},
			"serviceLevel": service_level,
			"connectivityProvider": {
				"technology": technology,
				"MCC": MCC,
				"MNC": MNC
			}
		})
		response = self.session.request("POST", self.server_url + "/acja/v1.00/subscribe",
										headers=headers, data=payload)
		jesponse = self._response_check_json(response)
		return jesponse['subscriptionId']

