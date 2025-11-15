import streamlit as st
import requests
import pandas as pd
import altair as alt # for my data

def dataStuff():

    st.title("Rick and Morty API Explorer")

    #Character overview
    st.header("Character Search")

    char_name = st.text_input("Search for a character:")

    if char_name.strip() != "":
        url = f"https://rickandmortyapi.com/api/character/?name={char_name}"
        resp = requests.get(url)

        if resp.status_code != 200:
            st.error("Character not found.")
            return

        data = resp.json().get("results", [])
        if len(data) == 0:
            st.warning("No match found.")
            return

        c = data[0]

        st.subheader(c["name"])
        st.image(c["image"], width=200)

        st.write(f"**Status:** {c['status']}")
        st.write(f"**Species:** {c['species']}")
        st.write(f"**Gender:** {c['gender']}")
        st.write(f"**Origin:** {c['origin']['name']}")
        st.write(f"**Appears in:** {len(c['episode'])} episodes")

        ep_df = pd.DataFrame({
            "stat": ["Episode Appearances"],
            "value": [len(c["episode"])]
        })

        st.subheader("Character Episode Count")

        chart = (
            alt.Chart(ep_df)
            .mark_bar()
            .encode(
                x="stat:N",
                y="value:Q",
                tooltip=["stat", "value"]
            )
            .interactive()
        )

        st.altair_chart(chart, use_container_width=True)

    st.write("---")

    #Num of Humans vs Ailens
    st.header("Num of Humans vs Ailens")

    count_limit = st.slider("How many top species should be shown?", 3, 10, 5)

    url = "https://rickandmortyapi.com/api/character"
    first_page = requests.get(url).json()

    df = pd.DataFrame(first_page["results"])

    species_counts = df["species"].value_counts().head(5).reset_index()
    species_counts.columns = ["species", "count"]

    chart2 = (
        alt.Chart(species_counts)
        .mark_bar()
        .encode(
            x="species:N",
            y="count:Q",
            tooltip=["species", "count"]
        )
        .interactive()
    )

    st.altair_chart(chart2, use_container_width=True)
    st.dataframe(species_counts)
