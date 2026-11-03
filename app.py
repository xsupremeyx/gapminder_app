# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(page_title="Gapminder Explorer", layout="wide")

# @st.cache_data
# def load():
#     return pd.read_csv("exp10_gapminder.csv")

# df = load()

# # ---------- Sidebar filters ----------
# st.sidebar.header("Filters")
# all_continents = sorted(df.continent.unique())
# continents = st.sidebar.multiselect("Continent", all_continents, default=all_continents)
# years = st.sidebar.slider("Year", int(df.year.min()), int(df.year.max()), (1952, 2007), step=5)
# country_search = st.sidebar.text_input("Search country")

# # base: continent + year filters only (drives country list and trend chart)
# base = df[df.continent.isin(continents) & df.year.between(*years)]

# # fdf: base plus country search (drives KPIs, snapshot charts, table)
# fdf = base
# if country_search:
#     fdf = base[base.country.str.contains(country_search, case=False)]

# if fdf.empty:
#     st.warning("No data matches the current filters. Select at least one continent, or change the year range or search.")
#     st.stop()

# # ---------- Header and KPI cards ----------
# st.title("Gapminder World Development Explorer")

# c1, c2, c3, c4 = st.columns(4)
# c1.metric("Countries", fdf.country.nunique())
# c2.metric("Avg life expectancy", f"{fdf.lifeExp.mean():.1f} yrs")
# c3.metric("Total population", f"{fdf['pop'].sum():,.0f}")
# c4.metric("Median GDP per capita", f"${fdf.gdpPercap.median():,.0f}")

# # ---------- Snapshot year ----------
# year_pick = years[1]          # upper bound of the year range
# snap = fdf[fdf.year == year_pick]

# # ---------- Bubble chart ----------
# st.subheader(f"GDP vs life expectancy, {year_pick}")
# if snap.empty:
#     st.info(f"No countries in the filtered set have data for {year_pick}. Move the upper year bound to a 5-year step (1952, 1957, ... 2007).")
# else:
#     fig = px.scatter(
#         snap, x="gdpPercap", y="lifeExp", size="pop", color="continent",
#         hover_name="country", log_x=True,
#         labels={"gdpPercap": "GDP per capita (US$, log)", "lifeExp": "Life expectancy (years)"},
#     )
#     st.plotly_chart(fig, use_container_width=True)

# # ---------- Trend over time ----------
# st.subheader("Trend over time")
# metric = st.selectbox("Metric", ["lifeExp", "gdpPercap", "pop"])
# all_countries = sorted(base.country.unique())
# default_picks = [c for c in ["India", "China"] if c in all_countries]
# picked = st.multiselect("Countries", all_countries, default=default_picks)
# trend = base[base.country.isin(picked)]
# if trend.empty:
#     st.info("Pick at least one country to see its trend.")
# else:
#     st.plotly_chart(
#         px.line(trend, x="year", y=metric, color="country", markers=True),
#         use_container_width=True,
#     )

# # ---------- Top-N ranking ----------
# st.subheader("Top N ranking")
# n = st.slider("N", 5, 20, 10)
# if snap.empty:
#     st.info("No ranking available for this year.")
# else:
#     top = snap.nlargest(n, metric)
#     st.plotly_chart(
#         px.bar(top, x=metric, y="country", orientation="h", color="continent"),
#         use_container_width=True,
#     )

# # ---------- Data table and download ----------
# st.subheader("Filtered data")
# st.dataframe(fdf, use_container_width=True)
# st.download_button(
#     "Download CSV",
#     fdf.to_csv(index=False),
#     "gapminder_filtered.csv",
#     "text/csv",
# )

import streamlit as st
st.title("Hello")