
if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    total_cost = round(meal_cost+(meal_cost*(tip_percent/100) + meal_cost*(tax_percent/100)))
    output = "The total meal cost is {} dollars.".format(total_cost)
    print(output)
