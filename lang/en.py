#!/usr/bin/env python3

def load_lang(data, doc_opener_keys):
    lang = 'en'

    data['comments'][lang]['title'] = "Library for involute gears, worms and spur gears"
    data['comments'][lang]['contents heading'] = "Contains the modules"
    data['comments'][lang]['examples notice'] = "Examples for each module are commented out at the end of this file."
    data['comments'][lang]['Author:'] = "Author:"
    data['comments'][lang]['author names'] = "2018 Dr Jörg Janssen, 2019 Erhannis, 2022 Jake \"Poikilos\" Gustafson"
    data['comments'][lang]['Date:'] = "Date:"
    data['comments'][lang]['date'] = "October 29, 2018"
    data['comments'][lang]['License:'] = "License:"
    data['comments'][lang]['license name'] = "[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)"
    data['comments'][lang]['permitted modules'] = "Permitted modules according to DIN 780:"
    data['comments'][lang]['globals tip'] = "Globals"
    data['comments'][lang]['play tip'] = "play between teeth"
    data['comments'][lang]['function to_deg tip'] = "Convert radians to degrees."
    data['comments'][lang]['function to_rad tip'] = "Convert degrees to radians."
    data['comments'][lang]['function polar_to_cartesion tip'] = "Convert 2D polar coordinates to Cartesian."
    data['comments'][lang]['function involute tip'] = "  The involute function"
    data['comments'][lang]['function involute description'] = "gets the polar coordinates of an involute of a circle."
    data['comments'][lang]['function spherical_involute tip'] = "The spherical involute function"
    data['comments'][lang]['function spherical_involute description'] = "gets the azimuth angle of a spherical involute."
    data['comments'][lang]['spherical_involute param theta0 tip'] = "polar angle of the cone at whose cutting edge to the large sphere the involute rolls off"
    data['comments'][lang]['spherical_involute param theta tip'] = "polar angle for which the azimuth angle of the involute is to be calculated"
    data['comments'][lang]['spherical_to_cartesian tip'] = "Convert spherical coordinates to Cartesian."
    data['comments'][lang]['spherical_to_cartesian param theta tip'] = "angle to z-axis"
    data['comments'][lang]['spherical_to_cartesian param phi tip'] = "Angle to x axis on xy plane"
    data['comments'][lang]['function is_even tip'] = "Check whether a number is even."
    data['comments'][lang]['function is_even result 1 tip'] = "if yes"
    data['comments'][lang]['function is_even result 0 tip'] = "if the number is not even"
    data['comments'][lang]['function gcd tip'] = "Get the greatest common divisor"
    data['comments'][lang]['function gcd description'] = "according to Euclidean algorithm."
    data['comments'][lang]['function gcd params'] = "Limits: 'a' must be greater than 'b'."
    data['comments'][lang]['function spiral tip'] = "The spiral function uses the polar angle and two variables."
    data['comments'][lang]['function copy_rotate tip'] = "Copy and rotate a body."
    data['comments'][lang]['module rack tip'] = "Create a parametric gear rack."
    data['comments'][lang]['tip angle'] = "tip angle"
    data['comments'][lang]['tip diameter'] = "Kopfkreisdurchmesser"
    doc_opener_keys[lang]['rack'] = 'module rack tip'
    doc_opener_keys[lang]['spur_gear'] = 'module spur_gear tip'

    data['variables'][lang]['play'] = "play"

    data['parameters'][lang]['rack module'] = "module_arc_len"
    # ^ Can't be "module" since that is a keyword in SCAD.
    data['param_help'][lang]['rack module'] = "height of the tooth tip above the pitch circle diameter (PCD) line"
    data['parameters'][lang]['rack length'] = "length"
    data['param_help'][lang]['rack length'] = "rack length"
    data['parameters'][lang]['rack height'] = "height"
    data['param_help'][lang]['rack height'] = "height of the gear rack to the pitch (PCD) line"
    data['parameters'][lang]['rack width'] = "width"
    data['param_help'][lang]['rack width'] = "width of a tooth"
    data['parameters'][lang]['rack pressure_angle'] = "pressure_angle"
    data['param_help'][lang]['rack pressure_angle'] = "pressure angle, standard value = 20° according to DIN 867; should not be greater than 45°."
    data['parameters'][lang]['rack helix_angle'] = "helix_angle"
    data['param_help'][lang]['rack helix_angle'] = "helix angle to the transverse axis of the rack; 0° = straight teeth"

    data['comments'][lang]['module spur_gear tip'] = "Create a parametric involute spur gear."

    data['functions'][lang]['function to_deg'] = "to_deg"
    data['functions'][lang]['function to_rad'] = "to_rad"
    data['functions'][lang]['function gcd'] = "gcd"
    data['functions'][lang]['function is_even'] = "is_even"
    data['functions'][lang]['function spiral'] = "spiral"
    data['functions'][lang]['function copy_rotate'] = "copy_rotate"
    data['functions'][lang]['function rack_dimensions'] = "rack_dimensions"
    data['functions'][lang]['module rack'] = "rack"
    data['functions'][lang]['module spur_gear'] = "spur_gear"
    data['functions'][lang]['function herringbone_involute_spur_gear'] = "herringbone_spur_gear"
    data['functions'][lang]['function rack_and_pinion'] = "rack_and_pinion"
    data['functions'][lang]['function involute_gear_ring'] = "gear_ring"
    data['functions'][lang]['function herringbone_involute_gear_ring'] = "herringbone_gear_ring"
    data['functions'][lang]['function herringbone_involute_planetary_gears'] = "herringbone_planetary_gears"
    data['functions'][lang]['function spherical_involute_bevel_gear'] = "bevel_gear"
    data['functions'][lang]['function spherical_herringbone_involute_bevel_gear'] = "herringbone_bevel_gear"
    data['functions'][lang]['function bevel_gear_pair'] = "bevel_gear_pair"
    data['functions'][lang]['function herringbone_bevel_gear_pair'] = "herringbone_bevel_gear_pair"
    data['functions'][lang]['function worm'] = "worm"
    data['functions'][lang]['function worm_and_pinion'] = "worm_and_pinion"
    data['functions'][lang]['function polar_to_cartesion'] = "polar_to_cartesion"
    data['functions'][lang]['function involute'] = "ev"
    data['functions'][lang]['function spherical_involute'] = "spherical_involute"
    data['functions'][lang]['function spherical_to_cartesian'] = "spherical_to_cartesian"

