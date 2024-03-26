*Updated: {% assign copenhagen_time = site.time | date: "%d-%m-%Y %H:%M:%S" | date: "%s" | plus: 3600 | date: "%d-%m-%Y %H:%M:%S" %}{{ copenhagen_time }}*


__Introduction__\
The data that we are working with in this project is *\*Police Department Incident Reports: Historical 2003 to May 2018\**, which is provided by the City and County of San Francisco. The data is about historical reported crimes in San Francisco. It contains 35 columns, each providing essential infomation about the observation, such as time, position and categori of the crime. In this project, we will be focusing on the crime category prostitution and explore how this crime has developed over time and in the different districts of San Francisco.


__First plot__\
_Short intro_

![One time-series / bar chart](/A2/plot1.png)

In the first plot of the subplot, a comprehensive overview of the crime trend from 2003 to 2015 is presented. It can be seen, that the prostitution rate peaked in 2003 and again in 2007, from where it steadily declined until 2015.

Looking closer at the subplot, Thursdays emerged as the day with the highest frequency of crimes, totaling 3630 incidents, whereas Sundays witnessed the fewest, with only 1059 reported crimes, .

<div style="margin-left: auto;
            margin-right: auto;
            width: 50%">

| Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|--------|---------|-----------|----------|--------|----------|--------|
|  1123  |   3003  | 3291      | 3630     | 2776   | 1571     | 1059   |



_Table 1: Total amount of prostitution crimes on the different weekdays._
</div>



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

