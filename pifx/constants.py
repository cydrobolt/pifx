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

A_OK_HTTP_CODES = [
    200,
    207
]

A_ERROR_HTTP_CODES = {
    400: "Request was invalid",
    401: "Invalid API key",
    403: "Bad OAuth scope",
    404: "Selector did not match any lights",
    422: "Missing or malformed parameters",
    426: "HTTP is required to perform transaction",
    # see http://api.developer.lifx.com/v1/docs/rate-limits
    429: "Rate limit exceeded",
    500: "API currently unavailable",
    502: "API currently unavailable",
    503: "API currently unavailable",
    523: "API currently unavailable"
}
