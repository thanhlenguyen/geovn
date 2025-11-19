import folium


class Map(folium.Map):
    def __init__(self, center=(0,0), zoom_start=2, **kwargs):
        super().__init__(center=center, zoom_start=zoom_start, **kwargs)
        folium.LayerControl().add_to(self)


