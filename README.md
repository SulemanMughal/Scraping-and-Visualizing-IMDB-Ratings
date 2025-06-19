# Scraping and Visualizing IMDB Ratings

[![Python](https://img.shields.io/badge/python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![Web Scraping](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-brightgreen)](https://www.crummy.com/software/BeautifulSoup/)
[![Data Visualization](https://img.shields.io/badge/Data%20Visualization-Matplotlib-orange)](https://matplotlib.org/)
[![License](https://img.shields.io/github/license/SulemanMughal/Scraping-and-Visualizing-IMDB-Ratings)](LICENSE)

> **Tagline:** Instantly fetch and visualize IMDB TV series episode ratings.
>  
> **Tags:** web scraping, IMDB, data visualization, TV ratings, Python, automation

---

## Overview

**Scraping and Visualizing IMDB Ratings** is a Python-based tool that automates the extraction of episode ratings for any TV series from IMDB and presents the data in an insightful, visual format. Whether you're a data enthusiast, TV series analyst, or simply curious about how ratings fluctuate across seasons, this project provides a seamless workflow for scraping, processing, and visualizing IMDB ratings.

---

## Key Features

- ⚡ **Automated Web Scraping:** Seamlessly scrapes IMDB for TV series episode ratings across all seasons.
- 📊 **Data Visualization:** Generates clear, informative charts to visualize rating trends over time.
- 🔄 **Multi-page Handling:** Supports scraping across multiple IMDB pages for complete data retrieval.
- 📁 **Flexible Input:** Works with any TV series listed on IMDB.
- 📝 **Comprehensive Output:** Provides tabular data and graphical plots for further analysis.

---

## Working Flow

1. **Web Scraping:**  
   The tool uses Python scripts (leveraging libraries such as BeautifulSoup and Requests) to automatically collect episode ratings from the IMDB website for a specified TV series.

2. **Data Processing:**  
   Extracted data is cleaned and structured using Python's data management libraries (such as Pandas).

3. **Visualization:**  
   The processed data is visualized using Matplotlib, generating insightful charts—such as line plots of ratings per episode/season.

4. **Output:**  
   Both tabular data (CSV/Excel) and visual plots (PNG/JPG) are saved for review and further use.

---

## Technologies Used

- **Python 3.7+**
- **BeautifulSoup** (Web Scraping)
- **Requests** (Web Requests)
- **Pandas** (Data Manipulation)
- **Matplotlib** (Data Visualization)

---

## Example Screenshots

![Ratings Table](https://github.com/SulemanMughal/Scraping-and-Visualizing-IMDB-Ratings/blob/main/demo.PNG)
![Rating Chart](https://github.com/SulemanMughal/Scraping-and-Visualizing-IMDB-Ratings/blob/main/Figure_1.png)

---

## Getting Started

1. Clone the repository:  
   `git clone https://github.com/SulemanMughal/Scraping-and-Visualizing-IMDB-Ratings.git`
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Run the script, specifying your desired IMDB TV series.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
