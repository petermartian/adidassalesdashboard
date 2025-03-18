import streamlit as st
import pandas as pd
import numpy as np


# --- Nigerian Tax and Deduction Rules (Simplified) ---
# You'll need to adjust these based on the latest official guidelines
PERSONAL_ALLOWANCE = 300000  # Example: NGN 300,000 annual
TAX_RATES = {
    300000: 0.07,
    300000: 0.11,  # Next 300,000
    500000: 0.15,  # Next 500,000
    500000: 0.19,  # Next 500,000
    1600000: 0.21, # Next 1,600,000
    None: 0.24,     # Above 3,200,000
}
PENSION_RATE_EMPLOYEE = 0.08
PENSION_RATE_EMPLOYER = 0.10
NHF_RATE = 0.025  # National Housing Fund

def calculate_paye(annual_income):
    taxable_income = max(0, annual_income - PERSONAL_ALLOWANCE)
    tax_payable = 0
    bracket_start = 0
    for limit, rate in TAX_RATES.items():
        bracket_end = limit if limit is not None else float('inf')
        taxable_in_bracket = max(0, min(taxable_income, bracket_end) - bracket_start)
        tax_payable += taxable_in_bracket * rate
        bracket_start = bracket_end
        if taxable_income <= bracket_end:
            break
    return tax_payable / 12  # Monthly PAYE

def calculate_salary(basic_salary, housing_allowance, transport_allowance, other_allowances=0):
    gross_salary = basic_salary + housing_allowance + transport_allowance + other_allowances
    annual_basic_salary = basic_salary * 12
    paye = calculate_paye(annual_basic_salary)
    pension_employee = gross_salary * PENSION_RATE_EMPLOYEE
    nhf = gross_salary * NHF_RATE
    total_deductions = paye + pension_employee + nhf
    net_salary = gross_salary - total_deductions
    pension_employer = gross_salary * PENSION_RATE_EMPLOYER
    return gross_salary, paye, pension_employee, nhf, total_deductions, net_salary, pension_employer

def main():
    st.title("Nigerian Company Salary Calculator")

    tab1, tab2, tab3, tab4 = st.tabs(["Employee Info", "Salary Details", "Results", "About"])

    with tab1:
        st.header("Employee Information")
        employee_name = st.text_input("Employee Name")
        employee_id = st.text_input("Employee ID (Optional)")
        department = st.text_input("Department (Optional)")

    with tab2:
        st.header("Enter Salary Details (Monthly in NGN)")
        basic_salary = st.number_input("Basic Salary", min_value=0, step=1000)
        housing_allowance = st.number_input("Housing Allowance", min_value=0, step=1000)
        transport_allowance = st.number_input("Transport Allowance", min_value=0, step=1000)
        other_allowances = st.number_input("Other Allowances", min_value=0, step=1000, value=0)

        if st.button("Calculate Salary"):
            if basic_salary is not None:
                gross_salary, paye, pension_employee, nhf, total_deductions, net_salary, pension_employer = calculate_salary(
                    basic_salary, housing_allowance, transport_allowance, other_allowances
                )
                st.session_state['results'] = {
                    'employee_name': employee_name,
                    'basic_salary': basic_salary,
                    'housing_allowance': housing_allowance,
                    'transport_allowance': transport_allowance,
                    'other_allowances': other_allowances,
                    'gross_salary': gross_salary,
                    'paye': paye,
                    'pension_employee': pension_employee,
                    'nhf': nhf,
                    'total_deductions': total_deductions,
                    'net_salary': net_salary,
                    'pension_employer': pension_employer,
                }
            else:
                st.warning("Please enter the basic salary to calculate.")

    with tab3:
        st.header("Salary Calculation Results")
        if 'results' in st.session_state:
            results = st.session_state['results']
            st.subheader(f"Salary Breakdown for: {results['employee_name']}")
            st.write(f"**Basic Salary (Monthly):** ₦{results['basic_salary']:,}")
            st.write(f"**Housing Allowance (Monthly):** ₦{results['housing_allowance']:,}")
            st.write(f"**Transport Allowance (Monthly):** ₦{results['transport_allowance']:,}")
            st.write(f"**Other Allowances (Monthly):** ₦{results['other_allowances']:,}")
            st.write(f"**Gross Salary (Monthly):** ₦{results['gross_salary']:,}")
            st.write("--- Deductions ---")
            st.write(f"**PAYE (Monthly):** ₦{results['paye']:,}")
            st.write(f"**Pension (Employee - 8%):** ₦{results['pension_employee']:,}")
            st.write(f"**NHF (2.5%):** ₦{results['nhf']:,}")
            st.write(f"**Total Deductions (Monthly):** ₦{results['total_deductions']:,}")
            st.write(f"**Net Salary (Monthly):** ₦{results['net_salary']:,}")
            st.write("--- Employer Contributions ---")
            st.write(f"**Pension (Employer - 10%):** ₦{results['pension_employer']:,}")
        else:
            st.info("Enter salary details in the 'Salary Details' tab and click 'Calculate Salary' to see the results.")

    with tab4:
        st.header("About this Application")
        st.markdown("""
        This is a simple web application built with Streamlit to calculate the monthly salary 
        for employees in a Nigerian company. 

        **Important Notes:**
        * The tax rates and deduction rules used in this application are simplified examples 
          and may not reflect the latest official regulations. 
        * For accurate payroll calculations, always refer to the official guidelines from the 
          relevant Nigerian tax authorities (e.g., Federal Inland Revenue Service - FIRS) and 
          pension regulatory bodies.
        * This application is for illustrative purposes only.

        Developed by: [Your Name/Organization]
        Date: March 18, 2025
        """)

if __name__ == "__main__":
    main()

