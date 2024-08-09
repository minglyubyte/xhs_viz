import json

def convert_to_new_format(data):
    new_data = []
    for item in data:
        for location_name, coordinates in item["locations"].items():
            if location_name not in ["Los Angeles", "LA", "California"]:
                new_data.append({
                    "location_name": location_name,
                    "location": coordinates,
                    "title": item["title"],
                    "image": item["image_list"].split(",")[0],
                    "link": item["note_url"],
                    "likes": item["liked_count"],
                    "collections": item["collected_count"],
                    "comments": item['comment_count'],
                    'categories': [k.strip() for k in item['categories'].split(",")],
                    'target_city': item['target_city']
                })
    return new_data

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        xhs_data = json.load(file)
    return convert_to_new_format(xhs_data)
