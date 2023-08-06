#      A python library for getting Load Shedding schedules.
#      Copyright (C) 2021  Werner Pieterson
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
from datetime import timezone
from typing import List

from load_shedding.libs import citypower
from load_shedding.providers import eskom, Area, ProviderError, Stage


class Area(Area):
    def __init__(self, /, **kwargs) -> object:
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.municipality = kwargs.get("municipality")
        self.province = kwargs.get("province")


class CityPower(eskom.Eskom):
    name = "City Power"

    def get_stage_forecast(self) -> List:
        """ Get Stage forecast from City Power."""
        try:
            stage_forecast = citypower.get_stage_forecast()

            for i in range(len(stage_forecast)):
                stage_forecast[i]["start_time"] = stage_forecast[i]["start_time"].astimezone(timezone.utc)
                stage_forecast[i]["end_time"] = stage_forecast[i]["end_time"].astimezone(timezone.utc)
                stage_forecast[i]["stage"] = Stage(stage_forecast[i].get("stage"))

        except Exception as e:
            raise ProviderError(e)
        else:
            return stage_forecast


