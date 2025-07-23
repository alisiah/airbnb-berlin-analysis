def clean_airbnb_data(df):
    df = df.copy()
    df = df[df['price'].notnull()]
    
    # Replace dollar signs ($) and commas (,) with an empty string in "price"- column:
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Drop columns (because of too many nulls):
    df = df.drop(columns=['name', 'host_name'], errors='ignore')

    # Filter out extreme prices (For better statistics):
    df = df[(df['price'] > 10) & (df['price'] < 500)]

    return df
