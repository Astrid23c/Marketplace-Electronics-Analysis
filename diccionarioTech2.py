    

# Estructura: Categoría > Marca > Producto > { Modelo: [Tokens] }


jerarquia_total = {
    'Dispositivos móviles': {
        'Apple': {
            'Smartphone':{
                'iPhone 17 Pro Max': ['17 pro max'],
                'iPhone 16 Pro Max': ['16 pro max'],
                'iPhone 15 Pro Max': ['15 pro max', '15pm'],
                'iPhone 14 Pro Max': ['14 pro max', '14pm'],
                'iPhone 17 Pro': ['17 pro'],
                'iPhone 17': ['iphon 17'],
                'iphone Air': ['iphone air'],
                'iPhone 16 Pro': ['16 pro'],
                'iPhone 16 Plus': ['iphone 16 plus'],
                'iPhone 16': ['iphon 16', 'iphon 16e'],
                'iPhone 15 Pro': ['15 pro'],
                'iPhone 15 Plus': ['iphone 15 plus'],
                'iPhone 15': ['iphon 15'],
                'iPhone 14 Pro': ['14 pro'],
                'iPhone 14 Plus': ['iphone 14 plus'],
                'iPhone 14': ['iphon 14'],
                'iPhone 13 Pro Max': ['13 pro max'],
                'iPhone 13 Pro': ['13 pro'],
                'iPhone 13 mini': ['iphone 13 mini'],
                'iPhone 13': ['iphone 13', '13 normal'],
                'iPhone 11': ['iphone 11'],
                'iPhone SE': ['iphone se'],
                'iPhone': ['iphone', 'iphon']
            },
            'Tablet': {
               'iPad Pro': ['ipad pro'],
               'iPad Air': ['ipad air'],
               'iPad Mini': ['ipad mini'],
               'iPad': ['ipad']
           },
            'Smartwatch': {
                'Watch': ['smartwatch apple', 'smartwatch ultra', 'watch']
            }     
        },
        'Samsung': {
            'Smartphone': {
                'Galaxy S24 Ultra': ['s24 ultra', 's24u'],
                'Galaxy S25 Ultra': ['s25 ultra', 's25u'],
                'Galaxy S23 Ultra': [ 's23 ultra', 's23u'],
                'Galaxy S25': ['s25'],
                'Galaxy S24':['s24'],
                'Galaxy S23': ['s23'],
                'Galaxy S22': ['s22'],
                'Galaxy S': ['samsung s', 'galaxy s'],
                'Galaxy Z': ['z fold7', 'z fold6', 'z fold5', 'z flip7', 'z flip6', 'galaxy z'],
                'Galaxy M': ['m 55 5g'],
                'Galaxy A': ['a54', 'galaxy a54', 'a55', 'a35', 'a25', 'a15', 'a06', 'a05', 'galaxy', 'samsung a'],
            },
            'Tablet': {
               'Galaxy Tab S11': ['galaxy tab s11'],
               'Galaxy Tab S10': ['galaxy tab s10'],
               'Galaxy Tab A11': ['galaxy tab a11'],
               'Galaxy Tab A9': ['galaxy tab a9'],
               'Galaxy Tab': ['galaxy tab']
           },
            'Smartwatch': {
                'Galaxy Watch': ['galaxy watch', 'smartwatch samsung']
            }
        },
        'Xiaomi': {
            'Smartphone': {
                'Redmi Note 13 Pro': ['note 13 pro', 'redmi 13'],
                'Redmi Note 14 Pro': ['note 14 pro', 'redmi 14'],
                'Poco X6': ['poco x6 pro', 'x6 pro'],
                'Poco F6': ['poco f6 pro', 'f6 pro'],
                'Xiaomi 15 Pro': ['xiaomi 15 pro'],
                'Xiaomi 15 Ultra': ['xiaomi 15 ultra'],
                'Xiaomi 15': ['xiaomi 15'],
                'Xiaomi 14T Pro': ['xiaomi 14t pro'],
                'Xiaomi 14T': ['Xiaomi 14t'],
                'Xiaomi 14 Ultra': ['xiaomi 14 ultra'],
                'Xiaomi 14': ['xiaomi 14'],
                'Xiaomi 13T Pro': ['xiaomi 13t pro', '13t pro'],
                'Xiaomi 13T': ['xiaomi 13t'],
                'Redmi 14C': ['redmi 14c'],
                'Redmi 13C': ['redmi 13c'],
                'Redmi 13': ['redmi 13'],
                'Redmi A3': ['redmi a3'],
                'Xiaomi': ['xiaomi'],
                'redmi': ['redmi'],
                'poco': ['poco']
            },
            'Tablet': {
               'Xiaomi Pad Mini': ['xiaomi pad mini'],
               'Xiaomi Pad': ['xiaomi pad'],
               'Redmi Pad': ['redmi pad']
           },
            'Smartbands': {
                'Smart Band': ['smartband xiaomi', 'smart band xiaomi', 'smart band', 'smartband']
            }
        },
        'Honor': {
            'Smartphone':{
                'Honor Magic 8 Pro': ['magic 8 pro'],
                'Honor Magic V6': ['magic v6'],
                'Honor Magic 8 Lite': ['magic 8 lite'],
                'Honor Magic 7 Pro': ['magic 7 pro'],
                'Honor 400 Pro': ['400 Pro'],
                'Honor 400': ['honor 400'],
                'Honor 90 Lite': ['90 lite'],
                'Honor X9c': ['honor x9c', 'x9c'],
                'Honor X7d': ['honor x7d', 'x7d'],
                'Honor X6C': ['honor x6C', 'x6c'],
                'Honor X5': ['honor x5', 'x5'],
                'Honor': ['honor']
            },
            'Tablet': {
               'MagicPad': ['honor magicpad', 'magicpad'],
               'Honor Pad': ['honor pad']
           }
        },
        'Motorola': {
            'Smartphone':{
                'Motorola Signature': ['motorola signature', 'signature'],
                'Motorola Razr': ['motorola razr', 'razr'],
                'Motorola Edge': ['motorola edge', 'edge'],
                'Motorola Moto G': ['g77', 'g67', 'motorola moto g', 'g17 power', 'g17', 'g84', 'g54', 'g53', 'g power'],
                'Motorola Moto E': ['motorola moto E', 'e15', 'e14', 'e6 play'],
                'Motorola': ['motorola']
            }
        },
        'Oppo': {
            'Smartphone':{
                'Oppo Find': ['oppo find', 'x9 pro', 'x9 ultra 5g', 'x9 ultra', 'x9', 'x5 pro'],
                'Oppo Reno': ['oppo reno', '14f 5g', '14 54g', '13f 5g', '12f 5g', '12 5g', '11f 5g'],
                'Oppo A6': ['oppo a6'],
                'Oppo A5': ['oppo a5'],
                'Oppo A': ['Oppo A', 'a80', 'a79', 'a78', 'a60', 'a58', 'a38'],
                'Oppo': ['oppo']
            }
        },
        'ZTE': {
            'Smartphone':{
                'ZTE Blade': ['zte blade', 'blade'],
                'Nubia Flip': ['nubia flip', 'flip'],
                'Nubia Focus': ['nubia focus'],
                'RedMagic': ['redmagic', 'red magic'],
                'Nubia Neo': ['nubia neo'],
                'ZTE Axon': ['zte axon'],
                'zte': ['zte', 'nubia']
            }
        },
        'Huawei': {
            'Smartphone':{
                'Huawei Pura': ['huawei pura'],
                'Huawei Mate': ['huawei mate'],
                'Huawei Nova': ['huawei nova'],
                'Huawei': ['huawei']
            },
            'Tablet': {
               'MatePad': ['huawei matepad', 'matepad']
           },
            'Smartwatch': {
                'Watch GT': ['watch gt', 'huawei watch gt', 'smartwatch huawei']
            }
        },
        'Vivo': {
            'Smartphone': {
                'Vivo V': ['vivo v'],
                'Vivo Y': ['vivo y'],
                'Vivo X': ['vivo x']
            }
        },
        'Advance': {
           'Tablet': {
               'NovaPad': ['novapad'],
               'SmartPad': ['smartpad'],
               'Intro': ['tablet intro'],
               'Prime': ['tablet prime'],
               'Advance': ['tablet advance']
           }
       },
       'TCL': {
           'Tablet': {
               'TCL NXTPAPER': ['tlc nxtpaper'],
               'TCL TAB': ['tlc tab']
           }
       },
       'Amazon': {
           'Tablet': {
               'Amazon Fire': ['tablet amazon']
           }
       },
       'Hyundai': {
           'Tablet': {
               'HyTab': ['tablet hytab', 'hytab', 'tablet hyundai']
           }
       },
       'Hp': {
           'Tablet': {
               'HP': ['tablet hp']
           }
       },
       'Acer': {
           'Tablet': {
               'Acer Enduro Urban': ['acer enduro urban', 'tablet acer']
           }
       },
       'Asus': {
           'Tablet': {
               'ROG Flow': ['tablet asus', 'tablet rog flow', 'rog flow'],
               'VivoBook': ['tablet vivobook', 'vicobook']
           }
       },
       'Blackview': {
           'Tablet': {
               'Blackview Active': ['tablet blackview active', 'blackview active'],
               'Blackview Tab': ['blackview tab'],
               'Oscal Pad': ['oscal pad']
           }
       },
       'Alldocube': {
           'Tablet': {
               'iPlay': ['tablet iPlay', 'alldocube iplay', 'tablet alldocube']
           }
       },       
       'Otro/Genérico': {
            'Smartphone': {
                'Otro': ['smartphone', 'cell', 'celular']    
            },
            'Tablet': {
               'Otro': ['tablet', 'table']
           } 
        }
    },
    'Tabletas digitalizadoras': {
        'Wacom': {
           'Tableta': {
               'One by Wacom': ['one by wacom'],
               'Intuos': ['wacom intuos'],
               'Wacom One': ['wacom one']
           }
       },
       'Huion': {
           'Tableta': {
               'Inspiroy': ['tablet inspiroy', 'ispiroy']
           }
       },
       'XP-Pen': {
           'Tableta': {
               'XP-Pen Magic': ['tableta xp-pen magic', 'xp-pen magic'],
               'Deco': ['tableta deco']
           },      
       },
       'Otro/Genérico': {
               'Tableta': {
                  'Otro': ['Tableta'] 
               }
           }
    },  
    'Laptops/PC': {
        'Dell': {
            'Laptop': {
                'Dell XPS': ['dell xps'],
                'Dell Inspiron': ['inspiron'],
                'Dell Latitude': ['latitude'],
                'Alienware': ['alienware'],
                'Dell Vostro': ['vostro'],
                'Dell Precision': ['dell Precision', 'precision'],
                'Rugged': ['rugged'],
                'Dell': ['laptop dell']
            },
            'PC escritorio': {
                'OptiPlex': ['optiplex'],
                'Inspiron Desktop': ['inspiron desktop'],
                'XPS Desktop': ['xps desktop'],
                'Precision Workstations': ['precision workstations'],
                'Dell': ['computadora dell', 'pc dell']
                }
            },
        'Apple': {
            'Laptop': {
                'MacBook Pro': ['macbook pro', 'mbp'],
                'MacBook Air': ['macbook air', 'mba'],
                'MacBook': ['mac book', 'macbook']
            },
            'PC escritorio': {
                'iMac': ['m4', 'imac'],
                'Mac mini': ['m4 pro'],
                'Mac Studio': ['m4 max', 'm3 ultra'],
                'Mac Pro': ['m2 ultra'],
                'Mac': ['mac']
            }
            },
        'HP': {
            'Laptop': {
                'HP Spectre x360': ['hp spectre x360'],
                'HP Envy': ['hp envy'],
                'HP OmniBook': ['hp omnibook ultra/x', 'hp omnibook'],
                'Omen': ['omen'],
                'Victus': ['victus'],
                'Elitebook': ['elitebook'], 
                'Probook':  ['probook'],
                'zbook': ['zbook'],
                'Hogar': ['pavilion', 'hp chromebook', 'hp essential'],
                'HP': ['laptop hp']
            },
            'PC escritorio': {
                'HP Slim': ['hp Slim'], 
                'HP Pavilion': ['pavilion'],
                'HP desktop': ['hp desktop'],
                'HP ProOne': ['hp proone'],
                'hp all-in-one': ['hp all-in-one'],
                'HP': ['computadora hp', 'pc hp']
            }
            },
        'Lenovo': {
             'Laptop': {
                'Yoga': ['yoga', 'yoga 7', 'yoga 7i', 'yoga book'],
                'Legion': ['legion', 'legion 5', 'legion 5i', 'legion 7i', 'legion pro 5'],
                'ThinkPad': ['thinkpad', ' t495', 't14', 'x1 carbon'],
                'IdeaPad': ['ideapad', 'slim 3', 'slim 5', '15IAU7'],
                'LOQ': ['loq 15.6', 'loq'],
                'ThinkBook': ['thinkbook'],
                'Chromebook': ['chromebook', 'lenovo 100e'],
                'Lenovo V Series': ['lenovo v series', 'lenovo v', 'v15', 'g4'],
                'Lenovo': ['laptop lenovo']
            },
            'PC escritorio': {
                'ThinkCentre': ['thinkcentre'],
                'IdeaCentre::': ['ideacentre'],
                'Legion Tower': ['legion tower'],
                'LOQ Desktop': ['loq desktop'],
                'Lenovo': ['computadora lenovo', 'pc lenovo']
            }
            },
        'Asus': {
            'Laptop': {
                'Zenbook': ['zenbook' ,'zenbook duo', 'UX8406', 's 13/14 oled'],
                'Vivobook': ['vivobook', 'x1605', 'f1504)'],
                'Chromebook': ['Chromebook'],
                'Asus': ['laptop asus']
            },
            'PC escritorio': {
                'ASUS Vivo AiO:': ['asus vivo', 'aio a3402'],
                'ROG Desktop': ['rog desktop'],
                'Asus': ['computadora asus', 'pc asus']
            }
            },
        'Acer': {
            'Laptop': {
                'Predator': ['Predator', 'Helios', 'Neo 16', 'Helios 16'],
                'Nitro': ['nitro 5', 'nitro v 15', 'Nitro v 16', 'nitro'],
                'Swift': ['Swift', 'Swift Edge', 'Swift Go'],
                'Spin Series': ['spin series'],
                'Aspire': ['aspire'],
                'Chromebooks': ['chromebooks'],
                'Enduro': ['enduro'],
                'Acer': ['laptop acer']
            },
            'PC escritorio': {
                'Predator Orion': ['predator orion'],
                'Nitro Desktop': ['nitro desktop'],
                'Aspire AIO': ['aspire aio'],
                'Veriton': ['veriton'],
                'Chromebox': ['mini pc chromebox'],
                'Acer': ['computadora acer', 'pc acer', 'compu acer']
            }
            },
        'MSI': {
            'Laptop': {
                'Katana': ['msi katana'],
                'Cyborg': ['msi cyborg'],
                'Raider': ['msi raider', 'msi titan'],
                'Vector': ['msi vector'],
                'Creator Pro': ['creatorpro','creator studio', 'creator pro'],
                'Modern': ['msi modern', 'summit'],
                'MSI': ['laptop msi']
            },
            'PC escritorio': {
                'Aegis': ['msi aegis'],
                'Codex': ['msi codex'],
                'MSI Pro': ['msi pro'],
                'MSI': ['computadora msi', 'compu msi', 'pc msi']
            }
        },
        'Honor': {
          'Laptop': {
              'Honor': ['laptop honor']
          }  
        },
        'Otro/Genérico': {
            'Computadora': {
                'Otro': ['pc', 'computadora', 'compu', 'pc gaming', 'pc gamer', 'computadora gamer', 'compu gamer'] 
            },
            'Laptop': {
                'Otro': ['laptop']
            }     
        }
    },
    'Consolas/Realidad Virtual': {
        'Sony': {
            'Consola': {
                'PlayStation': ['playstation', 'play'],
                'PSX': ['psx'],
                'PS4': ['ps4'],
                'PS5': ['ps5'],
                'PS3': ['ps3'],
                'PS2': ['ps2'],
                'PS': ['ps']
            },
            'Realidad Virtual': {
                'VR2': ['vr2'],
            } 
        },
        'Microsoft': {
            'Consola': {
                'Xbox': ['xbox']
            }
        },
        'Nintendo': {
            'Consola': {
                'NES': ['nes'],
                'Super Nintendo': ['snes', 'super nintendo'],
                'Game Cube': ['game cube'],
                'Wii': ['wii'],
                'Nintendo Switch': ['switch'],
                'Game boy': ['game boy'],
                'Nintendo': ['nintendo ds', 'nintendo 3ds', 'nintendo']
            }
        },
        'Valve': {
            'Consola': {
                'Steam': ['deck', 'machine', 'controller']
            },
            'Realidad Virtual': {
                'Valve Index': ['valve index']
            }
        },
        'Asus': {
            'Consola': {
                'Rog Xbox Ally': ['rog xbox ally'],
                'Rog Ally': ['rog ally']
            }
        },
        'Ayaneo': {
            'Consola': {
                'AYANEO': ['ayaneo 3', 'ayaneo 2'],
                'AYANEO FLIP': ['ayaneo flip'],
                'AYANEO Next': ['ayaneo next'],
                'AYANEO Air': ['ayaneo air'],
                'Ayaneo Pocket': ['ayaneo pocket']
            }                
        },
        'GPD': {
            'Consola': {
                'GPD WIN': ['gpd win', 'gpd'],
                'GPD XD': ['gpd xd'],
                'GPD Pocket': ['gpd pocket'],
                'GPD G1': ['gpd g1']
            }
        },
        'Abernic': {
            'Consola': {
                'RG35XX': ['rg35xx'],
                'RG40': ['rg40'],
                'RG35': ['rg35'],
                'RG': ['rg cube', 'rg505', 'rg nano', 'rg556', 'rg'],
                'WIN 600': ['win600'],
            }
        },
        'MSI': {
            'Consola': {
                'MSI Claw': ['msi claw']
            }
        },
        'Sega': {
            'Consola': {
                'Sega': ['sega', 'mega drive', 'game gear', 'saturn', 'nomad', 'dreamcast', 'sg-1000',
                        'advance pico', 'master system', 'mega drive', 'teradrive']
            }
        },
        'Atari': {
            'Consola': {
                'Atari': ['atari']
            }
        },
        'Evercade': {
            'Consola': {
                'Evercade': ['evercade']
            }
        },
        'Meta': {
            'Realidad Virtual': {
            'Meta': ['oculus', 'meta']
            }
        },
        'Pico':{
            'Realidad Virtual': {
                'Pico': ['pico'],
            }
        },
        'HTC Vive': {  
            'Realidad Virtual': {  
                'HTC Vive': ['htc vive']
            }
        },
        'Apple': {
            'Realidad Virtual': {
                'Apple': ['vision pro'],
            }
        },
        'Otro/Genérico': {
            'Consola': {
                'Otro': ['consola', 'video juegos']
            },
            'Mando': {
                'Otro': ['mando']
            },
            'Simulador': {
                'Otro': ['simulador']
            }  
        }
    },
    'Parlantes inteligentes': {
       'Amazon':{
           'Parlante inteligente': {
               'Echo': ['alexa', 'echo dot', 'echo show', 'echo hub']
           }
       },
       'Google':{
          'Parlante inteligente': {
               'Google Nest': ['google nest', 'nest mini', 'nest hub']
           }
       }, 
       'Apple':{
           'Parlante inteligente': {
               'HomePod': ['homekit', 'siri', 'homepod']
            }
        },
       'Otro/Genérico': {
           'Parlante inteligente': {
               'Otro': ['parlante inteligente']
           }  
       }
    },
    'Equipos de sonido': {
        'Sony': {
            'Altavoz portatil': {
                'Sony ULT FIELD': ['utl field', 'field 7', 'field 5', 'field'],
                'Sony SRS': ['srs-xb100', 'srs xb100']
            },
            'Sistema de sonido': {
                'Sony ULT Tower': ['ult tower', 'sony'],
                'Genezi': ['genezi']
            },
            'Barras de sonido': {
                'Sony Bravia': ['bravia', 'theater quad'],
                'Sony HT': ['sony ht']
            }
        },
        'LG': {
            'Altavoz portatil': {
                'LG XBOOM': ['xboom grab', 'xboom go', 'xboom bounce'],
            },
            'Sistema de sonido': {
                'LG XBOOM': ['xboom ck99', 'xboom cl98', 'xboom rnc9']
            },
            'Barras de sonido': {
                'LG S': ['s95tr', 's90tr', 's77ty', 'lg s'],
                'LG Sound': ['sound suite']
            }
        },
        'Samsung':{
            'Altavoz portatil': {
                'Samsung Music': ['music studio'],
                'Samsung HW': ['samsung hw', 'hw-qs90h'],
                'Samsung ST': ['samsung st']
            },
            'Sistema de sonido': {
                'Sound Tower': ['samsung st50f', 'samsung st40f']
            },
            'Barras de sonido': {
                'Samsung HW': ['Samsung HW']
            }
        },
        'Panasonic': {
            'Altavoz portatil': {
                'Panasonic SC': ['panasonic sc', 'pm270PP-k', 'ux100', 'sc-ux102']
            },
            'Sistema de sonido': {
                'Panasonic SC': ['max3600pu', 'akx110', 'tmax20', 'panasonic']
            },
            'Barras de sonido': {
                'Panasonic SC': ['htb700', 'htb600', 'htb490'],
                'Panasonic Soundslayer': ['soundslayer', 'htb01pp'] 
            }
        },
        'JBL': {
            'Altavoz portatil': {
                'JBL Go': ['jbl go'],
                'JBL Flip': ['jbl flip'],
                'JBL Charge': ['jbl charge'],
                'JBL Extreme': ['jbl extreme'],
                'JBL Boommbox': ['jbl boombox']
            },
            'Sistema de sonido': {
                'JBL PartyBox': ['Partybox']
            },
            'Barras de sonido': {
                'JBL Bar': ['jbl bar']
            }
        },
        'Miray': {
            'Altavoz portatil': {
                'Miray PMBT': ['Miray pmbt']
            },
            'Sistema de sonido': {
                'Miray SAM': ['miray sam', 'miray'],
            },
            'Barras de sonido': {
                'Miray PAM': ['miray pam'] 
            }
        },
        'Philips': {
            'Altavoz portatil': {
                'Philips GoGear': ['philips gogear'],
                'Philips Shoqbox': ['philips shoqbox'],
                'Philips Izzy': ['philips izzy']
            },
            'Sistema de sonido': {
                'Philips TAM': ['philips tam'],
                'Philips Nitro': ['philips nitro'],
                'Philips Party': ['philips party']
            },
            'Barras de sonido': {
                'Philips Fidelio': ['philips fidelio'],
                'Philips SC': ['philips sc', 'htb600', 'htb700'],
                'Philips Soundslayer': ['philips soundslayer']
            }
        },
        'Aiwa': {
            'Altavoz portatil': {
                'Aiwa Exos': ['aiwa exos'],
                'Aiwa AW': ['aiwa aw'],
                'Serie Retro': ['aw-770bt']
            },
            'Sistema de sonido': {
                'Aiwa AW': ['aiwa aw', 'pok100', 'pok600', 'fml2', 'ms500bt', 'a1200bt']
            },
            'Barras de sonido': {
                'Aiwa AW': ['asb21', 'asb55']
            }
        },
        'JVC': {
          'Altavoz portatil': {
                'JVC XS': ['jvc xs'],
                'JVC SP': ['jvc sp'],
                'JVC RV': ['jvc rv']
            },
            'Autoradio': {
                'JVC KW': ['jvc kw'],
                
            },
            'Barras de sonido': {
                'JVC TH': ['jvc th'],
                'JVC UX': ['jvc ux'],
                'JVC KD': ['jvc kd'],
                'JVC CS': ['jvc cs']
            }   
        },
        'TCL': {
            'Barras de sonido': {
                'TS8212': ['ts8212'],
                'TS8211': ['ts8211'],
                'S645W': ['s645w'],
                'TS3100': ['ts3100'],
                'S55H': ['s55h'],
                'S45H': ['s45h']
            }  
        },
        'Hisense': {
            'Altavoz portatil': {
                'Hisense': ['hisense']
            },
            'Barras de sonido': {
                'Hisense HS': ['hisense hs'],
                'Hisense AX': ['hisense ax']
            }
        },
        'Bose': {
           'Altavoz portatil': {
                'Bose SoundLink': ['bose soundlink']
            },
            'Altavoz inteligente': {
                'Bose Smart Speaker': ['bose smart speaker']
            },
            'Barras de sonido': {
                'Bose Smart': ['bose smart'],
                'Bose TV': ['bose tv']
            } 
        },
        'Sonos': {
            'Altavoz portatil': {
                'Sonos Era': ['sonos era'],
                'Sonos Five': ['sonos five'],
                'Sonos One': ['sonos one'],
                'Sonos Move': ['sonos move'],
                'Sonos Roam': ['sonos roam']
            },
            'Barras de sonido': {
                'Sonos Arc': ['sonos arc'],
                'Sonos Beam': ['sonos beam'],
                'Sonos Ray': ['sonos ray']
            }
        },
        'Technics': {
            'Altavoz inalámbrico': {
                'Technics Ottava': ['technics ottava'],
                'Hi-Fi': ['hi-fi', 'sb 7000']
            },
            'Tocadiscos': {
                'Technics SL': ['technics sl']
            },
            'Amplificadores': {
                'Technics SU': ['technics su']
            }
        },
        'Yamaha': {
           'Altavoz portatil': {
                'Yamaha WS': ['yamaha ws'],
                'Yamaha MusicCast': ['yamaha musiccast', 'musiccast']
            },
            'Sistema de sonido': {
                'Yamaha R': ['yamaha r'],
                'Serie AVENTAGE': ['aventage', 'rx a8a', 'rx a6a'],
                'Yamaha STAGEPAS': ['yamaha stagepas'],
                'Yamaha DBR': ['yamaha dbr ']
            },
            'Barras de sonido': {
                'Yamaha SR': ['yamaha sr'],
                'Yamaha YAS': ['yamaha yas']
            } 
        },
        'Pioneer': {
            'Equipos para DJ': {
                'Pioneer CDJ': ['pioneer cdj'],
                'Pioneer Opus': ['pioneer opus'],
                'Pioneer DDJ': ['pioneer ddj']
                
            },
            'Barras de sonido': {
                'Pioneer Elite': ['pioneer elite'],
                'Pioneer VSX': ['pioneer vsx']
            },
            'Altavoz': {
                'Pioneer VM': ['pioneer vm'],
                'Pioneer DM': ['pioneer dm']
            },
            'Autoradio': {
                'Pioneer DMH': ['pioneer dmh'],
                'Serie TS': ['serie ts'],
                'Subwoofers Champion': ['subwoofers champion']
            }
        },
        'Black Hawk': {
          'Parlante': {
              'Black Hawk': ['medios black', 'parlantes black']
          }  
        },
        'Otro/Genérico': {
            'Altavoz':{
                'Otro': ['altavoz']
            },
            'Equipo de sonido': {
                'Otro': ['equipo de sonido', 'minicomponente']
            },
            'Autoradio': {
                'Otro': ['autoradio', 'auto radio']
            },
            'Barra de sonido': {
                'Otro': ['barra de sonido']
            },
            'Radio': {
                'Otro': ['radio']
            },
            'Parlante': {
                'Otro': ['parlante', 'parlantes', 'bombox', 'medios']
            },
            'Amplificador': {
                'Otro': ['amplificador'] 
            },
            'Subwoofer': {
                'Otro': ['bajos de 12', 'subwoofer']
            }
        }
    },
    'Audífonos': {
        'Sony':{
            'Audífonos de Diadema (Over-Ear)': {
                'Sony WH': ['sony wh']
            },
            'Audífonos True Wireless': {
                'Sony WF': ['sony wf']
            },
            'Audífonos In-Ear (con cable)': {
                'Sony': ['audífonos sony']
            }
        },
        'JBL': {
            'Audífonos de Diadema (Over-Ear)': {
                'JBL Tour One': ['jbl tour one'],
                'JBL Live 770': ['jbl live 770'],
                'JBL Tune 770': ['jbl tune 770'],
                'JBL Tune 520': ['jbl tune 520']
            },
            'Audífonos True Wireless': {
                'JBL Live Beam': ['jbl live beam'],
                'JBL Live Buds': ['jbl live buds'],
                'JBL Live Flex': ['jbl live flex'],
                'JBL Live Pro': ['jbl live pro'],
                'JBL Vibe Buds': ['jbl vibe buds'],
                'JBL Tune Beam': ['jbl tune beam'],
                'JBL Endurance Peak': ['jbl endurance peak'],
                'JBL Endurance Run': ['jbl endurance run']
            },
            'Audífonos In-Ear (con cable)': {
                'JBL Tune 310': ['jbl tune 310']
            }
        },
        'Apple': {
            'Audífonos de Diadema (Over-Ear)':{
                'AirPods Max': ['airpods max'],
                'Beats Pro': ['beats pro'],
                'Beats Solo': ['beats solo'],
                
            },
            'Audífonos True Wireless': {
                'AirPods Pro': ['airpods pro'],
                'AirPods': ['airpods'],
                'Beats Studio': ['beats studio'],
                'Beats Fit Pro': ['beats fit Pro'],
                
            },
            'Audífonos In-Ear (con cable)': {
                'Beats Flex': ['beats flex']
            } 
        },
        'Xiaomi': {
            'Audífonos True Wireless': {
                'Xiaomi Redmi Buds': ['xiaomi redmi buds'],
                'Xiaomi Buds': ['xiaomi buds'],
                'Xiaomi Openwear': ['xiaomi openwear'],
                'Xiaomi Mi True': ['xiaomi mi true']
            },
            'Audífonos In-Ear (con cable)': {
                'Xiaomi Type-C': ['xiaomi type-c', 'xiaomi type c'],
                'Xiaomi Mi Basic': ['xiaomi mi basic']
            }
        },
        'Huawei': {
            'Audífonos True Wireless': {
                'Huawei FreeBuds': ['huawei freebuds'],
                'Huawei FreeClip': ['huawei freeclip'],
                
            },
            'Audífonos In-Ear (con cable)': {
                'Huawei Freelace': ['huawei freelace'],
                'Huawei AM': ['huawei am', 'huawei am115'],
                'Huawei CM33': ['huawei cm33', 'huawei cm']
            } 
        },
        'Samsung': {
            'Audífonos True Wireless': {
                'Samsung Galaxy Buds': ['samsung galaxy buds', 'galaxy buds']
            }
        },
        'Skullcandy': {
            'Audífonos de Diadema (Over-Ear)':{
                'Skullcandy Crusher': ['skullcandy crusher'],
                'Skullcandy Hesh': ['skullcandy hesh'],
                'Skullcandy Icon': ['skullcandy icon'],
                'Skullcandy Riff': ['skullcandy riff']
            },
            'Audífonos True Wireless': {
                'Skullcandy Rail': ['skullcandy rail'],
                'Skullcandy Indy': ['skullcandy indy'],
                'Skullcandy Push Active': ['skullcandy push active'],
                'Skullcandy Smokin': ['skullcandy smokin'],
                'Skullcandy Dime': ['skullcandy dime'],
                'Skullcandy Sesh': ['skullcandy sesh']
            },
            'Audífonos In-Ear (con cable)': {
                'Skullcandy Method': ['skullcandy method'],
                'Skullcandy Jib': ['skullcandy jib'],
                'Skullcandy Inkd': ['Skullcandy Inkd'],
                'Skullcandy XTplyo': ['skullcandy xtplyo'],
                'Skullcandy Push': ['skullcandy push'],
                'Skullcandy': ['skullcandy']
            } 
        },
        'Bose': {
            'Audífonos de Diadema (Over-Ear)':{
                'Bose QuietComfort Ultra Headphones': ['bose quietcomfort ultra headphones'],
                'Bose QuietComfort Headphones': ['bose quietcomfort headphones'],
                'Bose QuietComfort 45': ['bose quietcomfort 45']
            },
            'Audífonos True Wireless': {
                'Bose QuietComfort Ultra Earbuds': ['bose quietcomfort ultra earbuds'],
                'Bose Ultra Open Earbuds': ['bose ultra', 'bose Open earbuds'],
                'Bose QuietComfort Earbuds': ['bose quietcomfort earbuds'],
                'Bose Sport Earbuds': ['bose sport earbuds']
            }
        },
        'Anker': {
            'Audífonos de Diadema (Over-Ear)':{
                'Anker Soundcore Space': ['anker soundcore space'],
                'Anker Soundcore Life Q30': ['anker soundcore life q30'],
                'Anker Soundcore Life Q20': ['anker soundcore life q20', 'soundcore life q20i'],
                'Anker Soundcore H30i': ['anker soundcore h30i']
            },
            'Audífonos True Wireless': {
                'Anker Soundcore Space A40': ['anker soundcore space a40'],
                'Anker Soundcore C30i': ['anker soundcore c30i'],
                'Anker Soundcore Liberty': ['anker soundcore liberty'],
                'Anker Soundcore P40i ': ['anker soundcore p40i'],
                'Anker Soundcore Life A1': ['anker soundcore life a1'],
                'Anker Soundcore Life Dot 3i': ['anker soundcore life dot'],
                'Anker Soundcore A25i': ['anker soundcore a25i']
            }
        },
        'Lenovo':{
            'Audífonos de Diadema (Over-Ear)':{
                'Lenovo Audio': ['lenovo audio'],
                'Lenovo G60A': ['lenovo g60a'],
                'Lenovo Legion': ['lenovo legion'],
                'Lenovo Go': ['lenovo go'],
                'Lenovo Dual': ['lenovo dual']
            },
            'Audífonos True Wireless': {
                'Lenovo Thinkplus': ['lenovo thinkplus'],
                'Lenovo LP40': ['lenovo lp40'],
                'Lenovo HT38': ['lenovo ht38'],
                'Lenovo XT90': ['lenovo xt90'],
                'Lenovo XT93': ['lenovo xt93'],
                'Lenovo E310': ['lenovo e310'],
                'Lenovo Smart': ['lenovo smart']
            },
            'Audífonos In-Ear (con cable)': {
                'Lenovo QF310': ['lenovo qf310'],
                'Lenovo HF130': ['lenovo hf130'],
                'Lenovo C': ['lenovo c'],
                'Lenovo HE05': ['lenovo he05'],
                'Lenovo BT10': ['lenovo bt10:']
            } 
        },
        'FiiO': {
            'Audífonos de Diadema (Over-Ear)':{
                'FiiO FT': ['fiio ft'],
                'FiiO JT': ['fiio jt'],
                'Anytime': ['anytime'],
                'EH11': ['eh11']
            },
            'Audífonos True Wireless': {
                'FW5': ['fw5'],
                'FW3': ['fw3'],
                'JW1': ['jw1'],
                'UTWS': ['utws']
            },
            'Audífonos In-Ear (con cable)': {
                'FiiO FH': ['fiio fh'],
                'FiiO FD': ['fiio fd'],
                'FiiO FA': ['fiio fa'],
                'FiiO FX': ['fiio fx'],
                'FiiO JD': ['fiio jd'],
                'FiiO JH': ['fiio jh']
            },
            'Audífonos': {
                'FiiO': ['audífonos fiio']
            } 
        },
        'Audio-Technica': {
            'Audífonos de Diadema (Over-Ear)':{
                'ATH-M': ['ath-m'],
                'ATH-R': ['ath-r'],
                'ATH-AD': ['ath-ad'],
                'ATH-WP': ['ath-wp'],
                'ATH-GL': ['ath-gl']
                
            },
            'Audífonos True Wireless': {
                'ATH-TW': ['ath-tw'],
                'ATH-SQ': ['ath-sq'],
                'ATH-CK': ['ath-ck'],
                'ATH-SPORT': ['ath-sport']
            },
            'Audífonos In-Ear (con cable)': {
                'ATH-E': ['ath-e'],
                'ATH-CKR': ['ath-ckr'],
                'ATH-CKS': ['ath-cks']
            },
            'Audífonos': {
                'Audio-Technica': ['audio-technica', 'technica']
            } 
        },
        'Sennheiser': {
            'Audífonos True Wireless': {
                'Momentum True': ['momentum true'],
                'Accentum True': ['accentum true'],
                'CX Plus': ['cx plus'],
                'CX True': ['cx true'],
                'Sport True': ['sport true']
            },
            'Audífonos de Diadema (Over-Ear)':{
                'Momentum': ['momentum'],
                'Accentum': ['accentum'],
                'Sennheiser HD': ['sennheiser hd'],
                
            },
            'Audífonos In-Ear (con cable)': {
                'Sennheiser IE': ['sennheiser ie']
            } 
        },
        'Beyerddynamic': {
            'Audífonos de Diadema (Over-Ear)':{
                'Beyerddynamic DT': ['beyerddynamic dt'],
                'Aventho': ['aventho'],
                'Beyerddynamic MMX': ['beyerddynamic mmx']
            },
            'Audífonos True Wireless': {
                'Amiron': ['amiron'],
                'Free BYR': ['free byr']
            },
            'Audífonos In-Ear (con cable)': {
                'Xelento': ['xelento'],
                'Beyerddynamic IE': ['beyerddynamic ie'],
                'Blue BYRD': ['blue byrd'],
                'Soul BYRD': ['soul byrd']
            } 
        },
        'Shure': {
            'Audífonos True Wireless': {
                'AONIC Free': ['aonic free'],
                'AONIC 215 TW': ['Aaonic 215 tw'],
                'AONIC 50 TW': ['aonic 50 tw']
            },
            'Audífonos de Diadema (Over-Ear)':{
                'AONIC 50': ['aonic 50'],
                'AONIC 40': ['aonic 40'],
                'SHR': ['srh']
            },
            'Audífonos In-Ear (con cable)': {
                'AONIC': ['aonic'],
                'Shure SE': ['shure se'],
                'Shure KSE': ['shure kse']
            },
            'Audífonos': {
                'Shure': ['audífonos shure']
            } 
        },
        'Marshall': {
            'Audífonos de Diadema (Over-Ear)':{
                'Major': ['major'],
                'Monitor': ['monitor']
            },
            'Audífonos True Wireless': {
                'Motif': ['motif'],
                'Minor': ['minor']
            },
            'Audífonos In-Ear (con cable)': {
                'Minor II': ['minor ii'],
                'Mode': ['Mode']
            } 
        },
        'Logitech': {
            'Audífonos True Wireless': {
                'Logitech G Fits': ['logitech g fits'],
                'Logitech Zone True': ['logitech zone true'],
                'Logitech Zone Plus': ['logitech zone plus']
            },
            'Audífonos de Diadema (Over-Ear)':{
                'Logitech PRO': ['logitech pro'],
                'Logitech G': ['logitech g'],
                'Logitech Zone': ['logitech zone'],
                'Logitech H': ['logitech h']
            },
            'Audífonos In-Ear (con cable)': {
                'Logitech G333': ['logitech g333'],
                'Logitech Zone Wired': ['logitech zone wired']
            } 
        },
        'Razer': {
            'Audífonos de Diadema (Over-Ear)':{
                'BlackShark': ['blackshark'],
                'Kraken': ['kraken'],
                'Barracuda': ['barracuda']
            },
            'Audífonos True Wireless': {
               'Hammerhead True': ['hammerhead true'],
                'Hammerhead Pro': ['hammerhead pro'],
                'Hammerhead HyperSpeed': ['hammerhead hyperspeed']
            },
            'Audífonos In-Ear (con cable)': {
                'Hammerhead': ['hammerhead'],
                'Razer Moray': ['razer moray']
            } 
        },
        'HiperX': {
            'Audífonos de Diadema (Over-Ear)':{
                'Cloud III': ['cloud iii'],
                'Cloud Alpha': ['cloud alpha'],
                'Cloud Stinger': ['cloud stinger'],
                'Cloud Flight': ['cloud flight'],
                'Cloud Revolver': ['cloud revolver'],
                'Cloud Mini': ['cloud mini']
            },
            'Audífonos True Wireless': {
                'Cloud MIX': ['cloud mIX'],
                'Cirro Buds': ['cirro buds'],
                'Cloud Buds': ['cloud buds']
            },
            'Audífonos In-Ear (con cable)': {
                'Cloud Earbuds': ['cloud earbuds'],
                'Cloud MIX': ['cloud mix']
            } 
        },
        'Corsair': {
            'Audífonos True Wireless': {
                'Virtuoso True Wireless': ['virtuoso true wireless'],
                'Virtuoso Max Wireless': ['virtuoso max wireless']
            },
            'Audífonos In-Ear (con cable)': {
               'Virtuoso Pro': ['virtuoso pro'],
               'Corsair MG': ['corsair mg'] 
            },
            'Audífonos de Diadema (Over-Ear)':{
                'Virtuoso': ['Virtuoso'],
                'Corsair HS': ['corsair hs'],
                'Corsair Void': ['corsair void']
            }, 
        },
        'Miray': {
            'Audífonos': {
                'Miray': ['audífonos miray', 'miray am', 'audifonos miray']
            }
        },
        'QCY': {
            'Audífonos de Diadema (Over-Ear)':{
                'QCY H3': ['qcy h3']
            },
            'Audífonos True Wireless': {
                'MeloBuds': ['melobuds'],
                'AilyBuds': ['ailybuds'],
                'ArcBuds': ['arcbuds'],
                'T13 ANC': ['t13 anc', 't13']
            },
            'Audífonos In-Ear (con cable)': {
                'QCY': ['qcy'],
                'Crossky': ['crossky']
            } 
        },
        'Halion': {
            'Audífonos':{
                'Halion HA': ['halion ha', 'audífonos halion']
            }
        },
        'Awei': {
            'Audífonos':{
                'Awei': ['audífonos awei']
            }
        },
        'Hoco': {
            'Audífonos':{
                'Hoco': ['audífonos hoco']
            }
        },
        'Borofone': {
            'Audífonos':{
                'Berofone': ['audífonos berofone']
            }
        },
        'Otro/Genérico': {
            'Audífonos': {
               'Otro': ['audífonos', 'headphone', 'audifonos', 'auriculares', 'audífono', 'audifono', 'aurículares', 'auriculares inalámbricos'] 
            } 
        }
    },
    'Reproductores de Audio': {
        'Shanling': {
            'Reproductor de Audio': {
                'Shanling': ['shanling']
            }
        },
        'FiiO': {
            'Reproductor de Audio': {
                'FiiO': ['reproductor de audio fiio', 'fiio m23', 'fiio m11s', 'fiio m5']
            }
        },
        'HiBy': {
            'Reproductor de Audio': {
                'HiBy': ['reproductor de audio hiby', 'hiby']
            }
        },
        'Sony': {
             'Reproductor de Audio': {
                'Wallman': ['walkman']
            }
        },
        'Otro/Genérico': {
             'Reproductor de Audio': {
                'Otro': ['reproductor de audio', 'reproductor de musica']
            }
        }  
    },
    'Televisores': {
        'Samsung': {
            'Televisor': {
                'Samsung OLED': ['samsung oled', 'samsung qd oled', 'samsung woled'],
                'Samsung Neo QLED 8K': ['neo qled 8k', 'samsumg 8k'],
                'Samsung Neo QLED 4K': ['neo qled 4k', 'samsung 4k'],
                'Samsung QLED': ['samsung qled'],
                'Samsung Crystal UHD': ['crystal uhd'],
                'Samsung Lifestyle': ['lifestyle', 'the frame', 'the terrace', 'the serif'],
                'Samsung Micro RGB': ['micro rgb']
            }
        },
        'LG': {
            'Televisor': {
                'LG OLED': ['lg oled'],
                'LG QNED': ['lg qned'],
                'LG NanoCell': ['lg nano'],
                'LG UHD 4K': ['lg uhd', 'lg ut', 'lg 4k'],
                'LG OLED': ['lg oled'],
                'LG StandbyME': ['lg standbyme']
            }
        },
        'Sony': {
            'Televisor': {
                'Sony': ['televisor sony']
            }
        },
        'BRAVIA': {
            'Televisor': {
                'BRAVIA LED': ['bravia 3', 'bravia 2', 'bravia iii', 'bravia ii', 'bravia x90l'],
                'BRAVIA Mini LED': ['bravia'],   
            }
        },
        'TLC': {
            'Televisor': {
                'TCL SQD': ['tcl x11l', 'tcl 115'],
                'TCL RGB Mini LED': ['tcl rm9l'],
                'TCL C': ['tcl c'],
                'TCL Q': ['tcl q'],
                'TCL S': ['tcl s'],
                'TCL P': ['tcl p']
                
            }
        },
        'Hisense': {
            'Televisor': {
                'RGB Mini-LED': ['flagship', 'hisense ur9', 'hisense ur9s', 'hisense ur8', 'hisense ur8s'],
                'ULED Mini LED': ['hisense u'],
                'Hisense CanvasTV': ['canvastv'],
                'Hisense DécoTV': ['hisense decotv'],
                'Hisense S6 FollowMe': ['hisense s6 followme'],
                'Hisense QLED': ['hisense e', 'hisense a', 'hisense qled'],
                'Hisense Micro LED': ['hisense 163mx', 'hisense micro led'],
                'Hisense Laser TV': ['laser tv'],
                'Hisense PRO': ['hisense px3', 'hisense px4']
            }
        },
        'Xiaomi': {
            'Televisor': {
                'Xiaomi QD Mini LED': ['xiaomi tv s', 'xiaomi tv'],
                'Xiaomi QLED': ['xiaomi tv a pro', 'xiaomi tv q2', 'xiaomi tv q1e'],
                'Xiaomi UHD': ['xiaomi tv a', 'xiaomi tv f'],
                'Xiaomi Fire': ['xiaomi tv f2 fire', 'xiaomi fire']
            }
        },
        'AOC': {
            'Televisor': {
                'AOC 4K': ['aoc 4k'],
                'AOC HD': ['aoc hd'],
                'AOC G': ['aoc g', 'aoc 6305', 'aoc 6405', 'aoc s5145'],
                'AOC Xmart UI': ['aoc 5000', 'aoc 5100', 'aoc xmart'],
                'AOC VIDAA': ['aoc vidaa']
            }
        },
        'JVC': {
            'Televisor': {
                'JVC QLED': ['jvc qled pro 4k', 'jvc qled 4k', 'jvc qled full hd'],
                'JVC Smart Google TV': ['jvc smart', 'jvc 4k uhd', 'jvc km148'],
                'JVC Android TV': ['jvc android', 'jvc mar'],
                'JVC LT': ['jvc lt', 'jvc n']
            }
        },
        'Miray': {
            'Televisor': {
                'Miray QLED': ['miray e', 'miray t', 'miray qled'],
                'Miray LED 4K UHD': ['miray mk', 'miray vidaa', 'miray 4k'],
                'Miray HD': ['miray hd', 'miray full', 'miray ms']
            }
        },
        'Blackline': {
            'Televisor': {
                'Blackline QLED 4K': ['blackline qled', 'blackline bl'],
                'Blackline LED 4K': ['blackline led' ],
                'Blackline HD': ['blackline hd', 'blackline full']
            }
        },
        'Hyundai': {
            'Televisor': {
                'Hyundai QLED 4K': ['hyundai qled', 'hyled98', 'hyled85', 'hyled65', 'hyled55'],
                'Hyundai LED 4K UHD': ['hyuled75', 'hyled58', 'hyled50', 'hyundai led'],
                'Hyundai FULL HD': ['hyundai hd', 'hiunday full'],
                'Hyundai Digital LED': ['hyundai digital']
            }
        },
        'Caixun': {
            'Televisor': {
                'Caixun QLED 4K': ['caixun qled'],
                'Caixun LED 4K UHD': ['caixun led'],
                'Caixun FULL HD': ['caixun hd', 'caixun full'],
                'Caixun Digital LED': ['caixun digital']
            }
        },
        'Philips': {
            'Televisor': {
                'Philips OLED': ['philips oled'],
                'Philips Mini LED': ['philips pml'],
                'Philips The One': ['philips pus'],
                'Philips LED 4K': ['philips led', 'philips 4k'],
                'Philips QLED': ['philips qled'],  
            }
        },
        'Panasonic': {
            'Televisor': {
                'Panasonic OLED': ['panasonic oled', 'panasonic z'],
                'Panasonic Mini LED': ['panasonic mini led', 'panasonic w95', 'panasonic w93', 'panasonic w90'],
                'Panasonic LED 4K': ['panasonic w', 'panasonic mx', 'panasonic led', 'panasonic 4k'],
                'Panasonic FULL HD': ['panasonic s', 'panasonic n', 'panasonic hd', 'panasonic full']
            }
        },
        'Motorola': {
            'Televisor': {
                'Motorola EnvisionX': ['envisionx'],
                'Motorola ZX Pro': ['motorola zx'],
                'Motorola Revou': ['revou'],
                'Motorola Envision': ['envision']
            }
        },
        'Winia': {
            'Televisor': {
                'Smart 4K UHD': ['winia smart 4k'],
                'Winia Smart LED': ['winia smart led'],
                'Winia L22': ['winia l']
            }
        },
        'Master G': {
            'Televisor': {
                'Master G QLED': ['maste g qled'],
                'Smart 4K UHD': [' master g smart 4k uhd', 'master g m', 'master g vidaa'],
                'Smart FHD': ['master g mgg'],
                'Smart HD': ['master g mga', 'master g mgve'],
                'LED Digital': ['master g led']
            }
        },
        'Otro/Genérico': {
            'Televisor': {
                'Otro': ['tv', 'televisor', 'televisión', 'television', 'lcd']
            }  
        }
    },
    'Cámaras Fotográfica/Video': {
        'Sony':{
            'Cámara fotográfica': {
                'Alpha': ['sony alpha']
            },
            'Cámara de video': {
                'Sony ZV': ['sony zv', 'sony fx']
            }
        },
        'Canon': {
            'Cámara fotográfica': {
                'Canon EOS R5': ['canon eos']
            },
            'Cámara de video': {
                'Canon PowerShot': ['powershot']
            },
            'Cámara': {
                'canon': ['canon']
            }  
        },
        'Nikon': {
            'Cámara': {
                'Nikon': ['cámara nikon', 'camara nikon', 'nikon d80']
            }   
        },
        'Fujifilm': {
             'Cámara': {
                 'INSTAX': ['instax'],
                'Fujifilm': ['cámara fujifilm', 'camara fujifilm']
            }    
        },
        'Panasonic': {
              'Cámara': {
                'Panasonic': ['cámara panasonic', 'camara panasonic']
            } 
        },
        'DJI': {
             'Cámara': {
                'DJI': ['cámara dji', 'camara dji']
            }  
        },
        'GoPro': {
            'Cámara': {
                'GoPro': ['cámara gopro', 'camara gopro', 'gopro']
            }   
        },
        'Hikvision': {
            'Cámara de Seguridad': {
                'Hikvision': ['cámara hikvision', 'camaras hikvision', 'camara hikvision']
            },
        },
        'Dahua': {
            'Cámara de Seguridad': {
                'Dahua': ['cámara dahua', 'camara dahua']
            },    
        },
        'Ezviz': {
            'Cámara de Seguridad': {
                'Ezvis': ['cámara ezviz', 'camara ezviz']
            },    
        },
        'TP-Link': {
            'Cámara de Seguridad': {
                'TP-Link': ['cámara tp-link', 'camara tp-link']
            },    
        },
        'Xiaomi': {
            'Cámara de Seguridad': {
                'Xiaomi': ['cámara xiaomi', 'camara xiaomi']
            },    
        },
        'Eufi': {
           'Cámara de Seguridad': {
                'Eufi': ['cámara eufi', 'camara eufi']
            },     
        },
        'Blink': {
            'Cámara de Seguridad': {
                'Blink': ['cámara blink', 'camara blink']
            },    
        },
        'Imou': {
          'Cámara de Seguridad': {
                'Imou': ['cámara imou', 'camara imou']
            },      
        },
        'Insta360': {
           'Cámara': {
                'Insta360': ['insta']
            } 
        },
        'Otro/Genérico': {
            'Cámara': {
                'Otro': ['camara', 'cámara']
            }
        }
    },
    'Componentes PC': {
        'Intel': {
            'Procesador': {
                'Intel': ['procesador intel']
            }
        },
        'AMD': {
           'Procesador': {
               'AMD': ['procesador amd']
            } 
        },
        'Asus': {
            'Placa Madre': {
                'Asus': ['placa madre asus']
            },
            'Tarjeta Gráfica': {
                'Asus': ['tarjeta gráfica asus']
            },
            'Monitor': {
                'Asus': ['monitor asus', 'pantalla asus']
            }
        },
        'MSI': {
           'Placa Madre': {
               'MSI': ['placa madre msi']
            },
           'Tarjeta Gráfica': {
                'MSI': ['tarjeta gráfica msi']
            },
           'Monitor': {
               'MSI': ['monitor msi', 'pantalla msi']
           } 
        },
        'GYGABYTE': {
           'Placa Madre': {
               'GYGABYTE': ['placa madre gygabyte']
            },
           'Tarjeta Gráfica': {
                'GYGABYTE': ['tarjeta gráfica gygabyte']
            } 
        },
        'Kingston': {
            'Memoria Ram': {
               'Kingston': ['ddr4 kingston', 'ddr5 kingston', 'kingston ddr'] 
            }
        },
        'Corsair': {
            'Memoria Ram': {
                'Corsair': ['ddr corsair']
            },
            'Teclado': {
                'Corsair': ['teclado corsair']
            },
        },
        'Adata': {
            'Memoria Ram': {
                'Adata': ['ddr adata']
            }
        },
        'Samsung': {
            'Monitor/Pantalla': {
                'Odyssey': ['odyssey', 'monitor samsung']
            }
        },
        'iMac': {
            'pantalla':{
                'iMac': ['pantalla imac']
            }
        }, 
        'Logitech': {
            'Teclado': {
                'Logitech': ['teclado logitech']
            },
            'Mouse': {
                'Logitech': ['mouse logitech']
            }
        },
        'Razer': {
            'Teclado': {
                'Razer': ['teclado razer']
            },
            'Mouse': {
                'Razer': ['mouse razer']
            }
        },
        'Genius': {
           'Teclado': {
               'Genius': ['teclado genius']
            },
            'Mouse': {
                'Genius': ['mouse genius']
            } 
        },
        'Otro/Genérico': {
            'Memoria Ram': {
                'Otro': ['ddr', 'memoria ram']
            },
            'Monitor/Pantalla': {
                'Otro': ['monitor', 'pantalla']
            },
            'Teclado': {
                'Otro': ['teclado']
            },
            'Mouse': {
                'Otro': ['mouse']
            },
            'Tarjeta gráfica': {
                'Otro': ['tarjeta gráfica', 'tarjeta grafica', 'grafica', 'gráfica']
            },
            'Proyector': {
                'Otro': ['proyector']
            } 
        }
    },
    'Relojes': {
        'Casio': {
            'Reloj digital': {
                'Casio': ['reloj casio']
            }
        },
        'Citizen': {
            'Reloj analógico': {
                'Citizen': ['reloj citizen']
            }
        },
        'Seiko': {
            'Reloj analógico': {
                'Seiko': ['reloj seiko']
                }
        },
        'Fossil': {
            'Reloj analógico': {
                'Fossil': ['reloj fossil']
                }
        },
        'Tommy Hilfiger': {
            'Reloj analógico': {
                'Tommy Hilfiger': ['reloj tommy hilfiger']
            }
        },
        'Guess': {
            'Reloj analógico': {
                'Guess': ['reloj guess']
            }
        },
        'Rolex': {
           'Reloj analógico': {
                'Rolex': ['reloj rolex', 'rolex']
            } 
        },
        'Omega': {
           'Reloj analógico': {
                'Omega': ['reloj omega']
            } 
        },
        'Garmin': {
            'Reloj Deportivo': {
                'Garmin': ['reloj garmin']
            }
        },
        'Amazfit': {
            'Reloj Deportivo': {
                'Amazfit': ['reloj amazfit']
            }
        },
        'Otro/Genérico': {
            'Reloj': {
               'Otro': ['reloj'] 
            }            
        }
    },   
    'Drones': {
        'DJI': {
            'Drone': {
                'DJI': ['drone dji']
            }
        },
        'Autel Robotics': {
           'Drone': {
                'Autel Robotics': ['drone autel']
            } 
        },
        'Potensic': {
            'Drone': {
                'Potensic': ['drone potensic']
            }
        },
        'Fimi': {
            'Drone': {
                'Fimi': ['drone fimi']
            }
        },
        'Eachine': {
            'Drone': {
                'Eachine': ['drone eachine']
            }
        },
        'Bandai Namco': {
            'Drone': {
                'Bandai Namco': ['drone bandai']
            }
        },
        'DEERC': {
            'Drone': {
                'DEERC': ['drone deerc']
            }
        },
        'Rucco': {
            'Drone': {
                'Rucco': ['drone rucco']
            }
        },
        'Otro/Genérico': {
            'Drone': {
                'Otro': ['drone', 'dron', 'drom']
            }
        }
    },
   'Impresora/Escáner': {
       'Epson': {
           'Impresora': {
               'Epson': ['impresora epson']
           }
       },
       'HP': {
          'Impresora': {
               'HP': ['impresora hp']
           } 
       },
       'Canon': {
           'Impresora': {
               'Canon': ['impresora canon']
           }
       },
       'Brother': {
           'Impresora': {
               'Brother': ['impresora brother']
           }
       },
       'Xerox': {
           'Impresora': {
               'Xerox': ['impresora xerox']
           }
       },
       'Kyocera': {
           'Impresora': {
               'Kyocera': ['impresora kyocera']
           }
       },
       'Ricoh': {
           'Impresora': {
               'Ricoh': ['impresora ricoh', 'ricoh']
           }
       },
       'Zebra': {
           'Impresora': {
               'Zebra': ['impresora zebra']
           }
       },
       'Lexmark': {
           'Impresora': {
               'Lexmark': ['impresora lexmark']
           }
       },
       '3nStar': {
           'Impresora': {
               '3nStar': ['impresora 3nstar']
           }
       },
       'Advance': {
           'Impresora': {
               'Advance': ['impresora advance']
           }
       },
       'Pantum': {
           'Impresora': {
               'Pantum': ['impresora pantum']
           }
       },
       'Kodak': {
           'Impresora': {
               'Kodak': ['impresora kodak']
           }
       },
       'Konica Minolta': {
           'Impresora': {
               'Konica Minolta': ['impresora konica']
           }
       },
       'Otro/Genérico': {
           'Impresora': {
               'Otro': ['impresora', 'multifuncional']
           },
           'Escáner': {
               'Otro': ['escaner', 'escáner']
           },
           'Fotocopiadora': {
               'Otro': ['fotocopiadora', 'fotocopiadoras', 'copiadoras']
           }
       }
   },   
    'Conectividad/Redes': {
        'Mikrotik': {
            'Router': {
                'Mikrotik': ['router mikrotik', 'mikrotik']
            }
        },
        'Cisco': {
            'Router': {
                'Cisco': ['router cisco']
            },
            'Switch':{
                'Cisco': ['switch cisco']
            }         
        },
        'TP-Link': {
            'Router': {
                'TP-Link': ['router tp-link']
            },
            'Repetidor': {
                'TP-Link': ['repetidor tp-link', 'tp-link']
            }
        },
       'Otro/Genérico': {
           'switch': {
               'Otro': ['router', 'hub']
           },
           'Router': {
               'Otro': ['router']
           },
           'HUB': {
               'Otro': ['hub']
           },
           'Módem': {
               'Otro': ['módem', 'modem']
           },
           'Antena': {
               'Otro': ['antena']
           },
           'Repetidor': {
               'Otro': ['repetidor']
           },
           'Cable': {
               'Fibra': ['fibra'],
               'Patch cord': ['patch cord']
           }
       }
    },
    'Seguridad y Herramientas': {
       'Otro/Genérico': {
           'Detector de metales': {
               'Otro': ['detector', 'metales']
           },
           'Sistema facial': {
               'Otro': ['sistema facial']
           },
           'Estabilizador': {
               'Otro': ['estabilizador']
           }
       }
    },
   'Energía y Adaptadores': {
       'Otro/Genérico': {
           'Transformador': {
               'Otro': ['transformador']
           },
           'Adaptador': {
               'Otro': ['adaptador']
           },
           'Bateria': {
               'Otro': ['bateria', 'batería', 'baterías', 'baterias']
           },
           'Cargador': {
               'Otro': ['cargador']
           },
           'Estabilizador': {
               'Otro': ['estabilizador']
           }
       }
   },
   'Herramientas Pro': {
       'Otro/Genérico': {
           'Analizador': {
               'Otro': ['analizador']
           },
           'Laser': {
               'Otro': ['laser', 'láser']
           },
           'GPS': {
               'Otro': ['gps']
           },
           'Biometrico': {
               'Otro': ['biometrico']
           },
           'Scanner': {
               'Otro': ['scanner']
           },
           'Registradora': {
               'Otro': ['registradora']
           }
       }
   },
   'Calculadoras': {
       'Casio': {
           'Calculadora Científica': {
               'ClassWiz': ['classwiz', 'fx-82la', 'fx-991la']
           },
           'Calculadora Graficadora': {
               'Casio': ['fx-cg50']
           },
           'Calculadora financiera': {
               'Casio': ['fc-200v']
           },
           'Calculadora': {
               'Casio': ['calculadora casio']
           }
       },
       'HP': {
           'Calculadora': {
               'HP': ['hp prime', 'hp 12', 'hp 50', 'calculadora hp']
           }
       },
       'Texas Instruments (TI)': {
           'Calculadora': {
               'Texas Instruments': ['ti-nspire', 'ti-84', 'ti-ba', 'calculadora ti']
           }
       },
       'Citizen': {
           'Calculadora': {
               'Citizen': ['calculadora citizen']
           }
       },
       'Cifra': {
           'Calculadora': {
               'Cifra': ['calculadora cifra']
           }
       },
       'Otro/Genérico': {
           'Calculadora': {
               'Otro': ['calculadora']
           }
       }
   },
   'Micrófonos': {
       'Shure': {
           'Micrófono': {
               'Shure': ['micrófono shure', 'microfono shure']
           }
       },
       'Audio-Technica': {
           'Micrófono': {
               'Audio-Technica': ['micrófono audio-technica', 'microfono audio-technica']
           }
       },
       'Hollyland': {
          'Micrófono': {
               'Hollyland': ['micrófono hollyland', 'microfono hollyland']
           } 
       },
       'Otro/Genérico': {
           'Micrófono': {
               'Otro': ['micrófono', 'microfono']
           }
       }
   },
   'POS': {
       'Izipay': {
         'POS': {
             'Izipay': ['pos izipay']
         }  
       },
       'Niubiz': {
         'POS': {
             'Niubiz': ['pos niubiz']
         }   
       },
       'Culqi': {
         'POS': {
             'Culqi': ['pos culqi']
         }   
       },
       'Vendty': {
         'POS': {
             'Vendty': ['pos vendty']
         }   
       },
      'Otro/Genérico': {
           'POS': {
               'Otro': ['pos']
           }
       } 
   },
   'Teléfonos': {
       'Otro/Genérico': {
           'Télefono': {
               'Otro': ['teléfono', 'telefono']
           }
       }
   },
   'Dispositivos de radio': {
       'Lantun': {
           'Walkie Talkie': {
               'Lantun': ['walkie talkie lantun', 'lantun']
           }
       },
       'Otro/Genérico': {
           'Walkie Talkie': {
               'Otro': ['walkie talkie', 'walkie-talkie']
           }
       }
   }        
}



# Diccionario de Estados para limpieza de precios

diccionario_estados = {
    'Nuevo/Sellado': ['sellado', 'nuevo', 'new', 'caja', 'estrenar'],
    'Usado/Como Nuevo': ['como nuevo', '9/10', '10/10', 'impecable'],
    'Para Repuesto/Roto': ['repuesto', 'pantalla rota', 'para arreglar', 'bloqueado', 'roto']
}


