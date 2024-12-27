{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNTgnZPCoiyy+bE8F8ca3Bl",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Catz94/Practical-Discrete-Mathematics/blob/master/Assigment_3d.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install folium pandas"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QPf43z_C-4LW",
        "outputId": "63820b76-b295-4a36-e7f6-daf8785b2e02"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: folium in /usr/local/lib/python3.10/dist-packages (0.19.2)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (2.2.3)\n",
            "Requirement already satisfied: branca>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from folium) (0.8.1)\n",
            "Requirement already satisfied: jinja2>=2.9 in /usr/local/lib/python3.10/dist-packages (from folium) (3.1.5)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from folium) (2.2.1)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from folium) (2.32.3)\n",
            "Requirement already satisfied: xyzservices in /usr/local/lib/python3.10/dist-packages (from folium) (2024.9.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2>=2.9->folium) (3.0.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->folium) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->folium) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->folium) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->folium) (2024.12.14)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install streamlit folium pandas streamlit-folium"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xij1gcj1-7lb",
        "outputId": "690a00df-17fd-45c6-890b-19f73dc9427b"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/dist-packages (1.41.1)\n",
            "Requirement already satisfied: folium in /usr/local/lib/python3.10/dist-packages (0.19.2)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (2.2.3)\n",
            "Requirement already satisfied: streamlit-folium in /usr/local/lib/python3.10/dist-packages (0.24.0)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.2.1)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (11.0.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.25.5)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: branca>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from folium) (0.8.1)\n",
            "Requirement already satisfied: jinja2>=2.9 in /usr/local/lib/python3.10/dist-packages (from folium) (3.1.5)\n",
            "Requirement already satisfied: xyzservices in /usr/local/lib/python3.10/dist-packages (from folium) (2024.9.0)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (1.18.4)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2>=2.9->folium) (3.0.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.12.14)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import folium\n",
        "import pandas as pd\n",
        "from folium import FeatureGroup\n",
        "from streamlit_folium import st_folium\n",
        "\n",
        "# Load the data from the CSV file\n",
        "file_path = \"malaysia_tourist_attractions.csv\"  # Ensure this file exists\n",
        "data = pd.read_csv(file_path)\n",
        "\n",
        "# Define marker colors based on categories\n",
        "category_colors = {\n",
        "    \"Landmark\": \"blue\",\n",
        "    \"Cultural\": \"red\",\n",
        "    \"Nature\": \"green\",\n",
        "    \"Amusement\": \"orange\"\n",
        "}\n",
        "\n",
        "# Create a base map centered on Malaysia\n",
        "map_malaysia = folium.Map(location=[4.2105, 101.9758], zoom_start=6)\n",
        "\n",
        "# Create a feature group for each category\n",
        "categories = data[\"Category\"].unique()\n",
        "feature_groups = {category: FeatureGroup(name=category) for category in categories}\n",
        "\n",
        "# Add markers for each attraction into their respective feature groups\n",
        "for _, row in data.iterrows():\n",
        "    # Define the color for the marker based on the category\n",
        "    marker_color = category_colors.get(row[\"Category\"], \"gray\")\n",
        "\n",
        "    # Construct the popup content\n",
        "    popup_content = (\n",
        "        f\"<b>{row['Name']}</b><br>\"\n",
        "        f\"<i>Description</i>: {row['Description']}<br>\"\n",
        "        f\"<i>Category</i>: {row['Category']}<br>\"\n",
        "        f\"<i>State</i>: {row['State']}<br>\"\n",
        "        f\"<i>Opening Hours</i>: {row['Opening Hours']}<br>\"\n",
        "        f\"<i>Admission Fee</i>: {row['Admission Fee']}<br>\"\n",
        "        f\"<i>Website</i>: <a href='{row['Official Website']}' target='_blank'>\"\n",
        "        f\"{row['Official Website']}</a>\"\n",
        "    )\n",
        "\n",
        "    # Add marker to the corresponding feature group\n",
        "    folium.Marker(\n",
        "        location=[row[\"Latitude\"], row[\"Longitude\"]],\n",
        "        popup=folium.Popup(popup_content, max_width=300),\n",
        "        tooltip=row[\"Name\"],  # Tooltip to show the name of the attraction\n",
        "        icon=folium.Icon(color=marker_color, icon=\"info-sign\")\n",
        "    ).add_to(feature_groups[row[\"Category\"]])\n",
        "\n",
        "# Add feature groups to the map\n",
        "for category, group in feature_groups.items():\n",
        "    group.add_to(map_malaysia)\n",
        "\n",
        "# Add layer control for toggling categories\n",
        "folium.LayerControl().add_to(map_malaysia)\n",
        "\n",
        "# Streamlit App\n",
        "st.title(\"Interactive Map of Malaysia Tourist Attractions\")\n",
        "\n",
        "# Display the map\n",
        "st.write(\"Toggle attraction categories using the layer control below the map.\")\n",
        "st_folium(map_malaysia, width=800, height=600)\n",
        "\n",
        "# Display the total number of attractions at the bottom\n",
        "total_attractions = len(data)\n",
        "st.markdown(\"<hr>\", unsafe_allow_html=True)\n",
        "st.write(f\"### Total Tourist Attractions: {total_attractions}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VzvKZgr_--jr",
        "outputId": "f362968f-97a9-498d-bf93-f1231c87cf28"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-12-27 16:41:36.955 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:36.956 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:36.959 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:36.961 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:36.964 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:36.965 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.035 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.036 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.040 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.043 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.045 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.047 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.049 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-12-27 16:41:37.057 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}