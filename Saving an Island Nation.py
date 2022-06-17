"""IslandProblem.py
"""

# <METADATA>
import random

SOLUZION_VERSION = "0.1"
PROBLEM_NAME = "Saving an Island Nation"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['J. KHARCHENKO', 'K. SELVAKUMAR', 'M. VICKERS', 'T. WOODWARD']
PROBLEM_CREATION_DATE = "9-SEP-21"
PROBLEM_DESC = \
    ''' Saving an island nation from being wiped off the map due to an
        imminent rising sea level threat.
    '''
# </METADATA>

#<COMMON_DATA

# Constant variables across all islands
# Initial sea level rate is measured in meters per decade
START_DATE = 2021
DATE_INCREMENT = 1
INITIAL_SEA_LEVEL = 1.0
INITIAL_SEA_LEVEL_RATE = 1.0

# Used to signal when to reveal certain operators
OPERATOR_TURN = 1


""" Creates dictionaries of features that various islands can potentially
    have to randomly mix them together, creating a different
    user experience each time the user plays the game
"""

END_DATES = {
    0: 2041,
    1: 2051,
    2: 2061,
    3: 2071,
    4: 2081
}

BUDGETS = {
    0: 2500000,
    1: 5000000,
    2: 7500000,
    3: 10000000
}

MAX_SEA_LEVELS = {
    0: 3.0,
    1: 2.5,
    2: 3.0,
    3: 3.5,
    4: 4.0,
    5: 5.5,
    6: 6.0
}

# All these islands are under threat of rising sea levels
ISLAND_NAMES = {
    0: 'Kiribati',
    1: 'the Maldives',
    2: 'Fiji',
    3: 'Palau',
    4: 'Micronesia',
    5: 'Cabo Verde',
    6: 'Solomon Islands',
    7: 'Tangier Island',
    8: 'Sarichef Island',
    9: 'the Seychelles',
    10: 'the Torres Strait Islands',
    11: 'the Carteret Islands',
    12: 'Tuvalu',
    13: 'the Marshall Islands'
}

ROLES = {
    0: 'local citizen',
    1: 'government official'
}

from random import randint


# Randomly creates features of an island nation and the user's role
default_features = {
    'island_name': ISLAND_NAMES[randint(0, 13)],
    'island_features': {
        'INITIAL_BUDGET': BUDGETS[randint(0, 3)],
        'END_DATE': END_DATES[randint(0, 4)],
        'MAX_SEA_LEVEL': MAX_SEA_LEVELS[randint(0, 6)]
    },
    'role': ROLES[randint(0, 1)]
}


""" Positive costs will add money to the budget
    while negative costs will detract money.
    Positve impact will make sea levels rise quicker,
    whereas negative impact will slow the rate.
"""

""" Makes a dictionary of actions that government officials
    can do within each island nation along with their costs
    in a separate dictionary
"""

GOVERNMENT_ACTIONS_COST = {
    'BILL_ONE': 100000,
    'BILL_TWO': -100000,
    'BILL_THREE': 70000,
    'BILL_FOUR': -70000,
    'BILL_FIVE': 80000,
    'BILL_SIX': -80000,
    'BILL_SEVEN': 900000,
    'BILL_EIGHT': -900000
}

GOVERNMENT_ACTIONS_IMPACT = {
    'BILL_ONE': 0.3,
    'BILL_TWO': -0.3,
    'BILL_THREE': 0.2,
    'BILL_FOUR': -0.2,
    'BILL_FIVE': 0.5,
    'BILL_SIX': -0.5,
    'BILL_SEVEN': 0.4,
    'BILL_EIGHT': -0.4
}


""" Makes a dictionary of actions that ordinary civilians
    can do within each island nation along with their costs
    in a separate dictionary
"""

INDIVIDUAL_ACTIONS_COST = {
    'BIG_BUSINESS': 100000,
    'SMALL_BUSINESS': -100000,
    'DRIVING_CAR': 50000,
    'PUBLIC_TRANSPORT': -50000,
    'TRASH': 20000,
    'BEACH_CLEANUP': -20000,
    # Ignoring the problem has no cost
    'IGNORE': 0,
    'GOVERNMENT': -1000000
}

