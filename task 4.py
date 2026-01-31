def stacked_area_installs(df):
    if not is_within_time(time(16,0), time(18,0)):
        return None

    df_f = df[
        (df['Rating'] >= 4.2) &
        (~df['App'].str.contains(r'\d')) &
        (df['Category'].str.startswith(('T','P'))) &
        (df['Reviews'] > 1000) &
        (df['Size_MB'].between(20,80))
    ]

    translations = {
        'Travel & Local':'Voyage et Local',
        'Productivity':'Productividad',
        'Photography':'写真'
    }
    df_f['Category'] = df_f['Category'].replace(translations)

    import plotly.express as px
    return px.area(
        df_f,
        x='Date',
        y='Installs',
        color='Category',
        title='Cumulative Installs Over Time',
    )
