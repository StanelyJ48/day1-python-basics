
# ==========================================
# ELECTRICITY BILL GENERATOR
# ==========================================

print("=" * 45)
print("        ELECTRICITY BILL GENERATOR")
print("=" * 45)

# Meter readings
opening_reading = float(input("Enter opening meter reading: "))
current_reading = float(input("Enter current meter reading: "))

# Calculate units
units = current_reading - opening_reading

if units < 0:
    print("Error: Current reading cannot be less than opening reading.")
    exit()

# Tariff assumptions (editable)
energy_rate = 7.375
fixed_charges = 40
customer_charges = 55
duty_rate = 0.06
surcharge_rate = 0.27
fppca_rate = 0.825

# Bill calculations
energy_charges = units * energy_rate
electricity_duty = energy_charges * duty_rate
surcharge = units * surcharge_rate
fppca = units * fppca_rate

total_bill = (
    energy_charges
    + fixed_charges
    + customer_charges
    + electricity_duty
    + surcharge
    + fppca
)

rounded_bill = round(total_bill)

# Display bill
print("\n" + "=" * 45)
print("             ELECTRICITY BILL")
print("=" * 45)

print(f"Opening Reading       : {opening_reading:.0f}")
print(f"Current Reading       : {current_reading:.0f}")
print(f"Total Units Consumed  : {units:.0f}")

print("-" * 45)
print("BILL BREAKDOWN")
print("-" * 45)

print(f"Energy Charges        : Rs. {energy_charges:.2f}")
print(f"Fixed Charges         : Rs. {fixed_charges:.2f}")
print(f"Customer Charges      : Rs. {customer_charges:.2f}")
print(f"Electricity Duty      : Rs. {electricity_duty:.2f}")
print(f"Surcharge             : Rs. {surcharge:.2f}")
print(f"FPPCA                 : Rs. {fppca:.2f}")

print("-" * 45)
print(f"Estimated Total       : Rs. {total_bill:.2f}")
print(f"Rounded Bill          : Rs. {rounded_bill}")
print("=" * 45)

print("       BILL GENERATED SUCCESSFULLY!")
print("=" * 45)
