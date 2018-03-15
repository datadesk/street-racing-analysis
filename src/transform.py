import collections
import geopandas as gpd
from shapely.geometry import Point


def df_to_gdf(input_df, crs={'init': u'epsg:4269'}):
    """
    Accepts a DataFrame with longitude and latitude columns. Returns a GeoDataFrame.
    """
    df = input_df.copy()
    geometry = [Point(xy) for xy in zip(df.geocoder_x, df.geocoder_y)]
    return gpd.GeoDataFrame(df, crs=crs, geometry=geometry)


def groupby_point(input_gdf):
    """
    Accepts a GeoDataFrame and regroups it by point.
    """
    points_df = input_gdf.groupby([
        'geocoder_x',
        'geocoder_y'
    ]).size().reset_index()
    points_df.columns = ["geocoder_x", "geocoder_y", "fatalities"]
    points_gdf = df_to_gdf(points_df)
    return points_gdf


# A crosswalk between our raw columns and what we'd prefer to call them.
columns = collections.OrderedDict(
    CaseNum='case_number',
    Age='age',
    Race='race',
    Gender='gender',
    VictimRole='victim_role',
    DeathDateTime='death_datetime',
    full_event_address='event_address',
    geocoder_x='geocoder_x',
    geocoder_y='geocoder_y',
    is_mapped='is_mapped',
)