#!/usr/bin/env python3

def load_lang(data, doc_opener_keys):
    lang = 'de'

    data['comments'][lang]['title'] = "Bibliothek für Evolventen-Zahnräder, Schnecken und Zahnstangen"
    data['comments'][lang]['contents heading'] = "Enthält die Module"
    data['comments'][lang]['examples notice'] = "Beispiele für jedes Modul befinden sich auskommentiert am Ende dieser Datei"
    data['comments'][lang]['Author:'] = "Autor:"
    data['comments'][lang]['author names'] = "2018 Dr Jörg Janssen, 2019 Erhannis"  # "Dr Jörg Janssen"
    data['comments'][lang]['Date:'] = "Stand:"
    data['comments'][lang]['date'] = "29. Oktober 2018"
    data['comments'][lang]['License:'] = "Lizenz:"
    data['comments'][lang]['license name'] = "Creative Commons - Attribution, Non Commercial, Share Alike"
    data['comments'][lang]['permitted modules'] = "Erlaubte Module nach DIN 780:"
    data['comments'][lang]['globals tip'] = "Allgemeine Variablen"
    data['comments'][lang]['play tip'] = "Spiel zwischen Zähnen"
    data['comments'][lang]['function to_deg tip'] = "Wandelt Radian in Grad um"
    data['comments'][lang]['function to_rad tip'] = "Wandelt Grad in Radian um"
    data['comments'][lang]['function polar_to_cartesion tip'] = "Wandelt 2D-Polarkoordinaten in kartesische um"
    data['comments'][lang]['function involute tip'] = "\tKreisevolventen-Funktion:"
    data['comments'][lang]['function involute description'] = "Gibt die Polarkoordinaten einer Kreisevolvente aus"
    data['comments'][lang]['function spherical_involute tip'] = "Kugelevolventen-Funktion"
    data['comments'][lang]['function spherical_involute description'] = "Gibt den Azimutwinkel einer Kugelevolvente aus"
    data['comments'][lang]['spherical_involute param theta0 tip'] = "Polarwinkel des Kegels, an dessen Schnittkante zur Großkugel die Evolvente abrollt"
    data['comments'][lang]['spherical_involute param theta tip'] = "Polarwinkel, für den der Azimutwinkel der Evolvente berechnet werden soll"
    data['comments'][lang]['spherical_to_cartesian tip'] = "Wandelt Kugelkoordinaten in kartesische um"
    data['comments'][lang]['spherical_to_cartesian param theta tip'] = "Winkel zu z-Achse"
    data['comments'][lang]['spherical_to_cartesian param phi tip'] = "Winkel zur x-Achse auf xy-Ebene"
    data['comments'][lang]['function is_even tip'] = "prüft, ob eine Zahl gerade ist"
    data['comments'][lang]['function is_even result 1 tip'] = "wenn ja"
    data['comments'][lang]['function is_even result 0 tip'] = "wenn die Zahl nicht gerade ist"
    data['comments'][lang]['function gcd tip'] = "größter gemeinsamer Teiler"
    data['comments'][lang]['function gcd description'] = "nach Euklidischem Algorithmus."
    data['comments'][lang]['function gcd params'] = "Sortierung: a muss größer als b sein"
    data['comments'][lang]['function spiral tip'] = "Polarfunktion mit polarwinkel und zwei variablen"
    data['comments'][lang]['function copy_rotate tip'] = "Kopiert und dreht einen Körper"
    data['comments'][lang]['module rack tip'] = "Zahnstange"
    data['comments'][lang]['tip angle'] = "Kopfkegelwinkel"
    data['comments'][lang]['tip diameter'] = "Kopfkreisdurchmesser"
    doc_opener_keys[lang]['rack'] = 'module rack tip'
    doc_opener_keys[lang]['spur_gear'] = 'module spur_gear tip'

    data['variables'][lang]['play'] = "spiel"

    data['parameters'][lang]['rack module'] = "modul"
    # ^ Can't be "module" since that is a keyword in SCAD.
    data['param_help'][lang]['rack module'] = "Höhe des Zahnkopfes über der Wälzgeraden"
    data['parameters'][lang]['rack length'] = "laenge"
    data['param_help'][lang]['rack length'] = "Länge der Zahnstange"
    data['parameters'][lang]['rack height'] = "hoehe"
    data['param_help'][lang]['rack height'] = "Höhe der Zahnstange bis zur Wälzgeraden"
    data['parameters'][lang]['rack width'] = "width"
    data['param_help'][lang]['rack width'] = "Breite eines Zahns"
    data['parameters'][lang]['rack pressure_angle'] = "eingriffswinkel"
    data['param_help'][lang]['rack pressure_angle'] = "Eingriffswinkel, Standardwert = 20° gemäß DIN 867. Sollte nicht größer als 45° sein."
    data['parameters'][lang]['rack helix_angle'] = "schraegungswinkel"
    data['param_help'][lang]['rack helix_angle'] = "Schrägungswinkel zur Zahnstangen-Querachse; 0° = Geradverzahnung"

    data['comments'][lang]['module spur_gear tip'] = "Stirnrad"

    data['functions'][lang]['function to_deg'] = "grad"
    data['functions'][lang]['function to_rad'] = "radian"
    data['functions'][lang]['function gcd'] = "ggt"
    data['functions'][lang]['function is_even'] = "istgerade"
    data['functions'][lang]['function spiral'] = "spirale"
    data['functions'][lang]['function copy_rotate'] = "kopiere"
    data['functions'][lang]['function rack_dimensions'] = "zahnstange_dims"
    data['functions'][lang]['module rack'] = "zahnstange"
    data['functions'][lang]['module spur_gear'] = "stirnrad"
    data['functions'][lang]['function herringbone_involute_spur_gear'] = "pfeilrad"
    data['functions'][lang]['function rack_and_pinion'] = "zahnstange_und_rad"
    '''
    ^ documentation says zahnstange_und_ritzel but that function is not
    present in the upstream Getriebe.scad
    data['functions'][lang]['function rack_and_pinion'] =
    "zahnstange_und_ritzel"
    Note that ritzel means pinion and rad means gear (literally wheel).
    '''

    data['functions'][lang]['function involute_gear_ring'] = "hohlrad"
    data['functions'][lang]['function herringbone_involute_gear_ring'] = "pfeilhohlrad"
    data['functions'][lang]['function herringbone_involute_planetary_gears'] = "planetengetriebe"
    data['functions'][lang]['function spherical_involute_bevel_gear'] = "kegelrad"
    data['functions'][lang]['function spherical_herringbone_involute_bevel_gear'] = "pfeilkegelrad"
    data['functions'][lang]['function bevel_gear_pair'] = "kegelradpaar"
    data['functions'][lang]['function herringbone_bevel_gear_pair'] = "pfeilkegelradpaar"
    data['functions'][lang]['function worm'] = "schnecke"
    data['functions'][lang]['function worm_and_pinion'] = "schneckenradsatz"
    data['functions'][lang]['function polar_to_cartesion'] = "pol_zu_kart"
    data['functions'][lang]['function involute'] = "ev"
    data['functions'][lang]['function spherical_involute'] = "kugelev"
    data['functions'][lang]['function spherical_to_cartesian'] = "kugel_zu_kart"


