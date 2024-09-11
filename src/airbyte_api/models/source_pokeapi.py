"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class PokemonName(str, Enum):
    r"""Pokemon requested from the API."""
    BULBASAUR = 'bulbasaur'
    IVYSAUR = 'ivysaur'
    VENUSAUR = 'venusaur'
    CHARMANDER = 'charmander'
    CHARMELEON = 'charmeleon'
    CHARIZARD = 'charizard'
    SQUIRTLE = 'squirtle'
    WARTORTLE = 'wartortle'
    BLASTOISE = 'blastoise'
    CATERPIE = 'caterpie'
    METAPOD = 'metapod'
    BUTTERFREE = 'butterfree'
    WEEDLE = 'weedle'
    KAKUNA = 'kakuna'
    BEEDRILL = 'beedrill'
    PIDGEY = 'pidgey'
    PIDGEOTTO = 'pidgeotto'
    PIDGEOT = 'pidgeot'
    RATTATA = 'rattata'
    RATICATE = 'raticate'
    SPEAROW = 'spearow'
    FEAROW = 'fearow'
    EKANS = 'ekans'
    ARBOK = 'arbok'
    PIKACHU = 'pikachu'
    RAICHU = 'raichu'
    SANDSHREW = 'sandshrew'
    SANDSLASH = 'sandslash'
    NIDORANF = 'nidoranf'
    NIDORINA = 'nidorina'
    NIDOQUEEN = 'nidoqueen'
    NIDORANM = 'nidoranm'
    NIDORINO = 'nidorino'
    NIDOKING = 'nidoking'
    CLEFAIRY = 'clefairy'
    CLEFABLE = 'clefable'
    VULPIX = 'vulpix'
    NINETALES = 'ninetales'
    JIGGLYPUFF = 'jigglypuff'
    WIGGLYTUFF = 'wigglytuff'
    ZUBAT = 'zubat'
    GOLBAT = 'golbat'
    ODDISH = 'oddish'
    GLOOM = 'gloom'
    VILEPLUME = 'vileplume'
    PARAS = 'paras'
    PARASECT = 'parasect'
    VENONAT = 'venonat'
    VENOMOTH = 'venomoth'
    DIGLETT = 'diglett'
    DUGTRIO = 'dugtrio'
    MEOWTH = 'meowth'
    PERSIAN = 'persian'
    PSYDUCK = 'psyduck'
    GOLDUCK = 'golduck'
    MANKEY = 'mankey'
    PRIMEAPE = 'primeape'
    GROWLITHE = 'growlithe'
    ARCANINE = 'arcanine'
    POLIWAG = 'poliwag'
    POLIWHIRL = 'poliwhirl'
    POLIWRATH = 'poliwrath'
    ABRA = 'abra'
    KADABRA = 'kadabra'
    ALAKAZAM = 'alakazam'
    MACHOP = 'machop'
    MACHOKE = 'machoke'
    MACHAMP = 'machamp'
    BELLSPROUT = 'bellsprout'
    WEEPINBELL = 'weepinbell'
    VICTREEBEL = 'victreebel'
    TENTACOOL = 'tentacool'
    TENTACRUEL = 'tentacruel'
    GEODUDE = 'geodude'
    GRAVELER = 'graveler'
    GOLEM = 'golem'
    PONYTA = 'ponyta'
    RAPIDASH = 'rapidash'
    SLOWPOKE = 'slowpoke'
    SLOWBRO = 'slowbro'
    MAGNEMITE = 'magnemite'
    MAGNETON = 'magneton'
    FARFETCHD = 'farfetchd'
    DODUO = 'doduo'
    DODRIO = 'dodrio'
    SEEL = 'seel'
    DEWGONG = 'dewgong'
    GRIMER = 'grimer'
    MUK = 'muk'
    SHELLDER = 'shellder'
    CLOYSTER = 'cloyster'
    GASTLY = 'gastly'
    HAUNTER = 'haunter'
    GENGAR = 'gengar'
    ONIX = 'onix'
    DROWZEE = 'drowzee'
    HYPNO = 'hypno'
    KRABBY = 'krabby'
    KINGLER = 'kingler'
    VOLTORB = 'voltorb'
    ELECTRODE = 'electrode'
    EXEGGCUTE = 'exeggcute'
    EXEGGUTOR = 'exeggutor'
    CUBONE = 'cubone'
    MAROWAK = 'marowak'
    HITMONLEE = 'hitmonlee'
    HITMONCHAN = 'hitmonchan'
    LICKITUNG = 'lickitung'
    KOFFING = 'koffing'
    WEEZING = 'weezing'
    RHYHORN = 'rhyhorn'
    RHYDON = 'rhydon'
    CHANSEY = 'chansey'
    TANGELA = 'tangela'
    KANGASKHAN = 'kangaskhan'
    HORSEA = 'horsea'
    SEADRA = 'seadra'
    GOLDEEN = 'goldeen'
    SEAKING = 'seaking'
    STARYU = 'staryu'
    STARMIE = 'starmie'
    MRMIME = 'mrmime'
    SCYTHER = 'scyther'
    JYNX = 'jynx'
    ELECTABUZZ = 'electabuzz'
    MAGMAR = 'magmar'
    PINSIR = 'pinsir'
    TAUROS = 'tauros'
    MAGIKARP = 'magikarp'
    GYARADOS = 'gyarados'
    LAPRAS = 'lapras'
    DITTO = 'ditto'
    EEVEE = 'eevee'
    VAPOREON = 'vaporeon'
    JOLTEON = 'jolteon'
    FLAREON = 'flareon'
    PORYGON = 'porygon'
    OMANYTE = 'omanyte'
    OMASTAR = 'omastar'
    KABUTO = 'kabuto'
    KABUTOPS = 'kabutops'
    AERODACTYL = 'aerodactyl'
    SNORLAX = 'snorlax'
    ARTICUNO = 'articuno'
    ZAPDOS = 'zapdos'
    MOLTRES = 'moltres'
    DRATINI = 'dratini'
    DRAGONAIR = 'dragonair'
    DRAGONITE = 'dragonite'
    MEWTWO = 'mewtwo'
    MEW = 'mew'
    CHIKORITA = 'chikorita'
    BAYLEEF = 'bayleef'
    MEGANIUM = 'meganium'
    CYNDAQUIL = 'cyndaquil'
    QUILAVA = 'quilava'
    TYPHLOSION = 'typhlosion'
    TOTODILE = 'totodile'
    CROCONAW = 'croconaw'
    FERALIGATR = 'feraligatr'
    SENTRET = 'sentret'
    FURRET = 'furret'
    HOOTHOOT = 'hoothoot'
    NOCTOWL = 'noctowl'
    LEDYBA = 'ledyba'
    LEDIAN = 'ledian'
    SPINARAK = 'spinarak'
    ARIADOS = 'ariados'
    CROBAT = 'crobat'
    CHINCHOU = 'chinchou'
    LANTURN = 'lanturn'
    PICHU = 'pichu'
    CLEFFA = 'cleffa'
    IGGLYBUFF = 'igglybuff'
    TOGEPI = 'togepi'
    TOGETIC = 'togetic'
    NATU = 'natu'
    XATU = 'xatu'
    MAREEP = 'mareep'
    FLAAFFY = 'flaaffy'
    AMPHAROS = 'ampharos'
    BELLOSSOM = 'bellossom'
    MARILL = 'marill'
    AZUMARILL = 'azumarill'
    SUDOWOODO = 'sudowoodo'
    POLITOED = 'politoed'
    HOPPIP = 'hoppip'
    SKIPLOOM = 'skiploom'
    JUMPLUFF = 'jumpluff'
    AIPOM = 'aipom'
    SUNKERN = 'sunkern'
    SUNFLORA = 'sunflora'
    YANMA = 'yanma'
    WOOPER = 'wooper'
    QUAGSIRE = 'quagsire'
    ESPEON = 'espeon'
    UMBREON = 'umbreon'
    MURKROW = 'murkrow'
    SLOWKING = 'slowking'
    MISDREAVUS = 'misdreavus'
    UNOWN = 'unown'
    WOBBUFFET = 'wobbuffet'
    GIRAFARIG = 'girafarig'
    PINECO = 'pineco'
    FORRETRESS = 'forretress'
    DUNSPARCE = 'dunsparce'
    GLIGAR = 'gligar'
    STEELIX = 'steelix'
    SNUBBULL = 'snubbull'
    GRANBULL = 'granbull'
    QWILFISH = 'qwilfish'
    SCIZOR = 'scizor'
    SHUCKLE = 'shuckle'
    HERACROSS = 'heracross'
    SNEASEL = 'sneasel'
    TEDDIURSA = 'teddiursa'
    URSARING = 'ursaring'
    SLUGMA = 'slugma'
    MAGCARGO = 'magcargo'
    SWINUB = 'swinub'
    PILOSWINE = 'piloswine'
    CORSOLA = 'corsola'
    REMORAID = 'remoraid'
    OCTILLERY = 'octillery'
    DELIBIRD = 'delibird'
    MANTINE = 'mantine'
    SKARMORY = 'skarmory'
    HOUNDOUR = 'houndour'
    HOUNDOOM = 'houndoom'
    KINGDRA = 'kingdra'
    PHANPY = 'phanpy'
    DONPHAN = 'donphan'
    PORYGON2 = 'porygon2'
    STANTLER = 'stantler'
    SMEARGLE = 'smeargle'
    TYROGUE = 'tyrogue'
    HITMONTOP = 'hitmontop'
    SMOOCHUM = 'smoochum'
    ELEKID = 'elekid'
    MAGBY = 'magby'
    MILTANK = 'miltank'
    BLISSEY = 'blissey'
    RAIKOU = 'raikou'
    ENTEI = 'entei'
    SUICUNE = 'suicune'
    LARVITAR = 'larvitar'
    PUPITAR = 'pupitar'
    TYRANITAR = 'tyranitar'
    LUGIA = 'lugia'
    HO_OH = 'ho-oh'
    CELEBI = 'celebi'
    TREECKO = 'treecko'
    GROVYLE = 'grovyle'
    SCEPTILE = 'sceptile'
    TORCHIC = 'torchic'
    COMBUSKEN = 'combusken'
    BLAZIKEN = 'blaziken'
    MUDKIP = 'mudkip'
    MARSHTOMP = 'marshtomp'
    SWAMPERT = 'swampert'
    POOCHYENA = 'poochyena'
    MIGHTYENA = 'mightyena'
    ZIGZAGOON = 'zigzagoon'
    LINOONE = 'linoone'
    WURMPLE = 'wurmple'
    SILCOON = 'silcoon'
    BEAUTIFLY = 'beautifly'
    CASCOON = 'cascoon'
    DUSTOX = 'dustox'
    LOTAD = 'lotad'
    LOMBRE = 'lombre'
    LUDICOLO = 'ludicolo'
    SEEDOT = 'seedot'
    NUZLEAF = 'nuzleaf'
    SHIFTRY = 'shiftry'
    TAILLOW = 'taillow'
    SWELLOW = 'swellow'
    WINGULL = 'wingull'
    PELIPPER = 'pelipper'
    RALTS = 'ralts'
    KIRLIA = 'kirlia'
    GARDEVOIR = 'gardevoir'
    SURSKIT = 'surskit'
    MASQUERAIN = 'masquerain'
    SHROOMISH = 'shroomish'
    BRELOOM = 'breloom'
    SLAKOTH = 'slakoth'
    VIGOROTH = 'vigoroth'
    SLAKING = 'slaking'
    NINCADA = 'nincada'
    NINJASK = 'ninjask'
    SHEDINJA = 'shedinja'
    WHISMUR = 'whismur'
    LOUDRED = 'loudred'
    EXPLOUD = 'exploud'
    MAKUHITA = 'makuhita'
    HARIYAMA = 'hariyama'
    AZURILL = 'azurill'
    NOSEPASS = 'nosepass'
    SKITTY = 'skitty'
    DELCATTY = 'delcatty'
    SABLEYE = 'sableye'
    MAWILE = 'mawile'
    ARON = 'aron'
    LAIRON = 'lairon'
    AGGRON = 'aggron'
    MEDITITE = 'meditite'
    MEDICHAM = 'medicham'
    ELECTRIKE = 'electrike'
    MANECTRIC = 'manectric'
    PLUSLE = 'plusle'
    MINUN = 'minun'
    VOLBEAT = 'volbeat'
    ILLUMISE = 'illumise'
    ROSELIA = 'roselia'
    GULPIN = 'gulpin'
    SWALOT = 'swalot'
    CARVANHA = 'carvanha'
    SHARPEDO = 'sharpedo'
    WAILMER = 'wailmer'
    WAILORD = 'wailord'
    NUMEL = 'numel'
    CAMERUPT = 'camerupt'
    TORKOAL = 'torkoal'
    SPOINK = 'spoink'
    GRUMPIG = 'grumpig'
    SPINDA = 'spinda'
    TRAPINCH = 'trapinch'
    VIBRAVA = 'vibrava'
    FLYGON = 'flygon'
    CACNEA = 'cacnea'
    CACTURNE = 'cacturne'
    SWABLU = 'swablu'
    ALTARIA = 'altaria'
    ZANGOOSE = 'zangoose'
    SEVIPER = 'seviper'
    LUNATONE = 'lunatone'
    SOLROCK = 'solrock'
    BARBOACH = 'barboach'
    WHISCASH = 'whiscash'
    CORPHISH = 'corphish'
    CRAWDAUNT = 'crawdaunt'
    BALTOY = 'baltoy'
    CLAYDOL = 'claydol'
    LILEEP = 'lileep'
    CRADILY = 'cradily'
    ANORITH = 'anorith'
    ARMALDO = 'armaldo'
    FEEBAS = 'feebas'
    MILOTIC = 'milotic'
    CASTFORM = 'castform'
    KECLEON = 'kecleon'
    SHUPPET = 'shuppet'
    BANETTE = 'banette'
    DUSKULL = 'duskull'
    DUSCLOPS = 'dusclops'
    TROPIUS = 'tropius'
    CHIMECHO = 'chimecho'
    ABSOL = 'absol'
    WYNAUT = 'wynaut'
    SNORUNT = 'snorunt'
    GLALIE = 'glalie'
    SPHEAL = 'spheal'
    SEALEO = 'sealeo'
    WALREIN = 'walrein'
    CLAMPERL = 'clamperl'
    HUNTAIL = 'huntail'
    GOREBYSS = 'gorebyss'
    RELICANTH = 'relicanth'
    LUVDISC = 'luvdisc'
    BAGON = 'bagon'
    SHELGON = 'shelgon'
    SALAMENCE = 'salamence'
    BELDUM = 'beldum'
    METANG = 'metang'
    METAGROSS = 'metagross'
    REGIROCK = 'regirock'
    REGICE = 'regice'
    REGISTEEL = 'registeel'
    LATIAS = 'latias'
    LATIOS = 'latios'
    KYOGRE = 'kyogre'
    GROUDON = 'groudon'
    RAYQUAZA = 'rayquaza'
    JIRACHI = 'jirachi'
    DEOXYS = 'deoxys'
    TURTWIG = 'turtwig'
    GROTLE = 'grotle'
    TORTERRA = 'torterra'
    CHIMCHAR = 'chimchar'
    MONFERNO = 'monferno'
    INFERNAPE = 'infernape'
    PIPLUP = 'piplup'
    PRINPLUP = 'prinplup'
    EMPOLEON = 'empoleon'
    STARLY = 'starly'
    STARAVIA = 'staravia'
    STARAPTOR = 'staraptor'
    BIDOOF = 'bidoof'
    BIBAREL = 'bibarel'
    KRICKETOT = 'kricketot'
    KRICKETUNE = 'kricketune'
    SHINX = 'shinx'
    LUXIO = 'luxio'
    LUXRAY = 'luxray'
    BUDEW = 'budew'
    ROSERADE = 'roserade'
    CRANIDOS = 'cranidos'
    RAMPARDOS = 'rampardos'
    SHIELDON = 'shieldon'
    BASTIODON = 'bastiodon'
    BURMY = 'burmy'
    WORMADAM = 'wormadam'
    MOTHIM = 'mothim'
    COMBEE = 'combee'
    VESPIQUEN = 'vespiquen'
    PACHIRISU = 'pachirisu'
    BUIZEL = 'buizel'
    FLOATZEL = 'floatzel'
    CHERUBI = 'cherubi'
    CHERRIM = 'cherrim'
    SHELLOS = 'shellos'
    GASTRODON = 'gastrodon'
    AMBIPOM = 'ambipom'
    DRIFLOON = 'drifloon'
    DRIFBLIM = 'drifblim'
    BUNEARY = 'buneary'
    LOPUNNY = 'lopunny'
    MISMAGIUS = 'mismagius'
    HONCHKROW = 'honchkrow'
    GLAMEOW = 'glameow'
    PURUGLY = 'purugly'
    CHINGLING = 'chingling'
    STUNKY = 'stunky'
    SKUNTANK = 'skuntank'
    BRONZOR = 'bronzor'
    BRONZONG = 'bronzong'
    BONSLY = 'bonsly'
    MIMEJR = 'mimejr'
    HAPPINY = 'happiny'
    CHATOT = 'chatot'
    SPIRITOMB = 'spiritomb'
    GIBLE = 'gible'
    GABITE = 'gabite'
    GARCHOMP = 'garchomp'
    MUNCHLAX = 'munchlax'
    RIOLU = 'riolu'
    LUCARIO = 'lucario'
    HIPPOPOTAS = 'hippopotas'
    HIPPOWDON = 'hippowdon'
    SKORUPI = 'skorupi'
    DRAPION = 'drapion'
    CROAGUNK = 'croagunk'
    TOXICROAK = 'toxicroak'
    CARNIVINE = 'carnivine'
    FINNEON = 'finneon'
    LUMINEON = 'lumineon'
    MANTYKE = 'mantyke'
    SNOVER = 'snover'
    ABOMASNOW = 'abomasnow'
    WEAVILE = 'weavile'
    MAGNEZONE = 'magnezone'
    LICKILICKY = 'lickilicky'
    RHYPERIOR = 'rhyperior'
    TANGROWTH = 'tangrowth'
    ELECTIVIRE = 'electivire'
    MAGMORTAR = 'magmortar'
    TOGEKISS = 'togekiss'
    YANMEGA = 'yanmega'
    LEAFEON = 'leafeon'
    GLACEON = 'glaceon'
    GLISCOR = 'gliscor'
    MAMOSWINE = 'mamoswine'
    PORYGON_Z = 'porygon-z'
    GALLADE = 'gallade'
    PROBOPASS = 'probopass'
    DUSKNOIR = 'dusknoir'
    FROSLASS = 'froslass'
    ROTOM = 'rotom'
    UXIE = 'uxie'
    MESPRIT = 'mesprit'
    AZELF = 'azelf'
    DIALGA = 'dialga'
    PALKIA = 'palkia'
    HEATRAN = 'heatran'
    REGIGIGAS = 'regigigas'
    GIRATINA = 'giratina'
    CRESSELIA = 'cresselia'
    PHIONE = 'phione'
    MANAPHY = 'manaphy'
    DARKRAI = 'darkrai'
    SHAYMIN = 'shaymin'
    ARCEUS = 'arceus'
    VICTINI = 'victini'
    SNIVY = 'snivy'
    SERVINE = 'servine'
    SERPERIOR = 'serperior'
    TEPIG = 'tepig'
    PIGNITE = 'pignite'
    EMBOAR = 'emboar'
    OSHAWOTT = 'oshawott'
    DEWOTT = 'dewott'
    SAMUROTT = 'samurott'
    PATRAT = 'patrat'
    WATCHOG = 'watchog'
    LILLIPUP = 'lillipup'
    HERDIER = 'herdier'
    STOUTLAND = 'stoutland'
    PURRLOIN = 'purrloin'
    LIEPARD = 'liepard'
    PANSAGE = 'pansage'
    SIMISAGE = 'simisage'
    PANSEAR = 'pansear'
    SIMISEAR = 'simisear'
    PANPOUR = 'panpour'
    SIMIPOUR = 'simipour'
    MUNNA = 'munna'
    MUSHARNA = 'musharna'
    PIDOVE = 'pidove'
    TRANQUILL = 'tranquill'
    UNFEZANT = 'unfezant'
    BLITZLE = 'blitzle'
    ZEBSTRIKA = 'zebstrika'
    ROGGENROLA = 'roggenrola'
    BOLDORE = 'boldore'
    GIGALITH = 'gigalith'
    WOOBAT = 'woobat'
    SWOOBAT = 'swoobat'
    DRILBUR = 'drilbur'
    EXCADRILL = 'excadrill'
    AUDINO = 'audino'
    TIMBURR = 'timburr'
    GURDURR = 'gurdurr'
    CONKELDURR = 'conkeldurr'
    TYMPOLE = 'tympole'
    PALPITOAD = 'palpitoad'
    SEISMITOAD = 'seismitoad'
    THROH = 'throh'
    SAWK = 'sawk'
    SEWADDLE = 'sewaddle'
    SWADLOON = 'swadloon'
    LEAVANNY = 'leavanny'
    VENIPEDE = 'venipede'
    WHIRLIPEDE = 'whirlipede'
    SCOLIPEDE = 'scolipede'
    COTTONEE = 'cottonee'
    WHIMSICOTT = 'whimsicott'
    PETILIL = 'petilil'
    LILLIGANT = 'lilligant'
    BASCULIN = 'basculin'
    SANDILE = 'sandile'
    KROKOROK = 'krokorok'
    KROOKODILE = 'krookodile'
    DARUMAKA = 'darumaka'
    DARMANITAN = 'darmanitan'
    MARACTUS = 'maractus'
    DWEBBLE = 'dwebble'
    CRUSTLE = 'crustle'
    SCRAGGY = 'scraggy'
    SCRAFTY = 'scrafty'
    SIGILYPH = 'sigilyph'
    YAMASK = 'yamask'
    COFAGRIGUS = 'cofagrigus'
    TIRTOUGA = 'tirtouga'
    CARRACOSTA = 'carracosta'
    ARCHEN = 'archen'
    ARCHEOPS = 'archeops'
    TRUBBISH = 'trubbish'
    GARBODOR = 'garbodor'
    ZORUA = 'zorua'
    ZOROARK = 'zoroark'
    MINCCINO = 'minccino'
    CINCCINO = 'cinccino'
    GOTHITA = 'gothita'
    GOTHORITA = 'gothorita'
    GOTHITELLE = 'gothitelle'
    SOLOSIS = 'solosis'
    DUOSION = 'duosion'
    REUNICLUS = 'reuniclus'
    DUCKLETT = 'ducklett'
    SWANNA = 'swanna'
    VANILLITE = 'vanillite'
    VANILLISH = 'vanillish'
    VANILLUXE = 'vanilluxe'
    DEERLING = 'deerling'
    SAWSBUCK = 'sawsbuck'
    EMOLGA = 'emolga'
    KARRABLAST = 'karrablast'
    ESCAVALIER = 'escavalier'
    FOONGUS = 'foongus'
    AMOONGUSS = 'amoonguss'
    FRILLISH = 'frillish'
    JELLICENT = 'jellicent'
    ALOMOMOLA = 'alomomola'
    JOLTIK = 'joltik'
    GALVANTULA = 'galvantula'
    FERROSEED = 'ferroseed'
    FERROTHORN = 'ferrothorn'
    KLINK = 'klink'
    KLANG = 'klang'
    KLINKLANG = 'klinklang'
    TYNAMO = 'tynamo'
    EELEKTRIK = 'eelektrik'
    EELEKTROSS = 'eelektross'
    ELGYEM = 'elgyem'
    BEHEEYEM = 'beheeyem'
    LITWICK = 'litwick'
    LAMPENT = 'lampent'
    CHANDELURE = 'chandelure'
    AXEW = 'axew'
    FRAXURE = 'fraxure'
    HAXORUS = 'haxorus'
    CUBCHOO = 'cubchoo'
    BEARTIC = 'beartic'
    CRYOGONAL = 'cryogonal'
    SHELMET = 'shelmet'
    ACCELGOR = 'accelgor'
    STUNFISK = 'stunfisk'
    MIENFOO = 'mienfoo'
    MIENSHAO = 'mienshao'
    DRUDDIGON = 'druddigon'
    GOLETT = 'golett'
    GOLURK = 'golurk'
    PAWNIARD = 'pawniard'
    BISHARP = 'bisharp'
    BOUFFALANT = 'bouffalant'
    RUFFLET = 'rufflet'
    BRAVIARY = 'braviary'
    VULLABY = 'vullaby'
    MANDIBUZZ = 'mandibuzz'
    HEATMOR = 'heatmor'
    DURANT = 'durant'
    DEINO = 'deino'
    ZWEILOUS = 'zweilous'
    HYDREIGON = 'hydreigon'
    LARVESTA = 'larvesta'
    VOLCARONA = 'volcarona'
    COBALION = 'cobalion'
    TERRAKION = 'terrakion'
    VIRIZION = 'virizion'
    TORNADUS = 'tornadus'
    THUNDURUS = 'thundurus'
    RESHIRAM = 'reshiram'
    ZEKROM = 'zekrom'
    LANDORUS = 'landorus'
    KYUREM = 'kyurem'
    KELDEO = 'keldeo'
    MELOETTA = 'meloetta'
    GENESECT = 'genesect'
    CHESPIN = 'chespin'
    QUILLADIN = 'quilladin'
    CHESNAUGHT = 'chesnaught'
    FENNEKIN = 'fennekin'
    BRAIXEN = 'braixen'
    DELPHOX = 'delphox'
    FROAKIE = 'froakie'
    FROGADIER = 'frogadier'
    GRENINJA = 'greninja'
    BUNNELBY = 'bunnelby'
    DIGGERSBY = 'diggersby'
    FLETCHLING = 'fletchling'
    FLETCHINDER = 'fletchinder'
    TALONFLAME = 'talonflame'
    SCATTERBUG = 'scatterbug'
    SPEWPA = 'spewpa'
    VIVILLON = 'vivillon'
    LITLEO = 'litleo'
    PYROAR = 'pyroar'
    FLABEBE = 'flabebe'
    FLOETTE = 'floette'
    FLORGES = 'florges'
    SKIDDO = 'skiddo'
    GOGOAT = 'gogoat'
    PANCHAM = 'pancham'
    PANGORO = 'pangoro'
    FURFROU = 'furfrou'
    ESPURR = 'espurr'
    MEOWSTIC = 'meowstic'
    HONEDGE = 'honedge'
    DOUBLADE = 'doublade'
    AEGISLASH = 'aegislash'
    SPRITZEE = 'spritzee'
    AROMATISSE = 'aromatisse'
    SWIRLIX = 'swirlix'
    SLURPUFF = 'slurpuff'
    INKAY = 'inkay'
    MALAMAR = 'malamar'
    BINACLE = 'binacle'
    BARBARACLE = 'barbaracle'
    SKRELP = 'skrelp'
    DRAGALGE = 'dragalge'
    CLAUNCHER = 'clauncher'
    CLAWITZER = 'clawitzer'
    HELIOPTILE = 'helioptile'
    HELIOLISK = 'heliolisk'
    TYRUNT = 'tyrunt'
    TYRANTRUM = 'tyrantrum'
    AMAURA = 'amaura'
    AURORUS = 'aurorus'
    SYLVEON = 'sylveon'
    HAWLUCHA = 'hawlucha'
    DEDENNE = 'dedenne'
    CARBINK = 'carbink'
    GOOMY = 'goomy'
    SLIGGOO = 'sliggoo'
    GOODRA = 'goodra'
    KLEFKI = 'klefki'
    PHANTUMP = 'phantump'
    TREVENANT = 'trevenant'
    PUMPKABOO = 'pumpkaboo'
    GOURGEIST = 'gourgeist'
    BERGMITE = 'bergmite'
    AVALUGG = 'avalugg'
    NOIBAT = 'noibat'
    NOIVERN = 'noivern'
    XERNEAS = 'xerneas'
    YVELTAL = 'yveltal'
    ZYGARDE = 'zygarde'
    DIANCIE = 'diancie'
    HOOPA = 'hoopa'
    VOLCANION = 'volcanion'
    ROWLET = 'rowlet'
    DARTRIX = 'dartrix'
    DECIDUEYE = 'decidueye'
    LITTEN = 'litten'
    TORRACAT = 'torracat'
    INCINEROAR = 'incineroar'
    POPPLIO = 'popplio'
    BRIONNE = 'brionne'
    PRIMARINA = 'primarina'
    PIKIPEK = 'pikipek'
    TRUMBEAK = 'trumbeak'
    TOUCANNON = 'toucannon'
    YUNGOOS = 'yungoos'
    GUMSHOOS = 'gumshoos'
    GRUBBIN = 'grubbin'
    CHARJABUG = 'charjabug'
    VIKAVOLT = 'vikavolt'
    CRABRAWLER = 'crabrawler'
    CRABOMINABLE = 'crabominable'
    ORICORIO = 'oricorio'
    CUTIEFLY = 'cutiefly'
    RIBOMBEE = 'ribombee'
    ROCKRUFF = 'rockruff'
    LYCANROC = 'lycanroc'
    WISHIWASHI = 'wishiwashi'
    MAREANIE = 'mareanie'
    TOXAPEX = 'toxapex'
    MUDBRAY = 'mudbray'
    MUDSDALE = 'mudsdale'
    DEWPIDER = 'dewpider'
    ARAQUANID = 'araquanid'
    FOMANTIS = 'fomantis'
    LURANTIS = 'lurantis'
    MORELULL = 'morelull'
    SHIINOTIC = 'shiinotic'
    SALANDIT = 'salandit'
    SALAZZLE = 'salazzle'
    STUFFUL = 'stufful'
    BEWEAR = 'bewear'
    BOUNSWEET = 'bounsweet'
    STEENEE = 'steenee'
    TSAREENA = 'tsareena'
    COMFEY = 'comfey'
    ORANGURU = 'oranguru'
    PASSIMIAN = 'passimian'
    WIMPOD = 'wimpod'
    GOLISOPOD = 'golisopod'
    SANDYGAST = 'sandygast'
    PALOSSAND = 'palossand'
    PYUKUMUKU = 'pyukumuku'
    TYPENULL = 'typenull'
    SILVALLY = 'silvally'
    MINIOR = 'minior'
    KOMALA = 'komala'
    TURTONATOR = 'turtonator'
    TOGEDEMARU = 'togedemaru'
    MIMIKYU = 'mimikyu'
    BRUXISH = 'bruxish'
    DRAMPA = 'drampa'
    DHELMISE = 'dhelmise'
    JANGMO_O = 'jangmo-o'
    HAKAMO_O = 'hakamo-o'
    KOMMO_O = 'kommo-o'
    TAPUKOKO = 'tapukoko'
    TAPULELE = 'tapulele'
    TAPUBULU = 'tapubulu'
    TAPUFINI = 'tapufini'
    COSMOG = 'cosmog'
    COSMOEM = 'cosmoem'
    SOLGALEO = 'solgaleo'
    LUNALA = 'lunala'
    NIHILEGO = 'nihilego'
    BUZZWOLE = 'buzzwole'
    PHEROMOSA = 'pheromosa'
    XURKITREE = 'xurkitree'
    CELESTEELA = 'celesteela'
    KARTANA = 'kartana'
    GUZZLORD = 'guzzlord'
    NECROZMA = 'necrozma'
    MAGEARNA = 'magearna'
    MARSHADOW = 'marshadow'
    POIPOLE = 'poipole'
    NAGANADEL = 'naganadel'
    STAKATAKA = 'stakataka'
    BLACEPHALON = 'blacephalon'
    ZERAORA = 'zeraora'
    MELTAN = 'meltan'
    MELMETAL = 'melmetal'
    GROOKEY = 'grookey'
    THWACKEY = 'thwackey'
    RILLABOOM = 'rillaboom'
    SCORBUNNY = 'scorbunny'
    RABOOT = 'raboot'
    CINDERACE = 'cinderace'
    SOBBLE = 'sobble'
    DRIZZILE = 'drizzile'
    INTELEON = 'inteleon'
    SKWOVET = 'skwovet'
    GREEDENT = 'greedent'
    ROOKIDEE = 'rookidee'
    CORVISQUIRE = 'corvisquire'
    CORVIKNIGHT = 'corviknight'
    BLIPBUG = 'blipbug'
    DOTTLER = 'dottler'
    ORBEETLE = 'orbeetle'
    NICKIT = 'nickit'
    THIEVUL = 'thievul'
    GOSSIFLEUR = 'gossifleur'
    ELDEGOSS = 'eldegoss'
    WOOLOO = 'wooloo'
    DUBWOOL = 'dubwool'
    CHEWTLE = 'chewtle'
    DREDNAW = 'drednaw'
    YAMPER = 'yamper'
    BOLTUND = 'boltund'
    ROLYCOLY = 'rolycoly'
    CARKOL = 'carkol'
    COALOSSAL = 'coalossal'
    APPLIN = 'applin'
    FLAPPLE = 'flapple'
    APPLETUN = 'appletun'
    SILICOBRA = 'silicobra'
    SANDACONDA = 'sandaconda'
    CRAMORANT = 'cramorant'
    ARROKUDA = 'arrokuda'
    BARRASKEWDA = 'barraskewda'
    TOXEL = 'toxel'
    TOXTRICITY = 'toxtricity'
    SIZZLIPEDE = 'sizzlipede'
    CENTISKORCH = 'centiskorch'
    CLOBBOPUS = 'clobbopus'
    GRAPPLOCT = 'grapploct'
    SINISTEA = 'sinistea'
    POLTEAGEIST = 'polteageist'
    HATENNA = 'hatenna'
    HATTREM = 'hattrem'
    HATTERENE = 'hatterene'
    IMPIDIMP = 'impidimp'
    MORGREM = 'morgrem'
    GRIMMSNARL = 'grimmsnarl'
    OBSTAGOON = 'obstagoon'
    PERRSERKER = 'perrserker'
    CURSOLA = 'cursola'
    SIRFETCHD = 'sirfetchd'
    MRRIME = 'mrrime'
    RUNERIGUS = 'runerigus'
    MILCERY = 'milcery'
    ALCREMIE = 'alcremie'
    FALINKS = 'falinks'
    PINCURCHIN = 'pincurchin'
    SNOM = 'snom'
    FROSMOTH = 'frosmoth'
    STONJOURNER = 'stonjourner'
    EISCUE = 'eiscue'
    INDEEDEE = 'indeedee'
    MORPEKO = 'morpeko'
    CUFANT = 'cufant'
    COPPERAJAH = 'copperajah'
    DRACOZOLT = 'dracozolt'
    ARCTOZOLT = 'arctozolt'
    DRACOVISH = 'dracovish'
    ARCTOVISH = 'arctovish'
    DURALUDON = 'duraludon'
    DREEPY = 'dreepy'
    DRAKLOAK = 'drakloak'
    DRAGAPULT = 'dragapult'
    ZACIAN = 'zacian'
    ZAMAZENTA = 'zamazenta'
    ETERNATUS = 'eternatus'
    KUBFU = 'kubfu'
    URSHIFU = 'urshifu'
    ZARUDE = 'zarude'
    REGIELEKI = 'regieleki'
    REGIDRAGO = 'regidrago'
    GLASTRIER = 'glastrier'
    SPECTRIER = 'spectrier'
    CALYREX = 'calyrex'


class Pokeapi(str, Enum):
    POKEAPI = 'pokeapi'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePokeapi:
    pokemon_name: PokemonName = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pokemon_name') }})
    r"""Pokemon requested from the API."""
    SOURCE_TYPE: Final[Pokeapi] = dataclasses.field(default=Pokeapi.POKEAPI, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

