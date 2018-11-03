#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 11/03/2018(m/d/y) 19:57:43 UTC from "tmpstandard" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Assassin's Boots": {"base": "Assassin's Boots", "type": "unique extremely high"},
	"0 Callous Mask": {"base": "Callous Mask", "type": "unique extremely high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique extremely high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique extremely high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique extremely high"},
	"0 Harbinger Map": {"base": "Harbinger Map", "type": "unique extremely high"},
	"0 Maze Map": {"base": "Maze Map", "type": "unique extremely high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique extremely high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique extremely high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique extremely high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique extremely high"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique very high"},
	"1 Blood Raiment": {"base": "Blood Raiment", "type": "unique very high"},
	"1 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique very high"},
	"1 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"1 Cloth Belt Piece": {"base": "Cloth Belt Piece", "type": "unique very high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"1 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique very high"},
	"1 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"1 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique very high"},
	"1 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique very high"},
	"1 Hydrascale Boots": {"base": "Hydrascale Boots", "type": "unique very high"},
	"1 Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "type": "unique very high"},
	"1 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"1 Legion Gloves": {"base": "Legion Gloves", "type": "unique very high"},
	"1 Magistrate Crown": {"base": "Magistrate Crown", "type": "unique very high"},
	"1 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique very high"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique very high"},
	"1 Nightmare Mace": {"base": "Nightmare Mace", "type": "unique very high"},
	"1 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"1 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"1 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique very high"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique very high"},
	"1 Riveted Gloves": {"base": "Riveted Gloves", "type": "unique very high"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique very high"},
	"1 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique very high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique very high"},
	"1 Shore Map": {"base": "Shore Map", "type": "unique very high"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique very high"},
	"2 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique high"},
	"2 Blood Raiment": {"base": "Blood Raiment", "type": "unique high"},
	"2 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique high"},
	"2 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique high"},
	"2 Cloth Belt Piece": {"base": "Cloth Belt Piece", "type": "unique high"},
	"2 Courtyard Map": {"base": "Courtyard Map", "type": "unique high"},
	"2 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique high"},
	"2 Glorious Plate": {"base": "Glorious Plate", "type": "unique high"},
	"2 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique high"},
	"2 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique high"},
	"2 Hydrascale Boots": {"base": "Hydrascale Boots", "type": "unique high"},
	"2 Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "type": "unique high"},
	"2 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique high"},
	"2 Legion Gloves": {"base": "Legion Gloves", "type": "unique high"},
	"2 Magistrate Crown": {"base": "Magistrate Crown", "type": "unique high"},
	"2 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique high"},
	"2 Museum Map": {"base": "Museum Map", "type": "unique high"},
	"2 Nightmare Mace": {"base": "Nightmare Mace", "type": "unique high"},
	"2 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique high"},
	"2 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique high"},
	"2 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique high"},
	"2 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique high"},
	"2 Riveted Gloves": {"base": "Riveted Gloves", "type": "unique high"},
	"2 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique high"},
	"2 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique high"},
	"2 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique high"},
	"2 Shore Map": {"base": "Shore Map", "type": "unique high"},
	"2 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique special"},
	"6 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique special"},
	"6 Blunt Arrow Quiver Piece": {"base": "Blunt Arrow Quiver Piece", "type": "unique special"},
	"6 Carnal Armour": {"base": "Carnal Armour", "type": "unique special"},
	"6 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Cutlass": {"base": "Cutlass", "type": "unique special"},
	"6 Despot Axe": {"base": "Despot Axe", "type": "unique special"},
	"6 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"6 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique special"},
	"6 Elegant Sword": {"base": "Elegant Sword", "type": "unique special"},
	"6 Gavel": {"base": "Gavel", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Golden Plate": {"base": "Golden Plate", "type": "unique special"},
	"6 Goliath Greaves": {"base": "Goliath Greaves", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique special"},
	"6 Imperial Bow": {"base": "Imperial Bow", "type": "unique special"},
	"6 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Midnight Blade": {"base": "Midnight Blade", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Murder Boots": {"base": "Murder Boots", "type": "unique special"},
	"6 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique special"},
	"6 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Quartz Flask": {"base": "Quartz Flask", "type": "unique special"},
	"6 Ruby Flask": {"base": "Ruby Flask", "type": "unique special"},
	"6 Ruby Ring": {"base": "Ruby Ring", "type": "unique special"},
	"6 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"6 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique special"},
	"6 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique special"},
	"6 Silken Hood": {"base": "Silken Hood", "type": "unique special"},
	"6 Slink Boots": {"base": "Slink Boots", "type": "unique special"},
	"6 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique special"},
	"6 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique special"},
	"6 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique special"},
	"6 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique special"},
	"6 Topaz Flask": {"base": "Topaz Flask", "type": "unique special"},
	"6 Topaz Ring": {"base": "Topaz Ring", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Axe": {"base": "Vaal Axe", "type": "unique special"},
	"6 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique special"},
	"6 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique special"},
	"7 Ambusher": {"base": "Ambusher", "type": "unique low"},
	"7 Antique Rapier": {"base": "Antique Rapier", "type": "unique low"},
	"7 Assassin Bow": {"base": "Assassin Bow", "type": "unique low"},
	"7 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique low"},
	"7 Auric Mace": {"base": "Auric Mace", "type": "unique low"},
	"7 Aventail Helmet": {"base": "Aventail Helmet", "type": "unique low"},
	"7 Awl": {"base": "Awl", "type": "unique low"},
	"7 Baroque Round Shield": {"base": "Baroque Round Shield", "type": "unique low"},
	"7 Basket Rapier": {"base": "Basket Rapier", "type": "unique low"},
	"7 Bastard Sword": {"base": "Bastard Sword", "type": "unique low"},
	"7 Bone Circlet": {"base": "Bone Circlet", "type": "unique low"},
	"7 Boot Blade": {"base": "Boot Blade", "type": "unique low"},
	"7 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"7 Brass Maul": {"base": "Brass Maul", "type": "unique low"},
	"7 Bronze Gauntlets": {"base": "Bronze Gauntlets", "type": "unique low"},
	"7 Bronzescale Boots": {"base": "Bronzescale Boots", "type": "unique low"},
	"7 Bronzescale Gauntlets": {"base": "Bronzescale Gauntlets", "type": "unique low"},
	"7 Buckskin Tunic": {"base": "Buckskin Tunic", "type": "unique low"},
	"7 Chain Belt": {"base": "Chain Belt", "type": "unique low"},
	"7 Chiming Spirit Shield": {"base": "Chiming Spirit Shield", "type": "unique low"},
	"7 Clasped Boots": {"base": "Clasped Boots", "type": "unique low"},
	"7 Cleaver": {"base": "Cleaver", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Conquest Chainmail": {"base": "Conquest Chainmail", "type": "unique low"},
	"7 Copper Plate": {"base": "Copper Plate", "type": "unique low"},
	"7 Crude Bow": {"base": "Crude Bow", "type": "unique low"},
	"7 Crusader Plate": {"base": "Crusader Plate", "type": "unique low"},
	"7 Crystal Sceptre": {"base": "Crystal Sceptre", "type": "unique low"},
	"7 Crystal Wand": {"base": "Crystal Wand", "type": "unique low"},
	"7 Cutthroat's Garb": {"base": "Cutthroat's Garb", "type": "unique low"},
	"7 Death Bow": {"base": "Death Bow", "type": "unique low"},
	"7 Decimation Bow": {"base": "Decimation Bow", "type": "unique low"},
	"7 Decorative Axe": {"base": "Decorative Axe", "type": "unique low"},
	"7 Deerskin Boots": {"base": "Deerskin Boots", "type": "unique low"},
	"7 Demon's Horn": {"base": "Demon's Horn", "type": "unique low"},
	"7 Dragonscale Boots": {"base": "Dragonscale Boots", "type": "unique low"},
	"7 Dread Maul": {"base": "Dread Maul", "type": "unique low"},
	"7 Dream Mace": {"base": "Dream Mace", "type": "unique low"},
	"7 Dusk Blade": {"base": "Dusk Blade", "type": "unique low"},
	"7 Enameled Buckler": {"base": "Enameled Buckler", "type": "unique low"},
	"7 Estoc": {"base": "Estoc", "type": "unique low"},
	"7 Ezomyte Axe": {"base": "Ezomyte Axe", "type": "unique low"},
	"7 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique low"},
	"7 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique low"},
	"7 Fire Arrow Quiver": {"base": "Fire Arrow Quiver", "type": "unique low"},
	"7 Flaying Knife": {"base": "Flaying Knife", "type": "unique low"},
	"7 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique low"},
	"7 Gilded Sallet": {"base": "Gilded Sallet", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goat's Horn": {"base": "Goat's Horn", "type": "unique low"},
	"7 Golden Mask": {"base": "Golden Mask", "type": "unique low"},
	"7 Great Helmet": {"base": "Great Helmet", "type": "unique low"},
	"7 Great Mallet": {"base": "Great Mallet", "type": "unique low"},
	"7 Greater Mana Flask": {"base": "Greater Mana Flask", "type": "unique low"},
	"7 Grinning Fetish": {"base": "Grinning Fetish", "type": "unique low"},
	"7 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique low"},
	"7 Harmonic Spirit Shield": {"base": "Harmonic Spirit Shield", "type": "unique low"},
	"7 Headsman Axe": {"base": "Headsman Axe", "type": "unique low"},
	"7 Highland Blade": {"base": "Highland Blade", "type": "unique low"},
	"7 Holy Chainmail": {"base": "Holy Chainmail", "type": "unique low"},
	"7 Imbued Wand": {"base": "Imbued Wand", "type": "unique low"},
	"7 Imperial Skean": {"base": "Imperial Skean", "type": "unique low"},
	"7 Infernal Axe": {"base": "Infernal Axe", "type": "unique low"},
	"7 Iron Hat": {"base": "Iron Hat", "type": "unique low"},
	"7 Iron Mask": {"base": "Iron Mask", "type": "unique low"},
	"7 Iron Staff": {"base": "Iron Staff", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "type": "unique low"},
	"7 Jagged Foil": {"base": "Jagged Foil", "type": "unique low"},
	"7 Jagged Maul": {"base": "Jagged Maul", "type": "unique low"},
	"7 Karui Chopper": {"base": "Karui Chopper", "type": "unique low"},
	"7 Karui Maul": {"base": "Karui Maul", "type": "unique low"},
	"7 Lacquered Helmet": {"base": "Lacquered Helmet", "type": "unique low"},
	"7 Latticed Ringmail": {"base": "Latticed Ringmail", "type": "unique low"},
	"7 Leather Hood": {"base": "Leather Hood", "type": "unique low"},
	"7 Legion Boots": {"base": "Legion Boots", "type": "unique low"},
	"7 Lion Sword": {"base": "Lion Sword", "type": "unique low"},
	"7 Long Bow": {"base": "Long Bow", "type": "unique low"},
	"7 Long Staff": {"base": "Long Staff", "type": "unique low"},
	"7 Lunaris Circlet": {"base": "Lunaris Circlet", "type": "unique low"},
	"7 Mesh Boots": {"base": "Mesh Boots", "type": "unique low"},
	"7 Military Staff": {"base": "Military Staff", "type": "unique low"},
	"7 Mind Cage": {"base": "Mind Cage", "type": "unique low"},
	"7 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique low"},
	"7 Nailed Fist": {"base": "Nailed Fist", "type": "unique low"},
	"7 Opal Wand": {"base": "Opal Wand", "type": "unique low"},
	"7 Ornate Mace": {"base": "Ornate Mace", "type": "unique low"},
	"7 Ornate Ringmail": {"base": "Ornate Ringmail", "type": "unique low"},
	"7 Painted Buckler": {"base": "Painted Buckler", "type": "unique low"},
	"7 Paua Amulet": {"base": "Paua Amulet", "type": "unique low"},
	"7 Pine Buckler": {"base": "Pine Buckler", "type": "unique low"},
	"7 Plague Mask": {"base": "Plague Mask", "type": "unique low"},
	"7 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique low"},
	"7 Plate Vest": {"base": "Plate Vest", "type": "unique low"},
	"7 Plated Greaves": {"base": "Plated Greaves", "type": "unique low"},
	"7 Platinum Kris": {"base": "Platinum Kris", "type": "unique low"},
	"7 Poleaxe": {"base": "Poleaxe", "type": "unique low"},
	"7 Praetor Crown": {"base": "Praetor Crown", "type": "unique low"},
	"7 Primordial Staff": {"base": "Primordial Staff", "type": "unique low"},
	"7 Prophet Crown": {"base": "Prophet Crown", "type": "unique low"},
	"7 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"7 Quicksilver Flask": {"base": "Quicksilver Flask", "type": "unique low"},
	"7 Ranger Bow": {"base": "Ranger Bow", "type": "unique low"},
	"7 Reaver Sword": {"base": "Reaver Sword", "type": "unique low"},
	"7 Recurve Bow": {"base": "Recurve Bow", "type": "unique low"},
	"7 Regicide Mask": {"base": "Regicide Mask", "type": "unique low"},
	"7 Riveted Boots": {"base": "Riveted Boots", "type": "unique low"},
	"7 Rotted Round Shield": {"base": "Rotted Round Shield", "type": "unique low"},
	"7 Royal Bow": {"base": "Royal Bow", "type": "unique low"},
	"7 Royal Skean": {"base": "Royal Skean", "type": "unique low"},
	"7 Royal Staff": {"base": "Royal Staff", "type": "unique low"},
	"7 Rusted Sword": {"base": "Rusted Sword", "type": "unique low"},
	"7 Sage Wand": {"base": "Sage Wand", "type": "unique low"},
	"7 Sage's Robe": {"base": "Sage's Robe", "type": "unique low"},
	"7 Samite Gloves": {"base": "Samite Gloves", "type": "unique low"},
	"7 Samite Helmet": {"base": "Samite Helmet", "type": "unique low"},
	"7 Satin Gloves": {"base": "Satin Gloves", "type": "unique low"},
	"7 Scholar Boots": {"base": "Scholar Boots", "type": "unique low"},
	"7 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique low"},
	"7 Secutor Helm": {"base": "Secutor Helm", "type": "unique low"},
	"7 Sentinel Jacket": {"base": "Sentinel Jacket", "type": "unique low"},
	"7 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique low"},
	"7 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Shadow Axe": {"base": "Shadow Axe", "type": "unique low"},
	"7 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique low"},
	"7 Shagreen Boots": {"base": "Shagreen Boots", "type": "unique low"},
	"7 Silk Gloves": {"base": "Silk Gloves", "type": "unique low"},
	"7 Silk Slippers": {"base": "Silk Slippers", "type": "unique low"},
	"7 Simple Robe": {"base": "Simple Robe", "type": "unique low"},
	"7 Skinning Knife": {"base": "Skinning Knife", "type": "unique low"},
	"7 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique low"},
	"7 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"7 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique low"},
	"7 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique low"},
	"7 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique low"},
	"7 Spiked Club": {"base": "Spiked Club", "type": "unique low"},
	"7 Spine Bow": {"base": "Spine Bow", "type": "unique low"},
	"7 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique low"},
	"7 Stiletto": {"base": "Stiletto", "type": "unique low"},
	"7 Strapped Boots": {"base": "Strapped Boots", "type": "unique low"},
	"7 Strapped Leather": {"base": "Strapped Leather", "type": "unique low"},
	"7 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique low"},
	"7 Studded Belt": {"base": "Studded Belt", "type": "unique low"},
	"7 Studded Round Shield": {"base": "Studded Round Shield", "type": "unique low"},
	"7 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique low"},
	"7 Sundering Axe": {"base": "Sundering Axe", "type": "unique low"},
	"7 Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "type": "unique low"},
	"7 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique low"},
	"7 Thresher Claw": {"base": "Thresher Claw", "type": "unique low"},
	"7 Tiger Sword": {"base": "Tiger Sword", "type": "unique low"},
	"7 Timeworn Claw": {"base": "Timeworn Claw", "type": "unique low"},
	"7 Tomahawk": {"base": "Tomahawk", "type": "unique low"},
	"7 Tribal Circlet": {"base": "Tribal Circlet", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique low"},
	"7 Twilight Blade": {"base": "Twilight Blade", "type": "unique low"},
	"7 Vaal Blade": {"base": "Vaal Blade", "type": "unique low"},
	"7 Vaal Buckler": {"base": "Vaal Buckler", "type": "unique low"},
	"7 Vaal Hatchet": {"base": "Vaal Hatchet", "type": "unique low"},
	"7 Velvet Gloves": {"base": "Velvet Gloves", "type": "unique low"},
	"7 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique low"},
	"7 Vile Staff": {"base": "Vile Staff", "type": "unique low"},
	"7 Vine Circlet": {"base": "Vine Circlet", "type": "unique low"},
	"7 Visored Sallet": {"base": "Visored Sallet", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"7 War Hammer": {"base": "War Hammer", "type": "unique low"},
	"7 Wild Leather": {"base": "Wild Leather", "type": "unique low"},
	"7 Woodsplitter": {"base": "Woodsplitter", "type": "unique low"},
	"7 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"7 Wyrmscale Gauntlets": {"base": "Wyrmscale Gauntlets", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
