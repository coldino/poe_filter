#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Jeremy Parks
# Note: Requires Python 3.3.x or higher
desc = "Nonrare item for leveling or crafting"

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Driftwood Wand": {"base": "Driftwood Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 6"], "type": "leveling low"},
	"Goat's Horn": {"base": "Goat's Horn", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 11"], "type": "leveling low"},
	"Carved Wand": {"base": "Carved Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 17"], "type": "leveling low"},
	"Quartz Wand": {"base": "Quartz Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 23"], "type": "leveling low"},
	"Spiraled Wand": {"base": "Spiraled Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 29"], "type": "leveling low"},
	"Sage Wand": {"base": "Sage Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 35"], "type": "leveling low"},
	"Pagan Wand": {"base": "Pagan Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 39"], "type": "leveling low"},
	"Faun's Horn": {"base": "Faun's Horn", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 40"], "type": "leveling low"},
	"Engraved Wand": {"base": "Engraved Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 45"], "type": "leveling low"},
	"Crystal Wand": {"base": "Crystal Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 50"], "type": "leveling low"},
	"Serpent Wand": {"base": "Serpent Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 54"], "type": "ignore"},
	"Omen Wand": {"base": "Omen Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 58"], "type": "ignore"},
	"Heathen Wand": {"base": "Heathen Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 60"], "type": "ignore"},
	"Demon's Horn": {"base": "Demon's Horn", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 61"], "type": "ignore"},
	"Imbued Wand": {"base": "Imbued Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 64"], "type": "ignore"},
	"Opal Wand": {"base": "Opal Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 67"], "type": "ignore"},
	"Tornado Wand": {"base": "Tornado Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 70"], "type": "ignore"},
	"Prophecy Wand": {"base": "Prophecy Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 73"], "type": "ignore"},
	"Profane Wand": {"base": "Profane Wand", "class": "Wand", "other": ["Rarity <= Magic", "ItemLevel <= 75"], "type": "ignore"}
}
