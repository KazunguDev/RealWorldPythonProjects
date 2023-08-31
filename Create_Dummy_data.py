from faker import Faker

if __name__ == '__main__':
    fake = Faker()
    print(fake.name())
    print(fake.address())
    print(fake.text())
    print(fake.email())
    print(fake.country())
    print(fake.url())
    print(fake.latitude(), fake.longitude())
