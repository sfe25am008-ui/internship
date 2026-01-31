def bubble_chart(df):
    if not is_within_time(time(17,0), time(19,0)):
        return None

    allowed = ['Game','Beauty','Business','Comics','Communication',
               'Dating','Entertainment','Social','Events']

    df_f = df[
        (df['Rating'] > 3.5) &
        (df['Category'].isin(allowed)) &
        (df['Reviews'] > 500) &
        (~df['App'].str.contains('S')) &
        (df['Sentiment_Subjectivity'] > 0.5) &
        (df['Installs'] > 50000)
    ]

    translations = {'Beauty':'सुंदरता','Business':'வணிகம்','Dating':'Dating (DE)'}
    df_f['Category'] = df_f['Category'].replace(translations)

    import plotly.express as px
    fig = px.scatter(
        df_f,
        x='Size_MB',
        y='Rating',
        size='Installs',
        color='Category',
        title='Size vs Rating Bubble Chart'
    )
    fig.update_traces(marker=dict(line=dict(width=2)))
    return fi