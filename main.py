random = False
def on_forever():
    global random
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 30 and maqueen.ultrasonic(PingUnit.CENTIMETERS) != 0:
        random = Math.random_boolean()
        if random == True:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
            basic.pause(1000)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
            maqueen.motor_stop(maqueen.Motors.M1)
            basic.pause(800)
        if random == False:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
            basic.pause(1000)
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
            maqueen.motor_stop(maqueen.Motors.M2)
            basic.pause(800)
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
basic.forever(on_forever)
