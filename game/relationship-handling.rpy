default persistent.trust = 1.0
default persistent.affinity = 1.0

init 0 python:
    def relationship(change, multiplier=1):
        def affinity_increase(multiplier=1):
            if persistent.trust > 0:
                persistent.affinity += multiplier*(persistent.trust/20)

        def affinity_decrease(multiplier=1):
            if persistent.trust-50 > 0:
                persistent.affinity -= multiplier*(5 - (persistent.trust-50)/25)
            else:
                persistent.affinity -= multiplier*5

        def trust_increase(multiplier=1):
            if persistent.trust < 100:
                persistent.trust += multiplier*0.8*(round(math.tanh((persistent.affinity-75)/30)+1, 4)+1)
            if persistent.trust > 100:
                persistent.trust = 100

        def trust_decrease(multiplier=1):
            if persistent.trust > -100:
                persistent.trust -= multiplier*2*(3 - round(math.tanh((persistent.affinity-75)/30)+1, 4))
            if persistent.trust < -100:
                persistent.trust = -100

        if change == "affinity+":
            affinity_increase(multiplier)
        elif change == "affinity-":
            affinity_decrease(multiplier)
        elif change == "trust+":
            trust_increase(multiplier)
        elif change == "trust-":
            trust_decrease(multiplier)
        else:
            raise Exception(change+" is not a valid argument!")