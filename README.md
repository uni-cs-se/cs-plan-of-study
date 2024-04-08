# Rest API generator thing

Andy said he wanted alot of restapi's so I figured the best way to go about
satisfying this need would be to write a rest api generator. I wrote this in
continuation passing style because I really enjoy continuation passing style,
it is currently setup to generate a few rest apis that together will calculate
a fibonnacci number in O(2^n) rest api calls!

## Requirements
this has three dependencies that you can probably install with
```sh
pip install httpx fastapi uvicorn
```
if you can't the dependencies are httpx, fastapi, and uvicorn.

## Building
you can generate the rest apis with
```sh
make
```

the generated rest apis are in the /build directory, each subfolder is a rest api
and the foldername indicates the port that api will be launched on. I also
generate Docker files but I never actually got around to getting them all to
run in separate containers :/

## Running
you can run the rest apis with
```sh
./run.sh
```

there is an example rest client in /examples that allows you to input a number
which it then sends to the rest apis to calculate a fibonacci number!
