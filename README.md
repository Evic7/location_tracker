# Phone Number Locator Web App 📍🌍
A Flask-based web application that allows users to input a phone number (with international country code) and retrieve approximate geographical information, including:

Country/Region description
Mobile carrier/service provider
Approximate latitude and longitude (via geocoding the region)
An interactive map centered on the approximate location (using Folium)

It also supports basic IP address lookup (if a dotted IP is entered instead of a phone number), displaying city, region, country, and coordinates.
Important Disclaimer:
This tool provides an approximate location based on publicly available phone number registration data and geocoding. It does NOT offer real-time GPS tracking or exact device location. Precise tracking is impossible without carrier or device access. Use ethically and legally only.
Perfect for educational purposes, learning Flask, or OSINT demonstrations!

# Features ✨

Simple web interface with form input
Parse and validate international phone numbers using phonenumbers
Get the region description and the carrier name
Geocode the region to coordinates using the OpenCage API
Display results with an embedded interactive Folium map (commented out in the current code but ready to enable)
Bonus: Basic IP geolocation using the free DbIpCity database
Error handling for invalid inputs

# Tech Stack

Backend: Flask (Python)
Libraries:
phone numbers for parsing and metadata
OpenCage for geocoding (requires free API key)
folium for map generation (optional/enabled in code comments)
ip2geotools for IP lookup

Frontend: HTML templates (Jinja2)

Clone the repository: git clone https://github.com/Evic7/phone_number_locator.git

cd phone_number_locator
Create a virtual environment (recommended): 
python -m venv venv
source venv/bin/activate 
On Windows: 
venv\Scripts\activate

# Install dependencies: 
pip install -r requirements.txt(Includes Flask, phonenumbers, folium, opencage, etc.)

Get an OpenCage API Key (free tier available):

Sign up at https://opencagedata.com/

Replace the Key variable in app.py with your own key: 
PythonKey = "your_api_key_here."


# Usage
Run the app locally:
python app.py
Open your browser and go to http://127.0.0.1:5000/

Enter a phone number like +14155552671 (US example) or +2348012345678 (Nigeria)

Submit to see location details

To enable the interactive map:

Uncomment the Folium map section in app.py (around line 70+)

The map will embed directly in the results page

Project Structure
```
phone_number_locator/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── vercel.json               # Vercel deployment config
│
├── static/
│   ├── css/
│   │   └── main.css
│   │
│   ├── js/
│   │   └── index.js
│   │
│   └── resources/
│       ├── background.jpg
│       ├── earth.bmp
│       ├── loop1.jpg
│       ├── loop2.jpg
│       ├── loop3.jpg
│       ├── loop4.jpg
│       ├── loop5.jpg
│       ├── loop6.jpg
│       └── loop7.jpg
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── locate.html

```
# To Do / Improvements

Fully enable and style the Folium map embed.
Add validation for phone number format.
Improve UI with Bootstrap/CSS.
Deploy to platforms like Render, Vercel, or Heroku.
Add timezone info or more details.

# Disclaimer & Ethical Use
This project is for educational purposes only. Respect privacy laws—do not use for harassment, stalking, or illegal activities. Location data is approximate and often only region-level.
Contributing
Feel free to fork, improve the UI/map, fix bugs, or add features! Open issues or submit pull requests.
