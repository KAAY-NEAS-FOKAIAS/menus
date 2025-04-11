import qrcode

# URL of your GitHub Pages site
url = "https://kaay-neas-fokaias.github.io/menus/menu_bar.html"

# Create QR code
qr = qrcode.make(url)

# Save to file
qr.save("kaay_qr.png")

print("✅ QR code saved as 'kaay_qr.png'")