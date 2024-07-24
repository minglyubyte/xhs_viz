from src.icons import categories_to_icons_html

def create_popup_html(location, title, image, link, likes, collections, comments, categories):
    icons_html = categories_to_icons_html(categories)
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Popup</title>
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    </head>
    <body>
        <div style="width:250px">
            <h4>{location} <span>{icons_html}</span></h4>
            <h4>{title}</h4>
            <img src="{image}" style="width:95%">
            <div style="display: flex; align-items: center; margin-top: 10px;">
                <span style="font-size: 20px; margin-right: 3px;">❤️</span>
                <span style="font-size: 15px;">{likes}</span>
                <span style="font-size: 20px; margin-left: 10px; margin-right: 3px;">⭐</span>
                <span style="font-size: 15px;">{collections}</span>
                <span style="font-size: 20px; margin-left: 10px; margin-right: 3px;">💬</span>
                <span style="font-size: 15px;">{comments}</span>
            </div>
            <a href="{link}" target="_blank" style="text-decoration: none; color: blue; display: block; margin-top: 10px;">
                <h4 style="margin: 0;">Read more</h4>
            </a>
        </div>
    </body>
    </html>
    """
    return html
