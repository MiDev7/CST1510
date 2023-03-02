# Excellent
# ...................Input.................
employeeName = input('Enter employee\' name:  ')
workingHoursPerWeek = int(input('Enter number of hours worked in a week: '))
hourlyRate = float(input('Enter hourly pay rate: '))
federalTaxWithholdingRate = float(input('Enter federal tax withholding rate: '))
stateTaxWithholdingRate = float(input('Enter state tax withholding rate: '))
grossPay = hourlyRate * workingHoursPerWeek


# ..................Operations.......................
federalTaxWithholding = (grossPay * 20)/ 100
stateTaxWithholding = (grossPay * 9)/ 100
totalDeduction = federalTaxWithholding + stateTaxWithholding

# .................Output................................
print(f""""
Employee Name: {employeeName}
Hours Worked: {workingHoursPerWeek}
Pay Rate: ${hourlyRate}
Gross Pay: ${hourlyRate * workingHoursPerWeek}
Deductions:
    Federal Withholding (20.0%): ${federalTaxWithholding}
    State Withholding (9.0%): ${stateTaxWithholding}
    Total Deduction: ${totalDeduction}
Net Pay: ${grossPay - totalDeduction}
""")
