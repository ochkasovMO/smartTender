def clear_data(df):
    clear_cols = df.columns[[0, 1, 2,3, 4,5, 6, 8, 9, 19, 25, 27, 29, 30, 33, 35, 37, 39]]
    df = df.drop(clear_cols, axis=1)
    ORGANIZER_OKPO_TO_DROP = '00000000'
    df = df[df['organizer_okpo'] != ORGANIZER_OKPO_TO_DROP]
    df = df[df['supplier_okpo'] != ORGANIZER_OKPO_TO_DROP]
    return df