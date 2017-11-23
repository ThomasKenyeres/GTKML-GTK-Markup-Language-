# GTKML-GTK-Markup-Language-
Smart framework for rapid desktop development in Python and GTK+

You will be able to develop GTK+(3.*) applications as easily as an HTML document.
You only have to create an XML file and start your application with GTKML runtime environment.

Planned features (in first release)
* Python script integration (similar to JavaScript integration in HTML)
* Builtin python libraries for e.g.: HTTP requests, jQuery-like feature etc.

####Run your application(source):
```sh
python3 <directory where GTKML is unpacked\>/gtkml/runtime/main.py <your application's xml\>
```




####Sample:
app.xml
```xml
<application>

<window show="True">
    <meta></meta>
    <header>
        <python src="funcs.py"></python>    
        <title></title>
    </header>
    <body>
            <label 
            id="lbl1" color="red" 
                onclick="lbl1_clicked()">
                Hello world!
            </label>        
    </body>
</window>

</application>
```
funcs.py
```python
def lbl1_clicked():
    _("#lbl1").set_text("Hi there!")

def fill():
    content = _.get("http://example.com/content")
    for item in content:
        _("body").append(Label(item["name"]))
```

----------------------

Working example:
<img src="https://github.com/ThomasKenyeres/GTKML-GTK-Markup-Language-/blob/6cdf37e2e546cd663ab051fb5a26b3c8d5c861f8/img/gtkml-appmenu-1.png">


Further features to be implemented(later)
* Full CSS support
* Python snippets in DOM
* Less code, same features - concept
