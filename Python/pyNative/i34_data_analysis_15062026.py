trial =  {1, 2, 3, 4, 5}
paid = {4, 5, 6, 7, 8}

upgraded = trial & paid
leads = trial - paid
unique = trial ^ paid

print(f"Upgraded (both): {upgraded}")
print(f"Leads (Trial only): {leads}")
print(f"Unique Status (Not both): {unique}")
