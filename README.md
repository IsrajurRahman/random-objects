# random-objects
Web app to generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",".  These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics.

Sample extracted output:

*hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, 
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, 
nmarcysfa900jkifh, 3.781, 2.11, ....*

The output file is 2MB in size. Once file generation is done the output file can be downloaded by clicking on a link. 
Also, there is a Report button on the page.  When clicked, shows the total count of generated objects.

## To Run The APP

Pull the project from git and follow below steps
>Make sure your system has pipenv installed
```
pipenv shell
```

```
pipenv install uvicorn
```

```
uvicorn main:app
```


## Sample Image

![alt text](https://github.com/IsrajurRahman/random-objects/blob/main/templates/sample_image.png)