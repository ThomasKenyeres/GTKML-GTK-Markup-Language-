#**Tags in GTKML**
###```version 3.0.0```

##Basic structure of an application
```xml
<application>
    <window start="True">
        <header>
            <title>First Window</title>
        </header>
        <body>
            <label>Hello!</label>
        </body>
        <python src="display.py"></python>
        
    </window>
    
    <window id="fchooser1" type="filechooser"></window>
</application>
```

##`application`

##`window`

##`header`

##`title`

##`body`

##`python`

You can embed python code easily 
(similar to HTML and JavaScript) with 
file reference(recommended!).
```xml
<python src="display.py"></python>
```
You will be able to insert the code in the DOM like this(not available yet): 
```xml
<python>
    def sum(a, b):
        return a + b
</python>
```
You can add import statements in the DOM
```xml
<import from="os" import="system" as="sm"></import>
```

##Layout containers 
######in 3.0.1

##`hbox`

##`vbox`

##`grid`

##`listbox`

##`flowbox`

##`actionbar`

##`header`

##`fixed`

##`layout`


##Display widgets 
######in 3.0.1

##`label`

##`img`

##`spinner`

##`progressbar`


##Buttons
######in 3.0.1

##`button`

##`check`

##`radio`

##`toggle`

##`linkbutton`

##`modelbutton*`

Not implemented yet


##Entries
######in 3.0.1

##`entry`

##Text editors
######in 3.0.1

##`textview`

##Trees & Lists

##`listview`

##Menus

##`menu`


##Control tags

##`if`

```xml
<if condtition="everything.isready()">
    <label>Hi there it's finished</label>
</if>
```

##`for`
```xml
<for condtition="data in ['tee', 'coffee', 'cocoa']">
    <label>${data}</label>
</for>
```



-------------------------------------------------
##Higher level widgets in GTKML

##`table`

####`th`

####`tr`

####`td`