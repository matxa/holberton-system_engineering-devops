### <small>AUTHOR: MARCELO</small>
### PROJECT
<h1>0x15-api</h1>

## DESCRITION
<p>Make requests to API (<a href="https://jsonplaceholder.typicode.com/">
https://jsonplaceholder.typicode.com/</a>) using the requests module and saving reponse to different file formats ( .json and .csv )</p>

## MODULES

<b>csv</b> &#9660;
<pre>
    <b>Descrition</b>: format is the most common import and export format for spreadsheets and databases.
    <b>FUNCTIONS or METHODS used</b>:
        writer() - Return a writer object responsible for converting the user’s data into delimited
        strings on the given file-like object. csvfile can be any object with a write() method
        writerow() - adds row to the file object specified by writer
</pre>

<b>json</b> &#9660;
<pre>
    <b>Descrition</b>: a popular data format used for representing structured data.
    <b>FUNCTIONS or METHODS used</b>:
        json.load(): get data from json file
        json.dump(): save data to file in json format
</pre>
<b>requests</b> &#9660;
<pre>
    <b>Descrition</b>: allows you to send HTTP/1.1 requests extremely easily

    <b>FUNCTIONS or METHODS used</b>: 
        get(): for sending a get request and saving HTTP body response
</pre>

<b>sys</b> &#9660;
<pre>
    <b>Descrition</b>: manipulate different parts of the Python runtime environment.
    <b>FUNCTIONS or METHODS used</b>:
        argv: returns a list of command line arguments passed to a Python script.
</pre>


## HELPFUL LINKS &#8744;
<pre>
    <a  href="https://docs.python.org/3/library/csv.html">CSV</a>
    <a  href="https://www.programiz.com/python-programming/json">JSON</a>
    <a  href="https://www.programiz.com/python-programming/methods/built-in/open">open()</a>
    <a  href="https://requests.readthedocs.io/en/master/">Requests</a>
</pre>
