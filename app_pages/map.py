import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from src.data_processing import load_data
from src.icons import get_icon, categories_to_emojis
from src.popup import create_popup_html

# Load the data
file_path = './data/xhs_data.json'
data = load_data(file_path)

# Initialize Streamlit
st.title("小红书推荐可视化")

# Sidebar to show the list of locations
st.sidebar.header("Locations")
location_names = ["All"] + list(set([post["location_name"] for post in data]))
selected_location = st.sidebar.selectbox(
    "Select a location to view details",
    location_names
)

# Sidebar to show the list of categories
st.sidebar.header("Categories")
category_names = ["All"] + list(set([category for post in data for category in post['categories']]))
selected_category = st.sidebar.selectbox(
    "Select a category to view details",
    category_names
)

# Dropdown menu for selecting map style
map_style = st.selectbox("Select Map Style", ["CartoDB Positron (Recommended)", "OpenStreetMap"])

# Map style mapping
style_mapping = {
    "CartoDB Positron (Recommended)": "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    "OpenStreetMap": "OpenStreetMap",
}

# Get the selected map style
selected_style = style_mapping[map_style]

# Determine the initial map center
map_center = [34.0522, -118.2437]

# Create a map with the selected style
m = folium.Map(location=map_center, zoom_start=10, tiles=selected_style, attr='default')

# Add a marker cluster to handle multiple markers at the same location
marker_cluster = MarkerCluster().add_to(m)

# Function to add marker to map
def add_marker(location):
    iframe = folium.IFrame(create_popup_html(
        location['location_name'], location['title'], location['image'], location['link'],
        location['likes'], location['collections'], location['comments'], location['categories']
    ), width=250, height=350)
    popup = folium.Popup(iframe, max_width=250)
    folium.Marker(
        location=location['location'],
        popup=popup,
        tooltip=location['title'],
        icon=get_icon(location['categories'][0])  # Use the first category for the marker icon
    ).add_to(marker_cluster)

# Filter and display markers based on selected location and category
for location in data:
    if selected_location == "All" and selected_category == "All":
        add_marker(location)
    elif selected_location == "All" and selected_category in location['categories']:
        add_marker(location)
    elif selected_location == location["location_name"] and selected_category == "All":
        add_marker(location)
        map_center = location['location']  # Update map center to selected location
    elif selected_location == location["location_name"] and selected_category in location['categories']:
        add_marker(location)
        map_center = location['location']  # Update map center to selected location

# Show relevant posts in the sidebar
st.sidebar.header("Relevant Posts")
displayed_titles = set()
for location in data:
    if (selected_location == "All" or selected_location == location["location_name"]) and (selected_category == "All" or selected_category in location['categories']):
        if location['title'] not in displayed_titles:
            st.sidebar.image(location["image"], width=150)
            st.sidebar.write(f"**{location['title']}**")
            st.sidebar.write(f"{categories_to_emojis(location['categories'])}")
            st.sidebar.write(f"❤️ {location['likes']} ⭐ {location['collections']} 💬 {location['comments']}")
            st.sidebar.write(f"[Read more]({location['link']})")
            st.sidebar.write("---")
            displayed_titles.add(location['title'])

# If a specific location is selected, update the map center and zoom
if selected_location != "All":
    m.location = map_center
    m.zoom_start = 12

# Display the map in Streamlit
with st.container():
    st.components.v1.html(folium.Figure().add_child(m)._repr_html_(), height=500)
