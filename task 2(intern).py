#Filters
df2 = df[
    (df['Installs'] >= 10000) &
    (df['Revenue'] >= 10000) &
    (df['Android_Version'] > 4.0) &
    (df['Size_MB'] > 15) &
    (df['Content_Rating'] == 'Everyone') &
    (df['App'].str.len() <= 30)
]

#Top 3 Categories
top3 = df2.groupby('Category')['Installs'].sum().nlargest(3).index
df2 = df2[df2['Category'].isin(top3)]

#Plot
fig = go.Figure()

fig.add_bar(x=df2['Type'], y=df2['Installs'], name='Avg Installs')
fig.add_scatter(
    x=df2['Type'], y=df2['Revenue'],
    yaxis='y2', mode='lines+markers', name='Revenue'
)

fig.update_layout(
    yaxis2=dict(overlaying='y', side='right')
)