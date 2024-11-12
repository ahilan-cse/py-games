import qrcode

# Function to generate and save QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create the QR code image
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image file
    img.save("qrcode.png")
    print("QR code saved as 'qrcode.png'")

# Prompt user for input
data = input("Enter the data to generate QR code: ")
generate_qr_code(data)