INDIVIDUAL_ACTIONS_IMPACT = {
    'BIG_BUSINESS': 0.2,
    'SMALL_BUSINESS': -0.2,
    'DRIVING_CAR': 0.1,
    'PUBLIC_TRANSPORT': -0.1,
    'TRASH': 0.05,
    'BEACH_CLEANUP': -0.05,
    # Ignoring the problem has a big impact
    'IGNORE': 0.4,
    'GOVERNMENT': -0.4
}


#</COMMON_DATA>

#</COMMON_CODE>

def random_rising_sea_level_fact():
    """ Creates a list of facts relating to rising sea levels
        to relay to the players throughout the game

        Returns one random fact
    """
    facts = [
        'Every vertical inch of sea-level rise moves the ocean ' +
             '50 to 100 inches inland',
             '216 million people live on land that will be flooded by 2100',
             'The government of Kiribati has already begun planning a ' +
             '\"migration with dignity\", preparing to move its population to ' +
             'an area that will not be underwater',
             'Large coastal cities could experience damages of $1 trillion a year ' +
             'due to flooding',
             'Use permeable pavement instead of hard pavement in your homes - hard ' +
             'surfaces increase runoff and erosion because they prevent water from ' +
             'permeating the ground',
             'Even simple actions such as printing double-sided instead of single-sided' +
             'help save the planet',
             'Experts predict that both the Maldives and Kiribati will be underwater by 2050',
             'Five islands in the Solomon Islands disappeared from 1947 to 2014 because of ' +
             'rising sea levels',
             'If the sea level rises by 3.3 more feet, 3/4 of the Seychelles will be submerged',
             'Many people from the Carteret Islands are \"climate refugees\" because ' +
             'they often have to leave their sinking homes for higher ground or emigrate entirely',
             'the Maldives are creating man-made islands not only to hold tourists, but also to' +
             'support climate change refugees',
             'What are the legal implications of rising sea levels? If a country disappears under the sea, ' +
             'is it still a country? With fishing rights, a UN seat, etc?',
             'Reduce your carbon footprint, but also hold businesses and governments accountable for ' +
             'protecting the population',
             'Preserve wetlands! They act as natural buffers for coastal areas during rainstorms ' +
             'and absorb surge storm waters',
             'Plant more plants! They clean the air and soak up rain',
             'Reducing energy use will save both money and the planet',
             'Support restoration! Stay on designated paths to avoid stepping on fragile areas ' +
             'such as dunes and sod banks'
    ]

    return facts[random.randrange(0, len(facts))]


