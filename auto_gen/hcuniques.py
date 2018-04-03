#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 04/03/2018(m/d/y) 00:48:12 UTC from "Hardcore" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique very high"},
	"0 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique very high"},
	"0 Astral Plate": {"base": "Astral Plate", "type": "unique very high"},
	"0 Blue Pearl Amulet": {"base": "Blue Pearl Amulet", "type": "unique very high"},
	"0 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"0 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique very high"},
	"0 Citadel Bow": {"base": "Citadel Bow", "type": "unique very high"},
	"0 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique very high"},
	"0 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique very high"},
	"0 Desert Brigandine": {"base": "Desert Brigandine", "type": "unique very high"},
	"0 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique very high"},
	"0 Elegant Foil": {"base": "Elegant Foil", "type": "unique very high"},
	"0 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique very high"},
	"0 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique very high"},
	"0 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique very high"},
	"0 Full Scale Armour": {"base": "Full Scale Armour", "type": "unique very high"},
	"0 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique very high"},
	"0 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"0 Gold Ring": {"base": "Gold Ring", "type": "unique very high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique very high"},
	"0 Heavy Quiver": {"base": "Heavy Quiver", "type": "unique very high"},
	"0 Hellion's Paw": {"base": "Hellion's Paw", "type": "unique very high"},
	"0 Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "type": "unique very high"},
	"0 Judgement Staff": {"base": "Judgement Staff", "type": "unique very high"},
	"0 Lion Sword": {"base": "Lion Sword", "type": "unique very high"},
	"0 Marble Amulet": {"base": "Marble Amulet", "type": "unique very high"},
	"0 Meatgrinder": {"base": "Meatgrinder", "type": "unique very high"},
	"0 Midnight Blade": {"base": "Midnight Blade", "type": "unique very high"},
	"0 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique very high"},
	"0 Murder Mitts": {"base": "Murder Mitts", "type": "unique very high"},
	"0 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique very high"},
	"0 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique very high"},
	"0 Primordial Staff": {"base": "Primordial Staff", "type": "unique very high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique very high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique very high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique very high"},
	"0 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique very high"},
	"0 Saintly Chainmail": {"base": "Saintly Chainmail", "type": "unique very high"},
	"0 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"0 Savant's Robe": {"base": "Savant's Robe", "type": "unique very high"},
	"0 Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "type": "unique very high"},
	"0 Sorcerer Gloves": {"base": "Sorcerer Gloves", "type": "unique very high"},
	"0 Stealth Boots": {"base": "Stealth Boots", "type": "unique very high"},
	"0 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique very high"},
	"0 Vaal Mask": {"base": "Vaal Mask", "type": "unique very high"},
	"0 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique very high"},
	"0 Varnished Coat": {"base": "Varnished Coat", "type": "unique very high"},
	"0 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique very high"},
	"1 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique high"},
	"1 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique high"},
	"1 Atoll Map": {"base": "Atoll Map", "type": "unique high"},
	"1 Bismuth Flask": {"base": "Bismuth Flask", "type": "unique high"},
	"1 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique high"},
	"1 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique high"},
	"1 Bone Armour": {"base": "Bone Armour", "type": "unique high"},
	"1 Bone Bow": {"base": "Bone Bow", "type": "unique high"},
	"1 Bone Crypt Map": {"base": "Bone Crypt Map", "type": "unique high"},
	"1 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique high"},
	"1 Bronze Gauntlets": {"base": "Bronze Gauntlets", "type": "unique high"},
	"1 Carnal Armour": {"base": "Carnal Armour", "type": "unique high"},
	"1 Colossal Tower Shield": {"base": "Colossal Tower Shield", "type": "unique high"},
	"1 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique high"},
	"1 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique high"},
	"1 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique high"},
	"1 Corsair Sword": {"base": "Corsair Sword", "type": "unique high"},
	"1 Crusader Plate": {"base": "Crusader Plate", "type": "unique high"},
	"1 Cursed Crypt Map": {"base": "Cursed Crypt Map", "type": "unique high"},
	"1 Cutthroat's Garb": {"base": "Cutthroat's Garb", "type": "unique high"},
	"1 Destroyer Regalia": {"base": "Destroyer Regalia", "type": "unique high"},
	"1 Elder Sword": {"base": "Elder Sword", "type": "unique high"},
	"1 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique high"},
	"1 Engraved Wand": {"base": "Engraved Wand", "type": "unique high"},
	"1 Eternal Sword": {"base": "Eternal Sword", "type": "unique high"},
	"1 Eye Gouger": {"base": "Eye Gouger", "type": "unique high"},
	"1 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique high"},
	"1 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique high"},
	"1 Full Dragonscale": {"base": "Full Dragonscale", "type": "unique high"},
	"1 Gladius": {"base": "Gladius", "type": "unique high"},
	"1 Granite Flask": {"base": "Granite Flask", "type": "unique high"},
	"1 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"1 Imperial Claw": {"base": "Imperial Claw", "type": "unique high"},
	"1 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique high"},
	"1 Ivory Spirit Shield": {"base": "Ivory Spirit Shield", "type": "unique high"},
	"1 Jagged Foil": {"base": "Jagged Foil", "type": "unique high"},
	"1 Jagged Maul": {"base": "Jagged Maul", "type": "unique high"},
	"1 Karui Maul": {"base": "Karui Maul", "type": "unique high"},
	"1 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique high"},
	"1 Laminated Kite Shield": {"base": "Laminated Kite Shield", "type": "unique high"},
	"1 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique high"},
	"1 Lathi": {"base": "Lathi", "type": "unique high"},
	"1 Leather Cap": {"base": "Leather Cap", "type": "unique high"},
	"1 Legion Gloves": {"base": "Legion Gloves", "type": "unique high"},
	"1 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique high"},
	"1 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique high"},
	"1 Overgrown Shrine Map": {"base": "Overgrown Shrine Map", "type": "unique high"},
	"1 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique high"},
	"1 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique high"},
	"1 Platinum Sceptre": {"base": "Platinum Sceptre", "type": "unique high"},
	"1 Promenade Map": {"base": "Promenade Map", "type": "unique high"},
	"1 Prophet Crown": {"base": "Prophet Crown", "type": "unique high"},
	"1 Reaver Sword": {"base": "Reaver Sword", "type": "unique high"},
	"1 Reef Map": {"base": "Reef Map", "type": "unique high"},
	"1 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique high"},
	"1 Royal Skean": {"base": "Royal Skean", "type": "unique high"},
	"1 Ruby Flask": {"base": "Ruby Flask", "type": "unique high"},
	"1 Sage Wand": {"base": "Sage Wand", "type": "unique high"},
	"1 Samite Gloves": {"base": "Samite Gloves", "type": "unique high"},
	"1 Serpentscale Boots": {"base": "Serpentscale Boots", "type": "unique high"},
	"1 Silver Flask": {"base": "Silver Flask", "type": "unique high"},
	"1 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"1 Slaughter Knife": {"base": "Slaughter Knife", "type": "unique high"},
	"1 Slink Boots": {"base": "Slink Boots", "type": "unique high"},
	"1 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique high"},
	"1 Spine Bow": {"base": "Spine Bow", "type": "unique high"},
	"1 Stygian Vise": {"base": "Stygian Vise", "type": "unique high"},
	"1 Sundering Axe": {"base": "Sundering Axe", "type": "unique high"},
	"1 Supreme Spiked Shield": {"base": "Supreme Spiked Shield", "type": "unique high"},
	"1 Terror Claw": {"base": "Terror Claw", "type": "unique high"},
	"1 Throat Stabber": {"base": "Throat Stabber", "type": "unique high"},
	"1 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique high"},
	"1 Topaz Ring": {"base": "Topaz Ring", "type": "unique high"},
	"1 Tornado Wand": {"base": "Tornado Wand", "type": "unique high"},
	"1 Trapper Boots": {"base": "Trapper Boots", "type": "unique high"},
	"1 Tribal Circlet": {"base": "Tribal Circlet", "type": "unique high"},
	"1 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique high"},
	"1 Underground River Map": {"base": "Underground River Map", "type": "unique high"},
	"1 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique high"},
	"1 Vaal Axe": {"base": "Vaal Axe", "type": "unique high"},
	"1 Vaal Regalia": {"base": "Vaal Regalia", "type": "unique high"},
	"1 Vanguard Belt": {"base": "Vanguard Belt", "type": "unique high"},
	"1 Void Sceptre": {"base": "Void Sceptre", "type": "unique high"},
	"1 War Hammer": {"base": "War Hammer", "type": "unique high"},
	"1 War Sword": {"base": "War Sword", "type": "unique high"},
	"1 Zealot Helmet": {"base": "Zealot Helmet", "type": "unique high"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Assassin Bow": {"base": "Assassin Bow", "type": "unique special"},
	"6 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"6 Clasped Boots": {"base": "Clasped Boots", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Coral Amulet": {"base": "Coral Amulet", "type": "unique special"},
	"6 Coral Ring": {"base": "Coral Ring", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Crude Bow": {"base": "Crude Bow", "type": "unique special"},
	"6 Death Bow": {"base": "Death Bow", "type": "unique special"},
	"6 Elegant Sword": {"base": "Elegant Sword", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Great Mallet": {"base": "Great Mallet", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"6 Iron Ring": {"base": "Iron Ring", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Long Bow": {"base": "Long Bow", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Plate Vest": {"base": "Plate Vest", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Royal Bow": {"base": "Royal Bow", "type": "unique special"},
	"6 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique special"},
	"6 Sharktooth Arrow Quiver": {"base": "Sharktooth Arrow Quiver", "type": "unique special"},
	"6 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique special"},
	"6 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique special"},
	"7 Basket Rapier": {"base": "Basket Rapier", "type": "unique low"},
	"7 Brass Maul": {"base": "Brass Maul", "type": "unique low"},
	"7 Bronze Sceptre": {"base": "Bronze Sceptre", "type": "unique low"},
	"7 Carved Wand": {"base": "Carved Wand", "type": "unique low"},
	"7 Chain Gloves": {"base": "Chain Gloves", "type": "unique low"},
	"7 Cleaver": {"base": "Cleaver", "type": "unique low"},
	"7 Compound Spiked Shield": {"base": "Compound Spiked Shield", "type": "unique low"},
	"7 Gnarled Branch": {"base": "Gnarled Branch", "type": "unique low"},
	"7 Goathide Gloves": {"base": "Goathide Gloves", "type": "unique low"},
	"7 Golden Mask": {"base": "Golden Mask", "type": "unique low"},
	"7 Harbinger Bow": {"base": "Harbinger Bow", "type": "unique low"},
	"7 Highland Blade": {"base": "Highland Blade", "type": "unique low"},
	"7 Infernal Axe": {"base": "Infernal Axe", "type": "unique low"},
	"7 Ironscale Boots": {"base": "Ironscale Boots", "type": "unique low"},
	"7 Military Staff": {"base": "Military Staff", "type": "unique low"},
	"7 Nailed Fist": {"base": "Nailed Fist", "type": "unique low"},
	"7 Ornate Sword": {"base": "Ornate Sword", "type": "unique low"},
	"7 Paua Amulet": {"base": "Paua Amulet", "type": "unique low"},
	"7 Quartz Wand": {"base": "Quartz Wand", "type": "unique low"},
	"7 Rotted Round Shield": {"base": "Rotted Round Shield", "type": "unique low"},
	"7 Royal Staff": {"base": "Royal Staff", "type": "unique low"},
	"7 Rusted Sword": {"base": "Rusted Sword", "type": "unique low"},
	"7 Scholar Boots": {"base": "Scholar Boots", "type": "unique low"},
	"7 Serrated Arrow Quiver": {"base": "Serrated Arrow Quiver", "type": "unique low"},
	"7 Shadow Sceptre": {"base": "Shadow Sceptre", "type": "unique low"},
	"7 Short Bow": {"base": "Short Bow", "type": "unique low"},
	"7 Silk Slippers": {"base": "Silk Slippers", "type": "unique low"},
	"7 Simple Robe": {"base": "Simple Robe", "type": "unique low"},
	"7 Skinning Knife": {"base": "Skinning Knife", "type": "unique low"},
	"7 Spiraled Wand": {"base": "Spiraled Wand", "type": "unique low"},
	"7 Studded Belt": {"base": "Studded Belt", "type": "unique low"},
	"7 Timeworn Claw": {"base": "Timeworn Claw", "type": "unique low"},
	"7 Tricorne": {"base": "Tricorne", "type": "unique low"},
	"7 Velvet Gloves": {"base": "Velvet Gloves", "type": "unique low"},
	"7 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique low"},
	"7 Vile Staff": {"base": "Vile Staff", "type": "unique low"},
	"7 War Buckler": {"base": "War Buckler", "type": "unique low"},
	"7 Woodsplitter": {"base": "Woodsplitter", "type": "unique low"},
	"7 Wool Gloves": {"base": "Wool Gloves", "type": "unique low"},
	"7 Wool Shoes": {"base": "Wool Shoes", "type": "unique low"},
	"7 Wrapped Mitts": {"base": "Wrapped Mitts", "type": "unique low"},
	"9 Other uniques": {"type": "unique normal"}
}
