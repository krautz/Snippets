def installments_payment(
    installments_full_price,  # full price of the product, which will be paid in installments
    installments_amount,  # number of installments
    cash_full_price,  # discount price on paying without installments
    monthly_return_percentage = 0.01  # estimated investments monthly return percentage
):
    installment_monthly_price = installments_full_price / installments_amount
    installments_remaining_price = installments_full_price
    for _ in range(installments_amount):
        month_investments_return = installments_remaining_price * monthly_return_percentage
        installments_remaining_price -= (installment_monthly_price - month_investments_return)
    #
    investments_return = installments_remaining_price
    investments_return_percentage = (investments_return / installments_full_price) * 100
    installments_final_price = installments_full_price - investments_return
    cash_discount = installments_full_price - cash_full_price
    cash_discount_percentage = (cash_discount / installments_full_price) * 100
    print(f"Installments Full Price: {installments_full_price}")
    print(f"Installments Investment Return: {investments_return:.2f} ({investments_return_percentage:.2f}%)")
    print(f"Installments Price Less Return: {installments_final_price:.2f}")
    print("#############################################")
    print(f"Cash Discount Full Price: {cash_full_price}")
    print(f"Cash Discount: {cash_discount:.2f} ({cash_discount_percentage:.2f}%)")
    print("#############################################")
    #
    if installments_final_price < cash_full_price:
        print(f"Better to pay in installments. It will save {cash_full_price - installments_final_price:.2f}")
    elif installments_final_price > cash_full_price:
        print(f"Better to pay with discount. It will save {installments_final_price - cash_full_price:.2f}")
    else:
        print("No difference between payling with discount or in installments")
