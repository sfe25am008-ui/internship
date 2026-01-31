#Filters
df3 = df[
    (~df['Category'].str.startswith(tuple('ACGS'))) &
    (df['Installs'] > 1_000_000)
]

#Top 5 Categories
top5 = df3.groupby('Category')['Installs'].sum().nlargest(5).index
df3 = df3[df3['Category'].isin(top5)]

#Plotly Choropleth
fig = px.choropleth(
    df3,
    locations='Country_Code',
    color='Installs',
    hover_name='Category',
    color_continuous_scale='Viridis'
)
