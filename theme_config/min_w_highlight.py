#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "formattinglate for all files"

# Color values from http://pathofexile.gamepedia.com/Item_filter_guide
color = {
	"normal": "200 200 200",
	"magic": "136 136 255",
	"rare": "255 255 119",
	"unique": "175 96 37",
	"gem": "27 162 155",
	"currency": "170 158 130",
	"quest": "74 230 58",
	"divinationold": "170 230 230",
	"default": "127 127 127",
	"value": "255 255 255",
	"augmented": "136 136 255",
	"fire": "150 0 0",
	"cold": "54 100 146",
	"lightning": "255 215 0",
	"chaos": "208 32 144",
	"crafted": "184 218 242",
	"corrupted": "210 0 0",
	"supportpacknew": "180 96 0",
	"supporterpack": "163 141 109",
	"nemesis": "255 200 0",
	"nemesisoutline": "255 40 0",
	"bloodline": "210 0 220",
	"bloodlineoutline": "74 0 160",
	"torment": "50 230 100",
	"tormentoutline": "0 100 150",
	"title": "231 180 120",
	"favour": "170 158 120",
	"lpink": "255 192 203",
	"divinationnew": "30 144 255",
	"premiumbrown": "124 81 50",
	"premiumorange": "191 91 0",
	"premiumtan": "254 191 128",
	"premiumdpurple": "38 0 86",
	"premiumpurple": "88 0 179",
	"premiumlpurple": "192 128 254",
	"premiumdlime": "98 128 0",
	"premiumlime": "191 244 0",
	"premiumllime": "239 254 128",
	"premiumdred": "86 0 0",
	"premiumred": "191 0 0",
	"premiumlred": "254 128 128",
	"premiumdblue": "0 0 128",
	"premiumblue": "0 0 254",
	"premiumlblue": "128 179 254",
	"premiumdyellow": "254 170 0",
	"premiumyellow": "254 213 0",
	"premiumlyellow": "254 254 153",
	"premiumdlavender": "114 0 83",
	"premiumlavender": "204 0 154",
	"premiumllavender": "254 128 222",
	"premiumdgreen": "0 73 0",
	"premiumgreen": "0 191 0",
	"premiumlgreen": "128 254 128",
	"premiumdgrey": "42 42 42",
	"premiumgrey": "135 135 135",
	"premiumlgrey": "221 221 221",
	"black": "0 0 0",
	"prophecy": "128 0 200",
	"highlight": "51 58 75"
}

size = {
	"huge": "45",
	"vlarge": "40",
	"large": "35",
	"normal": "30",
	"small": "25",
	"minimum": "18",
}

volume = {
	"max": "300",
	"high": "100",
	"normal": "75",
	"medium": "45",
	"low": "20"
}

