#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    
    APP_ID = os.environ.get("MicrosoftAppId", "a89e2d78-4524-4f3d-b43e-dd566ae2863c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "_~l8Q~1EbcohQncBJXXYxZbX8IkETHUJHQ~nCa7d")