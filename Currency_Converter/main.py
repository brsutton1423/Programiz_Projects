import requests
answer = 'yes'

while answer == 'yes':
    try:
        from_code = input("From currency code (e.g. USD): ").upper()
        url = f"https://open.er-api.com/v6/latest/{from_code}"
        response = requests.get(url)
        data = response.json()

        to_code = input("Enter the target currency code (e.g. INR, EUR, JPY): ").upper()

        if to_code not in data["rates"]:
            print("Invalid currency code. Please try again.")
        else:
            rate = data["rates"][to_code]
            amount = float(input("Enter amount: "))
            converted = rate * amount
            print(f"{amount} {from_code} = {converted:.2f} {to_code}")

    except ValueError:
        print("Please enter a valid number for the amount.")
    except KeyError:
        print("Invalid currency code. Please try again.")
    except Exception as e:
        print("Something went wrong:", e)
    answer = input("Do you want to convert another amount? (yes/no):").lower()