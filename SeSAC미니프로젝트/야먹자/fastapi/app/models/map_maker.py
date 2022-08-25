import pandas as pd
import folium
from folium.features import CustomIcon
from folium import Marker, Icon, CircleMarker
from app.config import BASE_DIR

class Make_map:
    
    def load_data(data):
        df = pd.DataFrame(list(data))
        return df
    
    def makemap(df):
        m = folium.Map(location=[37.5222564, 126.9120236], zoom_start=14)

        for idx in df.index:
            folium.Marker([df['Y'][idx], df['X'][idx]],
                            popup=folium.Popup('<center><strong>'+ df['stores'][idx] + '</strong></center><br>'\
                                                + '별점 : '+ df['rating'][idx] + '<br>'\
                                                + '분류 : ' + df['category'][idx] + '<br>'\
                                                + '전화번호 : ' + df['phone_number'][idx] + '<br>'\
                                                + '영업시간 : ' + df['business_hours'][idx] + '<br>'\
                                                + '<a href=' + df['place_url'][idx] + '>' + ' 자세히 보기' + '</a><br>', max_width = 400),
            tooltip=df['stores'][idx]).add_to(m)
        return m._repr_html_()