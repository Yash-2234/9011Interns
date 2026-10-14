def calculate_lab_charges(number_of_tests, cost_per_test):
    return number_of_tests * cost_per_test


def calculate_treatment_charges(treatment_days, daily_treatment_cost):
    return treatment_days * daily_treatment_cost


def calculate_service_charges(consultation_fee, number_of_tests, cost_per_test, treatment_days, daily_treatment_cost, medicine_cost):
    lab_charges = calculate_lab_charges(number_of_tests, cost_per_test)
    treatment_charges = calculate_treatment_charges(treatment_days, daily_treatment_cost)
    return consultation_fee + lab_charges + treatment_charges + medicine_cost


def calculate_membership_discount(service_charges, membership_type):
    membership_type = membership_type.lower()
    discount_rates = {
        "regular": 0.00,
        "silver": 0.05,
        "gold": 0.10,
        "platinum": 0.15
    }
    discount_percent = discount_rates.get(membership_type, 0.00)
    return service_charges * discount_percent


def calculate_emergency_charge(is_emergency):
    if is_emergency:
        return 1500.00
    return 0.00


def calculate_final_bill(consultation_fee, number_of_tests, cost_per_test, treatment_days, daily_treatment_cost, medicine_cost, membership_type, is_emergency):
    service_charges = calculate_service_charges(
        consultation_fee,
        number_of_tests,
        cost_per_test,
        treatment_days,
        daily_treatment_cost,
        medicine_cost
    )

    membership_discount = calculate_membership_discount(service_charges, membership_type)
    discounted_service_charges = service_charges - membership_discount
    emergency_charge = calculate_emergency_charge(is_emergency)

    return discounted_service_charges + emergency_charge


# Optional challenge functions

def calculate_age_discount(service_charges, age):
    if age >= 60:
        return service_charges * 0.05
    return 0.00


def calculate_insurance_amount(bill_amount, insurance_coverage_percentage):
    return bill_amount * (insurance_coverage_percentage / 100)


def classify_bill(final_bill):
    if final_bill < 5000:
        return "Low"
    elif final_bill <= 10000:
        return "Moderate"
    else:
        return "High"


def calculate_total_savings(membership_discount, age_discount):
    return membership_discount + age_discount


def generate_hospital_bill(consultation_fee, number_of_tests, cost_per_test, treatment_days, daily_treatment_cost, medicine_cost, membership_type, is_emergency, age=0, insurance_coverage_percentage=0):
    lab_charges = calculate_lab_charges(number_of_tests, cost_per_test)
    treatment_charges = calculate_treatment_charges(treatment_days, daily_treatment_cost)
    service_charges = calculate_service_charges(
        consultation_fee,
        number_of_tests,
        cost_per_test,
        treatment_days,
        daily_treatment_cost,
        medicine_cost
    )
    membership_discount = calculate_membership_discount(service_charges, membership_type)
    age_discount = calculate_age_discount(service_charges - membership_discount, age)
    emergency_charge = calculate_emergency_charge(is_emergency)
    discounted_amount = service_charges - membership_discount - age_discount
    final_bill = discounted_amount + emergency_charge
    insurance_amount = calculate_insurance_amount(final_bill, insurance_coverage_percentage)
    final_payable = final_bill - insurance_amount

    print("========== HOSPITAL BILL ==========\n")
    print(f"Consultation Fee = {consultation_fee:.2f}")
    print(f"Laboratory Charges = {lab_charges:.2f}")
    print(f"Treatment Charges = {treatment_charges:.2f}")
    print(f"Medicine Charges = {medicine_cost:.2f}\n")
    print(f"Total Service Charges = {service_charges:.2f}")
    print(f"Membership Discount = {membership_discount:.2f}")
    print(f"Emergency Charge = {emergency_charge:.2f}\n")
    print(f"Final Payable Amount = {final_bill:.2f}")
    print("\n===================================")

    return final_payable


if __name__ == "__main__":
    consultation_fee = 800
    number_of_tests = 4
    cost_per_test = 500
    treatment_days = 3
    daily_treatment_cost = 2000
    medicine_cost = 2500
    membership_type = "Gold"
    is_emergency = True

    service_charges = calculate_service_charges(
        consultation_fee,
        number_of_tests,
        cost_per_test,
        treatment_days,
        daily_treatment_cost,
        medicine_cost
    )
    membership_discount = calculate_membership_discount(service_charges, membership_type)
    emergency_charge = calculate_emergency_charge(is_emergency)
    final_amount = calculate_final_bill(
        consultation_fee,
        number_of_tests,
        cost_per_test,
        treatment_days,
        daily_treatment_cost,
        medicine_cost,
        membership_type,
        is_emergency
    )

    print("========== HOSPITAL BILL ==========\n")
    print(f"Consultation Fee = {consultation_fee:.2f}")
    print(f"Laboratory Charges = {calculate_lab_charges(number_of_tests, cost_per_test):.2f}")
    print(f"Treatment Charges = {calculate_treatment_charges(treatment_days, daily_treatment_cost):.2f}")
    print(f"Medicine Charges = {medicine_cost:.2f}\n")
    print(f"Total Service Charges = {service_charges:.2f}")
    print(f"Membership Discount = {membership_discount:.2f}")
    print(f"Emergency Charge = {emergency_charge:.2f}\n")
    print(f"Final Payable Amount = {final_amount:.2f}")
    print("\n===================================")
