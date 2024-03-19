*Updated: {% assign copenhagen_time = site.time | date: "%d-%m-%Y %H:%M:%S" | date: "%s" | plus: 3600 | date: "%d-%m-%Y %H:%M:%S" %}{{ copenhagen_time }}*


__Introduction__\
The data that we are working with in this project is *Police Department Incident Reports: Historical 2003 to May 2018*, which is provided by the City and County of San Francisco. The data is about historical reported crimes in San Francisco. It contains 14 columns, each providing essential infomation about the observation, such as time, position and categori of the crime. In this project, we will be focusing on the crime category prostitution and explore how this crime has developed over time.


__First plot__\
![One time-series / bar chart](/A2/plot1.png)


__Second plot__
<div style="display: flex; justify-content: space-between;">
    <div>
        <embed 
                     type="text/html" 
                     src="/A2/plot21.html"
                     width="550"
                     height="600"
                     >
    </div>
    <div>
        <embed 
                     type="text/html" 
                     src="/A2/plot22.html"
                     width="550"
                     height="600"
                     >
    </div>
</div>


