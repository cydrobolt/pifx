# -*- coding: utf-8 -*-
#
# Copyright © 2015-2018 Chaoyi Zha <me@cydrobolt.com>
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

from pifx.client import LIFXWebAPIClient


class PIFX:
    """Main PIFX class"""
    def __init__(self, api_key, http_endpoint=None):
        self.client = LIFXWebAPIClient(api_key, http_endpoint)

    def list_lights(self, selector='all'):
        """Given a selector (defaults to all), return a list of lights.
        Without a selector provided, return list of all lights.
        """

        return self.client.perform_request(
            method='get', endpoint='lights/{}',
            endpoint_args=[selector], parse_data=False)

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
            Setting transition time, in seconds, from 0.0 to
            3155760000.0 (100 years).
        """

        argument_tuples = [
            ('power', power),
            ('color', color),
            ('brightness', brightness),
            ('duration', duration)
        ]

        return self.client.perform_request(
            method='put', endpoint='lights/{}/state',
            endpoint_args=[selector], argument_tuples=argument_tuples)

    def state_delta(self, selector='all',
        power=None, duration=1.0, infrared=None, hue=None,
        saturation=None, brightness=None, kelvin=None):
        """Given a state delta, apply the modifications to lights' state
        over a given period of time.

        selector: required String
            The selector to limit which lights are controlled.

        power: String
            The power state you want to set on the selector. on or off

        duration: Double
            How long in seconds you want the power action to take.
            Range: 0.0 – 3155760000.0 (100 years)

        infrared: Double
            The maximum brightness of the infrared channel.

        hue: Double
            Rotate the hue by this angle in degrees.

        saturation: Double
            Change the saturation by this additive amount; the resulting
            saturation is clipped to [0, 1].

        brightness: Double
            Change the brightness by this additive amount; the resulting
            brightness is clipped to [0, 1].

        kelvin: Double
            Change the kelvin by this additive amount; the resulting kelvin is
            clipped to [2500, 9000].
        """

        argument_tuples = [
            ("power", power),
            ("duration", duration),
            ("infrared", infrared),
            ("hue", hue),
            ("saturation", saturation),
            ("brightness", brightness),
            ("kelvin", kelvin)
        ]

        return self.client.perform_request(
            method='post', endpoint='lights/{}/state/delta',
            endpoint_args=[selector], argument_tuples=argument_tuples)

    def toggle_power(self, selector='all', duration=1.0):
        """Given a selector and transition duration, toggle lights (on/off)"""

        argument_tuples = [
            ("duration", duration)
        ]

        return self.client.perform_request(
            method='post', endpoint='lights/{}/toggle',
            endpoint_args=[selector], argument_tuples=argument_tuples)

    def breathe_lights(self, color, selector='all',
        from_color=None, period=1.0, cycles=1.0,
        persist=False, power_on=True, peak=0.5):
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

        argument_tuples = [
            ("color", color),
            ("from_color", from_color),
            ("period", period),
            ("cycles", cycles),
            ("persist", persist),
            ("power_on", power_on),
            ("peak", peak),
        ]

        return self.client.perform_request(
            method='post', endpoint='lights/{}/effects/breathe',
            endpoint_args=[selector], argument_tuples=argument_tuples)

    def pulse_lights(self, color, selector='all',
        from_color=None, period=1.0, cycles=1.0,
        persist=False, power_on=True):
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
        """

        argument_tuples = [
            ("color", color),
            ("from_color", from_color),
            ("period", period),
            ("cycles", cycles),
            ("persist", persist),
            ("power_on", power_on),
        ]

        return self.client.perform_request(
            method='post', endpoint='lights/{}/effects/pulse',
            endpoint_args=[selector], argument_tuples=argument_tuples)

    def cycle_lights(self, states,
        defaults, direction='forward', selector='all'):
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

        argument_tuples = [
            ("states", states),
            ("defaults", defaults),
            ("direction", direction)
        ]

        return self.client.perform_request(
            method='post', endpoint='lights/{}/cycle', endpoint_args=[selector],
            argument_tuples=argument_tuples, json_body=True)

    def list_scenes(self):
        """Return a list of scenes.
        See http://api.developer.lifx.com/docs/list-scenes
        """

        return self.client.perform_request(
            method='get', endpoint='scenes', parse_data=False)

    def activate_scene(self, scene_uuid, duration=1.0):
        """Activate a scene.

        See http://api.developer.lifx.com/docs/activate-scene

        scene_uuid: required String
            The UUID for the scene you wish to activate

        duration: Double
            The time in seconds to spend performing the scene transition.
            default: 1.0
        """

        argument_tuples = [
            ("duration", duration),
        ]

        return self.client.perform_request(
            method='put', endpoint='scenes/scene_id:{}/activate',
            endpoint_args=[scene_uuid], argument_tuples=argument_tuples)
