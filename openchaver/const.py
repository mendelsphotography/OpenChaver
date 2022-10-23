import os
import sys
from pathlib import Path
import oschmod
from .utils import is_frozen

TESTING = not is_frozen()  # Is testing if not frozen

PROGRAM_NAME = "OpenChaver"
SERVICE_NAME = ("OpenChaver Service (TESTING)"
                if TESTING else "OpenChaver Service")
EXE_NAME = 'openchaver.exe' if os.name == 'nt' else 'openchaver'

# Endpoints
BASE_URL = "https://openchaver.com"
API_BASE_URL = "https://api.openchaver.com"

# Port of local server
LOCAL_SERVER_PORT = 61195

# Dirs
if TESTING:
    INSTALL_DIR = Path(__file__).parent.parent  # Root of the project
    SYSTEM_DATA_DIR = Path(__file__).parent.parent / "system_data"
    USER_DATA_DIR = Path(__file__).parent.parent / "user_data"
elif os.name == 'nt':
    INSTALL_DIR = Path(
        os.path.expandvars('%ProgramFiles(x86)%')) / PROGRAM_NAME
    SYSTEM_DATA_DIR = Path(os.path.expandvars('%ProgramData%')) / PROGRAM_NAME
    USER_DATA_DIR = Path(os.getenv('APPDATA')) / PROGRAM_NAME
else:
    print('Unsupported OS')
    exit(1)

# Where AI models are stored
MODEL_DIR = USER_DATA_DIR / "nsfw_model"

# Where the Config file is stored
DATABASE_DIR = SYSTEM_DATA_DIR / 'db'

# Where the logs are stored, theseare user specific
LOG_DIR = USER_DATA_DIR / 'logs'

# Creating directories
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Creating system data dir needs admin privileges
if not DATABASE_DIR.exists():
    try:
        DATABASE_DIR.mkdir(parents=True, exist_ok=True)
        oschmod.set_mode(str(DATABASE_DIR), 'a+rwx')
    except:  # noqa: E722
        pass  # This is OK, the service will have privileges to create the dir

if not MODEL_DIR.exists():
    try:
        MODEL_DIR.mkdir(parents=True, exist_ok=True)
        oschmod.set_mode(str(MODEL_DIR), 'a+rwx')
    except:  # noqa: E722
        pass  # This is OK, the service will have privileges to create the dir

LOG_FILE = LOG_DIR / 'openchaver.log'
DB_PATH = DATABASE_DIR / 'database.db'

if TESTING:
    BASE_EXE = Path(sys.executable)
    SERVICES_ARGS = f'"{SYSTEM_DATA_DIR.parent / "openchaver.py"}" runservice'
    SERVICE_COMMAND = f'"{BASE_EXE}" {SERVICES_ARGS}'
    MONITOR_ARGS = f'"{SYSTEM_DATA_DIR.parent / "openchaver.py"}" runmonitor'
    MONITOR_COMMAND = f'"{BASE_EXE}" {MONITOR_ARGS}'
    MONITOR_COMMAND_LIST = [
        str(BASE_EXE),
        str(SYSTEM_DATA_DIR.parent / "openchaver.py"), "runmonitor"
    ]
else:
    BASE_EXE = INSTALL_DIR / 'openchaver.exe'
    SERVICES_ARGS = 'runservice'
    SERVICE_COMMAND = f'"{BASE_EXE}" {SERVICES_ARGS}'
    MONITOR_ARGS = 'runmonitor'
    MONITOR_COMMAND = f'"{BASE_EXE}" {MONITOR_ARGS}'
    MONITOR_COMMAND_LIST = [str(BASE_EXE), "runmonitor"]

# AI Models
DETECTION_MODEL_URL = 'https://pub-43a5d92b0b0b4908a9aec2a745986a23.r2.dev/detector_v2_default_checkpoint.onnx'  # noqa: E501
DETECTION_MODEL_SHA256_HASH = "D4BE1C504BE61851D9745E6DA8FA09455EB39B8856626DD6B5CA413C9E8B1578"  # noqa: E501
DETECTION_MODEL_PATH = MODEL_DIR / 'detector_v2_default_checkpoint.onnx'

