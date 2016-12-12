#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/10/2016(m/d/y) 01:15:14 UTC from "Hardcore" data
"""
* Copyright (c) 2016 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create an item filter based on config files
Note: Requires Python 3.4.x
"""

desc = "Unique"

# Base type : settings pair
items = {
	"0 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique very high"},
	"0 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique very high"},
	"0 Blinder": {"base": "Blinder", "type": "unique very high"},
	"0 Bone Bow": {"base": "Bone Bow", "type": "unique very high"},
	"0 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"0 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique very high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique very high"},
	"0 Citadel Bow": {"base": "Citadel Bow", "type": "unique very high"},
	"0 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique very high"},
	"0 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"0 Clutching Talisman": {"base": "Clutching Talisman", "type": "unique very high"},
	"0 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique very high"},
	"0 Despot Axe": {"base": "Despot Axe", "type": "unique very high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique very high"},
	"0 Fiend Dagger": {"base": "Fiend Dagger", "type": "unique very high"},
	"0 Fishing Rod": {"base": "Fishing Rod", "type": "unique very high"},
	"0 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique very high"},
	"0 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Golden Bracers": {"base": "Golden Bracers", "type": "unique very high"},
	"0 Golden Caligae": {"base": "Golden Caligae", "type": "unique very high"},
	"0 Golden Flame": {"base": "Golden Flame", "type": "unique very high"},
	"0 Golden Hoop": {"base": "Golden Hoop", "type": "unique very high"},
	"0 Golden Mantle": {"base": "Golden Mantle", "type": "unique very high"},
	"0 Golden Obi": {"base": "Golden Obi", "type": "unique very high"},
	"0 Golden Wreath": {"base": "Golden Wreath", "type": "unique very high"},
	"0 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique very high"},
	"0 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique very high"},
	"0 Jasper Chopper": {"base": "Jasper Chopper", "type": "unique very high"},
	"0 Jet Amulet": {"base": "Jet Amulet", "type": "unique very high"},
	"0 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"0 Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "type": "unique very high"},
	"0 Legion Gloves": {"base": "Legion Gloves", "type": "unique very high"},
	"0 Midnight Blade": {"base": "Midnight Blade", "type": "unique very high"},
	"0 Murder Boots": {"base": "Murder Boots", "type": "unique very high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Regicide Mask": {"base": "Regicide Mask", "type": "unique very high"},
	"0 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique very high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique very high"},
	"0 Royal Axe": {"base": "Royal Axe", "type": "unique very high"},
	"0 Royal Burgonet": {"base": "Royal Burgonet", "type": "unique very high"},
	"0 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique very high"},
	"0 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique very high"},
	"0 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"0 Siege Helmet": {"base": "Siege Helmet", "type": "unique very high"},
	"0 Silver Flask": {"base": "Silver Flask", "type": "unique very high"},
	"0 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique very high"},
	"0 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique very high"},
	"0 Spine Bow": {"base": "Spine Bow", "type": "unique very high"},
	"0 Steelhead": {"base": "Steelhead", "type": "unique very high"},
	"0 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique very high"},
	"0 Topaz Flask": {"base": "Topaz Flask", "type": "unique very high"},
	"0 Vaal Mask": {"base": "Vaal Mask", "type": "unique very high"},
	"0 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique very high"},
	"0 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique very high"},
	"0 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique very high"},
	"0 Vanguard Belt": {"base": "Vanguard Belt", "type": "unique very high"},
	"0 Void Axe": {"base": "Void Axe", "type": "unique very high"},
	"0 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique very high"},
	"1 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique high"},
	"1 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique high"},
	"1 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique high"},
	"1 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique high"},
	"1 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique high"},
	"1 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique high"},
	"1 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique high"},
	"1 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique high"},
	"1 Crusader Plate": {"base": "Crusader Plate", "type": "unique high"},
	"1 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique high"},
	"1 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique high"},
	"1 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique high"},
	"1 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique high"},
	"1 Gladius": {"base": "Gladius", "type": "unique high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"1 Graveyard Map": {"base": "Graveyard Map", "type": "unique high"},
	"1 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"1 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique high"},
	"1 Imperial Skean": {"base": "Imperial Skean", "type": "unique high"},
	"1 Judgement Staff": {"base": "Judgement Staff", "type": "unique high"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"1 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"1 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique high"},
	"1 Lion Pelt": {"base": "Lion Pelt", "type": "unique high"},
	"1 Meatgrinder": {"base": "Meatgrinder", "type": "unique high"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique high"},
	"1 Opal Wand": {"base": "Opal Wand", "type": "unique high"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique high"},
	"1 Praetor Crown": {"base": "Praetor Crown", "type": "unique high"},
	"1 Ranger Bow": {"base": "Ranger Bow", "type": "unique high"},
	"1 Raven Mask": {"base": "Raven Mask", "type": "unique high"},
	"1 Saintly Chainmail": {"base": "Saintly Chainmail", "type": "unique high"},
	"1 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique high"},
	"1 Savant's Robe": {"base": "Savant's Robe", "type": "unique high"},
	"1 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "unique high"},
	"1 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique high"},
	"1 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"1 Slink Boots": {"base": "Slink Boots", "type": "unique high"},
	"1 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique high"},
	"1 Trapper Boots": {"base": "Trapper Boots", "type": "unique high"},
	"1 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique high"},
	"1 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique high"},
	"1 Vaal Axe": {"base": "Vaal Axe", "type": "unique high"},
	"1 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique high"},
	"1 Varnished Coat": {"base": "Varnished Coat", "type": "unique high"},
	"1 Zealot Helmet": {"base": "Zealot Helmet", "type": "unique high"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Legion Boots": {"base": "Legion Boots", "type": "unique low"},
	"7 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
