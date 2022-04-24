class Address():
    def __init__(self, Street_name: str, Street_NR: int, ZIP_code: int, City: str, Country: str):
        self.Street_name = Street_name
        self.Street_NR = Street_NR
        self.Zip_code = ZIP_code
        self.City = City
        self.Country = Country

    def __str__(self):
        return f"Street_name: {self.Street_name}, Street_NR: {self.Street_NR}, Zip_code:{self.Zip_code}" \
               f"City: {self.City}, Country:{self.Country}"
