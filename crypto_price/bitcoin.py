import requests
import tkinter as tk

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[crypto_id]['usd']

def update_price():
    crypto_price = get_crypto_price(crypto_id)
    price_label.config(text=f"{crypto_symbol}: ${crypto_price:.2f}")
    root.after(10000, update_price)

root = tk.Tk()
root.title("Kripto Para Fiyat İzleme")

crypto_id = "bitcoin" # kripto para biriminin ID'si (örneğin: "bitcoin", "ethereum","solana")
crypto_symbol = crypto_id.capitalize()
price_label = tk.Label(root, text="", font=("Helvetica", 24))
price_label.pack(padx=20, pady=20)

update_price()

root.mainloop()
