# Last 100+ years Bangladesh-India-Bhutan-Myanmar(BIBM) region's Earthquake Data Analysis
Here, I did some data analysis using the last 100+ years of Earthquake data covering South Asia and Bangladesh region

This was a web scraping project along with dashboard visualization on Tableau.

I scraped and extracted data from a website using Python with the help of Request and BeautifulSoup libraries.
The source of the data was this [website](https://www.volcanodiscovery.com/earthquakes/bangladesh/largest.html).

This project aimed to scrape and extract data for data analysis on Earthquake data encompassing Bangladesh and other neighboring countries like India, Myanmar & Nepal. This analysis was done to get insights into the data like the magnitudes of the Earthquakes that took place over the last few years, where, occurred mostly in which month and in which region, and more.
The insights from the extracted data were later visualized using the popular data visualization tool, Tableau.

Note: This website only shows earthquakes since 1900 starting from a minimum magnitude of 5 or higher.


Here's the link to the Tableau Dashboard for the scraped data: Earthquake Data Tableau Dashboard [14 Sheets & 8 Dashboards](https://public.tableau.com/app/profile/md.reuzwan.hassan/viz/Last100yearsEarthquakeData-Analysis/TotalEarthquakeinBangladeshIndiaNepalMyanmarBINMsub-regionMap)


## CSV File (Data Example):

CSV file link: [File](https://github.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/blob/main/csv_files/EarthquakeData.csv)

| Serial        | Date             | Day    | Month  | Year        | Time (GMT)	  | Latitude (N)  | Longitude (E) | Magnitude  | Location                           | Country              |
| ------------- |:----------------:|:-------|:------:|:-----------:|:------------:|:-------------:|:-------------:|:----------:|:----------------------------------:| --------------------:|	
| 0             |Jun 16, 2023	   |16      |June    |2023	       |04:46         |24.75          |	92.0418       |5.0         |Near Shillong                   	| India                |
| 1             |Nov 25, 2021	   |25      |November|2021	       |23:45         |22.81          |	93.5248       |6.2         |Myanmar (Burma): 19 Km SW of Falam	| Myanmar              |
| 2             |Apr 28, 2021	   |28      |April   |2021	       |2:24          |26.75          |	92.42         |6.0         |Northeastern India                	| India                |
| 3             |Oct 10, 2020	   |10      |October |2020	       |17:38	      |24.56	      |93.58	      |5.4	       |Myanmar-India Border Region	        |Myanmar-India Border  |
| 4	            |Aug 30, 2020	   |30      |August	 |2020	       |1:47	      |23.4098	      |92.0087	      |5.1	       |33 Km N of Khagrachhari	            |Bangladesh            |
| 5             |Aug 27, 2020	   |27      |August	 |2020	       |12:07         |23.06          |93.29          |5.3         |Myanmar-India Border Region         |Myanmar-India Border  |
| 6             |Jun 21, 2020	   |21      |June    |2020         |22:40         |23.15          |93.32          |5.5         |Myanmar-India Border Region	        |Myanmar-India Border  |

## Findings and Observations from the Dashboard

![Earthquake magnitude over time in the last 100+ years.png](https://raw.githubusercontent.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/main/dashboard_images/Earthquake%20magnitude%20over%20time%20in%20the%20last%20100%2B%20years.png) 
[Dashboard Link](https://public.tableau.com/app/profile/md.reuzwan.hassan/viz/Last100yearsEarthquakeData-Analysis/Earthquakemagnitudeovertimeinthelast100years)

1. The highest recorded earthquake in the last hundred-plus years in this Bangladesh-India-Nepal_Myanmar region was 7.2 in magnitude on 8th July 1918. It took place in Bangladesh.
2. The lowest recorded earthquake in the last hundred-plus years in this Bangladesh-India-Nepal_Myanmar region was 5 in magnitude which took place in multiple regions of BIBM, But mostly in India and India-Bangladesh border region.

![Regionwise Earthquake occurance frequency over time in the last 100+ years.png](https://raw.githubusercontent.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/main/dashboard_images/Regionwise%20Earthquake%20occurance%20frequency%20over%20time%20in%20the%20last%20100%2B%20years.png)
[Dashboard Link](https://public.tableau.com/views/Last100yearsEarthquakeData-Analysis/RegionwiseEarthquakeoccurancefrequencyovertimeinthelast100years?:language=en-US&:display_count=n&:origin=viz_share_link)

3. The greatest number of earthquakes took place in India (49 in total)
4. In the Bangladesh region, There were respectively 22, 7, & 1 earthquakes in the Bangladesh-India border region, Bangladesh, and Bangladesh-Myanmar border region.
5. The lowest number of earthquakes took place in Bhutan and Myanmar-Bangladesh border regions (Both 1).

![Region wise Earthquake occurance frequency over time in the last 100+ years monthly categorized.png](https://raw.githubusercontent.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/main/dashboard_images/Region%20wise%20Earthquake%20occurance%20frequency%20over%20time%20in%20the%20last%20100%2B%20years%20monthly%20categorized.png)
[Dashboard Link](https://public.tableau.com/views/Last100yearsEarthquakeData-Analysis/RegionwiseEarthquakeoccurancefrequencyovertimeinthelast100yearsmonthlycategorized?:language=en-US&:display_count=n&:origin=viz_share_link)

6. In BIBM region, earthquakes mostly took place in February, September & December. All 7 in number and all in India.
7. In Bangladesh region, earthquakes mostly took place in November in the India-Bangladesh border region. 4 in quantity.

![Region wise Earthquake occurance frequency over time in the last 100+ years monthly categorized (Total).png](https://raw.githubusercontent.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/main/dashboard_images/Region%20wise%20Earthquake%20occurance%20frequency%20over%20time%20in%20the%20last%20100%2B%20years%20monthly%20categorized%20(Total).png)
[Dashboard Link](https://public.tableau.com/views/Last100yearsEarthquakeData-Analysis/RegionwiseEarthquakeoccurancefrequencyovertimeinthelast100yearsmonthlycategorizedTotal?:language=en-US&:display_count=n&:origin=viz_share_link)

8. In BIBM region, a maximum number of earthquakes took place in November. 13 in total.
9. In Bangladesh region, a maximum number of earthquakes took place in July & November Both 5 in quantity.

![Probable Earthquake occurring time in a day.png](https://raw.githubusercontent.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/main/dashboard_images/Probable%20Earthquake%20occurring%20time%20in%20a%20day.png)
[Dashboard Link](https://public.tableau.com/views/Last100yearsEarthquakeData-Analysis/ProbableEarthquakeoccurringtimeinaday?:language=en-US&:display_count=n&:origin=viz_share_link)

10. In BIBM region, Earthquakes mostly took place around 20.00 GMT, All in India and total of 5 in quantity.
11. In Bangladesh region, Earthquakes mostly took place around 7.00 GMT & 11.00 GMt, All in the India-Bangladesh border region & both 3 in quantity.

![Probable Earthquake occurance time in a month.png](https://raw.githubusercontent.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/main/dashboard_images/Probable%20Earthquake%20occurance%20time%20in%20a%20month.png)
[Dashboard Link](https://public.tableau.com/views/Last100yearsEarthquakeData-Analysis/ProbableEarthquakeoccurancetimeinamonth?:language=en-US&:display_count=n&:origin=viz_share_link)

12. In BIBM region, Earthquakes mostly took place on the 2nd day of the month, 6 in quantity.
13. In Bangladesh region, Earthquakes mostly took place on the 7th day of the month, 3 in quantity.

![Location wise Earthquake count (BIBM).png](https://raw.githubusercontent.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/main/dashboard_images/Location%20wise%20Earthquake%20count%20(BINM).png)
[Dashboard Link](https://public.tableau.com/views/Last100yearsEarthquakeData-Analysis/LocationwiseEarthquakecountBINM?:language=en-US&:display_count=n&:origin=viz_share_link)

14. Location-wise, In BIBM region Earthquakes mostly took place in the India-Bangladesh border region (22), then Assam (21), and then the Myanmar-India border region (17).

![Total Earthquake in Bangladesh, India, Bhutan & Myanmar (BIBM) sub-region (Map).png](https://raw.githubusercontent.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/main/dashboard_images/Total%20Earthquake%20in%20Bangladesh%2C%20India%2C%20Nepal%20%26%20Myanmar%20(BINM)%20sub-region%20(Map).png)
[Dashboard Link](https://public.tableau.com/views/Last100yearsEarthquakeData-Analysis/TotalEarthquakeinBangladeshIndiaNepalMyanmarBINMsub-regionMap?:language=en-US&:display_count=n&:origin=viz_share_link)

15. Country-wise, In the BIBM region, The name of the countries and the number of total earthquakes since 1918 are   Bangladesh (7), India (49), Bhutan (1) & Myanmar (14).


## Run Locally:

1. Clone the repository

```
git clone https://github.com/RezuwanHassan262/Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization
```

2. Go to the project directory

```
cd Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization
```

3. Initialize and activate Virtual Environment

```
virtualenv --no-site-packages  venv
source venv/bin/activate
```

4. Install dependencies

```
pip install -r requirements.txt
```
5. Run the scrapper:

```
python Last-100-plus-years-Earthquake-Data-Analysis-And-Visualization/scraper.py 
```

6. The CSV file named 'EarthquakeData.csv' will be generated within the project directory.



    