CLASSIFICATION_MODEL_URL = 'https://pub-43a5d92b0b0b4908a9aec2a745986a23.r2.dev/open-nsfw.onnx'  # noqa: E501
CLASSIFICATION_MODEL_SHA256_HASH = "864BB37BF8863564B87EB330AB8C785A79A773F4E7C43CB96DB52ED8611305FA"  # noqa: E501
CLASSIFICATION_MODEL_PATH = MODEL_DIR / 'open-nsfw.onnx'

# Bad Words for profanity filter
BAD_WORDS = [
    "2 girls 1 cup",
    "2g1c",
    "4r5e",
    "5h1t",
    "5hit",
    "a55",
    "a_s_s",
    "acrotomophilia",
    "alabama hot pocket",
    "alaskan pipeline",
    "anal",
    "anilingus",
    "anus",
    "apeshit",
    "ar5e",
    "arrse",
    "arse",
    "arsehole",
    "ass",
    "ass-fucker",
    "ass-hat",
    "ass-pirate",
    "assbag",
    "assbandit",
    "assbanger",
    "assbite",
    "assclown",
    "asscock",
    "asscracker",
    "asses",
    "assface",
    "assfucker",
    "assfukka",
    "assgoblin",
    "asshat",
    "asshead",
    "asshole",
    "assholes",
    "asshopper",
    "assjacker",
    "asslick",
    "asslicker",
    "assmonkey",
    "assmunch",
    "assmuncher",
    "asspirate",
    "assshole",
    "asssucker",
    "asswad",
    "asswhole",
    "asswipe",
    "auto erotic",
    "autoerotic",
    "b!tch",
    "b00bs",
    "b17ch",
    "b1tch",
    "babeland",
    "baby batter",
    "baby juice",
    "ball gag",
    "ball gravy",
    "ball kicking",
    "ball licking",
    "ball sack",
    "ball sucking",
    "ballbag",
    "balls",
    "ballsack",
    "bampot",
    "bangbros",
    "bareback",
    "barely legal",
    "barenaked",
    "bastard",
    "bastardo",
    "bastinado",
    "bbw",
    "bdsm",
    "beaner",
    "beaners",
    "beastial",
    "beastiality",
    "beastility",
    "beaver cleaver",
    "beaver lips",
    "bellend",
    "bestial",
    "bestiality",
    "bi+ch",
    "biatch",
    "big black",
    "big breasts",
    "big knockers",
    "big tits",
    "bimbos",
    "birdlock",
    "bitch",
    "bitcher",
    "bitchers",
    "bitches",
    "bitchin",
    "bitching",
    "black cock",
    "blonde action",
    "blonde on blonde action",
    "bloody",
    "blow job",
    "blow your load",
    "blowjob",
    "blowjobs",
    "blue waffle",
    "blumpkin",
    "boiolas",
    "bollock",
    "bollocks",
    "bollok",
    "bollox",
    "bondage",
    "boner",
    "boob",
    "boobie",
    "boobs",
    "booobs",
    "boooobs",
    "booooobs",
    "booooooobs",
    "booty call",
    "breasts",
    "brown showers",
    "brunette action",
    "buceta",
    "bugger",
    "bukkake",
    "bulldyke",
    "bullet vibe",
    "bullshit",
    "bum",
    "bung hole",
    "bunghole",
    "bunny fucker",
    "busty",
    "butt",
    "butt-pirate",
    "buttcheeks",
    "butthole",
    "buttmunch",
    "buttplug",
    "c0ck",
    "c0cksucker",
    "camel toe",
    "camgirl",
    "camslut",
    "camwhore",
    "carpet muncher",
    "carpetmuncher",
    "cawk",
    "chinc",
    "chink",
    "choad",
    "chocolate rosebuds",
    "chode",
    "cipa",
    "circlejerk",
    "cl1t",
    "cleveland steamer",
    "clit",
    "clitface",
    "clitoris",
    "clits",
    "clover clamps",
    "clusterfuck",
    "cnut",
    "cock",
    "cock-sucker",
    "cockbite",
    "cockburger",
    "cockface",
    "cockhead",
    "cockjockey",
    "cockknoker",
    "cockmaster",
    "cockmongler",
    "cockmongruel",
    "cockmonkey",
    "cockmunch",
    "cockmuncher",
    "cocknose",
    "cocknugget",
    "cocks",
    "cockshit",
    "cocksmith",
    "cocksmoker",
    "cocksuck",
    "cocksuck ",
    "cocksucked",
    "cocksucked ",
    "cocksucker",
    "cocksucking",
    "cocksucks ",
    "cocksuka",
    "cocksukka",
    "cok",
    "cokmuncher",
    "coksucka",
    "coochie",
    "coochy",
    "coon",
    "coons",
    "cooter",
    "coprolagnia",
    "coprophilia",
    "cornhole",
    "cox",
    "crap",
    "creampie",
    "cum",
    "cumbubble",
    "cumdumpster",
    "cumguzzler",
    "cumjockey",
    "cummer",
    "cumming",
    "cums",
    "cumshot",
    "cumslut",
    "cumtart",
    "cunilingus",
    "cunillingus",
    "cunnie",
    "cunnilingus",
    "cunt",
    "cuntface",
    "cunthole",
    "cuntlick",
    "cuntlick ",
    "cuntlicker",
    "cuntlicker ",
    "cuntlicking",
    "cuntlicking ",
    "cuntrag",
    "cunts",
    "cyalis",
    "cyberfuc",
    "cyberfuck ",
    "cyberfucked ",
    "cyberfucker",
    "cyberfuckers",
    "cyberfucking ",
    "d1ck",
    "dammit",
    "damn",
    "darkie",
    "date rape",
    "daterape",
    "deep throat",
    "deepthroat",
    "dendrophilia",
    "dick",
    "dickbag",
    "dickbeater",
    "dickface",
    "dickhead",
    "dickhole",
    "dickjuice",
    "dickmilk",
    "dickmonger",
    "dickslap",
    "dicksucker",
    "dickwad",
    "dickweasel",
    "dickweed",
    "dickwod",
    "dike",
    "dildo",
    "dildos",
    "dingleberries",
    "dingleberry",
    "dink",
    "dinks",
    "dipshit",
    "dirsa",
    "dirty pillows",
    "dirty sanchez",
    "dlck",
    "dog style",
    "dog-fucker",
    "doggie style",
    "doggiestyle",
    "doggin",
    "dogging",
    "doggy style",
    "doggystyle",
    "dolcett",
    "domination",
    "dominatrix",
    "dommes",
    "donkey punch",
    "donkeyribber",
    "doochbag",
    "dookie",
    "doosh",
    "double dong",
    "double penetration",
    "douche",
    "douchebag",
    "dp action",
    "dry hump",
    "duche",
    "dumbshit",
    "dumshit",
    "dvda",
    "dyke",
    "eat my ass",
    "ecchi",
    "ejaculate",
    "ejaculated",
    "ejaculates ",
    "ejaculating ",
    "ejaculatings",
    "ejaculation",
    "ejakulate",
    "erotic",
    "erotism",
    "escort",
    "eunuch",
    "f u c k",
    "f u c k e r",
    "f4nny",
    "f_u_c_k",
    "fag",
    "fagbag",
    "fagg",
    "fagging",
    "faggit",
    "faggitt",
    "faggot",
    "faggs",
    "fagot",
    "fagots",
    "fags",
    "fagtard",
    "fanny",
    "fannyflaps",
    "fannyfucker",
    "fanyy",
    "fart",
    "farted",
    "farting",
    "farty",
    "fatass",
    "fcuk",
    "fcuker",
    "fcuking",
    "fecal",
    "feck",
    "fecker",
    "felatio",
    "felch",
    "felching",
    "fellate",
    "fellatio",
    "feltch",
    "female squirting",
    "femdom",
    "figging",
    "fingerbang",
    "fingerfuck ",
    "fingerfucked ",
    "fingerfucker ",
    "fingerfuckers",
    "fingerfucking ",
    "fingerfucks ",
    "fingering",
    "fistfuck",
    "fistfucked ",
    "fistfucker ",
    "fistfuckers ",
    "fistfucking ",
    "fistfuckings ",
    "fistfucks ",
    "fisting",
    "flamer",
    "flange",
    "fook",
    "fooker",
    "foot fetish",
    "footjob",
    "frotting",
    "fuck",
    "fuck buttons",
    "fucka",
    "fucked",
    "fucker",
    "fuckers",
    "fuckhead",
    "fuckheads",
    "fuckin",
    "fucking",
    "fuckings",
    "fuckingshitmotherfucker",
    "fuckme ",
    "fucks",
    "fucktards",
    "fuckwhit",
    "fuckwit",
    "fudge packer",
    "fudgepacker",
    "fuk",
    "fuker",
    "fukker",
    "fukkin",
    "fuks",
    "fukwhit",
    "fukwit",
    "futanari",
    "fux",
    "fux0r",
    "g-spot",
    "gang bang",
    "gangbang",
    "gangbanged",
    "gangbanged ",
    "gangbangs ",
    "gay sex",
    "gayass",
    "gaybob",
    "gaydo",
    "gaylord",
    "gaysex",
    "gaytard",
    "gaywad",
    "genitals",
    "giant cock",
    "girl on",
    "girl on top",
    "girls gone wild",
    "goatcx",
    "goatse",
    "god damn",
    "god-dam",
    "god-damned",
    "goddamn",
    "goddamned",
    "gokkun",
    "golden shower",
    "goo girl",
    "gooch",
    "goodpoop",
    "gook",
    "goregasm",
    "gringo",
    "grope",
    "group sex",
    "guido",
    "guro",
    "hand job",
    "handjob",
    "hard core",
    "hardcore",
    "hardcoresex ",
    "heeb",
    "hell",
    "hentai",
    "heshe",
    "ho",
    "hoar",
    "hoare",
    "hoe",
    "hoer",
    "homo",
    "homoerotic",
    "honkey",
    "honky",
    "hooker",
    "hore",
    "horniest",
    "horny",
    "hot carl",
    "hot chick",
    "hotsex",
    "how to kill",
    "how to murder",
    "huge fat",
    "humping",
    "incest",
    "intercourse",
    "jack off",
    "jack-off ",
    "jackass",
    "jackoff",
    "jail bait",
    "jailbait",
    "jap",
    "jelly donut",
    "jerk off",
    "jerk-off ",
    "jigaboo",
    "jiggaboo",
    "jiggerboo",
    "jism",
    "jiz",
    "jiz ",
    "jizm",
    "jizm ",
    "jizz",
    "juggs",
    "kawk",
    "kike",
    "kinbaku",
    "kinkster",
    "kinky",
    "kiunt",
    "knob",
    "knobbing",
    "knobead",
    "knobed",
    "knobend",
    "knobhead",
    "knobjocky",
    "knobjokey",
    "kock",
    "kondum",
    "kondums",
    "kooch",
    "kootch",
    "kum",
    "kumer",
    "kummer",
    "kumming",
    "kums",
    "kunilingus",
    "kunt",
    "kyke",
    "l3i+ch",
    "l3itch",
    "labia",
    "leather restraint",
    "leather straight jacket",
    "lemon party",
    "lesbo",
    "lezzie",
    "lmfao",
    "lolita",
    "lovemaking",
    "lust",
    "lusting",
    "m0f0",
    "m0fo",
    "m45terbate",
    "ma5terb8",
    "ma5terbate",
    "make me come",
    "male squirting",
    "masochist",
    "master-bate",
    "masterb8",
    "masterbat*",
    "masterbat3",
    "masterbate",
    "masterbation",
    "masterbations",
    "masturbate",
    "menage a trois",
    "milf",
    "minge",
    "missionary position",
    "mo-fo",
    "mof0",
    "mofo",
    "mothafuck",
    "mothafucka",
    "mothafuckas",
    "mothafuckaz",
    "mothafucked ",
    "mothafucker",
    "mothafuckers",
    "mothafuckin",
    "mothafucking ",
    "mothafuckings",
    "mothafucks",
    "mother fucker",
    "motherfuck",
    "motherfucked",
    "motherfucker",
    "motherfuckers",
    "motherfuckin",
    "motherfucking",
    "motherfuckings",
    "motherfuckka",
    "motherfucks",
    "mound of venus",
    "mr hands",
    "muff",
    "muff diver",
    "muffdiver",
    "muffdiving",
    "mutha",
    "muthafecker",
    "muthafuckker",
    "muther",
    "mutherfucker",
    "n1gga",
    "n1gger",
    "nambla",
    "nawashi",
    "nazi",
    "negro",
    "neonazi",
    "nig nog",
    "nigg3r",
    "nigg4h",
    "nigga",
    "niggah",
    "niggas",
    "niggaz",
    "nigger",
    "niggers ",
    "niglet",
    "nimphomania",
    "nipple",
    "nipples",
    "nob",
    "nob jokey",
    "nobhead",
    "nobjocky",
    "nobjokey",
    "nsfw images",
    "nude",
    "nudity",
    "numbnuts",
    "nutsack",
    "nympho",
    "nymphomania",
    "octopussy",
    "omorashi",
    "one cup two girls",
    "one guy one jar",
    "orgasim",
    "orgasim ",
    "orgasims ",
    "orgasm",
    "orgasms ",
    "orgy",
    "p0rn",
    "paedophile",
    "paki",
    "panooch",
    "panties",
    "panty",
    "pawn",
    "pecker",
    "pe",
    "phuking",
    "phukked",
    "phukking",
    "phuks",
    "phuq",
    "piece of shit",
    "pigfucker",
    "pimpis",
    "pis",
    "pises",
    "pisin",
    "pising",
    "pisof",
    "piss",
    "piss pig",
    "pissed",
    "pisser",
    "pissers",
    "pisses ",
    "pissflap",
    "pissflaps",
    "pissin",
    "pissin ",
    "pissing",
    "pissoff",
    "pissoff ",
    "pisspig",
    "playboy",
    "pleasure chest",
    "pole smoker",
    "polesmoker",
    "pollock",
    "ponyplay",
    "poo",
    "poof",
    "poon",
    "poonani",
    "poonany",
    "poontang",
    "poop",
    "poop chute",
    "poopchute",
    "porn",
    "porno",
    "pornography",
    "pornos",
    "prick",
    "pricks ",
    "prince albert piercing",
    "pron",
    "pthc",
    "pube",
    "pubes",
    "punanny",
    "punany",
    "punta",
    "pusies",
    "pusse",
    "pussi",
    "pussies",
    "pussy",
    "pussylicking",
    "pussys ",
    "pusy",
    "puto",
    "queaf",
    "queef",
    "queerbait",
    "queerhole",
    "quim",
    "raghead",
    "raging boner",
    "rape",
    "raping",
    "rapist",
    "rectum",
    "renob",
    "retard",
    "reverse cowgirl",
    "rimjaw",
    "rimjob",
    "rimming",
    "rosy palm",
    "rosy palm and her 5 sisters",
    "ruski",
    "rusty trombone",
    "s hit",
    "s&m",
    "s.o.b.",
    "s_h_i_t",
    "sadism",
    "sadist",
    "santorum",
    "scat",
    "schlong",
    "scissoring",
    "screwing",
    "scroat",
    "scrote",
    "scrotum",
    "semen",
    "sex",
    "sexo",
    "sexy",
    "sh!+",
    "sh!t",
    "sh1t",
    "shag",
    "shagger",
    "shaggin",
    "shagging",
    "shaved beaver",
    "shaved pussy",
    "shemale",
    "shi+",
    "shibari",
    "shit",
    "shit-ass",
    "shit-bag",
    "shit-bagger",
    "shit-brain",
    "shit-breath",
    "shit-cunt",
    "shit-dick",
    "shit-eating",
    "shit-face",
    "shit-faced",
    "shit-fit",
    "shit-head",
    "shit-heel",
    "shit-hole",
    "shit-house",
    "shit-load",
    "shit-pot",
    "shit-spitter",
    "shit-stain",
    "shitass",
    "shitbag",
    "shitbagger",
    "shitblimp",
    "shitbrain",
    "shitbreath",
    "shitcunt",
    "shitdick",
    "shite",
    "shiteating",
    "shited",
    "shitey",
    "shitface",
    "shitfaced",
    "shitfit",
    "shitfuck",
    "shitfull",
    "shithead",
    "shitheel",
    "shithole",
    "shithouse",
    "shiting",
    "shitings",
    "shitload",
    "shitpot",
    "shits",
    "shitspitter",
    "shitstain",
    "shitted",
    "shitter",
    "shitters ",
    "shittiest",
    "shitting",
    "shittings",
    "shitty",
    "shitty ",
    "shity",
    "shiz",
    "shiznit",
    "shota",
    "shrimping",
    "skank",
    "skeet",
    "slanteye",
    "slut",
    "slutbag",
    "sluts",
    "smeg",
    "smegma",
    "smut",
    "snatch",
    "snowballing",
    "sodomize",
    "sodomy",
    "son-of-a-bitch",
    "spac",
    "spic",
    "spick",
    "splooge",
    "splooge moose",
    "spooge",
    "spread legs",
    "spunk",
    "strap on",
    "strapon",
    "strappado",
    "strip club",
    "style doggy",
    "suck",
    "sucks",
    "suicide girls",
    "sultry women",
    "swastika",
    "swinger",
    "t1tt1e5",
    "t1tties",
    "tainted love",
    "tard",
    "taste my",
    "tea bagging",
    "teets",
    "teez",
    "testical",
    "testicle",
    "threesome",
    "throating",
    "thundercunt",
    "tied up",
    "tight white",
    "tit",
    "titfuck",
    "tits",
    "titt",
    "tittie5",
    "tittiefucker",
    "titties",
    "titty",
    "tittyfuck",
    "tittywank",
    "titwank",
    "tongue in a",
    "topless",
    "tosser",
    "towelhead",
    "tranny",
    "tribadism",
    "tub girl",
    "tubgirl",
    "turd",
    "tushy",
    "tw4t",
    "twat",
    "twathead",
    "twatlips",
    "twatty",
    "twink",
    "twinkie",
    "two girls one cup",
    "twunt",
    "twunter",
    "undressing",
    "upskirt",
    "urethra play",
    "urophilia",
    "v14gra",
    "v1gra",
    "va-j-j",
    "vag",
    "vagina",
    "venus mound",
    "viagra",
    "vibrator",
    "violet wand",
    "vjayjay",
    "vorarephilia",
    "voyeur",
    "vulva",
    "w00se",
    "wang",
    "wank",
    "wanker",
    "wanky",
    "wet dream",
    "wetback",
    "white power",
    "whoar",
    "whore",
    "willies",
    "willy",
    "wrapping men",
    "wrinkled starfish",
    "xrated",
    "xx",
    "xxx",
    "yaoi",
    "yellow showers",
    "yiffy",
    "zoophilia",
]
