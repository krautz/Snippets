def installments_payment(
    installments_price,  # full price of the product, which will be paid in installments
    installments_amount,  # number of installments
    discount_price,  # discount price on paying without installments
    monthly_return = 0.01  # estimated investments monthly return percentage
):
    profit = 0
    installment_price = installments_price / installments_amount
    installments_original_price = installments_price
    for _ in range(installments_amount):
        month_profit = installments_price * monthly_return
        profit += month_profit
        installments_price -= (installment_price - month_profit)

    discount = installments_original_price - discount_price
    print(f"Discount: {(discount / installments_original_price) * 100:.2f}%")
    print(f"Installments Price: {installments_original_price}")
    print(f"Profit: {profit:.2f}")
    print(f"Installments Price Less Profit: {installments_original_price - profit:.2f}")
    print(f"Discount Price: {discount_price}")
    if installments_original_price - profit < discount_price:
        print("Better to pay in installments")
    elif installments_original_price - profit > discount_price:
        print("Better to pay with discount")
    else:
        print("No difference between payling with discount or in installments")
