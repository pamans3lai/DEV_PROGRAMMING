# https://pynative.com/python-basic-exercise-for-beginners/

# Explanation to Solution:

#    Cumulative Logic: The code doesn’t just check one condition; it accounts for every bracket the income “passes through.”
#    elif chain: This ensures that only the relevant calculation block is executed based on the total income range.
#    Mathematical Precision: By breaking the calculation into steps, you avoid the common mistake of taxing the entire 45,000 at the highest rate.
#

pendapatan = 45000
wajib_pajak = 0
print("pendapatan:", pendapatan)

if pendapatan <= 10000:
    wajib_pajak = 0
elif  pendapatan <= 20000:
    # pajak 10rb pertama adalah 0. selanjutnya 10%.
    wajib_pajak = (pendapatan - 10000) * 10 / 100
else:
    # 10rb pertama, 0 persen pajak
    # selanjutnya, 10 persen pajak = 1000
    wajib_pajak = 0 + (10000 * 10 / 100)
    # sisa pendapatan (20% pajak)
    wajib_pajak += (pendapatan - 20000) * 20 / 100

print("total pajak yang harus dibayarkan adalah", wajib_pajak)
