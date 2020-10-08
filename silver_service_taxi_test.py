from cp1404practicals.prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("${:2f}".format(taxi.get_fare()))


main()