class State:
    def __init__(self, island_name=None, island_features=None, role=None, old=None):
        # Establishes the initial parameters
        self.budget = island_features['INITIAL_BUDGET']
        self.seaLevel = INITIAL_SEA_LEVEL
        self.seaLevelRate = INITIAL_SEA_LEVEL_RATE
        self.date = START_DATE
        self.island_name = island_name
        self.island_features = island_features
        self.role = role
        self.end_date = island_features['END_DATE']
        self.operator_turn = OPERATOR_TURN
        if old is not None:
            self.budget = old.budget
            self.seaLevel = old.seaLevel
            self.seaLevelRate = old.seaLevelRate
            self.date = old.date
            self.island_name = island_name
            self.island_features = old.island_features
            self.role = old.role
            self.end_date = old.end_date
            self.operator_turn = old.operator_turn


    def can_move(self, cost, player_role, op_turn):
        """ The player can use certain Operators if
            a.) they are within the player's budget,
            b.) they are appropriate to the player's turn, and
            c.) they are relevant to their role of either a
                government official or local citizen
        """
        if self.role != player_role:
            return False
        if op_turn != self.operator_turn:
            return False
        return self.budget >= -cost


    def move(self, cost, seaLevelRateImpact):
        """ Increases the cost, seaLevel, and seaLevelRate
            based on the given operator.
            Increases the time.
        """
        self.island_features['INITIAL_BUDGET'] += cost
        self.seaLevel += self.seaLevelRate * DATE_INCREMENT / 10
        self.date += DATE_INCREMENT
        self.seaLevelRate += seaLevelRateImpact

        """ Allows for the next operator to be used in the
            future round
        """
        self.operator_turn += 1

        # Resets the operators to cycle through them again
        if self.operator_turn == 5:
            self.operator_turn = 1

        """ Prints out rising sea level facts during each iteration
            of the game
        """
        print("\n\nRANDOM FACT: %s\n\n" % random_rising_sea_level_fact())

        return self


    def describe_state(self):
        # Describes the current conditions the player is facing
        txt = """ You are a %s on %s. It is now the year %s.
The sea level is now at %.2f meters and is increasing at a rate of %.2f.
You have $%d left in your budget. Save the nation by %d""" % (self.role, self.island_name,
                                             self.date, self.seaLevel,
                                            self.seaLevelRate, self.budget,
                                            self.end_date)
        return txt


    def is_goal(self):
        """ The goal has been met if one of two possible conditions has
            been met:
            1.) The player reached the island's estimated 'drowning year'
            2.) The sea level has increased drastically and wiped out the
                nation before their estimated drowning year
        """
        if self.date >= self.island_features['END_DATE']:
            return True
        elif self.seaLevel > self.island_features['MAX_SEA_LEVEL']:
            return True
        return False


    def __eq__(self, s2):
        """ Returns whether there is no previous state or whether
            the previous state is the same as the current state (with
            identical budgets, sea levels, sea level rates, and dates)
        """
        if s2 is None: return False
        return self.budget == s2.budget and self.seaLevel == s2.seaLevel \
                and self.seaLevelRate == s2.seaLevelRate \
                and self.date == s2.date

    def __str__(self):
        # Prints out the describe_state() function
        return self.describe_state()


    def __hash__(self):
        return (str(self)).__hash__()

    def goal_message(self):
        """ Sends out a goal message with a negative tone if the player
            did not reach their goal (the sea level is too high) and a
            positive sea level if they did reach their goal (made it to the
            final year).
        """
        if self.seaLevel > self.island_features['MAX_SEA_LEVEL']:
            return "\n\nSorry, you were unable to save %s in time.\n\n" % self.island_name
        else:
            return "\n\nCongratulations! %s have survived until %d.\n\n" % (self.island_name,
                                                                    self.date)



def copy_state(s):
    """ Copies the state of the island w/ the island name, its features,
        and the role the player chose
    """
    return State(island_name=default_features['island_name'],
                  island_features=default_features['island_features'],
                  role=default_features['role'], old=s)


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

#</COMMON_CODE>

#<INITIAL_STATE>

INITIAL_STATE = State(island_name=default_features['island_name'],
                  island_features=default_features['island_features'],
                  role=default_features['role'])

#</INITIAL_STATE>

#<OPERATORS>


# Actions an individual can do
phi0 = Operator("Support a larger business with high emissions: cost -> %s, impact -> %s"
                % (INDIVIDUAL_ACTIONS_COST['BIG_BUSINESS'], INDIVIDUAL_ACTIONS_IMPACT['BIG_BUSINESS']),
                lambda s: s.can_move(INDIVIDUAL_ACTIONS_COST['BIG_BUSINESS'],
                                     'local citizen', 1),
                lambda s: s.move(INDIVIDUAL_ACTIONS_COST['BIG_BUSINESS'],
                                 INDIVIDUAL_ACTIONS_IMPACT['BIG_BUSINESS']))

phi1 = Operator("Support a smaller, climate-conscious business: cost -> %s, impact -> %s"
                % (INDIVIDUAL_ACTIONS_COST['SMALL_BUSINESS'], INDIVIDUAL_ACTIONS_IMPACT['SMALL_BUSINESS']),
                lambda s: s.can_move(INDIVIDUAL_ACTIONS_COST['SMALL_BUSINESS'],
                                     'local citizen', 1),
                lambda s: s.move(INDIVIDUAL_ACTIONS_COST['SMALL_BUSINESS'],
                                 INDIVIDUAL_ACTIONS_IMPACT['SMALL_BUSINESS']))

phi2 = Operator("Drive a car: cost -> %s, impact -> %s"
                % (INDIVIDUAL_ACTIONS_COST['DRIVING_CAR'], INDIVIDUAL_ACTIONS_IMPACT['DRIVING_CAR']),
                  lambda s: s.can_move(INDIVIDUAL_ACTIONS_COST['DRIVING_CAR'],
                                       'local citizen', 2),
                  lambda s: s.move(INDIVIDUAL_ACTIONS_COST['DRIVING_CAR'],
                                      INDIVIDUAL_ACTIONS_IMPACT['DRIVING_CAR']))

