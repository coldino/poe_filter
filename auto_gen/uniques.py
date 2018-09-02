#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/02/2018(m/d/y) 17:45:58 UTC from "Standard" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Callous Mask": {"base": "Callous Mask", "type": "unique very high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Golden Bracers": {"base": "Golden Bracers", "type": "unique very high"},
	"0 Golden Hoop": {"base": "Golden Hoop", "type": "unique very high"},
	"0 Golden Mantle": {"base": "Golden Mantle", "type": "unique very high"},
	"0 Golden Obi": {"base": "Golden Obi", "type": "unique very high"},
	"0 Golden Wreath": {"base": "Golden Wreath", "type": "unique very high"},
	"0 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique very high"},
	"0 Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "type": "unique very high"},
	"0 Jet Amulet": {"base": "Jet Amulet", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique very high"},
	"0 Royal Axe": {"base": "Royal Axe", "type": "unique very high"},
	"1 Ambush Mitts": {"base": "Ambush Mitts", "type": "unique high"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique high"},
	"1 Arcanist Slippers": {"base": "Arcanist Slippers", "type": "unique high"},
	"1 Assassin's Boots": {"base": "Assassin's Boots", "type": "unique high"},
	"1 Blood Raiment": {"base": "Blood Raiment", "type": "unique high"},
	"1 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique high"},
	"1 Carnal Boots": {"base": "Carnal Boots", "type": "unique high"},
	"1 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique high"},
	"1 Clutching Talisman": {"base": "Clutching Talisman", "type": "unique high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique high"},
	"1 Deicide Mask": {"base": "Deicide Mask", "type": "unique high"},
	"1 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique high"},
	"1 Gemstone Sword": {"base": "Gemstone Sword", "type": "unique high"},
	"1 Glorious Plate": {"base": "Glorious Plate", "type": "unique high"},
	"1 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique high"},
	"1 Harbinger Map": {"base": "Harbinger Map", "type": "unique high"},
	"1 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique high"},
	"1 Heavy Quiver": {"base": "Heavy Quiver", "type": "unique high"},
	"1 Hydrascale Boots": {"base": "Hydrascale Boots", "type": "unique high"},
	"1 Imperial Maul": {"base": "Imperial Maul", "type": "unique high"},
	"1 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique high"},
	"1 Legion Gloves": {"base": "Legion Gloves", "type": "unique high"},
	"1 Magistrate Crown": {"base": "Magistrate Crown", "type": "unique high"},
	"1 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique high"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique high"},
	"1 Nubuck Gloves": {"base": "Nubuck Gloves", "type": "unique high"},
	"1 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique high"},
	"1 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique high"},
	"1 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique high"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique high"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique high"},
	"1 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique high"},
	"1 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique high"},
	"1 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique high"},
	"1 Shore Map": {"base": "Shore Map", "type": "unique high"},
	"1 Siege Axe": {"base": "Siege Axe", "type": "unique high"},
	"1 Steel Ring": {"base": "Steel Ring", "type": "unique high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique high"},
	"1 Vaal Mask": {"base": "Vaal Mask", "type": "unique high"},
	"1 Void Axe": {"base": "Void Axe", "type": "unique high"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique high"},
	"1 Wyrmscale Doublet": {"base": "Wyrmscale Doublet", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique special"},
	"6 Assassin Bow": {"base": "Assassin Bow", "type": "unique special"},
	"6 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique special"},
	"6 Branded Kite Shield": {"base": "Branded Kite Shield", "type": "unique special"},
	"6 Carnal Armour": {"base": "Carnal Armour", "type": "unique special"},
	"6 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"6 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique special"},
	"6 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cloth Belt Piece": {"base": "Cloth Belt Piece", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique special"},
	"6 Coral Ring": {"base": "Coral Ring", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Crude Bow": {"base": "Crude Bow", "type": "unique special"},
	"6 Crystal Sceptre": {"base": "Crystal Sceptre", "type": "unique special"},
	"6 Cutlass": {"base": "Cutlass", "type": "unique special"},
	"6 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique special"},
	"6 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique special"},
	"6 Despot Axe": {"base": "Despot Axe", "type": "unique special"},
	"6 Dusk Blade": {"base": "Dusk Blade", "type": "unique special"},
	"6 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"6 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique special"},
	"6 Elegant Sword": {"base": "Elegant Sword", "type": "unique special"},
	"6 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique special"},
	"6 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique special"},
	"6 Gavel": {"base": "Gavel", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Golden Plate": {"base": "Golden Plate", "type": "unique special"},
	"6 Goliath Greaves": {"base": "Goliath Greaves", "type": "unique special"},
	"6 Granite Flask": {"base": "Granite Flask", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique special"},
	"6 Imperial Bow": {"base": "Imperial Bow", "type": "unique special"},
	"6 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Long Staff": {"base": "Long Staff", "type": "unique special"},
	"6 Maelström Staff": {"base": "Maelström Staff", "type": "unique special"},
	"6 Midnight Blade": {"base": "Midnight Blade", "type": "unique special"},
	"6 Mind Cage": {"base": "Mind Cage", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique special"},
	"6 Murder Boots": {"base": "Murder Boots", "type": "unique special"},
	"6 Murder Mitts": {"base": "Murder Mitts", "type": "unique special"},
	"6 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique special"},
	"6 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique special"},
	"6 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique special"},
	"6 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique special"},
	"6 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"6 Opal Ring": {"base": "Opal Ring", "type": "unique special"},
	"6 Paua Amulet": {"base": "Paua Amulet", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique special"},
	"6 Pine Buckler": {"base": "Pine Buckler", "type": "unique special"},
	"6 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique special"},
	"6 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Quartz Flask": {"base": "Quartz Flask", "type": "unique special"},
	"6 Reinforced Tower Shield": {"base": "Reinforced Tower Shield", "type": "unique special"},
	"6 Ruby Flask": {"base": "Ruby Flask", "type": "unique special"},
	"6 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"6 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique special"},
	"6 Sadist Garb": {"base": "Sadist Garb", "type": "unique special"},
	"6 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique special"},
	"6 Silken Hood": {"base": "Silken Hood", "type": "unique special"},
	"6 Simple Robe": {"base": "Simple Robe", "type": "unique special"},
	"6 Slink Boots": {"base": "Slink Boots", "type": "unique special"},
	"6 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique special"},
	"6 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique special"},
	"6 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique special"},
	"6 Spine Bow": {"base": "Spine Bow", "type": "unique special"},
	"6 Stealth Boots": {"base": "Stealth Boots", "type": "unique special"},
	"6 Steel Gauntlets": {"base": "Steel Gauntlets", "type": "unique special"},
	"6 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique special"},
	"6 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique special"},
	"6 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique special"},
	"6 Sundering Axe": {"base": "Sundering Axe", "type": "unique special"},
	"6 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique special"},
	"6 Titan Greaves": {"base": "Titan Greaves", "type": "unique special"},
	"6 Topaz Flask": {"base": "Topaz Flask", "type": "unique special"},
	"6 Topaz Ring": {"base": "Topaz Ring", "type": "unique special"},
	"6 Tornado Wand": {"base": "Tornado Wand", "type": "unique special"},
	"6 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Axe": {"base": "Vaal Axe", "type": "unique special"},
	"6 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"6 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique special"},
	"6 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique special"},
	"6 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique special"},
	"6 Wool Gloves": {"base": "Wool Gloves", "type": "unique special"},
	"6 Zealot Gloves": {"base": "Zealot Gloves", "type": "unique special"},
	"9 Other uniques": {"type": "unique normal"}
}
