from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import TypeAlias

from coordinates import Coordinates

Celsium: TypeAlias = int

class WeatherType(str, Enum):
    THINDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsium
    wheather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    """Запрашиваем погоду на OpenWheather"""
    return Weather(
        temperature = 20,
        wheather_type = WeatherType.CLEAR,
        sunrise = datetime.fromisoformat("2022-10-30 08:00:00"),
        sunset = datetime.fromisoformat("2022-10-30 18:00:00"),
        city = "Orenburg"
    )
