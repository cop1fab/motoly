## Product overview
 Motoly is the backbone of a tool to facilitate management of electric car businesses in Rwanda. It enables  calculating  the amount of energy a driver has used in a day and the kilometers the same driver has done.

## Development set up

#### Getting a copy on your local machine
- Clone the repo
	```
    git clone https://github.com/cop1fab/motoly.git
    ```
- Installing the virtual env 

    ```
    python3 -m pip install virtualenv |OR| python3 -m pip install --user virtualenv
    ```
- Creating your virtual env

    ```
    virtualenv <name of your virtualenv>  ie: virtualenv my_venv
    ```
- Activating the virtual env

    ``` 
    source my_venv/bin/activate 
    ```
- Deactivating the virtualenv   

    ``` deactivate```
 
- Installing dependencies 

    ``` 
    pip3 install -r requirements.txt
    ```

- Run application.
    ```
    flask run |OR| python3 app.py
    ```
- Databases and Migrations 

   This service is built using MongoDB, you need to have MongoDB installed and you don't need to run any migrations 



##### ENDPOINTS TO BE TESTED
  - Create vehicle 
	``` 
	POST /vehicle 
	```
	
	`` {
	"name": "audi",
	"odometer_reading": 900 }
	``
  - Getting all Vehicles
  	```
    GET /vehicles
  	```
 - Create a driver 
    ``` 
    POST /driver/<vehicle_id>
    ```
    ``{
	"name": "Copain" }``
	
- Get drivers

    ``` 
    GET /drivers
    ```
- Get one Driver 
  ```
  GET /driver/driver_id 
  ```
- Create a battery 
    ```
    POST /battery 
    ```
    ``{
	"voltage": 150,
	"capacity": 90 }``
- Get all batteries 
    ``` 
    GET /batteries
    ```
- Create Swapping station
    ``` 
    POST /station
    ```
    ``{
	"location": "Remera"
}``

- Getting all stations 
    ``` 
    GET /stations
    ```
- Creating the first swap [ Here a driver gets his first battery]
    ```  
    POST /swap/driver/<driver_id>/battery/<battery_id>/station/<station_id>
    ```
    ``{
	"initialBattery": 93
}``

- Completing a swap [ A driver returns the battery to get another one]
    ```
     PUT /swap/<swap_id>
    ```
    ``{
	"remainingBattery": 30
}``

- Getting total energy used in a day [Because we retrieve this at the end of the day we also take the odometer reading]
    ``` 
    POST /swap/driver/<driver_id>/vehicle/<vehicle_id>/day
    ```
    ``{
	"reading": 300
}``
- Getting Kilometers done in a day 

    ```  
    GET /vehicle/<vehicle_id>/day
    ```
- Getting swaps done by one driver a day
    ``` 
    GET /swap/driver/<driver_id>
    ```

## Built with
- Python version  3
- Flask
- MongoDb

## Contribution guide

##### Contributing
NB: There is still work being done on this project so
when contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.This Project shall be utilising a [Trello](https://www.trello.com) to track  the work done.


 ##### Pull Request Process
- A contributor shall identify a task to be done from the Trello board.If there is a bug , feature or chore that has not be included among the tasks, the contributor can add it only after consulting the owner of this repository and the task being accepted.
- The Contributor shall then create a branch off  the ` develop` branch where they are expected to undertake the task they have chosen.
- After  undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review.
- If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `develop` by the owners of this repository.
