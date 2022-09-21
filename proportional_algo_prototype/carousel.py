def build_html(views, n):
    result = '''
        <style>
        .carousel {
            display: flex;
            flex-wrap: wrap;
        }
        
        .carousel-card {
            border: solid 1px black;
            width: 100px;
            text-align: center;
            font-size: 24px;
            margin: 3px;
        }
        </style>
    '''
    cards_html = ''
    for view in views:
        green = (view + 1) * 254 / n
        color = f'rgb(0, {green:.0f}, 0)'
        text_color = 'white' if green < 150 else 'black'
        card_html = f'<div class="carousel-card" style="background-color:{color}; color:{text_color}">#{view + 1}</div>'
        cards_html += card_html
    result += f'''
        <div class="carousel">
            {cards_html}
        </div>
    '''

    return result
