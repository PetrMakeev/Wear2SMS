from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float
    
def get_gps_coordinates() -> Coordinates: 
    """Возвращаем текущие координаты"""
    return Coordinates(10, 20)
