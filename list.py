#!/usr/bin/python3

import csv
import random
import string

kenyan_counties = {
    "Nairobi": {"postal_code": "00100", "address": "Nairobi CBD"},
    "Mombasa": {"postal_code": "80100", "address": "Mombasa Island"},
    "Kisumu": {"postal_code": "40100", "address": "Kisumu City"},
    "Nakuru": {"postal_code": "20100", "address": "Nakuru Town"},
    "Eldoret": {"postal_code": "30100", "address": "Eldoret Town"},
    "Thika": {"postal_code": "01000", "address": "Thika Town"},
    "Malindi": {"postal_code": "80200", "address": "Malindi Town"},
    "Kitale": {"postal_code": "30200", "address": "Kitale Town"},
    "Garissa": {"postal_code": "70100", "address": "Garissa Town"},
    "Kakamega": {"postal_code": "50100", "address": "Kakamega Town"},
    "Nyeri": {"postal_code": "10100", "address": "Nyeri Town"},
    "Meru": {"postal_code": "60200", "address": "Meru Town"},
    "Lamu": {"postal_code": "80500", "address": "Lamu Town"},
    "Naivasha": {"postal_code": "20117", "address": "Naivasha Town"},
    "Bungoma": {"postal_code": "50200", "address": "Bungoma Town"}
}

kenyan_supplier_names = [
    "Wanjiru Traders", "Omondi Enterprises", "Nyambura Supplies", "Kamau Importers",
    "Atieno Exporters", "Mutua Enterprises", "Achieng Traders", "Njoroge Distributors",
    "Mwangi Wholesalers", "Kariuki Merchants", "Njeri Trading Co.", "Odhiambo Imports",
    "Kamau & Sons", "Wangari Exports", "Njuguna Limited", "Wambui Enterprises"
]

major_banks_kenya = [
    "Kenya Commercial Bank (KCB)",
    "Equity Bank",
    "Cooperative Bank of Kenya",
    "Standard Chartered Bank",
    "Barclays Bank of Kenya",
    "Absa Bank Kenya",
    "National Bank of Kenya",
    "Stanbic Bank Kenya",
    "Diamond Trust Bank (DTB)",
    "CITIBANK"
]

def generate_supplier():
    supplier_name = random.choice(kenyan_supplier_names)
    supplier_email = f"info@{supplier_name.replace(' ', '').lower()}.{random.choice(['co.ke', 'com', 'biz'])}"
    supplier_phone_number = '07' + ''.join(random.choices(string.digits, k=8))
    kra_pin = 'P' + ''.join(random.choices(string.digits, k=9))
    bank_account = ''.join(random.choices(string.digits, k=12))
    bank_name = random.choice(major_banks_kenya)
    branch_name = ''.join(random.choices(string.ascii_letters, k=8))
    swift_code = ''.join(random.choices(string.ascii_uppercase, k=8))
    county = random.choice(list(kenyan_counties.keys()))
    postal_code = kenyan_counties[county]["postal_code"]
    billing_address = f"{kenyan_counties[county]['address']}, {postal_code}"

    return [supplier_name, supplier_email, supplier_phone_number, kra_pin, bank_account,
            bank_name, branch_name, swift_code, billing_address, postal_code, county]

def generate_csv(file_name, num_suppliers):
    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["SupplierName", "SupplierEmail", "SupplierPhoneNumber",
                             "KraPin", "BankAccount", "BankName", "BranchName",
                             "SwiftCode", "BillingAddress", "PostalCode", "County"])
        for _ in range(num_suppliers):
            csv_writer.writerow(generate_supplier())

file_name = "suppliers.csv"
num_suppliers = 20
generate_csv(file_name, num_suppliers)
print(f"Generated {file_name}")

