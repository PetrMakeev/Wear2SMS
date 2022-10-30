from coordinates import get_gps_coordinates
#from weather_api_service import get_wheather
#from weather_formatter import format_weather


# основное тело программы   
def main():
    coordinates = get_gps_coordinates()    
    # wheather = get_wheather()

    print(coordinates.latitude)


# точка входа.
if __name__ == '__main__':
    main()


