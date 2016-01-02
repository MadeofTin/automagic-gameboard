
# Board Design


Go is played on a 19x19 board. That means there are 361 different possible places you can place a stone. But, sometimes you place a stone in a whole surrounded by other stones. If a board was going to move a piece into one of those it would need to be able to move the surrounding stones to the side while maintaining the state of the board. 

![board position](https://docs.google.com/drawings/d/1_1M-o0svgAh_4IqHX_HJmS3yj5bIYeInQkfLHPykSQ8/pub?w=400)

## Pin Mechanism
![Moving Pins](https://docs.google.com/drawings/d/14bEfK6NYotXaWkZ-BxQ3KW4m4vwG1d_WnZmKQ5pUg9k/pub?w=300)
