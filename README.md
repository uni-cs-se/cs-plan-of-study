#Rest API generator thing

Andy said he wanted alot of restapi's so i figured the best way to go about
satisfying this need would be to write a rest api generator. I wrote this in
continuation passing style because I really enjoy continuation passing style,
it is currently setup to generate a few rest apis that together will calculate
the a fibonnacci number in O(2^n) rest api calls!

##Requirements
this has three dependencies that you can probably install with
```
pip install httpx fastapi uvicorn
```
if you can't the dependencies are httpx, fastapi, and uvicorn.

##building
you can generate the rest apis with
```
make
```

the generated rest apis in the /build directory, each subfolder is a rest api
and the foldername indicates the port that api will be launched on. I also
generate Docker files but I never actually got around to getting them all to
run in separate containers :/


##Running
you can run them with
```
./run.sh
```

there is an example rest client in /examples that allows you to input a number
which it then sends to the restapis to calculate a fibonacci number!
