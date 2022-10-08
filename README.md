# Module for calculating and displaying complete training information from the sensor unit.

## Task
To implement a program module according to the OOP methodology to calculate and display information
of the last training session based on the data from the sensor unit.

## Base class
``python
class Training
```
### class properties

* action - main action to be read during training (step - running, walking; rowing - swimming);
* duration - duration of training;
* weight - weight of the athlete;
* M_IN_KM = 1000 - constant to convert values from meters to kilometers;
* LEN_STEP - the distance the athlete covers in one step or stroke. One step is `0.65` meters, one stroke is `1.38` meters.

### Class methods

* get_distance() - the method returns the value of the distance covered during the workout.
``python
## basic formula for calculating
step * LEN_STEP / M_IN_KM
```
* get_mean_speed() - The method returns the value of the average running speed during the workout.
```python
# basic formula for calculating
distance / duration
```
* get_spent_calories() - method returns the number of calories spent.
* show_training_info() - method returns a message class object.

## Successor classes.
Running training class
``python
class Running
```
### Class properties

are inherited

### Class methods
override method:
* get_spent_calories() - the method returns the number of calories spent.
``python
### formula to calculate
(18 * average_speed - 20) * athlete_weight / M_IN_KM * exercise_time_in_minutes
```
---
---
Athletic Walking Class
``python
class SportsWalking
```
### Class Properties
Addable properties:
### height

### Class methods
override method:
* get_spent_calories() - method returns the number of calories spent.
``python
# # calculation formula
(0.035 * weight + (speed ** 2 // height) * 0.029 * weight) * time_exercise_in_minutes
```
---
---
Pool workout class
``python
class Swimming
```
### Class Properties
Addable properties:
* length_pool - length of pool;
* count_pool - number of pools swum.

### Class methods
Override method:
* get_mean_speed() - method returns the value of average speed during the workout.
``python
## formula for calculating
length_pool * count_pool / M_IN_KM / time_exercise
```
* get_spent_calories() method returns the number of calories spent.
``python
# calculation formula
(speed + 1.1) * 2 * weight
```
## Informational message class
``python
class InfoMessage
```
### Class properties
* training_type - type of training;
* duration - duration of training;
* distance - distance covered during training;
* speed - average speed of movement;
* calories - kilocalories spent during training.


### Class methods

* get_message() - method returns the message string.
``python
# # message to be displayed
# all float type values are rounded to 3 decimal places
'Training type: {training_type}; Duration: {duration} hr; Distance: {distance} km; cfr speed: {speed} km/h; kcalories expended: {calories}'.
```

## Module functions
``python
def read_package()
```
* The read_package() function takes as input the training code and a list of its parameters.
* The function must determine the type of workout and create an object of the corresponding class,
by passing to it on input parameters, received in the second argument. This object should be returned by the function.

---
---
``python
def main(training)
```
The `main()` function must take an instance of the `Training` class as input.

- When the function `main()` is executed, the `show_training_info()` method must be called for that instance;
The result of the method must be an object of class `InfoMessage` and it must be saved in the variable `info`.
- For the `InfoMessage` object saved in the `info` variable, the method,
which returns a message string with training data; this string must be passed to the `print()` function.

Translated with www.DeepL.com/Translator (free version)
