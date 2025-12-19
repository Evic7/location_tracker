from datetime import datetime
from flask import Flask, render_template, url_for, request
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
import socket
import requests
import os
from opencage.geocoder import OpenCageGeocode


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    """ if request.method == 'POST':
      number1 = request.form['pnumber']
      number2 = request.form['pnumber2']
      
      if number2 == "":
          return number1 + "<br>" "the second number is not given"
      else:
          return number1 +" "+ number2
       """
    return render_template("index.html")
  
@app.route('/locator/',methods=['GET','POST'])
def locator():
 try:
  # taking input the phonenumber along with the country code
  if request.method == 'POST':
      number1 = request.form['pnumber']
      outputs = {"phone1":number1}
        
      if "." in number1:  # Assuming this checks for IP format
       try:
        api_url = f"http://ip-api.com/json/{number1}"
        res = requests.get(api_url).json()
        if res["status"] == "success":
            outputs.update({"ipaddress": res["query"]})
            outputs.update({"iplocation": f"{res['city']}, {res['regionName']}, {res['country']}"})
            outputs.update({"ipcoord": f"Coords: (Lat: {res['lat']}, Lng: {res['lon']})"})
            outputs.update({"lat1": res["lat"]})
            outputs.update({"lng1": res["lon"]})
            #Extras
            outputs.update({"isp": res.get("isp", "Unknown")})
            outputs.update({"org": res.get("org", "Unknown")})  # Often the company/network owner
            outputs.update({"timezone": res.get("timezone", "Unknown")})
            
            # Proxy/VPN/Mobile detection
            proxy_status = "Yes" if res.get("proxy", False) else "No"
            outputs.update({"proxy_vpn": proxy_status})
            
        else:
           outputs.update({"mainerror": f"IP lookup failed: {res.get('message', 'Unknown error')}" })
       except Exception as e:
           outputs.update({"mainerror": "An error occurred while getting IP details. Try again."})
    
       return render_template("locate.html", outputs=outputs)
       
      # Parsing the phonenumber string to convert it into phonenumber format
      phoneNumber = phonenumbers.parse(number1)
      
      # Storing the API Key in the Key variable
      # Get the key from environment variable, fallback for local testing
      Key = os.getenv("OPENCAGE_KEY", "No key found")  # Optional fallback
      if not Key or Key == "No key found":
           outputs.update({"mainerror": "Fatal error API communication failed."})
           return render_template("locate.html",outputs = outputs)
          
          
      # Using the geocoder module of phonenumbers to print the Location in console
      yourLocation = geocoder.description_for_number(phoneNumber,"en")
      
      #print("location : "+yourLocation)
      outputs.update({"location": yourLocation})
      
 
      # Using the carrier module of phonenumbers to print the service provider name in console
      yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
      #print("service provider : "+yourServiceProvider)
      outputs.update({"serviceprovider": yourServiceProvider})
      
      # Using opencage to get the latitude and longitude of the location
      numgeocoder = OpenCageGeocode(Key)
      query = str(yourLocation)
      results = numgeocoder.geocode(query)
 
      # Assigning the latitude and longitude values to the lat and lng variables
      lat = results[0]['geometry']['lat']
      lng = results[0]['geometry']['lng']
      if lat is None or lng is None:
          outputs.update({"mainerror": "Could not geocode the location (vague region or API issue)"})
          
      outputs.update({"lat1": lat})
      outputs.update({"lng1": lng})
      """  # Getting the map for the given latitude and longitude
      myMap = folium.Map(location=[lat,lng],zoom_start = 15)
      #Add a red circle marker to the map at the specified 'location' 
      folium.CircleMarker(location=[lat,lng], radius=50, color="red").add_to(myMap)

      #Add a standard marker (pin) to the map at the same 'location' coordinates
      folium.Marker(location=[lat,lng]).add_to(myMap)
      
      myMap.get_root().width = "800px"
      myMap.get_root().height = "600px"
      # get folium result in an html iframe tags
      mapfme = myMap.get_root()._repr_html_()
      
      outputs.update({"mapframe": mapfme})  """
 except Exception as e:
     error = "An error occured you can try again"
     #print(e)
     outputs.update({"mainerror": error})
 #print(outputs)

 return render_template("locate.html",outputs = outputs)
 
if __name__ == "__main__":
    #app.run(debug=True)

    app.run()

