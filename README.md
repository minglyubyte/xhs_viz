# XHS Recommendation Visualization and Statistics

## Project Description

This project aims to visualize and statistically analyze data from little red book, providing users with recommended locations, popular posts, and relevant statistical information. The project uses Streamlit for visualization, Folium for map display, and Matplotlib and WordCloud for statistical analysis.

## Directory Structure

```
├── data
│   ├── xhs_data.json
│   ├── xhs_data_converted.csv
├── pages
│   ├── map.py
│   ├── statistics.py
├── src
│   ├── data_processing.py
│   ├── icons.py
│   ├── popup.py
├── .gitignore
├── requirements.txt
├── README.md
```

## Usage

1. **Run the project**

   You can run the two Streamlit applications separately:

   - `map.py`: For visualizing recommended locations and related posts.
   - `statistics.py`: For displaying statistical information such as word clouds, location counts, and top posts.

   Run the following commands to start the applications:

   ```sh
   streamlit run pages/map.py
   streamlit run pages/statistics.py
   ```

2. **Browse the features**

   - **Location Recommendation Visualization**: In `map.py`, you can select different locations and categories. The map will update automatically to show relevant recommended locations and posts.
   - **Statistical Information**: In `statistics.py`, you can choose different statistical views such as word clouds, location counts, and top posts.

## Main Scripts

### `pages/map.py`

This script is used for visualizing recommended locations and related posts. Main features include:

- Loading data from `xhs_data.json`.
- Displaying the map using Folium and Streamlit, allowing users to select different locations and categories.
- Focusing the map on the selected location and displaying relevant posts in the sidebar.

### `pages/statistics.py`

This script is used for displaying statistical information. Main features include:

- Loading and preprocessing data from `xhs_data_converted.csv`.
- Displaying word clouds, location counts, and top posts.
- Providing multiple views that users can select from the sidebar.

### `src/data_processing.py`

This script contains functions for data processing, mainly:

- `load_data`: Function for loading data.

### `src/icons.py`

This script contains functions for defining and retrieving icons, mainly:

- `get_icon`: Retrieve the corresponding icon based on the category.
- `categories_to_icons_html`: Convert categories to HTML representations of icons.
- `categories_to_emojis`: Convert categories to emojis.

### `src/popup.py`

This script contains functions for creating popup content, mainly:

- `create_popup_html`: Create HTML content for popups based on location, title, image, link, likes, collections, comments, and categories.

## Data Description

- `data/xhs_data.json`: JSON file containing recommended locations and posts data.
- `data/xhs_data_converted.csv`: CSV file containing converted XiaoHongShu data.