How to Format A File For This Translator
========================================

In our ExampleData.txt we have

     3
     Data
     1
     a
     Data2
     2
     b
     Data3
     3
     c

From this, in ExampleResults.csv we get

<table>
<tr>
    <td>Data</td>
    <td>1</td>
    <td>a</td>
</tr>
<tr>
    <td>Data2</td>
    <td>2</td>
    <td>b</td>
</tr>
<tr>
    <td>Data3</td>
    <td>3</td>
    <td>c</td>
</tr>
</table>
Lets break this down. The "3" means that there are 3 lines per row. This means that each time you write the file you write it with three datapoints on a newline each. After this, everything is pretty self-expanatory. Data, 1, and a become a row, then Data2, 2, and b are a row etc.
