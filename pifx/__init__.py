# -*- coding: utf-8 -*-
#
# Copyright © 2015 Chaoyi Zha <me@cydrobolt.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests
import util

class PIFX:
    def __init__(self, api_key, http_endpoint=None):
        # use default API base endpoint if none defined
        self.http_base = "https://api.lifx.com/v1/" if http_endpoint == None
        self.api_key = api_key
        # generate HTTP authentication header
        self.headers = util.generate_auth_header(self.api_key)

    def full_http_endpoint(self, suffix):
        return self.http_base + suffix

    def parse_data(self, response):
        parsed_response = json.loads(response.text)
        return parsed_response

    def has_error(self, response):
        """Return True if request contains error, False if request is successful"""
        if response.status_code != 200:
            return True
        else:
            return False

    def handle_error(self, parsed_data):
        """Given parsed response, raise appropriate errors."""
        return False
    def parse_data(self, parsed_data):
        """Given parsed response, return correct return values"""
        return parsed_data['results']

    def list_lights(self, selector='all'):
        """
        Given a selector (defaults to all), return a list of lights.
        Without a selector provided, return list of all lights.
        """

        endpoint = full_http_endpoint(
            "lights/{}".format(selector)
        )
        res = request.get(endpoint, headers=self.headers)
        parsed_data = self.parsed_response(res)

        if self.has_error(res):
            return self.handle_error(parsed_data)

        return parsed_data

    def set_state(self, selector='all',
        power=None, color=None, brightness=None, duration=None):
        """
        Given a selector (defaults to all), set the state of a light.
        Selector can be based on id, scene_id, group_id, label, etc.
        Returns list of lightbulb statuses if successful.
        See http://api.developer.lifx.com/v1/docs/selectors

        Arguments (all optional):
            power (str):
                e.g "on" or "off"
            color (str):
                e.g #ff0000 or "red"
                Hex color code, color name, saturation percentage, hue, RGB, etc.
                See http://api.developer.lifx.com/v1/docs/colors
            brightness (double):
                e.g 0.5
                Brightness level from 0 to 1
            duration (double):
                e.g 10
                Transition time, in seconds. From 0.0 to 3155760000.0 (100 years).
        """

        endpoint = full_http_endpoint(
            "lights/{}/state".format(selector)
        )
        argument_tuples = [
            ('power', power),
            ('color', color),
            ('brightness', brightness),
            ('duration', duration)
        ]
        data = dict()
        for arg_name, arg_val in argument_tuples:
            if arg_val not None:
                data[arg_name] = arg_val

        res = request.put(endpoint, data=data, headers=self.headers)
        parsed_data = self.parsed_response(res)

        if self.has_error(res):
            return self.handle_error(parsed_data)

        return self.parse_data(parsed_data)

    def toggle_power(self, selector='all', duration=1.0):
        """Given a selector and transition duration, toggle lights (on/off)"""
        endpoint = full_http_endpoint(
            "lights/{}/toggle".format(selector)
        )

        data = {
            "duration": duration
        }

        res = request.post(endpoint, data=data, headers=self.headers)
        parsed_data = self.parsed_response(res)

        if self.has_error(res):
            return self.handle_error(parsed_data)

        return self.parse_data(parsed_data)

    def breathe_lights(self, selector='all',
        color, from_color=None, period=1.0, cycles=1.0,
        persist=False, power_on=True, peak=0.5, duration=1.0):
        """
        Perform breathe effect on lights.
        selector: required String
            The selector to limit which lights will run the effect.

        color: required String
            Color attributes to use during effect. See set_state for more.

        from_color:	String
            The color to start the effect from. See set_state for more.
            default: current bulb color

        period:	Double
            The time in seconds for one cyles of the effect.
            default: 1.0

        cycles:	Double
            The number of times to repeat the effect.
            default: 1.0

        persist: Boolean
            If false set the light back to its previous
            value when effect ends, if true leave the last effect color.
            default: false

        power_on: Boolean
            If true, turn the bulb on if it is not already on.
            default: true

        peak: String
            Defines where in a period the target color is at its maximum.
            Minimum 0.0, maximum 1.0.
            default: 0.5

        """
        endpoint = full_http_endpoint(
            "lights/{}/toggle".format(selector)
        )

        data = {
            "duration": duration
        }

        res = request.post(endpoint, data=data, headers=self.headers)
        parsed_data = self.parsed_response(res)

        if self.has_error(res):
            return self.handle_error(parsed_data)

        return self.parse_data(parsed_data)
