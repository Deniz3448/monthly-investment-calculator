months = int(input("How many months will you invest: "))
monthly_growth_rate = float(input("Monthly growth rate (%): "))
monthly_contribution = float(input("Monthly contribution (currency): "))

total_amount = 0

print("\n--- MONTHLY INVESTMENT SUMMARY ---")

for month in range(1, months + 1):
    
    total_amount += monthly_contribution

    total_amount += total_amount * (monthly_growth_rate / 100)

    print(f"End of Month {month}: {total_amount:,.2f} Currency")

print("\n--- FINAL RESULT ---")
print(f"Total amount after {months} months: {total_amount:,.2f} Currency")
print(f"Total invested amount: {monthly_contribution * months:,.2f} Currency")