phi3 = Operator("Opt for public transport: cost -> %s, impact -> %s"
                % (INDIVIDUAL_ACTIONS_COST['PUBLIC_TRANSPORT'], INDIVIDUAL_ACTIONS_IMPACT['PUBLIC_TRANSPORT']),
                  lambda s: s.can_move(INDIVIDUAL_ACTIONS_COST['PUBLIC_TRANSPORT'],
                                       'local citizen', 2),
                  lambda s: s.move(INDIVIDUAL_ACTIONS_COST['PUBLIC_TRANSPORT'],
                                    INDIVIDUAL_ACTIONS_IMPACT['PUBLIC_TRANSPORT']))

phi4 = Operator("Throw trash into the ocean: cost -> %s, impact -> %s"
                % (INDIVIDUAL_ACTIONS_COST['TRASH'], INDIVIDUAL_ACTIONS_IMPACT['TRASH']),
                  lambda s: s.can_move(INDIVIDUAL_ACTIONS_COST['TRASH'],
                                       'local citizen', 3),
                  lambda s: s.move(INDIVIDUAL_ACTIONS_COST['TRASH'],
                                   INDIVIDUAL_ACTIONS_IMPACT['TRASH']))

phi5 = Operator("Work to clean up the beach: cost -> %s, impact -> %s"
                % (INDIVIDUAL_ACTIONS_COST['BEACH_CLEANUP'], INDIVIDUAL_ACTIONS_IMPACT['BEACH_CLEANUP']),
                  lambda s: s.can_move(INDIVIDUAL_ACTIONS_COST['BEACH_CLEANUP'],
                                       'local citizen', 3),
                  lambda s: s.move(INDIVIDUAL_ACTIONS_COST['BEACH_CLEANUP'],
                                   INDIVIDUAL_ACTIONS_IMPACT['BEACH_CLEANUP']))

phi6 = Operator("Ignore the average global temperature increase: cost -> %s, impact -> %s"
                % (INDIVIDUAL_ACTIONS_COST['IGNORE'], INDIVIDUAL_ACTIONS_IMPACT['IGNORE']),
                  lambda s: s.can_move(INDIVIDUAL_ACTIONS_COST['IGNORE'],
                                       'local citizen', 4),
                  lambda s: s.move(INDIVIDUAL_ACTIONS_COST['IGNORE'],
                                   INDIVIDUAL_ACTIONS_IMPACT['IGNORE']))

phi7 = Operator("Advocate for governmental actions to cut emissions: cost -> %s, impact -> %s"
                % (INDIVIDUAL_ACTIONS_COST['GOVERNMENT'], INDIVIDUAL_ACTIONS_IMPACT['GOVERNMENT']),
                  lambda s: s.can_move(INDIVIDUAL_ACTIONS_COST['GOVERNMENT'],
                                       'local citizen', 4),
                  lambda s: s.move(INDIVIDUAL_ACTIONS_COST['GOVERNMENT'],
                                   INDIVIDUAL_ACTIONS_IMPACT['GOVERNMENT']))


# Actions governments can do
phi8 = Operator("Support Bill 1 that supports building sea walls: cost -> %s, impact -> %s"
                % (GOVERNMENT_ACTIONS_COST['BILL_ONE'], GOVERNMENT_ACTIONS_IMPACT['BILL_ONE']),
                lambda s: s.can_move(GOVERNMENT_ACTIONS_COST['BILL_ONE'],
                                     'government official', 1),
                lambda s: s.move(GOVERNMENT_ACTIONS_COST['BILL_ONE'],
                                   GOVERNMENT_ACTIONS_IMPACT['BILL_ONE']))

phi9 = Operator("Support Bill 2 that builds more pipelines: cost -> %s, impact -> %s"
                % (GOVERNMENT_ACTIONS_COST['BILL_TWO'], GOVERNMENT_ACTIONS_IMPACT['BILL_TWO']),
                lambda s: s.can_move(GOVERNMENT_ACTIONS_COST['BILL_TWO'],
                                     'government official', 1),
                lambda s: s.move(GOVERNMENT_ACTIONS_COST['BILL_TWO'],
                                   GOVERNMENT_ACTIONS_IMPACT['BILL_TWO']))

