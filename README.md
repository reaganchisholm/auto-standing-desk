# Auto Standing Desk
Raspberry Pi setup to randomly pick times during my work hours to change my desk to standing mode

![Finished Project](/imgs/finished-pi.jpg)
![Soldered standing desk board](/imgs/soldered-board.jpg)

## Parts used
- [Raspberry Pi](https://www.raspberrypi.org/products/) (I used a Model B I already owned)
- [Relay](https://www.amazon.ca/gp/product/B0057OC6D8)
- [Electric Standing Desk](https://www.amazon.ca/PrimeCables%C2%AE-Electric-Sit-Stand-Dual-Motor-Adjustable/dp/B0794XZC8X)

## How it works
1.  Wire Raspberry Pi to relay
2.  Solder wires into preset height button on standing desk board
3.  Wire standing desk into relay
4.  Turning on relay via Raspberry Pi will make standing desk stand up
5.  Run script to choose stand up times for days you wish