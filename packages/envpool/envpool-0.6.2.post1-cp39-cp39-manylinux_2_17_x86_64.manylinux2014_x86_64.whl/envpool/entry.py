# Copyright 2021 Garena Online Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Entry point for all envs' registration."""

import envpool.atari.registration  # noqa: F401
import envpool.box2d.registration  # noqa: F401
import envpool.classic_control.registration  # noqa: F401
import envpool.mujoco.dmc.registration  # noqa: F401
import envpool.mujoco.gym.registration  # noqa: F401
import envpool.toy_text.registration  # noqa: F401
import envpool.vizdoom.registration  # noqa: F401
