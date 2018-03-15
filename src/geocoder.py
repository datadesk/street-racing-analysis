import time
import pandas as pd
from googlegeocoder import GoogleGeocoder
geocoder = GoogleGeocoder()


def geocode(row):
    """
    Accepts a row from our fatalities list. Returns it with geocoded coordinates.
    """
    # If it's already been geocoded, it's already mapped and just return the row.
    if hasattr(row, 'geocoder_x') and not pd.isnull(row.geocoder_x):
        row['is_mapped'] = True
        return row
    
    try:
        search = geocoder.get(row['full_event_address'])
        # If there's a hit, add it to the row.
        hit = search[0]
        row['geocoder_address'] = hit.formatted_address
        row['geocoder_x'] = hit.geometry.location.lng
        row['geocoder_y'] = hit.geometry.location.lat
        row['is_mapped'] = True
    except ValueError:
        # If there's not a match, return a blank row
        row['geocoder_address'] = pd.np.NaN
        row['geocoder_x'] =  pd.np.NaN
        row['geocoder_y'] =  pd.np.NaN
        row['is_mapped'] = False

    # Add a little delay at the end so we don't get banned.
    time.sleep(1)
    
    # Return the row
    return row