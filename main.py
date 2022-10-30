from coordinates import get_gps_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather


# основное тело программы   
def main():
    coordinates = get_gps_coordinates()    
    weather = get_weather(coordinates)

    print(weather)


# точка входа.
if __name__ == '__main__':
    main()


