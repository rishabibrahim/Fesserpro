purchase_price= float(input("Purchase price"))
selling_price= float(input("Selling price"))
no_of_shares_traded=float(input("No.of shares traded"))
profit_loss= (selling_price-purchase_price)*no_of_shares_traded
print(profit_loss)
if profit_loss>2000:
    print("High")
elif profit_loss>1000 or profit_loss<2000:
    print("Moderate")
else:
    print("Low")         