# Text settings for various categories
# This is where you would define general settings for a category, such as PlayAlertSoundPositional.
# Each config should be its own array element.  Parsing will handle tabs/etc.
# ignore and hide have special meaning(see comment)
settings = {
	"challenge high": ["SetBorderColor {}".format(color['prophecy']),
					   'MinimapIcon 0 Brown Triangle',
					   'PlayEffect Brown',
					   "SetFontSize {}".format(size['huge']),
					   'CustomAlertSound "{}_challenge.wav"'.format(volume['high']),
					   "SetBackgroundColor {} 220".format(color['black'])],
	"challenge normal": ["SetBorderColor {}".format(color['prophecy']),
						 'MinimapIcon 1 Brown Triangle',
						 "SetFontSize {}".format(size['large']),
						 'CustomAlertSound "{}_challenge.wav"'.format(volume['low']),
						 "SetBackgroundColor {} 220".format(color['black'])],
	"challenge low": ["SetBorderColor {}".format(color['prophecy']),
					  "SetFontSize {}".format(size['small']),
					  "SetBackgroundColor {} 220".format(color['black'])],

	"animate melee b": ["SetFontSize {}".format(size['minimum']),
						"SetTextColor {}".format(color['premiumlred']),
						"SetBorderColor {} 150".format(color['premiumlred']),
						"SetBackgroundColor {} 0".format(color['black'])],
	"animate melee": ["SetFontSize {}".format(size['minimum']),
					  "SetTextColor {} 150".format(color['premiumlred']),
					  "SetBackgroundColor {} 0".format(color['black'])],

	"animate range b": ["SetFontSize {}".format(size['small']),
						"SetTextColor {}".format(color['premiumlred']),
						"SetBorderColor {} 200".format(color['premiumtan']),
						"SetBackgroundColor {} 150".format(color['premiumbrown'])],

	"animate range": ["SetFontSize {}".format(size['small']),
					  "SetTextColor {}".format(color['black']),
					  "SetBackgroundColor {} 150".format(color['premiumbrown'])],

	"quest": ["SetFontSize {}".format(size['normal']),
			  'MinimapIcon 2 Green Triangle',
			  'PlayEffect Green',
			  "SetBorderColor {} 200".format(color['quest']),
			  "SetBackgroundColor {} 220".format(color['black'])],

	"chance": ["Rarity Normal",
	           'Corrupted False',
			   "SetFontSize {}".format(size['large']),
			   "SetBorderColor {} 150".format(color['premiumorange']),
			   "SetBackgroundColor {} 220".format(color['premiumdpurple'])],

	"chromatic": ["SocketGroup RGB",
				  "SetBorderColor {}".format(color['premiumgreen']),
				  "SetFontSize {}".format(size['normal']),
				  "SetBackgroundColor {} 220".format(color['black'])],

	"t1 ilvl83/84 crafting": ["Rarity <= Magic",
							  "SetFontSize {}".format(size['small']),
							  "SetBackgroundColor {} 220".format(color['black'])],

	"currency extremely high": ["SetBorderColor {}".format(color['currency']),
								'MinimapIcon 0 Yellow Circle',
								'PlayEffect Yellow',
								"SetFontSize {}".format(size['huge']),
								'CustomAlertSound "{}_valuable.wav"'.format(volume['max']),
								"SetBackgroundColor {} 220".format(color['highlight'])],
	"currency very high": ["SetBorderColor {}".format(color['currency']),
						   'MinimapIcon 1 Yellow Circle',
						   'PlayEffect Yellow',
						   "SetFontSize {}".format(size['huge']),
						   'CustomAlertSound "{}_currency.wav"'.format(volume['high']),
						   "SetBackgroundColor {} 220".format(color['black'])],
	"currency high": ["SetBorderColor {}".format(color['currency']),
					  'MinimapIcon 1 Yellow Circle',
					  "SetFontSize {}".format(size['vlarge']),
					  'CustomAlertSound "{}_currency.wav"'.format(volume['normal']),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"currency normal": ["SetBorderColor {}".format(color['currency']),
						'MinimapIcon 2 Yellow Circle',
						"SetFontSize {}".format(size['large']),
						'CustomAlertSound "{}_currency.wav"'.format(volume['low']),
						"SetBackgroundColor {} 220".format(color['black'])],
	"currency low": ["SetFontSize {}".format(size['small']),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"currency show": ["SetBorderColor {} 150".format(color['currency']),
#					  'MinimapIcon 2 Yellow Circle',
					  "SetFontSize {}".format(size['normal']),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"currency very low": ["SetFontSize {}".format(size['small']),
						  "SetBackgroundColor {} 150".format(color['black'])],

	"divination extremely high": ["SetBorderColor {}".format(color['divinationnew']),
								  'MinimapIcon 0 Blue Circle',
								  'PlayEffect Blue',
								  "SetFontSize {}".format(size['huge']),
								  'CustomAlertSound "{}_valuable.wav"'.format(volume['max']),
								  "SetBackgroundColor {} 220".format(color['highlight'])],
	"divination very high": ["SetBorderColor {}".format(color['divinationnew']),
							 'MinimapIcon 1 Blue Circle',
							 'PlayEffect Blue',
							 "SetFontSize {}".format(size['huge']),
							 'CustomAlertSound "{}_divination.wav"'.format(volume['high']),
							 "SetBackgroundColor {} 220".format(color['black'])],
	"divination high": ["SetBorderColor {}".format(color['divinationnew']),
						'MinimapIcon 1 Blue Circle',
						'CustomAlertSound "{}_divination.wav"'.format(volume['normal']),
						"SetBackgroundColor {} 220".format(color['black'])],
	"divination normal": ['MinimapIcon 2 Blue Circle',
						  'CustomAlertSound "{}_divination.wav"'.format(volume['low']),
						  "SetBackgroundColor {} 220".format(color['black'])],
	"divination low": ["SetBackgroundColor {} 220".format(color['black']),
					   "SetFontSize {}".format(size['small'])],

	"gem very high": ["SetBorderColor {}".format(color['gem']),
					  'MinimapIcon 1 Brown Hexagon',
					  'CustomAlertSound "{}_gem.wav"'.format(volume['normal']),
					  "SetFontSize {}".format(size['large']),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"gem high": ["SetBorderColor {}".format(color['gem']),
				 'MinimapIcon 2 Brown Hexagon',
				 'CustomAlertSound "{}_gem.wav"'.format(volume['low']),
				 "SetFontSize {}".format(size['normal']),
				 "SetBackgroundColor {} 220".format(color['black'])],
	"gem normal": ["SetBorderColor {} 150".format(color['gem']),
				   "SetBackgroundColor {} 220".format(color['black']),
				   "SetFontSize {}".format(size['small'])],
	"gem low": ["SetFontSize {}".format(size['small']),
				"SetBackgroundColor {} 220".format(color['black'])],

	"leveling high": ["SetFontSize {}".format(size['normal']),
					  "SetBackgroundColor {} 150".format(color['black']),
					  "SetBorderColor {}".format(color['nemesisoutline'])],
	"leveling normal": ["SetFontSize {}".format(size['small']),
						"SetBackgroundColor {} 150".format(color['black']),
						"SetBorderColor {}".format(color['tormentoutline'])],
	"leveling low": ["SetFontSize {}".format(size['minimum']),
					 "SetBackgroundColor {} 150".format(color['black']),
					 "SetBorderColor {}".format(color['normal'])],

	"map red": ["SetBorderColor {} 150".format(color['fire']),
				'MinimapIcon 1 Red Diamond',
				"SetFontSize {}".format(size['vlarge']),
				'CustomAlertSound "{}_map_okay.wav"'.format(volume['normal']),
				"SetBackgroundColor {} 220".format(color['black'])],
	"map yellow": ["SetBorderColor {} 150".format(color['lightning']),
				   'MinimapIcon 2 Yellow Diamond',
				   "SetFontSize {}".format(size['large']),
				   "SetBackgroundColor {} 220".format(color['black'])],
	"map white": ["SetBorderColor {} 150".format(color['normal']),
				  'MinimapIcon 2 White Diamond',
				  "SetBackgroundColor {} 220".format(color['black'])],

	"map very good": ["SetBorderColor {}".format(color['fire']),
					 'MinimapIcon 0 Red Diamond',
					 'PlayEffect Red',
					 "SetFontSize {}".format(size['huge']),
					 'CustomAlertSound "{}_valuable.wav"'.format(volume['normal']),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"map red good": ["SetBorderColor {}".format(color['fire']),
					 'MinimapIcon 0 Red Diamond',
					 'PlayEffect Red',
					 "SetFontSize {}".format(size['huge']),
					 'CustomAlertSound "{}_map_good.wav"'.format(volume['high']),
					 "SetBackgroundColor {} 220".format(color['black'])],
	"map yellow good": ["SetBorderColor {}".format(color['lightning']),
						'MinimapIcon 1 Yellow Diamond',
						'PlayEffect Yellow',
						'CustomAlertSound "{}_map_good.wav"'.format(volume['medium']),
						"SetFontSize {}".format(size['large']),
						"SetBackgroundColor {} 220".format(color['black'])],
	"map white good": ["SetBorderColor {}".format(color['normal']),
					   'MinimapIcon 1 White Diamond',
					   'PlayEffect White',
					   "SetBackgroundColor {} 220".format(color['black']),
					   'CustomAlertSound "{}_map_good.wav"'.format(volume['low'])],

	"levelling rare high": ["Rarity Rare",
							"SetBorderColor {} 150".format(color['rare']),
							"SetFontSize {}".format(size['large']),
							"SetBackgroundColor {} 220".format(color['black'])],

	"rare highlight": ["Rarity Rare",
					   'MinimapIcon 2 Green Hexagon',
					   "SetFontSize {}".format(size['large']),
					   "SetBorderColor {} 150".format(color['premiumorange']),
					   "SetBackgroundColor {} 220".format(color['premiumdpurple'])],
	"rare high": ["Rarity Rare",
				  "SetBorderColor {}".format(color['rare']),
				  "SetFontSize {}".format(size['normal']),
				  "SetBackgroundColor {} 220".format(color['black'])],
	"levelling rare normal": ["Rarity Rare",
							  "SetBorderColor {} 150".format(color['rare']),
							  "SetFontSize {}".format(size['normal']),
							  "SetBackgroundColor {} 220".format(color['black'])],
	"rare normal": ["Rarity Rare",
					"SetFontSize {}".format(size['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],
	"rare low": ["Rarity Rare",
				 "SetFontSize {}".format(size['small']),
				 "SetBackgroundColor {} 220".format(color['black'])],

	"recipe item normal": ["SetBorderColor {}".format(color['premiumlavender']),
						   "SetFontSize {}".format(size['normal']),
						   "SetBackgroundColor {} 220".format(color['black'])],

	"show very high": ["SetBorderColor {}".format(color['premiumlpurple']),
					   'MinimapIcon 0 White Square',
					   "SetFontSize {}".format(size['huge']),
					   'CustomAlertSound "{}_show.wav"'.format(volume['high']),
					   "SetBackgroundColor {} 220".format(color['black'])],
	"show high": ["SetBorderColor {}".format(color['premiumlpurple']),
				  'MinimapIcon 1 White Square',
				  "SetFontSize {}".format(size['large']),
				  "SetBackgroundColor {} 220".format(color['black'])],
	"show normal": ["SetBorderColor {}".format(color['premiumlpurple']),
					'MinimapIcon 2 White Square',
					"SetFontSize {}".format(size['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],
	"show low": ["SetFontSize {}".format(size['small']),
				 "SetBackgroundColor {} 220".format(color['black'])],

	"item mod": ["SetBorderColor {}".format(color['premiumlpurple']),
					'MinimapIcon 2 Blue Square',
					"SetFontSize {}".format(size['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],

	"t1 83/84 rare highlight": ["Rarity Rare",
						   "SetBorderColor {}".format(color['nemesisoutline']),
						   "SetFontSize {}".format(size['large']),
						   "SetBackgroundColor {} 220".format(color['premiumdpurple'])],

	"t1 83/84 rare high": ["Rarity Rare",
						   "SetBorderColor {}".format(color['nemesisoutline']),
						   "SetFontSize {}".format(size['large']),
						   "SetBackgroundColor {} 220".format(color['black'])],

	"base extremely high": ["Rarity < Unique",
							'MinimapIcon 0 Green Hexagon',
							'PlayEffect Green',
							"SetBorderColor {}".format(color['premiumgreen']),
							"SetFontSize {}".format(size['huge']),
							'CustomAlertSound "{}_valuable.wav"'.format(volume['max']),
							"SetBackgroundColor {} 220".format(color['highlight'])],
	"base very high": ["Rarity < Unique",
					   'MinimapIcon 1 Green Hexagon',
					   'PlayEffect Green',
					   "SetBorderColor {}".format(color['premiumgreen']),
					   "SetFontSize {}".format(size['huge']),
					   'CustomAlertSound "{}_base.wav"'.format(volume['high']),
					   "SetBackgroundColor {} 220".format(color['black'])],
	"unique extremely high": ["Rarity Unique",
							  'MinimapIcon 0 Yellow Star',
							  'PlayEffect Yellow',
							  "SetBorderColor {}".format(color['unique']),
							  "SetFontSize {}".format(size['huge']),
							  'CustomAlertSound "{}_valuable.wav"'.format(volume['max']),
							  "SetBackgroundColor {} 220".format(color['highlight'])],
	"unique very high": ["Rarity Unique",
						 'MinimapIcon 1 Yellow Star',
						 'PlayEffect Yellow',
						 "SetBorderColor {}".format(color['unique']),
						 "SetFontSize {}".format(size['huge']),
						 'CustomAlertSound "{}_unique.wav"'.format(volume['high']),
						 "SetBackgroundColor {} 220".format(color['black'])],
	"unique high": ["Rarity Unique",
					'MinimapIcon 1 Yellow Star',
					"SetFontSize {}".format(size['vlarge']),
					"SetBorderColor {}".format(color['unique']),
					'CustomAlertSound "{}_unique.wav"'.format(volume['normal']),
					"SetBackgroundColor {} 220".format(color['black'])],
	# Special class of unique that has a low average value buthas some items that are quite valuable
	"unique special": ["Rarity Unique",
					   "SetFontSize {}".format(size['large']),
					   'MinimapIcon 2 Yellow Star',
					   "SetBorderColor {}".format(color['chaos']),
	                   'CustomAlertSound "{}_unique.wav"'.format(volume['medium']),
					   "SetBackgroundColor {} 220".format(color['black'])],
	"unique normal": ["Rarity Unique",
					  "SetFontSize {}".format(size['normal']),
#					  "SetBorderColor {}".format(color['unique']),
					  'MinimapIcon 2 Yellow Star',
					  'CustomAlertSound "{}_unique.wav"'.format(volume['low']),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"unique low": ["Rarity Unique",
				   "SetFontSize {}".format(size['small']),
				   "SetBackgroundColor {} 220".format(color['black'])],

	"high": ["SetBorderColor {}".format(color['premiumdyellow']),
			 "SetFontSize {}".format(size['large']),
			 "SetBackgroundColor {} 220".format(color['black'])],
	"normal border": ["SetFontSize {}".format(size['normal']),
					  "SetBorderColor {}".format(color['normal']),
					  "SetBackgroundColor {} 220".format(color['black'])],
	"normal": ["SetFontSize {}".format(size['normal']),
			   "SetBackgroundColor {} 220".format(color['black'])],
	"low": ["SetFontSize {}".format(size['minimum']),
			"SetBackgroundColor {} 150".format(color['black'])],

	"ignore": [""],  # will have no styling applied and will use the default set at the end
	"hide": [""]  # Will be explicitly hidden with applied styling
}