import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# Convert data to DataFrame
df = pd.read_csv("./data/xhs_data_converted.csv")
df = df.drop(df[df['location_name'] == 'Los Angeles'].index)
df = df.drop(df[df['location_name'] == 'California'].index)
df = df.drop(df[df['location_name'] == 'LA'].index)

# Sidebar
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a view:", ["Wordcloud", "Location Counts", "Top 10 Posts", "All Together"])

# Main content
st.title("XHS Data Statistics")

def display_wordcloud():
    st.header("Wordcloud of Locations")
    locations = df['location_name'].dropna()
    word_counts = Counter(locations)
    
    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white', font_path='./SimHei.ttf')
    
    # Generate the word cloud from the word frequencies
    wordcloud.generate_from_frequencies(word_counts)
    
    # Display the wordcloud
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def display_location_counts():
    st.header("Location Counts")
    
    # Ensure the 'location_name' column exists
    if 'location_name' in df.columns:
        locations = df['location_name'].dropna()
        location_counts = locations.value_counts().head(20)

        # Display the pie chart
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%', startangle=90, counterclock=False)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
    else:
        st.error("The 'location_name' column is not found in the DataFrame.")

def display_top_10_posts():
    st.header("Top 10 Posts by Likes and Collections")
    if 'liked_count' in df.columns and 'collected_count' in df.columns:
        top_posts = df[['note_id', 'title', 'desc', 'liked_count', 'collected_count', 'note_url', 'image_list']].dropna().astype({'liked_count': 'int', 'collected_count': 'int'})
        top_posts = top_posts.drop_duplicates(subset=['note_id'])
        top_posts = top_posts.sort_values(by=['liked_count', 'collected_count'], ascending=False).head(10)
        
        rows = 2
        cols = 5
        
        for row in range(rows):
            cols_list = st.columns(cols)
            for col, (_, post) in zip(cols_list, top_posts.iloc[row*cols:(row+1)*cols].iterrows()):
                with col:
                    # Ensure title fits within a specific height for three lines
                    padded_title = f"<div style='font-weight: bold; height: 3em; line-height: 1em; overflow: hidden;'>{post['title']}</div>"
                    st.markdown(padded_title, unsafe_allow_html=True)
                    st.image(post['image_list'].split(",")[0])
                    if len(post['desc']) > 100:
                        st.write(post['desc'][:100] + "...")
                    else:
                        st.write(post['desc'][:100])
                    st.write(f"❤️ {post['liked_count']} ⭐ {post['collected_count']}")
                    st.markdown(f"[Read more]({post['note_url']})")
    else:
        st.error("The 'liked_count' or 'collected_count' column is not found in the DataFrame.")

if options == "Wordcloud":
    display_wordcloud()
elif options == "Location Counts":
    display_location_counts()
elif options == "Top 10 Posts":
    display_top_10_posts()
elif options == "All Together":
    col1, col2 = st.columns(2)
    with col1:
        display_wordcloud()
    with col2:
        display_location_counts()
    display_top_10_posts()
