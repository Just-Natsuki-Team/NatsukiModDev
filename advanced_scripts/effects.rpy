#This is a copy of effects.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Effects.rpy defines a set of special effects, including the glitchy Effects
#Used in act 2

########## invert(length,delay)
#This screen is called using a statement like `show screen invert(0.15,0.3)`
#Delay for `delay` seconds, then invert the screens colors for `length` seconds
#and play a glitchy sound

#Define some python stuff
init python:
    #Screen cap the current screen, used by multiple functions
    def screenshot_srf():
        srf = renpy.display.draw.screenshot(None, False)
        #if srf.get_width != 1280: srf = renpy.display.scale.smoothscale(srf, (1280, 720))
        return srf

    #Invert the colors of the current screen.
    def invert():
        srf = screenshot_srf()
        inv = renpy.Render(srf.get_width(), srf.get_height()).canvas().get_surface()
        inv.fill((255,255,255,255))
        inv.blit(srf, (0,0), None, 2) #pygame.BLEND_RGB_SUB enum is 2
        return inv

    #This defines a displayable for the inverted screen
    class Invert(renpy.Displayable):
        def __init__(self, delay=0.0, screenshot_delay=0.0):
            super(Invert, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            self.height = self.width * 9 / 16
            self.srf = invert()
            self.delay = delay

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            if st >= self.delay:
              render.blit(self.srf, (0, 0))
            return render

    #Hide all windows, revealing the background
    def hide_windows_enabled(enabled=True):
        global _windows_hidden
        _windows_hidden = not enabled

#Define the screen for renpy
screen invert(length, delay=0.0):
    add Invert(delay) size (1280, 720)
    timer delay action PauseAudio("music")
    timer delay action Play("sound", "sfx/glitch1.ogg")
    timer length + delay action Hide("invert")
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action PauseAudio("music", False)
    on "hide" action Stop("sound")
    on "hide" action Function(hide_windows_enabled, enabled=True)

########## tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None)
#This screen is called using a statement like
#`show screen tear(20, 0.1, 0.1, 0, 40)`
#Cut the screen up into some number of pieces and make them offset from eachother
#at random. In about 100% when called on top corner.

#Define some python stuff
init python:
    #This class defines the little blinking pieces of the screen tear effect
    class TearPiece:
        def __init__(self, startY, endY, offtimeMult, ontimeMult, offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax

        def update(self, st):
            st = st % (self.offTime + self.onTime)
            if st > self.offTime and self.offset == 0:
                self.offset = random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0

    #This class defines a renpy displayable made up of `number` of screen tear
    #sections, that bounce back and forth, based on ontimeMult & offtimeMult
    #and each piece is randomly offset by an amount between offsetMin & offsetMax
    class Tear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf=None):
            super(Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            #Force screen to 16:9 ratio
            if float(self.width) / float(self.height) > 16.0/9.0:
                self.width = self.height * 16 / 9
            else:
                self.height = self.width * 9 / 16
            self.number = number
            #Use a special image if specified, or tear current screen by default
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf

            #Rip the screen into `number` pieces
            self.pieces = []
            tearpoints = [0, self.height]
            for i in range(number):
                tearpoints.append(random.randint(10, self.height - 10))
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(TearPiece(tearpoints[i], tearpoints[i+1], offtimeMult, ontimeMult, offsetMin, offsetMax))

        #Render the displayable
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.blit(self.srf, (0,0))
            #Render each piece
            for piece in self.pieces:
                piece.update(st)
                subsrf = self.srf.subsurface((0, max(0, piece.startY - 1), self.width, max(0, piece.endY - piece.startY)))#.pygame_surface()
                render.blit(subsrf, (piece.offset, piece.startY))
            renpy.redraw(self, 0)
            return render

#Define the screen for Renpy, by default, tear the screen into 10 pieces
screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None):
    zorder 150 #Screen tear appears above pretty much everything
    add Tear(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size (1280,720)
    on "show" action Function(hide_windows_enabled, enabled=False) #This makes sure UI is hidden
    on "hide" action Function(hide_windows_enabled, enabled=True)

########## rectstatic
#These are three displayables (m_rectstatic, m_rectstatic2, m_rectstatic3) and
#one displayable effect RectStatic() that make a bunch of little boxes on the screen
#that blink on and off.

#Little black squares
image m_rectstatic:
    RectStatic(Solid("#000"), 32, 32, 32).sm
    pos (0, 0)
    size (32, 32)
#Little squares with a part of the logo
image m_rectstatic2:
    RectStatic(im.FactorScale(im.Crop("gui/logo.png", (100, 100, 128, 128)), 0.25), 2, 32, 32).sm
#Little squares with a part of the menu
image m_rectstatic3:
    RectStatic(im.FactorScale(im.Crop("gui/menu_art_s.png", (100, 100, 64, 64)), 0.5), 2, 32, 32).sm

init python:
    import math
    #This effect takes a displayable, a number of rectangles to show concurrently,
    #and a size for the rectangles, then makes them randomly show up on the screen
    #RectStatic(Solid("#000"), 32, 32, 32) would make 32 32x32 black squares
    #That show up randomly on the screen
    class RectStatic(object):
        def __init__(self, theDisplayable, numRects=12, rectWidth = 30, rectHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.timers = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.rectWidth = rectWidth
            self.rectHeight = rectHeight

            #Make copies of the displayables
            for i in range(self.numRects):
                self.add(self.displayable)
                self.timers.append(random.random() * 0.4 + 0.1)

        #Rectangles show up on a grid
        def add(self, d):
            s = self.sm.create(d)
            s.x = random.randint(0, 40) * 32
            s.y = random.randint(0, 23) * 32
            s.width = self.rectWidth
            s.height = self.rectHeight
            self.rects.append(s)

        def update(self, st):
            for i, s in enumerate(self.rects):
                if st >= self.timers[i]:
                    s.x = random.randint(0, 40) * 32
                    s.y = random.randint(0, 23) * 32
                    self.timers[i] = st + random.random() * 0.4 + 0.1
            return 0

########## ParticleBurst
#This is used to make the glowy sparkles that shoot out on the menu screen when
#the logo comes down. Used for the displayable "menu_particles" defined in
#splash.rpy:
#ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    class ParticleBurst(object):
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 3, particleYSpeed = 3):
            self.sm = SpriteManager(update=self.update)
            # A list of (sprite, starting-x, speed).
            self.stars = [ ]
            self.displayable = theDisplayable #The image for the particle
            self.explodeTime = explodeTime #Unused
            self.numParticles = numParticles #How many particles
            self.particleTime = particleTime #How long do the partcles last
            self.particleXSpeed = particleXSpeed #Average particle speed
            self.particleYSpeed = particleYSpeed
            self.gravity = 3 #How fast do paricles fall
            self.timePassed = 0

            for i in range(self.numParticles):
                self.add(self.displayable, 1)

        def add(self, d, speed):
            s = self.sm.create(d)
            ySpeed = (random.random() - 0.5) * self.particleYSpeed
            xSpeed = (random.random() - 0.5) * self.particleXSpeed
            s.x += xSpeed * 40
            s.y += ySpeed * 40
            pTime = self.particleTime
            self.stars.append((s, ySpeed, xSpeed, pTime))

        def update(self, st):
            sindex=0
            for s, ySpeed, xSpeed, particleTime in self.stars:
                if (st < particleTime):
                    s.x += xSpeed
                    s.y += (ySpeed + (self.gravity * st))
                else:
                    s.destroy()
                    self.stars.pop(sindex)
                sindex += 1
            return 0

########## Blood
#This defines a blood effect that is later used to make displayables for blood
#drops and spurts. Used for creepy blood drips and also for stabbing blood
#squirts
    class Blood(object):
        def __init__(self, theDisplayable, density=120.0, particleTime=1.0, dripChance=0.05, dripSpeedX=0.0, dripSpeedY=120.0, dripTime=180.0, burstSize=100, burstSpeedX=200.0, burstSpeedY=400.0, numSquirts=4, squirtPower=400, squirtTime=0.25):
            self.sm = SpriteManager(update=self.update)
            self.drops = []
            self.squirts = []
            self.displayable = theDisplayable #The image used for blood
            self.density = density #How much blood
            self.particleTime = particleTime #How long do particles last
            self.dripChance = dripChance
            self.dripSpeedX = dripSpeedX
            self.dripSpeedY = dripSpeedY
            self.gravity = 800.0
            self.dripTime = dripTime
            self.burstSize = burstSize #How many drops in the burst around the cut
            self.burstSpeedX = burstSpeedX
            self.burstSpeedY = burstSpeedY
            self.lastUpdate = 0
            self.delta = 0.0

            for i in range(burstSize): self.add_burst(theDisplayable, 0)
            for i in range(numSquirts): self.add_squirt(squirtPower, squirtTime)

        #This makes a single squirt of blood that follows an arc
        def add_squirt(self, squirtPower, squirtTime):
            angle = random.random() * 6.283
            xSpeed = squirtPower * math.cos(angle)
            ySpeed = squirtPower * math.sin(angle)
            self.squirts.append([xSpeed, ySpeed, squirtTime])

        #This makes a burst of blood that pops out of some area
        def add_burst(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.burstSpeedX + 20
            ySpeed = (random.random() - 0.75) * self.burstSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        #This makes a dripping stream of blood
        def add_drip(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.dripSpeedX + 20
            ySpeed = random.random() * self.dripSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        #This handles the time progression of the blood effect
        def update(self, st):
            delta = st - self.lastUpdate
            self.delta += st - self.lastUpdate
            self.lastUpdate = st

            #Start with a burst of blood with squirts
            sindex = 0
            for xSpeed, ySpeed, squirtTime in self.squirts:
                if st > squirtTime: self.squirts.pop(sindex)
                sindex += 1

            #Follow with a dripping stream of blood for dripTime seconds
            pindex = 0
            if st < self.dripTime:
                while self.delta * self.density >= 1.0:
                    self.delta -= (1.0 / self.density)
                    if random.random() >= 1 - self.dripChance: self.add_drip(self.displayable, st)
                    for xSpeed, ySpeed, squirtTime in self.squirts:
                        s = self.sm.create(self.displayable)
                        s.x += (random.random() - 0.5) * 5
                        s.y += (random.random() - 0.5) * 5
                        self.drops.append([s, xSpeed + (random.random() - 0.5) * 20, ySpeed + (random.random() - 0.5) * 20, self.particleTime, st])
            for s, xSpeed, ySpeed, particleTime, startTime in self.drops:
                if (st - startTime < particleTime):
                    s.x += xSpeed * delta
                    s.y += ySpeed * delta
                    self.drops[pindex][2] += self.gravity * delta
                else:
                    s.destroy()
                    self.drops.pop(pindex)
                pindex += 1
            return 0

#A blood drip, it gets longer and thinner over time
image blood_particle_drip:
    "gui/blood_drop.png"
    yzoom 0 yanchor 0.2 subpixel True
    linear 10 yzoom 8 #Extends vertically

#A small blood droplet that shrinks at a random speed
image blood_particle:
    subpixel True
    "gui/blood_drop.png"
    zoom 0.75
    alpha 0.75
    choice:
        linear 0.25 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.55 zoom 0

#A blood object using the default Blood effect settings:
#An initial burst of blood with 4 squirts that drips quickly for 3 minutes
image blood:
    size (1, 1)
    truecenter
    Blood("blood_particle").sm

#A blood splash with no squirts thats bleeds slowly
image blood_eye:
    size (1, 1)
    truecenter
    Blood("blood_particle", dripChance=0.5, numSquirts=0).sm

#A blood drip so slow that it's possible to think you imagined it
image blood_eye2:
    size (1, 1)
    truecenter
    Blood("blood_particle", dripChance=0.005, numSquirts=0, burstSize=0).sm


########## Animated Mask
#These effects are used to animate the moving layers that create the "Space Background"
#that appears outside the window in Act 3 with Monika.
#Also
init python:
    import math
    class AnimatedMask(renpy.Displayable):

        def __init__(self, child, mask, maskb, oc, op, moving=True, speed=1.0, frequency=1.0, amount=0.5, **properties):
            super(AnimatedMask, self).__init__(**properties)

            self.child = renpy.displayable(child) #The image (or color) being filtered
            self.mask = renpy.displayable(mask) #A mask that hides the image
            self.maskb = renpy.displayable(maskb) #A second mask that hides the image
            self.oc = oc
            self.op = op
            self.null = None
            self.size = None
            self.moving = moving
            self.speed = speed
            self.amount = amount
            self.frequency = frequency

        def render(self, width, height, st, at):

            cr = renpy.render(self.child, width, height, st, at)#.subsurface(((st * 50) % width, 0, width, height))
            mr = renpy.render(self.mask, width, height, st, at)#.subsurface(((-st * 50) % width, 0, width, height))
            mb = renpy.Render(width, height)

            #mr.blit(mb, ((-st * 150) % width,0))
            if self.moving:
                mb.place(self.mask, ((-st * 50) % (width * 2)) - (width * 2), 0)
                mb.place(self.maskb, -width / 2, 0)
            else:
                mb.place(self.mask, 0, 0)
                mb.place(self.maskb, 0, 0)

            #mr = mr.subsurface((0, 0, mr.width, mr.height))

            cw, ch = cr.get_size()
            mw, mh = mr.get_size()

            w = min(cw, mw)
            h = min(ch, mh)
            size = (w, h)

            if self.size != size:
                self.null = Null(w, h)

            nr = renpy.render(self.null, width, height, st, at)

            rv = renpy.Render(w, h, opaque=False)

            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = 1.0
            rv.operation_complete = self.oc + math.pow(math.sin(st * self.speed / 8), 64 * self.frequency) * self.amount #Opacity varies sinusoidally with time
            rv.operation_parameter = self.op

            rv.blit(mb, (0, 0), focus=False, main=False)
            rv.blit(nr, (0, 0), focus=False, main=False)
            rv.blit(cr, (0, 0))

            renpy.redraw(self, 0)
            return rv

    #This makes an image be transparent for a while then suddenly fade in and out
    #Used for the lensflair in the spaceroom
    def monika_alpha(trans, st, at):
        trans.alpha = math.pow(math.sin(st / 8), 64) * 1.4
        return 0


########## Blue Screen of Death
#These displayables make it look like windows has crashed
image bsod_1:
    "images/bg/bsod.png"
    size (1280,720)
image bsod_2:
    "black"
    0.1
    yoffset 250
    0.1
    yoffset 500
    0.1
    yoffset 750

image bsod = LiveComposite((1280, 720), (0, 0), "bsod_1", (0, 0), "bsod_2")

########## Veins
#This displayable creates a veiny border around the outside of the screen that shakes and pulses.
#Used in ch22 as party of a fainting effect that appears in 1/3rd of playthroughs
image veins:
    AnimatedMask("images/bg/veinmask.png", "images/bg/veinmask.png", "images/bg/veinmaskb.png", 0.15, 16, moving=False, speed=10.0, frequency=0.25, amount=0.1)
    xanchor 0.05 zoom 1.10
    xpos -5
    subpixel True
    parallel:
        ease 2.0 xpos 5
        ease 1.0 xpos 0
        ease 1.0 xpos 5
        ease 2.0 xpos -5
        ease 1.0 xpos 0
        ease 1.0 xpos -5
        repeat
    parallel:
        choice:
            0.6
        choice:
            0.2
        choice:
            0.3
        choice:
            0.4
        choice:
            0.5
        pass
        choice:
            xoffset 0
        choice:
            xoffset 1
        choice:
            xoffset 2
        choice:
            xoffset -1
        choice:
            xoffset -2
        repeat
