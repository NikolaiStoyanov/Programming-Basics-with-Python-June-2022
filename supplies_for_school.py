pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())

pens_price = pens * 5.80
markers_price = markers * 7.20
detergent_price = detergent * 1.20
total_price = pens_price + markers_price + detergent_price
price_with_discount = total_price - (total_price * (discount/100))
print(price_with_discount)
