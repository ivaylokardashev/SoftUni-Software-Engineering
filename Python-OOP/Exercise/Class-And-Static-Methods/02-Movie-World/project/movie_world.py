from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.CUSTOMER_CAPACITY:  # len(self.customers) < self.customer_capacity()
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.DVD_CAPACITY:  # len(self.dvds) < self.dvd_capacity
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
        except StopIteration:
            return None

        try:
            dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))
        except StopIteration:
            return None

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        try:
            customer = next(filter(lambda c: c.id == customer_id, self.customers))
        except StopIteration:
            return None

        try:
            dvd = next(filter(lambda d: d.id == dvd_id, customer.rented_dvds))
        except StopIteration:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False

        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        customers_result = "\n".join(c.__repr__() for c in self.customers)
        dvds_result = "\n".join(d.__repr__() for d in self.dvds)

        # return "\n".join([
        #     *[str(c) for c in self.customers],
        #     *[str(d) for d in self.dvds],
        # ])

        return f"{customers_result}\n{dvds_result}"
