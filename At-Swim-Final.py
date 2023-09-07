import pandas as pd
import folium
from folium.raster_layers import ImageOverlay
from streamlit_folium import folium_static
import streamlit as st
import base64
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_lighthouse = load_lottieurl("https://assets9.lottiefiles.com/datafiles/WIRy7Ny0KV28BJg/data.json")

st.set_page_config(page_title="At-Swim", page_icon="🍀")

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
        border-radius: 0;
        box-shadow: none;
        max-height: 80vh;
        overflow-y: auto;
    }
    .text-area {
        border: none;
        border-radius: 0;
        box-shadow: none;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

Title_col, Book_col = st.columns(2)

Title_col.markdown("<h1 class='title'> Immersion for Memory: </h1>", unsafe_allow_html=True)
Title_col.markdown("<h1 class='title'> At Swim, Two Boys</h1>", unsafe_allow_html=True)

Book_col.image('images/bookcover.png', width=200)

with st.container():
    st.markdown("<h2 class='green-text'>Immersion and Prosthetic Memory</h2>", unsafe_allow_html=True)
    st.markdown("<div class='center-content'>"
                "Throughout Drexel's 'At Swim, Two Boys' course, students have delved into memory studies and explored the historical fiction queer literature piece 'At Swim, Two Boys' by Jamie O'Neill, guided by the instruction of Kelsey Hanson and Eric Kennedy. A central focus of the course revolved around grasping the concept of prosthetic memory—how it takes shape and is utilized. Drawing from my comprehension of the potent formation of prosthetic memory through simulation, immersion, and media, I embarked on a project that harnesses technology to engage with this concept. In an era dominated by Augmented Reality and Artificial Intelligence, the potential to craft prosthetic or fabricated memories of historical events is profound. While this website may not entirely construct an immersive metaverse of 'At Swim, Two Boys,' particularly regarding the Easter Rising, it aspires to enrich the prosthetic memory cultivated by the class through the novel by introducing supplementary contexts and engaging additional senses."
                "</div>", unsafe_allow_html=True)

st.markdown("<h2 class='green-text'>Cultural Memory</h2>", unsafe_allow_html=True)
st.markdown("<div class='center-content'>"
                "The cultural memory of the Easter Rising is indelibly etched into Dublin's geographical landscape, with the iconic Shelbourne Hotel standing as a historic witness to the events of 1916. Likewise, the haunting melody and lyrics of 'Who Fears to Speak of Easter Week' serve as a musical vessel that carries the emotions, narratives, and collective memory of the Rising, ensuring that its legacy lives on through the power of music and song. In the realm of literature and text, echoes of the Rising resonate through the writings of authors like James Joyce and W.B. Yeats, who, through their works, have embedded the spirit of 1916 in the city's cultural consciousness for generations to come."
                "</div>", unsafe_allow_html=True)

data = {'Places': ['1. The Forty Foot', '2. Muglins Lighthouse', '3. Shelbourne Hotel', '5. Liberty Hall', '6. Killiney Hill'],
        'latitude': [53.278339, 53.275306, 53.338884, 53.348483, 53.269589], 
        'longitude': [-6.097655, -6.075384, -6.256256, -6.255979, -6.108549]} 
df = pd.DataFrame(data)

m = folium.Map(location=[53.349770, -6.26334], zoom_start=11.45)

for i, row in df.iterrows():
    marker = folium.Marker(
        location=[row['latitude'], row['longitude']],
        icon=folium.DivIcon(html=f"""<div style='font-size: 20px; font-weight: bold; background-color: green; color: white; text-align: center; width: 24px; height: 24px; line-height: 24px;'>{i + 1}</div>""")
    )
    popup_content = f"""
        <h3>{row['Places']}</h3>
    """
    popup = folium.Popup(popup_content, max_width=300)
    popup.add_to(marker)
    
    marker.add_to(m)

image = ImageOverlay(
    'images/Dublin_1900.jpg',
    bounds=[[53.39825008318412, -6.430249587495973], [53.267079, -6.083627]],
    opacity=1
)
image.add_to(m)

with st.expander("Explore the Interactive Map"):
    st.markdown("<h2 class='green-text'>Mapping At Swim, Two Boys </h2>", unsafe_allow_html=True)
    folium_static(m)
    Selected_location = st.selectbox("", ["Select a Location to Explore!", "1. The Forty Foot", "2. Muglins Lighthouse", "3. Shelbourne Hotel", '4. Killiney Hill'])
    if Selected_location == "Select a Location to Explore!":
        st.write("")  
    elif Selected_location == "1. The Forty Foot":
        st.write("The Forty Foot:")
        forty_foot_desc, forty_foot_pics = st.columns(2) 
        forty_foot_desc.write('The Forty Foot is a famous sea swimming spot in Sandycove, County Dublin, Ireland, known for its clear waters and dramatic cliffs. It has a rich history as a traditional male-only swimming spot, and its name possibly originates from a 40-foot jump that swimmers used to wager on. Today, it is a popular year-round destination for swimmers and visitors, attracting people from all over who seek to experience its natural beauty and the invigorating waters of the Irish Sea.')  
        forty_foot_pics.image('images/forty_foot.png', width=300)  
        forty_foot_pics.image('images/forty_foot_men.png', width=300)
        forty_foot_pics.write('1971, Forty Foot, Sandycove. Irish Times')
        forty_foot_desc.write('At Swim, Two Boys:')  
        forty_foot_desc.write('In Jamie O Neills novel "At Swim, Two Boys," the Forty Foot holds significant symbolic value as a location where the two main characters, Jim and Doyler, find solace and develop their deepening relationship amidst the tumultuous backdrop of early 20th-century Ireland. This coastal setting becomes a sanctuary for their blossoming love, reflecting the novels overarching themes of love, freedom, and defiance against societal norms.') 
    elif Selected_location == "2. Muglins Lighthouse":
        st.write("Muglins Lighthouse: ")
        muligins_desc, muligins_pics = st.columns(2)
        muligins_desc.write('Muglins Lighthouse, located on the Muglins Rocks off the coast of Dublin, Ireland, is a historic maritime landmark. Built in 1887, this lighthouse has guided ships safely through the treacherous waters of Dublin Bay for over a century. Its distinctive red and white stripes make it easily recognizable, and it continues to serve as a crucial navigation aid for vessels entering and leaving Dublins bustling harbor.')
        muligins_pics.image('images/Muligans.png', width=300)  
        muligins_desc.write('At Swim, Two Boys:')
        muligins_desc.write('Muglins Lighthouse in the novel "At Swim, Two Boys" becomes a symbol of their desire for freedom, particularly queer freedom.')
        muligins_pics.write('Mulgins Lighthouse, Irish Lights')  
    elif Selected_location == "3. Shelbourne Hotel":
        st.write("Shelbourne Hotel: ")
        Shelbourne_desc, Shelbourne_pics = st.columns(2)
        Shelbourne_desc.write('The Shelbourne Hotel in Dublin is historically significant for its connection to the Easter Rising of 1916, as it served as a pivotal hub for the rebel leaders. During the Rising, the hotels prominent location on St. Stephens Green made it a strategic meeting place for planning and coordination among the rebellions leaders, underscoring its role in the events of that fateful period in Irish history. In 1922 it became the home of the draftings of Irelands first Constitution.')
        Shelbourne_pics.image('images/shelbourne.jpeg', width=300) 
        Shelbourne_pics.write('The Citizens Army before the Shelbourne, The Irish History Museum')
        Shelbourne_desc.write('At Swim, Two Boys:')
        Shelbourne_desc.write('"Whistles blew; and every so often a party jumped the park railings and dashed the street to the College of Surgeons, a grim cold columned ediface whose pavement and roof were periodically swept by machine-gun fire from the Shelbourne" page 548')
        Shelbourne_desc.write('The novels incorporation of the historically accurate Shelbourne Hotel serves as a commendable example of historical fiction, preserving cultural memory and providing readers with a vivid and authentic glimpse into the pivotal role this iconic establishment played during the Easter Rising of 1916.')
    elif Selected_location == "4. Killiney Hill":
        killiney_desc, killiney_pics = st.columns(2)
        killiney_pics.image('images/kill_hill.png', width=300)  
        killiney_desc.write('"Thats not Rome burning,thats Dublin."') 
        killiney_desc.write('"They would crowd Killiney Hill for the view."')
        killiney_desc.write('"My poor Father"  558')

with st.expander("Explore Musical Storytelling"):
    st.markdown("<h2 class='green-text'>Musical Storytelling</h2>", unsafe_allow_html=True)
    st.markdown("""
    Experience the emotions and themes of "At Swim, Two Boys" through carefully selected music. Choose a song from the options below to immerse yourself further in the narrative.
    """)

    selected_song = st.selectbox("Select a Song", ["Select an Audio to learn more!", "The Foggy Dew", "Off to Dublin in the Green", "Who Fears to Speak of Easter Week"])

    if selected_song == "Select an Audio to learn more!":
        st.write(" ")
    elif selected_song == "The Foggy Dew":
        st.video("https://www.youtube.com/watch?v=SH50D2TAIa8")
        st.write('"The Foggy Dew" is more than just a song; it is a cultural memory that resonates deeply with Irelands history and struggle for independence. Through its poignant lyrics and haunting melody, the song not only encapsulates the past but also fosters a prosthetic memory, enabling listeners to emotionally connect with the events and sentiments of Irelands tumultuous journey toward freedom.')
    elif selected_song == "Off to Dublin in the Green":
        st.video("https://www.youtube.com/watch?v=VR12Q4kcdqQ")
        st.write('"Then if the day was still Id steal a kiss and whisper"')
        st.write('"Darling, hold me fast and well watch the years go rolling"')
        st.write('"When I dream about the time Ill be going."')
        st.write('These lyrics convey a sense of nostalgia, longing, and hope for a brighter future. The songs cultural memory lies in its connection to Irish history, particularly the struggles for independence in the 19th and 20th centuries. It serves as a musical reminder of the resilience and determination of the Irish people during those challenging times, and it continues to be cherished as a symbol of Irish identity and the quest for freedom.') 
    elif selected_song == "Who Fears to Speak of Easter Week":
        st.write('"Who Fears to Speak of Easter Week" preserves the narrative of the Irish during the Easter Rising by documenting the historical events, creating an emotional connection, transmitting oral history, reinforcing cultural identity, and providing political and social commentary. It serves as a powerful reminder of Irelands struggle for independence and continues to be a poignant expression of Irish heritage and pride.')

show_contents = False

st.markdown("---") 

if st.button('Work Cited'):
    show_contents = not show_contents 
if show_contents:
    st.write('“Historic Hotels in Ireland – the Shelbourne Dublin.” The Shelbourne - 27 St. Stephens Green, Dublin 2, Leinster D02 K224, 28 Aug. 2023, www.theshelbourne.com/history. ')
    st.write('Landsberg, Alison. “Introduction, 1. Prosthetic Memory.” Posthetic Memory: The Transformation of American Mass Culture, Columbia University Press, New York, 2004.  ')
    st.write('Lights, Commissioners of Irish. “Muglins Lighthouse.” Muglins, www.irishlights.ie/tourism/our-lighthouses/muglins.aspx. Accessed 7 Sept. 2023.')
    st.write('O’Neill, Jamie. At Swim, Two Boys. Scribner, 2001. ')
    st.write('“The Forty Foot.” The Forty Foot Dun Laoghaire - J D Wetherspoon')
