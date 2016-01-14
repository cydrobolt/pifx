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

from . import util
import re
import requests, json, six

class PIFX:
    """Main PIFX class"""
    def __init__(self, api_key, http_endpoint=None):
        # use default API base endpoint if none defined
        if http_endpoint == None:
            self.http_base = "https://api.lifx.com/v1/"
        else:
            self.http_base = http_endpoint

        self.api_key = api_key
        # generate HTTP authentication header
        self.headers = util.generate_auth_header(self.api_key)
        self._s = requests.Session()

    def encode_url_arg(self, url_arg):
        arg_regex = '(\w+):(.*)'

        if ":" not in url_arg:
            # no identifiers
            # can encode entire argument
            return six.moves.urllib.parse.quote_plus(url_arg)
        else:
            # identifier found
            # separate identifier string from argument
            # text, then encode argument text
            url_arg_matches = re.match(arg_regex, url_arg)

            identifier_name = url_arg_matches.group(1)
            argument_content = url_arg_matches.group(2)

            encoded_arg = six.moves.urllib.parse.quote_plus(argument_content)

            return identifier_name + ":" + encoded_arg

    def full_http_endpoint(self, suffix):
        return self.http_base + suffix

    def list_lights(self, selector='all'):
        """Given a selector (defaults to all), return a list of lights.
        Without a selector provided, return list of all lights.
        """

        endpoint = self.full_http_endpoint(
            "lights/{}".format(self.encode_url_arg(selector))
        )
        res = self._s.get(endpoint, headers=self.headers)
        parsed_data = util.parse_response(res)

        util.handle_error(res)

        return parsed_data

    def set_state(self, selector='all',
        power=None, color=None, brightness=None, duration=None):
        """Given a selector (defaults to all), set the state of a light.
        Selector can be based on id, scene_id, group_id, label, etc.
        Returns list of lightbulb statuses if successful.
        See http://api.developer.lifx.com/v1/docs/selectors

        selector: required String
            The selector to limit which lights will run the effect.

        power: String
            e.g "on" or "off"

        color: String
            e.g #ff0000 or "red"
            Color to set selected bulbs.
            Hex color code, color name, saturation percentage, hue, RGB, etc.
            See http://api.developer.lifx.com/v1/docs/colors

        brightness: Double
            e.g 0.5
            Set brightness level from 0 to 1

        duration: Double
            e.g 10
            Setting transition time, in seconds, from 0.0 to 3155760000.0 (100 years).

        """

        endpoint = self.full_http_endpoint(
            "lights/{}/state".format(self.encode_url_arg(selector))
        )
        argument_tuples = [
            ('power', power),
            ('color', color),
            ('brightness', brightness),
            ('duration', duration)
        ]
        data = util.arg_tup_to_dict(argument_tuples)

        res = self._s.put(endpoint, data=data, headers=self.headers)
        parsed_data = util.parse_response(res)

        util.handle_error(res)

        return util.parse_data(parsed_data)

    def toggle_power(self, selector='all', duration=1.0):
        """Given a selector and transition duration, toggle lights (on/off)"""
        endpoint = self.full_http_endpoint(
            "lights/{}/toggle".format(self.encode_url_arg(selector))
        )

        data = {
            "duration": duration
        }

        res = self._s.post(endpoint, data=data, headers=self.headers)
        parsed_data = util.parse_response(res)

        util.handle_error(res)

        return util.parse_data(parsed_data)

    def breathe_lights(self, color, selector='all',
        from_color=None, period=1.0, cycles=1.0,
        persist=False, power_on=True, peak=0.5, duration=1.0):
        """Perform breathe effect on lights.

        selector: String
            The selector to limit which lights will run the effect.
            default: all

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
        endpoint = self.full_http_endpoint(
            "lights/{}/effects/breathe".format(self.encode_url_arg(selector))
        )

        data = {
            "selector": selector,
            "color": color,
            "from_color": from_color,
            "period": period,
            "cycles": cycles,
            "persist": persist,
            "power_on": power_on,
            "peak": peak,
            "duration": duration
        }

        res = self._s.post(endpoint, data=data, headers=self.headers)
        parsed_data = util.parse_response(res)

        util.handle_error(res)

        return util.parse_data(parsed_data)

    def pulse_lights(self, color, selector='all',
        from_color=None, period=1.0, cycles=1.0,
        persist=False, power_on=True, peak=0.5, duration=1.0):
        """Perform pulse effect on lights.

        selector: String
            The selector to limit which lights will run the effect.
            default: all

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
        endpoint = self.full_http_endpoint(
            "lights/{}/effects/pulse".format(self.encode_url_arg(selector))
        )

        data = {
            "color": color,
            "from_color": from_color,
            "period": period,
            "cycles": cycles,
            "persist": persist,
            "power_on": power_on,
            "peak": peak,
            "duration": duration
        }

        res = self._s.post(endpoint, data=data, headers=self.headers)
        parsed_data = util.parse_response(res)

        util.handle_error(res)

        return util.parse_data(parsed_data)

    def cycle_lights(self, states,
        defaults, direction='forward', selector='all',):
        """Cycle through list of effects.

        Provide array states as a list of dictionaries with set_state arguments.
        See http://api.developer.lifx.com/docs/cycle

        selector: String
            The selector to limit which lights will run the effect.
            default: all

        states: required List of Dicts
            List of arguments, named as per set_state. Must have 2 to 5 entries.

        defaults: Object
            Default values to use when not specified in each states[] object.
            Argument names as per set_state.

        direction: String
            Direction in which to cycle through the list. Can be forward or backward
            default: forward
        """
        endpoint = self.full_http_endpoint(
            "lights/{}/cycle".format(self.encode_url_arg(selector))
        )

        states_json = json.dumps(states)

        data = {
            'states': states_json,
            'defaults': defaults,
            'direction': direction
        }

        res = self._s.post(endpoint, data=data, headers=self.headers)
        parsed_data = util.parse_response(res)

        util.handle_error(res)

        return util.parse_data(parsed_data)

    def list_scenes(self):
        """Return a list of scenes.
        See http://api.developer.lifx.com/docs/list-scenes
        """

        endpoint = self.full_http_endpoint(
            "scenes"
        )
        res = self._s.get(endpoint, headers=self.headers)
        parsed_data = util.parse_response(res)

        util.handle_error(res)

        return parsed_data

    def activate_scene(self, scene_uuid, duration=1.0):
        """Activate a scene.

        See http://api.developer.lifx.com/docs/activate-scene

        scene_uuid: required String
            The UUID for the scene you wish to activate

        duration: Double
            The time in seconds to spend performing the scene transition.
            default: 1.0
        """

        endpoint = self.full_http_endpoint(
            "scenes/scene_id:{}/activate".format(scene_uuid)
        )

        data = {
            'duration': duration
        }

        res = self._s.put(endpoint, data=data, headers=self.headers)
        parsed_data = util.parse_response(res)

        return parsed_data
