#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 03/24/2018(m/d/y) 05:45:21 UTC from "Hardcore" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique very high"},
	"0 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique very high"},
	"0 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique very high"},
	"0 Astral Plate": {"base": "Astral Plate", "type": "unique very high"},
	"0 Blinder": {"base": "Blinder", "type": "unique very high"},
	"0 Callous Mask": {"base": "Callous Mask", "type": "unique very high"},
	"0 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique very high"},
	"0 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique very high"},
	"0 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique very high"},
	"0 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"0 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique very high"},
	"0 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"0 Diamond Flask": {"base": "Diamond Flask", "type": "unique very high"},
	"0 Elegant Foil": {"base": "Elegant Foil", "type": "unique very high"},
	"0 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique very high"},
	"0 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique very high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique very high"},
	"0 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique very high"},
	"0 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique very high"},
	"0 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Granite Flask": {"base": "Granite Flask", "type": "unique very high"},
	"0 Great Mallet": {"base": "Great Mallet", "type": "unique very high"},
	"0 Harbinger Map": {"base": "Harbinger Map", "type": "unique very high"},
	"0 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique very high"},
	"0 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"0 Judgement Staff": {"base": "Judgement Staff", "type": "unique very high"},
	"0 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique very high"},
	"0 Lathi": {"base": "Lathi", "type": "unique very high"},
	"0 Meatgrinder": {"base": "Meatgrinder", "type": "unique very high"},
	"0 Midnight Blade": {"base": "Midnight Blade", "type": "unique very high"},
	"0 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique very high"},
	"0 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique very high"},
	"0 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique very high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"0 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique very high"},
	"0 Sadist Garb": {"base": "Sadist Garb", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Scholar's Robe": {"base": "Scholar's Robe", "type": "unique very high"},
	"0 Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "type": "unique very high"},
	"0 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"0 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique very high"},
	"0 Slink Boots": {"base": "Slink Boots", "type": "unique very high"},
	"0 Sorcerer Gloves": {"base": "Sorcerer Gloves", "type": "unique very high"},
	"0 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique very high"},
	"0 Stygian Vise": {"base": "Stygian Vise", "type": "unique very high"},
	"0 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique very high"},
	"0 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique very high"},
	"0 Vaal Blade": {"base": "Vaal Blade", "type": "unique very high"},
	"0 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique very high"},
	"0 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique very high"},
	"0 Vanguard Belt": {"base": "Vanguard Belt", "type": "unique very high"},
	"0 Zealot Gloves": {"base": "Zealot Gloves", "type": "unique very high"},
	"1 Amber Amulet": {"base": "Amber Amulet", "type": "unique high"},
	"1 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique high"},
	"1 Auric Mace": {"base": "Auric Mace", "type": "unique high"},
	"1 Bone Circlet": {"base": "Bone Circlet", "type": "unique high"},
	"1 Branded Kite Shield": {"base": "Branded Kite Shield", "type": "unique high"},
	"1 Close Helmet": {"base": "Close Helmet", "type": "unique high"},
	"1 Colossal Tower Shield": {"base": "Colossal Tower Shield", "type": "unique high"},
	"1 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique high"},
	"1 Crusader Chainmail": {"base": "Crusader Chainmail", "type": "unique high"},
	"1 Crusader Plate": {"base": "Crusader Plate", "type": "unique high"},
	"1 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique high"},
	"1 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique high"},
	"1 Despot Axe": {"base": "Despot Axe", "type": "unique high"},
	"1 Destroyer Regalia": {"base": "Destroyer Regalia", "type": "unique high"},
	"1 Elder Sword": {"base": "Elder Sword", "type": "unique high"},
	"1 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique high"},
	"1 Engraved Wand": {"base": "Engraved Wand", "type": "unique high"},
	"1 Estoc": {"base": "Estoc", "type": "unique high"},
	"1 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique high"},
	"1 Gavel": {"base": "Gavel", "type": "unique high"},
	"1 Gladius": {"base": "Gladius", "type": "unique high"},
	"1 Gold Ring": {"base": "Gold Ring", "type": "unique high"},
	"1 Goliath Gauntlets": {"base": "Goliath Gauntlets", "type": "unique high"},
	"1 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"1 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique high"},
	"1 Heavy Belt": {"base": "Heavy Belt", "type": "unique high"},
	"1 Imperial Skean": {"base": "Imperial Skean", "type": "unique high"},
	"1 Imperial Staff": {"base": "Imperial Staff", "type": "unique high"},
	"1 Infernal Axe": {"base": "Infernal Axe", "type": "unique high"},
	"1 Infernal Sword": {"base": "Infernal Sword", "type": "unique high"},
	"1 Iron Gauntlets": {"base": "Iron Gauntlets", "type": "unique high"},
	"1 Jasper Chopper": {"base": "Jasper Chopper", "type": "unique high"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"1 Leather Cap": {"base": "Leather Cap", "type": "unique high"},
	"1 Lion Sword": {"base": "Lion Sword", "type": "unique high"},
	"1 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique high"},
	"1 Painted Tower Shield": {"base": "Painted Tower Shield", "type": "unique high"},
	"1 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique high"},
	"1 Platinum Sceptre": {"base": "Platinum Sceptre", "type": "unique high"},
	"1 Reef Map": {"base": "Reef Map", "type": "unique high"},
	"1 Rock Breaker": {"base": "Rock Breaker", "type": "unique high"},
	"1 Rustic Sash": {"base": "Rustic Sash", "type": "unique high"},
	"1 Samite Gloves": {"base": "Samite Gloves", "type": "unique high"},
	"1 Samite Helmet": {"base": "Samite Helmet", "type": "unique high"},
	"1 Savant's Robe": {"base": "Savant's Robe", "type": "unique high"},
	"1 Sentinel Jacket": {"base": "Sentinel Jacket", "type": "unique high"},
	"1 Serpentine Staff": {"base": "Serpentine Staff", "type": "unique high"},
	"1 Silken Hood": {"base": "Silken Hood", "type": "unique high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"1 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique high"},
	"1 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique high"},
	"1 Spiked Club": {"base": "Spiked Club", "type": "unique high"},
	"1 Spine Bow": {"base": "Spine Bow", "type": "unique high"},
	"1 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique high"},
	"1 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique high"},
	"1 Throat Stabber": {"base": "Throat Stabber", "type": "unique high"},
	"1 Titan Greaves": {"base": "Titan Greaves", "type": "unique high"},
	"1 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique high"},
	"1 Vaal Axe": {"base": "Vaal Axe", "type": "unique high"},
	"1 Void Sceptre": {"base": "Void Sceptre", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Assassin Bow": {"base": "Assassin Bow", "type": "unique special"},
	"6 Assassin's Mitts": {"base": "Assassin's Mitts", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Coral Ring": {"base": "Coral Ring", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Death Bow": {"base": "Death Bow", "type": "unique special"},
	"6 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Iron Ring": {"base": "Iron Ring", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Paua Amulet": {"base": "Paua Amulet", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Praetor Crown": {"base": "Praetor Crown", "type": "unique special"},
	"6 Reaver Sword": {"base": "Reaver Sword", "type": "unique special"},
	"6 Royal Bow": {"base": "Royal Bow", "type": "unique special"},
	"6 Sage Wand": {"base": "Sage Wand", "type": "unique special"},
	"6 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique special"},
	"6 Scholar Boots": {"base": "Scholar Boots", "type": "unique special"},
	"6 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique special"},
	"6 Terror Claw": {"base": "Terror Claw", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Woodsplitter": {"base": "Woodsplitter", "type": "unique special"},
	"7 Bastard Sword": {"base": "Bastard Sword", "type": "unique low"},
	"7 Boot Knife": {"base": "Boot Knife", "type": "unique low"},
	"7 Crude Bow": {"base": "Crude Bow", "type": "unique low"},
	"7 Decorative Axe": {"base": "Decorative Axe", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Jagged Foil": {"base": "Jagged Foil", "type": "unique low"},
	"7 Latticed Ringmail": {"base": "Latticed Ringmail", "type": "unique low"},
	"7 Ornate Ringmail": {"base": "Ornate Ringmail", "type": "unique low"},
	"7 Painted Buckler": {"base": "Painted Buckler", "type": "unique low"},
	"7 Quartz Flask": {"base": "Quartz Flask", "type": "unique low"},
	"7 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"7 Rusted Sword": {"base": "Rusted Sword", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Short Bow": {"base": "Short Bow", "type": "unique low"},
	"7 Simple Robe": {"base": "Simple Robe", "type": "unique low"},
	"7 Sledgehammer": {"base": "Sledgehammer", "type": "unique low"},
	"7 Soldier Helmet": {"base": "Soldier Helmet", "type": "unique low"},
	"7 Sulphur Flask": {"base": "Sulphur Flask", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Vine Circlet": {"base": "Vine Circlet", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"7 War Hammer": {"base": "War Hammer", "type": "unique low"},
	"7 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
