import streamlit as st
import requests
import pandas as pd

# Title and description
st.title("🛰️ ISS Live Tracker")
st.markdown("Get real-time data on the International Space Station's position and astronauts currently in space.")

# Get astronauts in space
astro_url = "http://api.open-notify.org/astros.json"
astro_response = requests.get(astro_url).json()

# Display data
st.subheader("👨‍🚀 People Currently in Space")
st.write(f"Total: {astro_response['number']}")
names = [person['name'] for person in astro_response['people']]
st.write("Names:", ", ".join(names))

# Get ISS location
loc_url = "http://api.open-notify.org/iss-now.json"
loc_response = requests.get(loc_url).json()
latitude = float(loc_response['iss_position']['latitude'])
longitude = float(loc_response['iss_position']['longitude'])

# Display location
st.subheader("📍 Current ISS Location")
st.write(f"Latitude: {latitude}, Longitude: {longitude}")

# Map
st.map(pd.DataFrame([[latitude, longitude]], columns=["lat", "lon"]))

st.markdown("This map shows the real-time position of the ISS based on the latest available data.")