phi10 = Operator("Support Bill 3 that aims to lower carbon emissions: cost -> %s, impact -> %s"
                 % (GOVERNMENT_ACTIONS_COST['BILL_THREE'], GOVERNMENT_ACTIONS_IMPACT['BILL_THREE']),
                lambda s: s.can_move(GOVERNMENT_ACTIONS_COST['BILL_THREE'],
                                     'government official', 2),
                lambda s: s.move(GOVERNMENT_ACTIONS_COST['BILL_THREE'],
                                   GOVERNMENT_ACTIONS_IMPACT['BILL_THREE']))

phi11 = Operator("Support Bill 4 that builds more polluting factories: cost -> %s, impact -> %s"
                 % (GOVERNMENT_ACTIONS_COST['BILL_FOUR'], GOVERNMENT_ACTIONS_IMPACT['BILL_FOUR']),
                lambda s: s.can_move(GOVERNMENT_ACTIONS_COST['BILL_FOUR'],
                                     'government official', 2),
                lambda s: s.move(GOVERNMENT_ACTIONS_COST['BILL_FOUR'],
                                   GOVERNMENT_ACTIONS_IMPACT['BILL_FOUR']))

phi12 = Operator("Support Bill 5 that puts a tax on the use of plastic: cost -> %s, impact -> %s"
                 % (GOVERNMENT_ACTIONS_COST['BILL_FIVE'], GOVERNMENT_ACTIONS_IMPACT['BILL_FIVE']),
                 lambda s: s.can_move(GOVERNMENT_ACTIONS_COST['BILL_FIVE'],
                                      'government official', 3),
                 lambda s: s.move(GOVERNMENT_ACTIONS_COST['BILL_FIVE'],
                                  GOVERNMENT_ACTIONS_IMPACT['BILL_FIVE']))

phi13 = Operator("Support Bill 6 that builds more landfills to hold more plastic: cost -> %s, impact -> %s"
                 % (GOVERNMENT_ACTIONS_COST['BILL_SIX'], GOVERNMENT_ACTIONS_IMPACT['BILL_SIX']),
                 lambda s: s.can_move(GOVERNMENT_ACTIONS_COST['BILL_SIX'],
                                      'government official', 3),
                 lambda s: s.move(GOVERNMENT_ACTIONS_COST['BILL_SIX'],
                                  GOVERNMENT_ACTIONS_IMPACT['BILL_SIX']))

phi14 = Operator("Support Bill 7 that makes public transport more affordable: cost -> %s, impact -> %s"
                 % (GOVERNMENT_ACTIONS_COST['BILL_SEVEN'], GOVERNMENT_ACTIONS_IMPACT['BILL_SEVEN']),
                 lambda s: s.can_move(GOVERNMENT_ACTIONS_COST['BILL_SEVEN'],
                                      'government official', 4),
                 lambda s: s.move(GOVERNMENT_ACTIONS_COST['BILL_SEVEN'],
                                  GOVERNMENT_ACTIONS_IMPACT['BILL_SEVEN']))

phi15 = Operator("Support Bill 8 that entices car companies to donate more "
                 + "to political campaigns: cost - %s, impact - %s"
                 % (GOVERNMENT_ACTIONS_COST['BILL_EIGHT'], GOVERNMENT_ACTIONS_IMPACT['BILL_EIGHT']),
                 lambda s: s.can_move(GOVERNMENT_ACTIONS_COST['BILL_EIGHT'],
                                      'government official', 4),
                 lambda s: s.move(GOVERNMENT_ACTIONS_COST['BILL_EIGHT'],
                                  GOVERNMENT_ACTIONS_IMPACT['BILL_EIGHT']))

OPERATORS = [
    phi0, phi1, phi2, phi3,
    phi4, phi5, phi6, phi7,
    phi8, phi9, phi10, phi11,
    phi12, phi13, phi14, phi15
]

#</OPERATORS>

#<GOAL_MESSAGE_FUNCION>
GOAL_MESSAGE_FUNCTION = lambda s: s.goal_message()
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
 #</STATE_VIS>



