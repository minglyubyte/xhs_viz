import folium

icon_dict = {
    "景点推荐": "glyphicon glyphicon-map-marker",
    "美食推荐": "glyphicon glyphicon-cutlery",
    "住宿推荐": "glyphicon glyphicon-home",
    "购物指南": "glyphicon glyphicon-shopping-cart",
    "旅行攻略": "glyphicon glyphicon-list-alt",
    "文化体验": "glyphicon glyphicon-music",
    "户外活动": "glyphicon glyphicon-tree-conifer",
    "摄影指南": "glyphicon glyphicon-camera",
    "旅行感悟": "glyphicon glyphicon-book",
    "实用信息": "glyphicon glyphicon-cog"
}

emoji_dict = {
    "景点推荐": "🏰",
    "美食推荐": "🍔",
    "住宿推荐": "🏨",
    "购物指南": "🛍️",
    "旅行攻略": "🗺️",
    "文化体验": "🎭",
    "户外活动": "🏕️",
    "摄影指南": "📷",
    "旅行感悟": "📖",
    "实用信息": "ℹ️"
}

def get_icon(category):
    return folium.Icon(icon=icon_dict.get(category, "glyphicon glyphicon-map-marker"), prefix='glyphicon')

def categories_to_icons_html(categories):
    icons_html = ' '.join([f'<span class="{icon_dict[category]}" style="margin-right: 1px;"></span>' for category in categories if category in icon_dict])
    return icons_html

def categories_to_emojis(categories):
    emojis = ' '.join([emoji_dict[category] for category in categories if category in emoji_dict])
    return emojis
