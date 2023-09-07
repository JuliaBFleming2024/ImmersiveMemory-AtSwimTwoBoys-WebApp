import pandas as pd
import folium
from folium.raster_layers import ImageOverlay
from streamlit_folium import folium_static
import streamlit as st
import base64
import requests


# Define a function to load Lottie animation JSON data from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the Lottie animation JSON data
lottie_lighthouse = load_lottieurl("https://assets9.lottiefiles.com/datafiles/WIRy7Ny0KV28BJg/data.json")

# Set page icon to shamrock
st.set_page_config(page_title="At-Swim", page_icon="🍀")

# Add custom CSS
custom_css = """
<style>
    @font-face { font-family: "Celtica-Bold"; src: url("./fonts/celtic/Celtica-Bold.ttf") format("truetype"); }
    body { font-family: "Celtica-Bold", sans-serif; }
    .title { text-align: center; color: green; }
    .green-text { color: green; }
    .image-container { display: flex; justify-content: center; align-items: center; }
    .center-content {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 0; /* Removed border-radius */
        box-shadow: none; /* Removed box-shadow */
        max-height: 80vh;
        overflow-y: auto;
    }
    .text-area {
        border: none; /* Removed border */
        border-radius: 0; /* Removed border-radius */
        box-shadow: none; /* Removed box-shadow */
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Create two header columns
Title_col, Book_col = st.columns(2)

# Set titles on the left pane
Title_col.markdown("<h1 class='title'> Immersion for Memory: </h1>", unsafe_allow_html=True)
Title_col.markdown("<h1 class='title'> At Swim, Two Boys</h1>", unsafe_allow_html=True)

# Set book cover on the right pane
Book_col.image('images/bookcover.png', width=200)

# Information about the immersive experience
with st.container():
    st.markdown("<h2 class='green-text'>Creating an Immersive Experience</h2>", unsafe_allow_html=True)
    st.markdown("<div class='center-content'>"
                "The immersive experience presented here aims to complement the exploration of queer Irish literature through a multi-sensory journey. As you delve into the pages of 'At Swim, Two Boys,' you can simultaneously engage with the historical and cultural context of Dublin. By combining visual elements like historic maps and markers, we create an environment that enhances your connection with the narrative, enabling a more profound understanding of the events and emotions portrayed in the novel."
                "</div>", unsafe_allow_html=True)

# Connection to memory studies
with st.container():
    st.markdown("<h2 class='green-text'>Prosthetic Memory and Deeper Engagement</h2>", unsafe_allow_html=True)
    st.markdown("<div class='center-content'>"
                "This immersive experience attempts to conjure a deeper prosthetic memory for readers of 'At Swim, Two Boys'. Just as a prosthetic limb enhances physical capabilities, this interactive environment amplifies your engagement with the literature."
                "</div>", unsafe_allow_html=True)

# Create a DataFrame with the latitude and longitude of Dublin
data = {'Places': ['1. The Forty Foot', '2. Muglins Lighthouse'],
        'latitude': [53.278339, 53.275306],
        'longitude': [-6.097655, -6.075384]}
df = pd.DataFrame(data)

# Centers map at Dublin center and adjusts zoom
m = folium.Map(location=[53.349770, -6.26334], zoom_start=11.45)

# Increments label number of each added map point
for i, row in df.iterrows():
    marker = folium.Marker(
        location=[row['latitude'], row['longitude']],
        icon=folium.DivIcon(html=f"""<div style='font-size: 20px; font-weight: bold; background-color: green; color: white; text-align: center; width: 24px; height: 24px; line-height: 24px;'>{i + 1}</div>""")
    )
    # Description assigned to each data point
    # Create a custom popup content
    popup_content = f"""
        <h3>{row['Places']}</h3>
    """
    # Adds the label to the marker
    popup = folium.Popup(popup_content, max_width=300)
    popup.add_to(marker)
    
    # Add the marker to the map
    marker.add_to(m)

# Orients then overlays the historical map of Dublin
image = ImageOverlay(
    'images/Dublin_1900.jpg',
    bounds=[[53.39825008318412, -6.430249587495973], [53.267079, -6.083627]],
    opacity=1
)
image.add_to(m)

# Display the map in Streamlit
with st.expander("Explore the Interactive Map"):
    st.markdown("<h2 class='green-text'>Mapping At Swim, Two Boys </h2>", unsafe_allow_html=True)
    folium_static(m)
    # Create a dropdown for location selection
    Selected_location = st.selectbox("", ["Select Location to Explore", "1. The Forty Foot", "2. Muglins Lighthouse", "Dublin"])
    # Display relevant information or player based on the selected location
    if Selected_location == "Select Location to Explore":
        st.write("")  # Blank
    elif Selected_location == "1. The Forty Foot":
        st.write("Forty Foot")
        forty_foot_desc, forty_foot_pics = st.columns(2)
        forty_foot_desc.write('Talk about Forty Foot here, historical and book contents |||Talk about Forty Foot here, historical and book contents |||Talk about Forty Foot here, historical and book contents  |||Talk about Forty Foot here, historical and book contents  |||Talk about Forty Foot here, historical and book contents  |||Talk about Forty Foot here, historical and book contents  |||Talk about Forty Foot here, historical and book contents  |||Talk about Forty Foot here, historical and book contents    ')  # Left column
        forty_foot_pics.image('images/forty_foot.png', width=300)  # Right column
        forty_foot_pics.image('images/forty_foot_men.png', width=300)
        forty_foot_desc.write('More description of Forty Foot')  # Left column

# Musical Storytelling
with st.expander("Musical Storytelling"):
    st.markdown("<h2 class='green-text'>Musical Storytelling</h2>", unsafe_allow_html=True)
    st.markdown("""
    Experience the emotions and themes of "At Swim, Two Boys" through carefully selected music. Choose a song from the options below to immerse yourself further in the narrative.
    """)

    # Create a dropdown for song selection
    selected_song = st.selectbox("Select a Song", ["Select an Audio to learn more!", "The Foggy Dew", "Off to Dublin in the Green", "Who Fears to Speak of Easter Week"])

    # Display relevant information or player based on the selected song
    if selected_song == "Select an Audio to learn more!":
        st.write(" ")
    elif selected_song == "The Foggy Dew":
        st.video("https://www.youtube.com/watch?v=SH50D2TAIa8")
    ##st.write("[Watch this Video!](https://www.youtube.com/watch?v=zlzzO1e6dws)")
    elif selected_song == "Off to Dublin in the Green":
        # Add a music player or description for the second song
        st.video("https://www.youtube.com/watch?v=VR12Q4kcdqQ")
    elif selected_song == "Who Fears to Speak of Easter Week":
        # Add a music player or description for the third song
        st.video("https://www.youtube.com/watch?v=Nd3AW4QQ38M")

# Musical Storytelling
with st.expander("Memory Studies and Motivation"):
    st.markdown("<h2 class='green-text'>Musical Storytelling</h2>", unsafe_allow_html=True)
    st.markdown("""
    Experience the emotions and themes of "At Swim, Two Boys" through carefully selected music. Choose a song from the options below to immerse yourself further in the narrative.
    """)
 
