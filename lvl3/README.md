## Car Self-Driving Interface : Brief

You need to re-implement the controlCar function.

To implement it in JavaScript use the editor on the left.

When implemented, controlCar function will be called several times per second during the chase to allow for course corrections.

The controlCar function takes a single parameter – scanArray – which is an array containing 17 integers denoting distance from your car to the nearest obstacle:

    [indexes 0-7]: on the left side of the car (index 7 is the measurement at the left headlight),
    [index 8]: at the center of the car,
    [indexes 9-16]: on the right side of the car (index 9 is the measurement at the right headlight).

See also this image (it's not precise, but will give you an idea what you are looking at).

All measurements are parallel to each other.

A negative measurement might appear if the obstacle is very close behind our car.

The controlCar must return an integer denoting where the car should drive:

    -1 (or any other negative value): drive more to the left,
    0: continue straight / straighten up the car,
    1 (or any other positive value): drive more to the right.

## Solve

We write a simple algorithm to put the car on the 3-lines-wide-space where the obstacles is the furthest (see solve.js)

After a hefty slalom, we're left with a flag

Flag is `CTF{cbe138a2cd7bd97ab726ebd67e3b7126707f3e7f}`
