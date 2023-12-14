import tkinter as tk
from tkinter import messagebox
import webbrowser
import requests

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")

        self.label = tk.Label(root, text="Enter URL:")
        self.label.pack()

        self.url_entry = tk.Entry(root)
        self.url_entry.pack()

        self.shorten_button = tk.Button(root, text="Shorten URL", command=self.shorten_url)
        self.shorten_button.pack()

        self.shortened_url = tk.Label(root, text="", wraplength=300, justify='left', fg="blue", cursor="hand2")
        self.shortened_url.pack()
        self.shortened_url.bind("", self.open_shortened_url)

    def shorten_url(self):
        long_url = self.url_entry.get()

        # Use a URL shortening API (e.g., Bitly) to generate a short URL
        short_url = self.generate_short_url(long_url)

        if short_url:
            self.shortened_url.config(text=f"Shortened URL: {short_url}")
        else:
            messagebox.showerror("Error", "Failed to generate a short URL.")

    def generate_short_url(self, long_url):
        # Replace 'YOUR_ACCESS_TOKEN' with your actual access token from a URL shortening service
        access_token = 'YOUR_ACCESS_TOKEN'
        url = f"https://api-ssl.bitly.com/v4/shorten"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        payload = {
            "long_url": long_url
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            short_url = response.json().get("id")
            return short_url
        else:
            return None

    def open_shortened_url(self, event):
        short_url = self.shortened_url.cget("text")
        short_url = short_url.replace("Shortened URL: ", "")
        webbrowser.open(short_url)

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()
    
