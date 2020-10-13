import requests

def main():
    base = input("Base currency: ")
    other = input("Other currency: ")
    res = requests.get("https://api.exchangeratesapi.io/latest", params={"base":base, "symbols": other})
    if res.status_code != 200:
        raise Exception("Error, Api access unsuccessful")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} = {rate} {other}")

if __name__ == "__main__":
    main()