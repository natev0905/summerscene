daytime = 0

nighttime = 0

add_library('minim')
sound = None


def ytime(n):

    flag = False

    for i in range(n+1):

        print(i,n)

        if i == n:

            flag = True

    return flag



def setup () :

    global daytime

    global nighttime
    global sound

    size(600, 339)

    global Music

    minim = Minim(this)

    sound = minim.loadFile('oceanwaves.mp3')
    sound.loop()

    global cornerPointX, cornerPointY, canvasX, canvasY, back, Nathan

    global NathanX, NathanY, NathanXX, NathanYY, backHeight, backWidth, chunkSize, chunkIncr, chunkX, chunkY


    backHeight = 600 #background image height

    backWidth = 600 #background image width


    chunkSize = 100 #source image width; how much of the image we want to see

    chunkIncr = 1  #increment; used to increase the speed of background image movement

    chunkX = 0      #x coordinate of the source image upper left corner

    chunkY = 0      #y coordinate of the source image upper left corner


    NathanX = 215 #x coordinate of me

    NathanY = 70 #y coordinate of me


    NathanXX = 110 #x size of me

    NathanYY = 110  #y size of me


    cornerPointX = 0 #x coordinate of the destination image upper left corner

    cornerPointY = 0 #y coordinate of the destination image upper left corner


    canvasX = 600 #destination image width

    canvasY = 600 #destination image height


    Nathan = loadImage( "nathansummerscene.jpg" )

    back = loadImage( "daytimebackground.jpg" )

    #Syntax:

    #copy(src, sx,     sy,     sw,        sh,         dx,           dy,           dw,      dh)

    copy(back, chunkX, chunkY, chunkSize, backHeight, cornerPointX, cornerPointY, canvasX, canvasY)



def draw ():

    global daytime

    global nighttime

    global Nathan

    daytime = loadImage("daytimebackground.jpg")

    nighttime = loadImage("nighttimebackground.jpg")

    Nathan = loadImage("nathansummerscene.jpg")

    background(0)

    image(nighttime, 0, 0)

    global cornerPointX, cornerPointY, canvasX, canvasY, back, Nathan

    global NathanX, NathanY, NathanXX, NathanYY, backHeight, backWidth, chunkSize, chunkIncr, chunkX, chunkY


    chunkX += chunkIncr #increments the X coordinate of the source image upper left corner

    if ( chunkX + chunkSize ) >= backWidth: #if the X coordinate and size is greater than the background image width

        chunkX = 0 #reset it to 0


    #Syntax:

    #copy(src, sx,     sy,     sw,        sh,         dx,           dy,           dw,      dh)

    copy(back, chunkX, chunkY, chunkSize, backHeight, cornerPointX, cornerPointY, canvasX, canvasY)




    print(chunkX)


    if chunkX <570:

        fill('#FFFF00')

        ellipse(275, 120, 150, 150)


    if chunkX >= 570:

        fill("#808080")

        ellipse(275, 120, 150, 150)


    image(Nathan, NathanX, NathanY, NathanXX, NathanYY)


    message = ytime(52)

    print(message)

    if message == True:

        textSize(40)

        fill("#FF0000")

        text("It's summer get hyped!", 100, 300)


    fill(255)

    noStroke()

    ellipse(100, 100, 50, 50)

    ellipse(110, 110, 50, 50)

    ellipse(80, 80, 50, 50)

    ellipse(90, 110, 50, 50)

    ellipse(110, 80, 50, 50)

    ellipse(90, 120, 50, 50)

    ellipse(80, 115, 50, 50)

    ellipse(80, 110, 50, 50)

    ellipse(140, 110, 50, 50)

    ellipse(1400, 95, 50, 50)

    ellipse(110, 110, 80, 80)

    ellipse(400, 110, 50, 50)

    ellipse(420, 110, 50, 50)

    ellipse(430, 110, 50, 50)

    ellipse(400, 100, 50, 50)

    ellipse(420, 110, 50, 50)

    ellipse(430, 105, 50, 50)

    ellipse(440, 100, 50, 50)

    ellipse(430, 95, 50, 50)

    ellipse(390, 100, 50, 50)

    ellipse(400, 90, 50, 50)

    ellipse(390, 120, 50, 50)

    ellipse(400, 110, 50, 50)

    ellipse(420, 90, 50, 50)

    ellipse(430, 90, 50, 50)


def keyPressed():
    global sound



    if key == 'p':

        sound.play()

    elif key == 's':

        sound.pause()

    elif key == "r":

        sound.rewind()
