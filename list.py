#!/usr/bin/python3

import csv
import random
import string

def generate_supplier():
    supplier_name = ''.join(random.choices(string.ascii_letters, k=8))
    supplier_email = f"{supplier_name}@example.com"
    supplier_phone_number = ''.join(random.choices(string.digits, k=10))
    kra_pin = 'P' + ''.join(random.choices(string.digits, k=9))
    bank_account = ''.join(random.choices(string.digits, k=12))
    bank_name = ''.join(random.choices(string.ascii_letters, k=8))
    branch_name = ''.join(random.choices(string.ascii_letters, k=8))
    swift_code = ''.join(random.choices(string.ascii_uppercase, k=8))
    billing_address = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    postal_code = ''.join(random.choices(string.digits, k=5))
    county = ''.join(random.choices(string.ascii_letters, k=8))

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

file_name = "all_suppliers.csv"
num_suppliers = 20
generate_csv(file_name, num_suppliers)
print(f"Generated {file_name}")

