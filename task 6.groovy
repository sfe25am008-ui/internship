def time_series_growth(df):
    if not is_within_time(time(18,0), time(21,0)):
        return None

    df_f = df[
        (~df['App'].str.startswith(('x','y','z'))) &
        (df['Category'].str.startswith(('E','C','B'))) &
        (df['Reviews'] > 500) &
        (~df['App'].str.contains('S'))
    ]

    translations = {'Beauty':'सुंदरता','Business':'வணிகம்','Dating':'Dating (DE)'}
    df_f['Category'] = df_f['Category'].replace(translations)

    import plotly.express as px
    fig = px.line(
        df_f,
        x='Date',
        y='Installs',
        color='Category',
        title='Installs Growth Over Time'
    )
    return fig