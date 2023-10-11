usb_sticks_price = 6
total_budget = 50
usb_bought = total_budget // usb_sticks_price
pounds_left = total_budget % usb_sticks_price

print(f"She can buy {usb_bought} USB sticks.")
print(f"She will have £{pounds_left} left.")
